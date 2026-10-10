#!/usr/bin/env python3
"""CHINA 250-article editorial factory. Stdlib only; no text generation or API keys.

Commands:
  status
  plan [--batch B01] [--limit 5]
  validate [--drafts]
  qa --ids CN-0001,CN-0002
  publish --ids CN-0001,CN-0002 --confirm PUBLISH

PLANNED is the only state before publication. A draft is detected from
the physical _drafts/CN-xxxx.md file; no blind claim mutations are made.
"""
import argparse
import csv
import datetime as dt
import json
from pathlib import Path
import re
import sys
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "data" / "china-matrix.csv"
SOURCE = ROOT / "_data" / "china-plan.json"
DRAFTS = ROOT / "_drafts"
POSTS = ROOT / "_posts"
DOMAIN = "https://zh.rentbikehanoi.com"
STATUSES = {"PLANNED", "PUBLISHED"}
IMMUTABLE = ("article_id", "batch_id", "topic", "subtopic", "primary_keyword",
             "search_intent", "working_title", "slug", "draft_path", "permalink", "parent_hub")
FIELDS = IMMUTABLE + ("status", "qa_score", "published_date", "notes")
HAN = re.compile(r"[\u3400-\u9fff]")
FRONT = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)
KEY = re.compile(r'^([a-z][a-z_]*):\s*(.*?)\s*$', re.M)
ALLOWED_LINKS = {"/", "/blog/", "/prices/", "/contact/", "/faq/", "/about/",
                 "/topics/rental/", "/topics/rental/scooters/", "/topics/rental/monthly/",
                 "/topics/rental/automatic/", "/topics/pricing/", "/topics/pricing/daily/",
                 "/topics/pricing/weekly/", "/topics/pricing/deposits/", "/topics/50cc/",
                 "/topics/50cc/models/", "/topics/50cc/requirements/", "/topics/old-quarter/",
                 "/topics/old-quarter/directions/", "/topics/old-quarter/pickup/",
                 "/topics/guides/", "/topics/guides/contracts/", "/topics/guides/safety/",
                 "/topics/guides/returns/"}

def fail(msg):
    raise ValueError(msg)

def count_han(s):
    return len(HAN.findall(s))

def read_rows():
    with MATRIX.open(encoding="utf-8", newline="") as f:
        rd = csv.DictReader(f)
        if rd.fieldnames != list(FIELDS):
            fail("matrix columns mismatch (do not reorder)")
        return list(rd)

def source_rows():
    d = json.loads(SOURCE.read_text(encoding="utf-8"))
    if d.get("article_limit") != 250 or d.get("batch_size") != 25 or d.get("domain") != DOMAIN:
        fail("manifest must be 250 Chinese articles / 25 per batch / target domain")
    return d["planned_articles"]

