#!/usr/bin/env python3
"""Read-only AI Search FAQ scanner for 300 China posts and 31 pages."""
import csv,html,json,re
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"docs"
DOMAIN="https://zh.rentbikehanoi.com"
FIELDS=("scope","article_id","url","title","topic","subtopic","status","found_qa","question_only","faq_heading","faq_schema","source","question_examples","priority","action","review_required")
DETAIL=("article_id","url","source","question","answer_excerpt","answer_length","evidence_type","confidence","review_required")

def front(raw):
    m=re.match(r"\A---\s*\n(.*?)\n---\s*\n",raw,re.S)
    if not m:raise ValueError("Missing front matter")
    data={}
    for k in ("article_id","permalink","title","topic","subtopic","schema_faq"):
        match=re.search(r"^"+k+r":\s*(.*?)\s*$",m[1],re.M)
        v=match[1].strip() if match else ""
        try:v=json.loads(v) if v.startswith('"') else v
        except ValueError:pass
        data[k]=v
    return data,raw[m.end():]

def clean(s):
    s=re.sub(r"\{[%{].*?[}%]\}"," ",s,flags=re.S)
    s=re.sub(r"!?\[([^\]]+)\]\([^)]+\)",lambda m:m[1],s)
    return re.sub(r"\s+"," ",html.unescape(s.replace("*","").replace("_",""))).strip()

