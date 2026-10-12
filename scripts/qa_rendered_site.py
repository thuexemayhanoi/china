#!/usr/bin/env python3
"""Built-site SEO and internal-link integrity checks (stdlib only)."""
from html.parser import HTMLParser
from html import unescape
from pathlib import Path
from urllib.parse import urlparse, unquote
import json
import re
import sys
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/"_site"
CONFIG=json.loads((ROOT/"_data/site.json").read_text(encoding="utf-8"))
ORIGIN=CONFIG["domain"]
EXPECTED=set(CONFIG["sitemap_base"])
class Parse(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title=False;self.titles=[];self.h1=0
        self.canon=[];self.alternates=[];self.desc=[];self.robots=[];self.langs=[];self.verifications=[];self.links=[];self.imgs=[]
        self.script=False;self.scripts=[];self.buff=""
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if tag=="title":self.title=True
        if tag=="html":self.langs.append(d.get("lang",""))
        if tag=="h1":self.h1+=1
        if tag=="link" and d.get("rel")=="canonical":self.canon.append(d.get("href",""))
        if tag=="link" and d.get("rel")=="alternate" and d.get("type")=="text/plain":self.alternates.append(d.get("href",""))
        if tag=="meta" and d.get("name")=="description":self.desc.append(d.get("content",""))
        if tag=="meta" and d.get("name")=="robots":self.robots.append(d.get("content",""))
        if tag=="meta" and d.get("name")=="google-site-verification":self.verifications.append(d.get("content",""))
        if tag=="a" and d.get("href"):self.links.append(d["href"])
        if tag=="img":self.imgs.append(d)
        if tag=="script" and d.get("type")=="application/ld+json":self.script=True;self.buff=""
    def handle_data(self,data):
        if self.title:self.titles.append(data)
        if self.script:self.buff+=data
    def handle_endtag(self,tag):
        if tag=="title":self.title=False
        if tag=="script" and self.script:self.scripts.append(self.buff);self.script=False
def file_for(path):
    clean=unquote(urlparse(path).path)
    if not clean.startswith("/") or ".." in Path(clean).parts:return None
    target=DEST/clean.lstrip("/")
    if clean.endswith("/"):target=target/"index.html"
    elif not target.suffix:target=target/"index.html"
    return target
def main():
    errors=[]
    def check(cond,msg):
        if not cond:errors.append(msg)
    sitemap=DEST/"sitemap.xml"
    guide=DEST/"llms.txt"
    check(guide.is_file(),"Missing Jekyll-rendered llms.txt")
    if guide.is_file():
        guide_text=guide.read_text(encoding="utf-8")
        check("{{" not in guide_text and "{%" not in guide_text,
              "llms.txt Liquid templates were not rendered")
        for required in ("/blog/", "/prices/", "/faq/", "/contact/", "/sitemap.xml"):
            check("]("+ORIGIN+required+")" in guide_text,
                  "llms.txt missing important discovery route "+required)
        check(CONFIG["business"]["name"] in guide_text,
              "llms.txt business name not sourced from central config")
    check(sitemap.exists(),"Missing sitemap.xml")
    if not sitemap.exists():raise AssertionError(errors)
    data=ET.parse(sitemap).getroot()
    listed=[(n.text or "").strip() for n in data.iter() if n.tag.endswith("loc")]
    check(len(listed)==len(set(listed)),"Duplicated sitemap loc URL")
    for url in EXPECTED:check(ORIGIN+url in listed,"Missing 26-core sitemap URL: "+url)
    generated_index=DEST/"assets/search/posts.json"
    check(generated_index.exists(),"Missing generated post-search JSON")
    posts=json.loads(generated_index.read_text(encoding="utf-8")) if generated_index.exists() else []
    intended=set(EXPECTED)|{p["url"] for p in posts}
    check(set(listed)=={ORIGIN+x for x in intended},"Sitemap not equal to published pages + actual posts")
    for route in sorted(intended):
        dest=file_for(route)
        check(bool(dest and dest.exists()),"Missing output HTML for "+route)
        if not dest or not dest.exists():continue
        raw=dest.read_text(encoding="utf-8")
        parser=Parse();parser.feed(raw)
        check(parser.h1==1,f"{route}: expected 1 H1, got {parser.h1}")
        check(len(parser.canon)==1 and parser.canon[0]==ORIGIN+route,f"{route}: invalid canonical {parser.canon}")
        check(parser.alternates==[ORIGIN+"/llms.txt"],f"{route}: llms discovery link missing/duplicate {parser.alternates}")
        check(parser.langs==["zh-CN"],f"{route}: expected default Simplified Chinese HTML lang, got {parser.langs}")
        check([r.lower().replace(" ","") for r in parser.robots]==["index,follow"],f"{route}: robots indexability regressed {parser.robots}")
        check(parser.verifications==["HwLeUnxn5y1nBbGQD-54b3hR_dw10qMQ12wfmuDPfBg"],f"{route}: Google site verification tag changed or missing")
        check(len(parser.titles)>=1 and 0<len("".join(parser.titles).strip())<155,route+": blank/excessively long title")
        check(len(parser.desc)==1 and parser.desc[0].strip(),route+": missing meta description")
        check(all("alt" in img for img in parser.imgs),route+": image missing alt attribute")
        check(bool(parser.scripts),route+": JSON-LD missing")
        if route=="/faq/":
            # The page includes structured Q&A ONLY when all 12 answers are visible.
            expected_faq=json.loads((ROOT/"_data/faqs.json").read_text(encoding="utf-8"))
            pairs=re.findall(r'<details>\\s*<summary>(.*?)</summary>\\s*<p>(.*?)</p>',raw,re.S)
            def plain(value):
                return unescape(re.sub(r"<[^>]*>","",value)).strip()
            pairs=[(plain(q),plain(a)) for q,a in pairs]
            check(len(pairs)==len(expected_faq)==12,"FAQ should render exactly 12 visible pairs")
            graph=[]
            try:
                for code in parser.scripts:graph.extend(json.loads(code).get("@graph",[]))
            except (json.JSONDecodeError,AttributeError) as exc:
                errors.append("FAQ schema parse error: "+str(exc))
            faq_nodes=[n for n in graph if n.get("@type")=="FAQPage"]
            check(len(faq_nodes)==1,"FAQ page should have one FAQPage node")
            if faq_nodes and len(pairs)==len(expected_faq):
                claims=[(q.get("name"),q.get("acceptedAnswer",{}).get("text")) for q in faq_nodes[0].get("mainEntity",[])]
                check(len(claims)==12,"FAQ schema should contain exactly 12 Q&A entries")
                check(claims==pairs,"FAQ schema answers differ from what visitors see")
                check([q for q,a in pairs]==[x["q"] for x in expected_faq],
                      "FAQ visible questions no longer match central data")
                for amount in ("address", "phone_display", "hours"):
                    value=CONFIG["business"][amount]
                    check(any(value in a for q,a in pairs),
                          "FAQ failed to render central business fact: "+amount)
                vehicles=json.loads((ROOT/"_data/vehicles.json").read_text(encoding="utf-8"))
                for vehicle in vehicles[:5]:
                    check(vehicle["display"]["day"] in pairs[8][1],
                          "Daily price in FAQ is not sourced from vehicles.json: "+vehicle["name"])
                check("vbpl.vn/TW/Pages/vbpq-toanvan.aspx?ItemID=170620" in raw,
                      "FAQ must link to official statute for 50cc eligibility")
        for code in parser.scripts:
            try:
                obj=json.loads(code)
                types=[n.get("@type") for n in obj.get("@graph",[])]
                check("LocalBusiness" in types,route+": existing LocalBusiness schema missing")
                check("WebSite" in types,route+": existing WebSite schema missing")
                if route not in EXPECTED:
                    check("BlogPosting" in types,route+": published article schema missing")
            except (json.JSONDecodeError,AttributeError) as exc:
                errors.append(f"{route}: invalid JSON-LD {exc}")
        for href in parser.links:
            parsed=urlparse(href)
            if parsed.scheme in ("mailto","tel","sms","javascript","data"):continue
            if parsed.scheme and parsed.scheme not in ("http","https"):continue
            if parsed.netloc and parsed.netloc!=urlparse(ORIGIN).netloc:continue
            if not parsed.path or parsed.path=="/#":continue
            destlink=file_for(parsed.path)
            if destlink and not destlink.is_file():
                errors.append(f"{route}: broken same-site link {href}")
    if errors:
        print("Rendered CHINA SEO/links QA FAIL:")
        print("\n".join(" - "+e for e in errors[:60]))
        sys.exit(1)
    print(f"Rendered CHINA SEO/links QA PASS: {len(intended)} pages, {len(posts)} real posts, valid sitemap, canonicals, zh-CN, indexability, Google verification, schema, H1, titles, alt and links.")
if __name__=="__main__":main()