def validate_matrix():
    planned = source_rows()
    rows = read_rows()
    if len(planned) != 250 or len(rows) != 250:
        fail("expected exactly 250 matrix rows")
    ids, titles, slugs, urls = set(), set(), set(), set()
    for i, (r, p) in enumerate(zip(rows, planned), 1):
        for k in IMMUTABLE:
            if str(r[k]) != str(p[k]):
                fail("immutable matrix drift at %s %s" % (r["article_id"], k))
        aid = "CN-%04d" % i
        bid = "B%02d" % ((i-1)//25 + 1)
        if r["article_id"] != aid or r["batch_id"] != bid:
            fail("matrix sequence must be CN-0001..CN-0250, batches B01..B10")
        if r["topic"] not in ("rental", "pricing", "50cc", "old-quarter", "guides"):
            fail(aid + ": topic not in live menu")
        if r["status"] not in STATUSES:
            fail(aid + ": unexpected status")
        if not r["parent_hub"].startswith("/topics/") or r["parent_hub"] not in ALLOWED_LINKS:
            fail(aid + ": missing real parent hub")
        if r["draft_path"] != "_drafts/"+aid+".md":
            fail(aid + ": invalid draft path")
        if r["permalink"] != "/blog/"+r["slug"]+"/":
            fail(aid + ": invalid permalink")
        if not re.fullmatch(r"[a-z0-9-]+", r["slug"]):
            fail(aid + ": invalid slug")
        if count_han(r["working_title"]) < 5 or len(r["working_title"]) < 12:
            fail(aid + ": title not Chinese")
        for label, item, seen in (("id",aid,ids),("title",r["working_title"],titles),
                                   ("slug",r["slug"],slugs),("permalink",r["permalink"],urls)):
            if item in seen: fail("duplicate "+label+" "+item)
            seen.add(item)
    # Published files MUST map back to exactly one matrix row, without orphans.
    published = [r for r in rows if r["status"] == "PUBLISHED"]
    expected_names = set()
    for r in published:
        stamp = r["published_date"]
        if not re.fullmatch(r"20\d\d-\d\d-\d\d", stamp):
            fail(r["article_id"] + ": invalid published date")
        if not r["qa_score"].isdigit() or int(r["qa_score"]) < 80:
            fail(r["article_id"] + ": published below QA gate")
        name = stamp + "-" + r["slug"] + ".md"
        expected_names.add(name)
        if not (POSTS / name).is_file(): fail(r["article_id"] + ": published file missing")
        if (DRAFTS / (r["article_id"]+".md")).exists():
            fail(r["article_id"] + ": published article also exists as draft")
    actual_names = {p.name for p in POSTS.glob("*.md")} if POSTS.is_dir() else set()
    if actual_names != expected_names:
        fail("untracked published posts or missing matrix rows: "+str(sorted(actual_names ^ expected_names)[:5]))
    for r in rows:
        if r["status"] == "PLANNED" and r["published_date"]:
            fail(r["article_id"]+": unpublished row has published_date")
    return rows

def parse_draft(path):
    s = path.read_text(encoding="utf-8")
    m = FRONT.match(s)
    if not m: fail(str(path)+": missing YAML front matter")
    fm = {}
    for k, raw in KEY.findall(m.group(1)):
        if k in fm: fail(str(path)+": duplicate front matter key "+k)
        if raw.startswith('"') or raw.startswith("["):
            try: fm[k] = json.loads(raw)
            except json.JSONDecodeError: fail(str(path)+": invalid JSON-compatible YAML value "+k)
        elif raw == "true": fm[k] = True
        elif raw == "false": fm[k] = False
        else: fm[k] = raw
    return fm, s[m.end():]

def audit_draft(r):
    aid = r["article_id"]
    path = ROOT / r["draft_path"]
    if not path.is_file(): fail(aid+": draft missing; writer must create "+r["draft_path"])
    fm, body = parse_draft(path)
    errors = []
    def req(condition, detail):
        if not condition: errors.append(detail)
    req(fm.get("article_id")==aid, "article_id differs from matrix")
    req(fm.get("layout")=="post", "layout must be post")
    req(fm.get("topic")==r["topic"], "topic must match matrix category")
    req(fm.get("subtopic")==r["subtopic"], "subtopic must match matrix")
    req(fm.get("permalink")==r["permalink"], "permalink must match matrix")
    req(fm.get("title")==r["working_title"], "title must match approved matrix brief (edit brief first if needed)")
    title = str(fm.get("title",""))
    description = str(fm.get("description",""))
    req(count_han(title)>=5 and 12<=len(title)<=95, "Chinese H1 must have >=5 Hanzi and 12–95 total characters (allow Latin vehicle model names)")
    req(40<=count_han(description)<=150, "meta description needs 40–150 Hanzi")
    req(count_han(body)>=800, "article needs >=800 substantive Chinese characters")
    req(len(re.findall(r"(?m)^##\s+\S",body))>=3, "at least 3 descriptive H2 sections")
    links = set(re.findall(r"\]\((/[^\s)#?]+/?)(?:#[^)]*)?\)",body))
    req(r["parent_hub"] in links, "link to its actual parent topic hub")
    req(len(links)>=2, "at least 2 distinct useful internal links")
    for l in links:
        if not l.startswith("/blog/") and l not in ALLOWED_LINKS:
            errors.append("possibly broken internal link: "+l)
    req(not re.search(r"<script|javascript:|<iframe",body,re.I), "unsafe embed / script not allowed")
    prohibited = ("免押金","无需押金","保证有车","保证第一","100%保证","无需驾照","肯定不需要驾照","免费配送")
    req(not any(w in body or w in title for w in prohibited), "unsupported guarantee/no-deposit/licence/delivery claim")
    req(DOMAIN not in str(fm.get("permalink","")), "permalink should be relative")
    if r["topic"] in ("50cc","guides") and re.search(r"法律|法规|驾驶资格|许可|驾照", title+body):
        notes = str(fm.get("source_notes",""))
        req("https://" in notes and len(notes)>=35, "legal claims require an attributable source note (review accuracy separately)")
    req(fm.get("editor_approved") is True, "editor_approved: true required after actual review")
    req(fm.get("reviewed_by")=="thuexemayhanoi", 'reviewed_by: "thuexemayhanoi" required')
    # Score is deterministic, NOT fact-checking. Any critical failure rejects publication.
    score = max(0,100-15*len(errors))
    return {"id":aid,"score":score,"passed":not errors and score>=80,"errors":errors,
            "chinese_characters":count_han(body),"h2":len(re.findall(r"(?m)^##\s+\S",body)),
            "internal_links":len(links)}

def ids_arg(value, rows):
    arr = [a.strip() for a in (value or "").split(",") if a.strip()]
    if not arr or len(arr)>5 or len(arr)!=len(set(arr)):
        fail("provide 1..5 distinct IDs (max five per manual release)")
    byid = {r["article_id"]:r for r in rows}
    if any(a not in byid for a in arr): fail("unknown matrix article ID")
    return [byid[a] for a in arr]

def status(rows):
    counts={state:sum(r["status"]==state for r in rows) for state in STATUSES}
    drafts=sum((ROOT / r["draft_path"]).is_file() for r in rows if r["status"]=="PLANNED")
    print(json.dumps({"total":len(rows),"published":counts["PUBLISHED"],
      "planned":counts["PLANNED"],"drafts_prepared":drafts,"remaining":250-counts["PUBLISHED"],
      "next_id":next((r["article_id"] for r in rows if r["status"]=="PLANNED"),None),
      "batches":[{"batch":"B%02d"%i,
       "published":sum(r["status"]=="PUBLISHED" for r in rows if r["batch_id"]=="B%02d"%i)}
       for i in range(1,11)]},ensure_ascii=False,indent=2))

def plan(rows,batch,limit):
    if batch and not re.fullmatch(r"B(0[1-9]|10)",batch): fail("batch must be B01..B10")
    if limit<1 or limit>25: fail("limit must be 1..25")
    pool=[r for r in rows if r["status"]=="PLANNED" and (not batch or r["batch_id"]==batch)]
    # Do not silently jump to future batches with unfinished drafts.
    if not batch and pool:pool=[r for r in pool if r["batch_id"]==pool[0]["batch_id"]]
    print(json.dumps([{"id":r["article_id"],"batch":r["batch_id"],
      "title":r["working_title"],"draft":r["draft_path"],
      "draft_exists":(ROOT/r["draft_path"]).is_file(),"hub":r["parent_hub"],
      "permalink":r["permalink"]} for r in pool[:limit]],ensure_ascii=False,indent=2))

def save_matrix(rows):
    MATRIX.parent.mkdir(parents=True,exist_ok=True)
    with MATRIX.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=FIELDS,lineterminator="\n")
        w.writeheader();w.writerows(rows)

