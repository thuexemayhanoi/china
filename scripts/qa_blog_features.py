#!/usr/bin/env python3
"""Dependency-free checks for the shared CHINA blog features.
Usage: python3 scripts/qa_blog_features.py source|built|make-fixtures|fixtures|disable|disabled
Temporary fixtures are generated only inside GitHub Actions' disposable checkout.
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"
POSTS = ROOT / "_posts"
URL_BASE = "https://zh.rentbikehanoi.com"
FIXTURES = {
    "2026-10-01-ci-scooter-one.md": ("测试踏板车首篇", "rental", "rental/scooters", "租车关键字A", "租车车型二级标题", "租车车型三级标题"),
    "2026-10-02-ci-scooter-two.md": ("测试踏板车次篇", "rental", "rental/scooters", "租车关键字B", "停车安全二级标题", "停车安全三级标题"),
    "2026-10-03-ci-monthly-other.md": ("测试月租独立篇", "rental", "rental/monthly", "月租关键字C", "月租内容二级标题", "月租内容三级标题"),
    "2026-10-04-ci-pricing-other.md": ("测试价格独立篇", "pricing", "pricing/daily", "租金关键字D", "租金内容二级标题", "租金内容三级标题"),
}
def require(condition, message):
    if not condition:
        raise AssertionError(message)

def read(path):
    return (ROOT / path).read_text(encoding="utf-8")

def check_source():
    config = json.loads(read("_data/site.json"))
    flags = config["features"]
    for key in ("smart_search", "show_post_navigation", "show_author_box"):
        require(flags.get(key) is True, key + " feature flag not enabled")
    require(config["publisher"]["logo"] == "/assets/favicon.svg", "publisher logo should be site brand mark")
    header = read("_includes/header.html")
    layout = read("_layouts/default.html")
    post = read("_layouts/post.html")
    index = read("assets/search/posts.json")
    js = read("assets/blog-search.js")
    require("smart-search-trigger.html" in header, "missing shared header search trigger")
    require("smart-search.html" in layout and "blog-search.js" in layout, "missing lazy search integration")
    require("post-footer.html" in post, "post layout missing centralized post-footer hook")
    require("site.posts" in index and "p.content | markdownify" in index, "search index not generated from published post HTML")
    require("primary_keyword" in index and "h2_parts" in index and "h3_parts" in index, "search index fields missing")
    require("fetch(\"/assets/search/posts.json\"" in js, "search doesn't fetch generated index")
    require("button.addEventListener(\"click\",open)" in js, "search data should load on user activation")
    require("fetch(" not in read("assets/site.js"), "existing navigation JS should not fetch the search index")
    require("where: \"seo_silo\"" in read("_includes/post-navigation.html"), "missing same-silo filtering")
    require("where: \"topic\"" in read("_includes/post-navigation.html"), "missing category fallback")
    require("site.data.site.business.name" in read("_includes/author-box.html"), "publisher not using shared actual business")
    require("rel=\"prev\"" in read("_includes/post-navigation.html"), "missing previous article")
    require("rel=\"next\"" in read("_includes/post-navigation.html"), "missing next article")
    require("post-footer.html" in post, "post layout must use shared post-footer hook")
    footer = read("_includes/post-footer.html")
    for slot in ("post-navigation.html", "author-box.html", "cta.html", "related-posts.html", "post-hub-links.html"):
        require(slot in footer, "post footer missing reusable slot "+slot)
    require(flags.get("show_post_hub_links") is True, "hub link feature flag not enabled")
    cta = config["post_ui"]["cta"]["default"]
    require(cta["title"]=="确认租车需求" and cta["href"]=="/contact/", "default CTA source config or destination changed")
    require("site.data.site.post_ui.cta.default" in read("_includes/cta.html"), "CTA not read from shared site config")
    require("where: \"seo_silo\"" in read("_includes/related-posts.html"), "related posts must prefer same SEO silo")
    require("where: \"topic\"" in read("_includes/related-posts.html"), "related posts missing topic fallback")
    hubs=config["post_ui"]["hub_links"]
    require(set(hubs)=={"rental","pricing","50cc","old-quarter","guides"}, "hub mappings must follow existing topics")
    for topic,links in hubs.items():
        require(3<=len(links)<=8, "links outside curated 3-8 range: "+topic)
        urls=[l["href"] for l in links]
        require(len(set(urls))==len(urls), "duplicate hub links "+topic)
        require(all(u in config["sitemap_base"] for u in urls), "hub must point at existing indexed pages "+topic)
    require("site.data.site.sitemap_base contains hub.href" in read("_includes/post-hub-links.html"), "hub partial must refuse stale URLs")
    for path in ("CNAME", "assets/assistant-cn.js", "assets/assistant-cn.css", "assets/chat/site-index.json"):
        require((ROOT / path).exists(), "missing protected integration "+path)

def check_built(fixtures=False, disabled=False):
    require(SITE.is_dir(), "Jekyll output missing")
    index_path = SITE / "assets/search/posts.json"
    require(index_path.is_file(), "generated JSON index missing")
    entries = json.loads(index_path.read_text(encoding="utf-8"))
    require(isinstance(entries,list), "generated index must be JSON array")
    # Every listed URL must correspond to a generated, published post. No _drafts.
    for item in entries:
        require(item["url"].startswith("/blog/"), "unexpected blog URL in index")
        require((SITE / item["url"].strip("/") / "index.html").exists(),
                "broken index link "+item["url"])
        require(isinstance(item["headings"],list), "headings must be an array")
    homepage = (SITE / "index.html").read_text(encoding="utf-8")
    blog = (SITE / "blog/index.html").read_text(encoding="utf-8")
    if disabled:
        require('id="smart-search-trigger"' not in homepage, "disabled search trigger leaked")
        require('id="smart-search"' not in homepage, "disabled search modal leaked")
    else:
        require(homepage.count('id="smart-search-trigger"') == 1, "must have exactly one search trigger")
        require(homepage.count('id="smart-search"') == 1, "must have exactly one search modal")
        require('rel="canonical" href="'+URL_BASE+'/"' in homepage, "home canonical changed")
        require('id="china-chat-fab"' not in homepage, "dynamic chatbot must not be duplicated by template")
        require("blog-enhancements.css" in homepage, "feature styles missing")
    require('rel="canonical" href="'+URL_BASE+'/blog/"' in blog, "blog canonical changed")
    sitemap = (SITE / "sitemap.xml").read_text(encoding="utf-8")
    require(sitemap.count("<loc>") == len(json.loads(read("_data/site.json"))["sitemap_base"])+len(entries),
            "sitemap count changed beyond published posts")
    if not fixtures:
        actual_post_count = sum(1 for p in POSTS.glob("*.md")) if POSTS.exists() else 0
        require(len(entries)==actual_post_count,"search index count should match published posts")
        return
    require(len(entries)>=len(FIXTURES),"expected fixture posts in Jekyll index")
    by_url={x["url"]:x for x in entries}
    for filename,(title,topic,silo,keyword,h2,h3) in FIXTURES.items():
        slug=filename[11:-3]
        url="/blog/"+slug+"/"
        require(url in by_url,"fixture missing from JSON index: "+url)
        item=by_url[url]
        require(item["title"]==title and item["keyword"]==keyword and item["topic"]==topic,
                "fixture title/keyword/topic not indexed "+url)
        require(h2 in item["headings"], "H2 not indexed "+url)
        require(h3 in item["headings"], "H3 not indexed "+url)
        page=(SITE / url.strip("/") / "index.html").read_text(encoding="utf-8")
        require('rel="canonical" href="'+URL_BASE+url+'"' in page, "post canonical changed")
        if not disabled:
            require("post-publisher-card" in page and "Cho Thuê Xe Máy Nguyễn Tú" in page,
                    "author box missing real publisher")
            require("/assets/favicon.svg" in page, "publisher logo missing")
    older=(SITE/"blog/ci-scooter-one/index.html").read_text(encoding="utf-8")
    newer=(SITE/"blog/ci-scooter-two/index.html").read_text(encoding="utf-8")
    monthly=(SITE/"blog/ci-monthly-other/index.html").read_text(encoding="utf-8")
    pricing=(SITE/"blog/ci-pricing-other/index.html").read_text(encoding="utf-8")
    if disabled:
        for page in (older,newer,monthly,pricing):
            require("post-publisher-card" not in page, "disabled publisher leaked")
            require("post-navigation-item" not in page, "disabled post navigation leaked")
            require("post-hub-links" not in page, "disabled contextual hub links leaked")
            require("确认租车需求" not in page, "disabled CTA leaked")
            require('class="card-id">相关阅读' not in page, "disabled related posts leaked")
    else:
        for page in (older,newer,monthly,pricing):
            require("确认租车需求" in page, "centralized default CTA missing")
            require("租金、车型、押金与取还车安排均需在签约前确认。" in page,
                    "centralized CTA copy changed")
            require('href="'+URL_BASE+'/contact/"' in page, "central CTA destination broken")
            require("post-hub-links" in page, "contextual hub links missing")
        require('href="'+URL_BASE+'/topics/rental/"' in older, "rental topic hub missing")
        require('href="'+URL_BASE+'/topics/pricing/"' in pricing, "pricing topic hub missing")
        require(older.count('class="card-id">相关阅读')==1,
                "expected exactly one same-silo related post")
        require(newer.count('class="card-id">相关阅读')==1,
                "expected exactly one reciprocal related post")
        require('class="card-id">相关阅读' not in monthly,
                "isolated monthly silo must not link to a different silo")
        require('class="card-id">相关阅读' not in pricing,
                "isolated pricing silo must not invent related posts")
        require('rel="next" href="'+URL_BASE+'/blog/ci-scooter-two/"' in older,
                "older post must link to newer article in same silo")
        require('rel="prev" href="'+URL_BASE+'/blog/ci-scooter-one/"' in newer,
                "newer post must link back to older article in same silo")
        require("post-navigation-item" not in monthly and "post-navigation-item" not in pricing,
                "cross-silo or missing-post navigation must not render")
        for page in (older,newer):
            # Existing Related Posts intentionally uses broad topic grouping.
            # Enforce the stricter silo rule ONLY inside the Previous/Next nav.
            found = re.search(r'<nav class="post-navigation section"[^>]*>(.*?)</nav>', page, re.S)
            require(found is not None, "expected same-silo navigation block")
            nav_html = found.group(1)
            require("/blog/ci-monthly-other/" not in nav_html and "/blog/ci-pricing-other/" not in nav_html,
                    "cross-silo Previous/Next link leaked")
def make_fixtures():
    POSTS.mkdir(parents=True,exist_ok=True)
    for name,(title,topic,silo,keyword,h2,h3) in FIXTURES.items():
        dst=POSTS/name
        require(not dst.exists(),"fixture already present "+name)
        permalink="/blog/"+name[11:-3]+"/"
        front={"layout":"post","title":title,"description":"测试文章描述，用于验证静态站点功能，不会发布到线上。","permalink":permalink,
               "topic":topic,"seo_silo":silo,"primary_keyword":keyword}
        lines=["---"]+[f'{k}: {json.dumps(v,ensure_ascii=False)}' for k,v in front.items()]
        lines += [f'date: "{name[:10]} 10:00:00 +0700"',"---","","## "+h2,
                  "专供CI测试的第二级章节。","","### "+h3,"这是第三级章节，供搜索索引验证。"]
        dst.write_text("\n".join(lines)+"\n",encoding="utf-8")
    print("Created 4 disposable CI-only post fixtures (NOT committed/published)")
def disable():
    p=ROOT/"_data/site.json"
    config=json.loads(p.read_text(encoding="utf-8"))
    for key in ("smart_search","show_post_navigation","show_author_box","show_post_hub_links","show_related_posts","show_post_cta"):
        config["features"][key]=False
    p.write_text(json.dumps(config,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
def main():
    command=sys.argv[1] if len(sys.argv)>1 else "source"
    if command=="source":check_source()
    elif command=="built":check_built()
    elif command=="make-fixtures":make_fixtures()
    elif command=="fixtures":check_built(fixtures=True)
    elif command=="disable":disable()
    elif command=="disabled":check_built(fixtures=True,disabled=True)
    else:raise ValueError("Unknown command "+command)
    print("CHINA BLOG FEATURES QA PASS:",command)
if __name__=="__main__":
    try:main()
    except (AssertionError,ValueError,KeyError,FileNotFoundError) as e:
        print("CHINA BLOG FEATURES QA FAIL:",e,file=sys.stderr)
        sys.exit(1)
