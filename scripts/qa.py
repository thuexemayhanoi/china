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
post_count = len(list((root / "_posts").glob("*.md"))) if (root / "_posts").exists() else 0
if errors:
    print("CHINA QA FAILED:")
    print("\n".join(" - " + e for e in errors))
    sys.exit(1)
print("CHINA source QA passed: %d pages, %d nav items, %d posts, stable canonical." % (len(pages), len(nav), post_count))