class Parse(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.items=[];self.kind=None;self.buff=[];self.hidden=0
    def handle_starttag(self,t,a):
        if t in ("script","style"):self.hidden+=1
        elif self.kind is None and t in ("h1","h2","h3","h4","p","li","summary") and not self.hidden:
            self.kind=t;self.buff=[]
    def handle_data(self,s):
        if self.kind and not self.hidden:self.buff.append(s)
    def handle_endtag(self,t):
        if t in ("script","style") and self.hidden:self.hidden-=1
        if t==self.kind:
            s=clean("".join(self.buff))
            if s:self.items.append((t,s))
            self.kind=None;self.buff=[]

def blocks(body,scope):
    if scope=="page":
        p=Parse();p.feed(body);return p.items
    result=[];paragraph=[]
    def flush():
        if paragraph:
            result.append(("p",clean(" ".join(paragraph))))
            paragraph.clear()
    for line in body.splitlines():
        heading=re.match(r"^\s*(#{1,4})\s+(.*?)\s*$",line)
        if heading:
            flush();result.append(("h"+str(len(heading[1])),clean(heading[2])))
        elif not line.strip():flush()
        else:paragraph.append(line.strip())
    flush();return result

def scan(info,body,scope,faqs):
    b=blocks(body,scope)
    faq_heading=any(k.startswith("h") and re.search("常见问题|问答|FAQ",v,re.I) for k,v in b)
    if info["permalink"]=="/faq/":
        return [(v["q"],v["a"],"central_faq_json","high") for v in faqs],[],True
    hits=[];missing=[]
    for i,(kind,q) in enumerate(b):
        if not (kind.startswith("h") or kind=="summary") or not re.search(r"[?？]\s*$",q) or not 4<=len(q)<=110:continue
        following=[]
        for t,val in b[i+1:]:
            if t.startswith("h") or t=="summary":break
            following.append(val)
            if sum(map(len,following))>450:break
        answer=clean(" ".join(following))
        if len(answer)>=35:hits.append((q,answer,"heading_plus_paragraph","medium"))
        else:missing.append(q)
    for q,a in re.findall(r"(?:^|\n)\s*(?:问(?:题)?|Q)\s*[：:]\s*([^\n]{4,100})\n\s*(?:答(?:案)?|A)\s*[：:]\s*([^\n]{30,1000})",body,re.I):
        if q not in [v[0] for v in hits]:hits.append((clean(q),clean(a),"inline_QA","high"))
    return hits,missing,faq_heading

def main():
    site=json.loads((ROOT/"_data/site.json").read_text(encoding="utf-8"))
    faqs=json.loads((ROOT/"_data/faqs.json").read_text(encoding="utf-8"))
    posts=sorted((ROOT/"_posts").glob("*.md"))
    pages=sorted(ROOT.rglob("index.html"))
    if len(posts)!=300 or len(pages)!=31:raise ValueError("Expected 300 posts and 31 pages")
    known=set(site["sitemap_base"])
    rows=[];details=[];routes=set();ids=set()
    for path in posts+pages:
        scope="post" if path in posts else "page"
        info,body=front(path.read_text(encoding="utf-8"))
        route=info["permalink"]
        if not route.startswith("/") or route in routes:raise ValueError("Duplicate/invalid URL: "+route)
        routes.add(route)
        if scope=="page" and route not in known:raise ValueError("Page not in sitemap: "+route)
        if scope=="post":
            article_id=info["article_id"]
            if not re.fullmatch(r"CN-\d{4}",article_id) or article_id in ids:raise ValueError("Invalid ID "+article_id)
            ids.add(article_id)
        hits,missing,faqheading=scan(info,body,scope,faqs)
        if route=="/faq/":status,priority,action="CURATED_FAQ","P0","VERIFY_CENTRAL_12_FACTS"
        elif hits:status,priority,action="EXISTING_QA_CANDIDATE","P1","REVIEW_VISIBLE_ANSWER_QUALITY"
        elif missing:status,priority,action="QUESTION_WITHOUT_CLEAR_ANSWER","P1","REVIEW_CONTEXT_BEFORE_ADDING_ANSWER"
        else:status,priority,action="NO_EXPLICIT_QA","P2" if scope=="post" else "P3","DO_NOT_FORCE_FAQ"
        source=path.relative_to(ROOT).as_posix()
        rows.append(dict(scope=scope,article_id=info["article_id"],url=DOMAIN+route,title=info["title"],
            topic=info["topic"],subtopic=info["subtopic"],status=status,found_qa=len(hits),
            question_only=len(missing),faq_heading=str(bool(faqheading)).lower(),
            faq_schema=str(info["schema_faq"]=="true").lower(),source=source,
            question_examples=" | ".join(h[0][:80] for h in hits[:3]),priority=priority,action=action,
            review_required="true"))
        for q,a,kind,confidence in hits:
            details.append(dict(article_id=info["article_id"],url=DOMAIN+route,source=source,
                question=q,answer_excerpt=a[:200],answer_length=len(a),
                evidence_type=kind,confidence=confidence,review_required="true"))
    if ids!={f"CN-{i:04d}" for i in range(1,301)}:raise ValueError("Incomplete CN IDs")
    OUT.mkdir(exist_ok=True)
    for filename,header,items in (("AI-SEARCH-FAQ-URL-MATRIX.csv",FIELDS,rows),
                                  ("AI-SEARCH-FAQ-QUESTION-EVIDENCE.csv",DETAIL,details)):
        with (OUT/filename).open("w",encoding="utf-8-sig",newline="") as f:
            writer=csv.DictWriter(f,fieldnames=header);writer.writeheader();writer.writerows(items)
    counts=Counter(r["status"] for r in rows)
    by_type={t:Counter(r["status"] for r in rows if r["scope"]==t) for t in ("post","page")}
    priority_rows=sorted((r for r in rows if r["found_qa"]),
                         key=lambda r:(-r["found_qa"],r["scope"]!="page",r["url"]))
    lines=["# China AI Search FAQ Audit — full URL Matrix","",
           "Audit-only: source Q&A candidates, NOT AI visibility or Google index confirmation.","",
           "## Scope","",
           "- Repo: thuexemayhanoi/china; live domain: "+DOMAIN,
           "- Inspected 300 Markdown posts and 31 core HTML pages; 331 unique URLs and complete CN-0001 to CN-0300 IDs.",
           "- The /faq/ page renders 12 central questions from _data/faqs.json; schema_faq is already enabled for that page.",
           "- No new FAQ or schema added. Google retired FAQ rich results in May 2026; do not add generic FAQPage to every blog post.",
           "- Question-heading with adjacent substantive paragraph = candidate Q&A, NOT verified FAQ. Human review is required.","",
           "## Classifications","",
           "| Class | Total URLs | Posts | Pages |","|---|---:|---:|---:|"]
    for k in ("CURATED_FAQ","EXISTING_QA_CANDIDATE","QUESTION_WITHOUT_CLEAR_ANSWER","NO_EXPLICIT_QA"):
        lines.append("| "+k+f" | {counts[k]} | {by_type['post'][k]} | {by_type['page'][k]} |")
    lines+=["",f"- Evidence matrix includes {len(details)} existing question/adjacent-answer candidate rows.","",
            "## Highest-priority existing question pages","",
            "| URL | Q&A candidates | Status |","|---|---:|---|"]
    for r in priority_rows[:45]:
        lines.append(f'| [{r["url"][len(DOMAIN):]}]({r["url"]}) | {r["found_qa"]} | {r["status"]} |')
    lines+=["","## Implementation sequence — not executed","",
            "1. P0: fact-check 12 central FAQ answers against store policies and official legal sources. Retain current centralized source and visible FAQ.",
            "2. P1: review real on-page question headings and answer excerpts. Prioritize answer-first summaries, unique usefulness and contextual same-topic links. No invented facts.",
            "3. P1: for question headings with weak adjacent answers, review context manually before adding any text.",
            "4. P2/P3: informational posts and core pages with no explicit FAQ are not automatically missing FAQ. Don't inject boilerplate.",
            "5. Structured data: preserve existing WebSite, LocalBusiness, BlogPosting and BreadcrumbList. Do not blanket-inject FAQPage or QAPage.",
            "6. Regression QA for future edits: preserve all 300 posts, 331 sitemap routes, canonical, indexability, language and production Pages deploy.","",
            "## Evidence files","",
            "- AI-SEARCH-FAQ-URL-MATRIX.csv: all 331 URLs, priorities and review status.",
            "- AI-SEARCH-FAQ-QUESTION-EVIDENCE.csv: existing questions and adjacent answers with source paths.","",
            "## Limits","",
            "- Source-level inspection, not full live browser crawl of 331 pages. HTML includes are not rendered except /faq/ shared JSON.",
            "- Answers have not been human fact-checked; Google, Baidu, AI Overviews, ChatGPT citations and GSC performance not measured."]
    (OUT/"AI-SEARCH-FAQ-AUDIT.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    print(json.dumps(dict(urls=len(rows),posts=len(posts),pages=len(pages),central_faq=len(faqs),
        candidate_pairs=len(details),by_status=dict(counts)),ensure_ascii=False))

if __name__=="__main__":main()
