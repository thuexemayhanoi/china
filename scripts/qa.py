#!/usr/bin/env python3
"""Dependency-free source checks for the CHINA Jekyll blog. Run: python3 scripts/qa.py"""
from pathlib import Path
import json
import re
import sys

root = Path(__file__).resolve().parents[1]
errors = []
def check(ok, reason):
    if not ok:
        errors.append(reason)

site = json.loads((root / "_data/site.json").read_text(encoding="utf-8"))
nav = json.loads((root / "_data/navigation.json").read_text(encoding="utf-8"))
prices = json.loads((root / "_data/vehicles.json").read_text(encoding="utf-8"))
faq = json.loads((root / "_data/faqs.json").read_text(encoding="utf-8"))

# Central FAQ answer content and schema must have one source and verified links.
keys = [item.get("key") for item in faq]
check(len(faq) == 12 and len(set(keys)) == 12 and all(keys), "12 unique FAQ answer keys")
for item in faq:
    check(bool(item.get("q")) and len(item.get("a", "")) >= 30,
          "FAQ question/answer missing for "+str(item.get("key")))
    check(item.get("more_path") in site["sitemap_base"],
          "FAQ destination missing from 31 approved core URLs: "+str(item.get("key")))
    if item.get("source_url"):
        check(item["source_url"].startswith("https://vbpl.vn/"),
              "FAQ external legal source must use official legal database")
faq_include = (root / "_includes/faqs.html").read_text(encoding="utf-8")
faq_schema = (root / "_includes/schema.html").read_text(encoding="utf-8")
faq_answer = (root / "_includes/faq-answer.html").read_text(encoding="utf-8")
check("include faq-answer.html f=f" in faq_include and
      "include faq-answer.html f=f" in faq_schema,
      "FAQ visible content and JSON-LD must use identical answer renderer")
for field in ("site.data.site.business.address", "site.data.site.business.phone_display",
              "site.data.site.business.hours", "site.data.vehicles[0].display.day"):
    check(field in faq_answer, "FAQ dynamic data source missing: "+field)

pages = sorted(root.rglob("index.html"))
check(site["domain"] == "https://zh.rentbikehanoi.com", "canonical domain")
check((root / "CNAME").read_text(encoding="utf-8").strip() == "zh.rentbikehanoi.com", "CNAME")
branding = site.get("branding", {})
for key in ("mark", "wordmark", "header_subtitle", "footer_subtitle"):
    check(isinstance(branding.get(key), str) and bool(branding[key].strip()), "shared branding missing " + key)
for filename in ("_includes/header.html", "_includes/footer.html"):
    source = (root / filename).read_text(encoding="utf-8")
    check("site.data.site.branding.mark" in source and "site.data.site.branding.wordmark" in source,
          filename + " must use shared brand")
author_box = (root / "_includes/author-box.html").read_text(encoding="utf-8")
check("site.data.site.post_ui.cta.default" in author_box, "publisher CTA not shared")
llms_source = (root / "llms.txt")
check(llms_source.is_file(), "llms.txt missing")
if llms_source.is_file():
    guide = llms_source.read_text(encoding="utf-8")
    check("site.data.navigation" in guide and "site.data.site.business" in guide,
          "llms guide must use shared navigation and business data")
    check(guide.startswith("---\n") and "permalink: /llms.txt" in guide,
          "llms guide requires Jekyll front matter and fixed URL")

check(len(pages) == 31, "expected 31 core HTML pages, got %d" % len(pages))
check(len(site["sitemap_base"]) == 31, "31 sitemap base URLs")
check(sum(len(n.get("children",[])) for n in nav) >= 19, "new child categories missing from navigation")
check(len(prices) == 6 and len(faq) == 12, "vehicle/FAQ counts")
check([n["href"] for n in nav][:2] == ["/", "/about/"], "About must follow Home")
check([n["href"] for n in nav][-4:] == ["/faq/", "/contact/", "/privacy/", "/terms/"], "FAQ/Contact/Privacy/Terms order")
check(len(set(n["href"] for n in nav)) == len(nav), "duplicate main navigation URL")
urls = set()
for page in pages:
    html = page.read_text(encoding="utf-8")
    check(html.startswith("---\n"), str(page) + " missing Jekyll front matter")
    match = re.search(r'^permalink: "([^"]+)"$', html, re.M)
    check(bool(match), str(page) + " missing permalink")
    if match:
        check(match.group(1) not in urls, "duplicate permalink " + match.group(1))
        urls.add(match.group(1))
    check(bool(re.search(r'^title:', html, re.M)), str(page) + " missing title")
    check(bool(re.search(r'^description:', html, re.M)), str(page) + " missing description")
    check("<h1" in html, str(page) + " missing H1")
    check("<header class=\"site-header\">" not in html, str(page) + " duplicated header")
    check("<footer class=\"footer\">" not in html, str(page) + " duplicated footer")
for item in nav:
    check(item["href"] in urls, "bad navigation " + item["href"])
    for child in item.get("children", []):
        check(child["href"] in urls, "bad subnav " + child["href"])
for p in site["sitemap_base"]:
    check(p in urls, "bad sitemap base " + p)
for path in ("_layouts/default.html", "_layouts/post.html", "_includes/schema.html", "_includes/navigation.html", "_includes/footer-navigation.html", "_includes/sidebar.html", "_includes/calculator.html", "_includes/pricing-table.html", "_includes/blog-posts.html", "_includes/topic-posts.html"):
    check((root / path).is_file(), "missing " + path)