def publish(selected,rows):
    today=dt.datetime.now(ZoneInfo("Asia/Ho_Chi_Minh"))
    stamp=today.strftime("%Y-%m-%d")
    operations=[]
    for r in selected:
        if r["status"]!="PLANNED":fail(r["article_id"]+": already published, will never overwrite")
        report=audit_draft(r)
        if not report["passed"]:fail(json.dumps(report,ensure_ascii=False))
        target=POSTS/(stamp+"-"+r["slug"]+".md")
        if target.exists():fail(r["article_id"]+": destination already exists")
        fm, body=parse_draft(ROOT/r["draft_path"])
        # We own publication date and breadcrumb linkage; one central schema/layout.
        fm["date"]=today.strftime("%Y-%m-%d %H:%M:%S %z")
        fm["breadcrumbs"]=[{"label":"博客","href":"/blog/"},
                           {"label":"专题","href":r["parent_hub"]},
                           {"label":r["working_title"]}]
        # Remove editorial-only flags from published metadata.
        fm.pop("editor_approved",None);fm.pop("reviewed_by",None)
        newfront="---\n"+"\n".join(k+": "+json.dumps(v,ensure_ascii=False) for k,v in fm.items())+"\n---\n"
        operations.append((r,ROOT/r["draft_path"],target,newfront+body,report))
    # This changes a GitHub Actions disposable checkout. Only the workflow makes a
    # single fast-forward Git commit if validation passes; never force-push.
    POSTS.mkdir(exist_ok=True)
    for r,draft,target,content,rep in operations:
        target.write_text(content,encoding="utf-8")
        draft.unlink()
        r["status"]="PUBLISHED"
        r["qa_score"]=str(rep["score"])
        r["published_date"]=stamp
        r["notes"]="Manually approved and batch-published by GitHub Actions"
    save_matrix(rows)
    validate_matrix()
    print(json.dumps({"published":[r["article_id"] for r,_,_,_,_ in operations],
      "new_urls":[DOMAIN+r["permalink"] for r,_,_,_,_ in operations],
      "matrix_total":250},ensure_ascii=False,indent=2))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("command",choices=("status","plan","validate","qa","publish"))
    ap.add_argument("--batch",default=None)
    ap.add_argument("--limit",type=int,default=5)
    ap.add_argument("--ids",default="")
    ap.add_argument("--confirm",default="")
    ap.add_argument("--drafts",action="store_true")
    a=ap.parse_args()
    try:
        rows=validate_matrix()
        if a.command=="status":status(rows)
        elif a.command=="plan":plan(rows,a.batch,a.limit)
        elif a.command=="validate":
            if a.drafts:
                reports=[audit_draft(r) for r in rows if r["status"]=="PLANNED" and
                         (ROOT/r["draft_path"]).is_file()]
                bad=[r for r in reports if not r["passed"]]
                print(json.dumps({"staged_drafts":len(reports),"failed":bad},ensure_ascii=False))
                if bad:return 1
            print("CHINA FACTORY VALIDATION PASS: exactly 250 matrix entries")
        elif a.command=="qa":
            reports=[audit_draft(r) for r in ids_arg(a.ids,rows)]
            print(json.dumps(reports,ensure_ascii=False,indent=2))
            return 0 if all(x["passed"] for x in reports) else 1
        elif a.command=="publish":
            if a.confirm!="PUBLISH":fail("manual confirmation PUBLISH is required")
            publish(ids_arg(a.ids,rows),rows)
        return 0
    except (ValueError, OSError) as e:
        print("CHINA_FACTORY_ERROR: "+str(e),file=sys.stderr)
        return 1

if __name__=="__main__":
    sys.exit(main())