# Quick Call / chatbot must only use our own Chinese public content and centralized data.
index = root / "assets/chat/site-index.json"
assistant = root / "assets/assistant-cn.js"
assistant_css = root / "assets/assistant-cn.css"
layout = (root / "_layouts/default.html").read_text(encoding="utf-8")
check(site["features"].get("quick_contact") is True, "Quick Call flag disabled")
check(site["features"].get("local_chatbot") is True, "local chatbot flag disabled")
check((root / "_includes/assistant-data.html").is_file(), "missing shared assistant config")
for file in (index, assistant, assistant_css):
    check(file.is_file(), "missing " + str(file))
check("assets/assistant-cn.js" in layout and "assets/assistant-cn.css" in layout, "assistant assets not in default layout")
check("assets/chat/site-index.json" in assistant.read_text(encoding="utf-8"), "assistant missing local search index")
check("site.data.faqs" in index.read_text(encoding="utf-8"), "search index not generated from FAQs")
check("site.posts" in index.read_text(encoding="utf-8"), "search index not generated from published posts")
check("fr.rentbikehanoi.com" not in assistant.read_text(encoding="utf-8"), "French site link accidentally copied")
check("https://wa.me/84942467674" == site["business"].get("whatsapp"), "WhatsApp number mismatch")
check("https://zalo.me/0942467674" == site["business"].get("zalo"), "Zalo number mismatch")

# AEO implementation Matrix must distinguish real edits from pending reviews.
import csv
impl_matrix = root / "docs/AI-SEARCH-FAQ-IMPLEMENTATION-MATRIX.csv"
if impl_matrix.is_file():
    with impl_matrix.open(encoding="utf-8-sig", newline="") as fh:
        all_url_rows = list(csv.DictReader(fh))
    check(len(all_url_rows) == 331, "AI FAQ implementation Matrix must retain 331 URL rows")
    check(len({row["url"] for row in all_url_rows}) == 331,
          "AI FAQ implementation Matrix has duplicate URLs")
    refined_pages = [row for row in all_url_rows if row["implementation_status"] == "P1_ANSWER_REFINED"]
    for row in refined_pages:
        url = row["url"]
        prefix = site["domain"] + "/"
        check(url.startswith(prefix) and url.endswith("/"), "Invalid refined P1 URL: "+url)
        if not (url.startswith(prefix) and url.endswith("/")): continue
        route = url[len(prefix):]
        source_file = root / route / "index.html"
        check(source_file.is_file(), "Missing P1 page source: "+route)
        if not source_file.is_file(): continue
        content = source_file.read_text(encoding="utf-8")
        check("<h2" in content and "<strong>" in content,
              "Refined Q&A must have a specific answer: "+route)
        check("site.data.site." in content and "site.data.site.domain" in content,
              "Refined answer should link from shared site config: "+route)
        check("schema_faq: true" not in content and '"@type":"FAQPage"' not in content,
              "Do not inject FAQ rich result schema onto general pages: "+route)
    changed = [row for row in all_url_rows if row["implementation_status"] == "P2_ANSWER_FIRST_REVISED"]
    revised_pages = [row for row in all_url_rows if row["implementation_status"] == "P1_CONTENT_REVISED"]
    for row in revised_pages:
        url = row["url"]
        prefix = site["domain"] + "/"
        check(url.startswith(prefix) and url.endswith("/"),
              "Invalid P1 topic URL: "+url)
        if not (url.startswith(prefix) and url.endswith("/")): continue
        relative = url[len(prefix):]
        topic_source = root / relative / "index.html"
        check(topic_source.is_file(), "P1 revised topic source missing: "+relative)
        if not topic_source.is_file(): continue
        html_source = topic_source.read_text(encoding="utf-8")
        check(html_source.count('<section class="inner-panel">') >= 3,
              "P1 revised topic needs three substantive question sections: "+relative)
        check("本专题的主要内容" not in html_source and "其他相关租车指南" not in html_source,
              "P1 revised topic still has generic template text: "+relative)
        check("site.data.site.domain" in html_source and "<strong>" in html_source,
              "P1 revised topic needs evidence-backed direct answers and live internal links: "+relative)
        check("schema_faq: true" not in html_source,
              "Do not inject FAQPage schema into topical guide pages: "+relative)
    post_sources = {}
    for post in (root / "_posts").glob("*.md"):
        source = post.read_text(encoding="utf-8")
        ident = re.search(r'^article_id:\s*"?(CN-\d{4})"?', source, re.M)
        if ident: post_sources[ident.group(1)] = source
    for row in changed:
        ident = row["article_id"]
        source = post_sources.get(ident, "")
        check(bool(source), "AEO edited article missing: "+ident)
        check(bool(re.search(r'^last_modified_at:\s*"?\d{4}-\d{2}-\d{2}"?', source, re.M)),
              "AEO revised post needs last_modified_at: "+ident)
        body = source.split("\n---\n", 1)[-1]
        intro = body.split("\n\n##",1)[0]
        check("**" in intro and len(intro) >= 70,
              "AEO revised post missing direct, highlighted opening answer: "+ident)

post_count = len(list((root / "_posts").glob("*.md"))) if (root / "_posts").exists() else 0
if errors:
    print("CHINA QA FAILED:")
    print("\n".join(" - " + e for e in errors))
    sys.exit(1)
print("CHINA source QA passed: %d pages, %d nav items, %d posts, stable canonical." % (len(pages), len(nav), post_count))
