#!/usr/bin/env python3
"""Read-only CHINA SEO inventory and search-intent watch; Python stdlib only.

Run after a GitHub Pages-compatible Jekyll build:
    python3 scripts/seo_monitor.py --output /tmp/china-seo-monitor.json

This verifies generated output. It cannot query Search Console, Bing, Baidu,
PageSpeed field data or prove indexing/search-engine citation.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
from html import unescape
from pathlib import Path
import json
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ZH = re.compile(r"[\u3400-\u9fff]")
SCALAR = re.compile(r'^([a-z_]+):[ \t]*(.*?)\s*$', re.M)
JSON_LD = re.compile(r'<script\b[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', re.S | re.I)
CANONICAL = re.compile(r'<link\b[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']+)', re.I)
ROBOTS = re.compile(r'<meta\b[^>]*name=["\']robots["\'][^>]*content=["\']([^"\']+)', re.I)


def frontmatter(raw: str) -> tuple[dict[str, str], str]:
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", raw, re.S)
    if not match:
        return {}, raw
    props = {key: value.strip().strip('"').strip("'") for key, value in SCALAR.findall(match.group(1))}
    return props, raw[match.end():]


def normalize(value: str) -> str:
    return re.sub(r"[^\w\u3400-\u9fff]+", "", unicodedata.normalize("NFKC", value).casefold()).replace("_", "")


def main() -> int:
    cli = argparse.ArgumentParser()
    cli.add_argument("--output", default="/tmp/china-seo-monitor.json")
    args = cli.parse_args()
    errors: list[str] = []
    warnings: list[str] = []
    config = json.loads((ROOT / "_data/site.json").read_text(encoding="utf-8"))
    origin = config["domain"].rstrip("/")
    base = config["sitemap_base"]
    files = sorted((ROOT / "_posts").glob("*.md"))
    ids: list[str] = []
    paths: list[str] = []
    title_groups: dict[str, list[str]] = defaultdict(list)
    intent_groups: dict[str, list[str]] = defaultdict(list)
    short_posts: list[str] = []
    low_structure: list[str] = []
    outside_sources = 0
    for file in files:
        meta, body = frontmatter(file.read_text(encoding="utf-8"))
        ident = meta.get("article_id", file.name)
        ids.append(ident)
        permalink = meta.get("permalink", "")
        paths.append(permalink)
        if not permalink.startswith("/blog/") or not permalink.endswith("/"):
            errors.append(f"{ident}: missing or invalid blog permalink")
        title = meta.get("title", "")
        description = meta.get("description", "")
        keyword = meta.get("primary_keyword", "")
        if not title or not description:
            errors.append(f"{ident}: missing title or description")
        title_groups[normalize(title)].append(ident)
        if keyword:
            intent_groups[normalize(keyword)].append(ident)
        if len(ZH.findall(body)) < 800:
            short_posts.append(ident)
        if len(re.findall(r"^##\s+", body, re.M)) < 3:
            low_structure.append(ident)
        if re.search(r"https?://(?!zh\.rentbikehanoi\.com)", body, re.I):
            outside_sources += 1

    for field, values in (("article IDs", ids), ("permalinks", paths)):
        repeats = [value for value, count in Counter(values).items() if count > 1]
        if repeats:
            errors.append(f"Duplicate {field}: {', '.join(repeats[:10])}")
    exact_titles = {title: group for title, group in title_groups.items() if len(group) > 1}
    if exact_titles:
        errors.append(f"Duplicate normalized titles across {len(exact_titles)} sets")
    if short_posts:
        warnings.append(f"{len(short_posts)} posts under 800 Chinese characters; inspect editorial quality")
    if low_structure:
        warnings.append(f"{len(low_structure)} posts have fewer than three H2 sections")
    repeated_intents = sorted(
        ({"normalized_primary_keyword": key, "posts": len(members), "ids": members[:8]}
         for key, members in intent_groups.items() if len(members) > 1),
        key=lambda x: (-x["posts"], x["normalized_primary_keyword"])
    )
    if repeated_intents:
        warnings.append(f"{len(repeated_intents)} repeated keyword groups; investigate intent, not automatic duplicates")

    dest = ROOT / "_site"
    sitemap = dest / "sitemap.xml"
    seen_urls: list[str] = []
    if not sitemap.exists():
        errors.append("Rendered sitemap missing; run Jekyll first")
    else:
        try:
            seen_urls = [(node.text or "").strip() for node in ET.parse(sitemap).iter()
                         if node.tag.endswith("loc")]
        except ET.ParseError as exc:
            errors.append(f"Invalid sitemap XML: {exc}")
    expected_urls = {origin + path for path in (base + paths)}
    if len(seen_urls) != len(set(seen_urls)):
        errors.append("Duplicate sitemap URLs")
    if set(seen_urls) != expected_urls:
        errors.append(f"Sitemap mismatch: expected {len(expected_urls)}, found {len(set(seen_urls))}")
    if len(set(base + paths)) != len(base) + len(paths):
        errors.append("Duplicate canonical routes between pages and posts")
    robots = dest / "robots.txt"
    if not robots.exists():
        errors.append("Rendered robots.txt missing")
    else:
        robots_text = robots.read_text(encoding="utf-8")
        if "User-agent: *" not in robots_text or "Allow: /" not in robots_text:
            errors.append("Robots policy does not allow general crawling")
        if f"Sitemap: {origin}/sitemap.xml" not in robots_text:
            errors.append("Robots sitemap directive differs from canonical domain")

    measured = Counter()
    schema_errors: list[str] = []
    for route in base + paths:
        file = dest / route.lstrip("/") / "index.html" if route != "/" else dest / "index.html"
        if not file.is_file():
            errors.append(f"Missing rendered route: {route}")
            continue
        raw = file.read_text(encoding="utf-8")
        measured["pages_scanned"] += 1
        canons = CANONICAL.findall(raw)
        if canons != [origin + route]:
            errors.append(f"Canonical mismatch: {route}")
        else:
            measured["self_canonical"] += 1
        robot_tags = ROBOTS.findall(raw)
        if len(robot_tags) != 1 or "noindex" in robot_tags[0].lower() or "index" not in robot_tags[0].lower():
            errors.append(f"Indexability mismatch: {route}")
        else:
            measured["index_allowed"] += 1
        if re.search(r'<html\b[^>]*lang=["\']zh-CN["\']', raw):
            measured["zh_cn_lang"] += 1
        else:
            errors.append(f"Missing zh-CN document lang: {route}")
        if re.search(r'<meta\b[^>]*name=["\']viewport["\']', raw, re.I):
            measured["mobile_viewport"] += 1
        else:
            errors.append(f"Missing mobile viewport: {route}")
        if not re.search(r'<meta\b[^>]*name=["\']description["\']', raw, re.I):
            errors.append(f"Missing meta description: {route}")
        graph_types: set[str] = set()
        codes = JSON_LD.findall(raw)
        for code in codes:
            try:
                record = json.loads(unescape(code))
                nodes = record.get("@graph", [record])
                for node in nodes:
                    category = node.get("@type")
                    if isinstance(category, str):
                        graph_types.add(category)
            except (json.JSONDecodeError, AttributeError, TypeError) as exc:
                schema_errors.append(f"{route}: {exc}")
        required = {"WebSite", "LocalBusiness", "BlogPosting"} if route in paths else {"WebSite", "LocalBusiness"}
        missing = required - graph_types
        if missing:
            schema_errors.append(f"{route}: missing {','.join(sorted(missing))}")
        else:
            measured["schema_valid"] += 1
        if "BreadcrumbList" in graph_types:
            measured["breadcrumb_schema"] += 1

    if schema_errors:
        errors.extend(schema_errors[:30])
    report = {
        "audit": "CHINA SEO Foundation and intent monitor",
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "domain": origin,
        "source_posts": len(files),
        "planned_target": 300,
        "published_routes_expected": len(expected_urls),
        "sitemap_urls": len(seen_urls),
        "metrics": dict(measured),
        "posts_under_800_hanzi": len(short_posts),
        "sample_short_post_ids": short_posts[:15],
        "posts_with_fewer_than_3_h2": len(low_structure),
        "posts_with_external_links": outside_sources,
        "repeated_keyword_groups": repeated_intents[:25],
        "warnings": warnings,
        "errors": errors[:80],
        "search_engine_verification": {
            "google_indexed_urls": None,
            "bing_indexed_urls": None,
            "baidu_indexed_urls": None,
            "note": "Index counts require verified webmaster-console data, not sitemap enumeration.",
        },
        "mobile_field_cwv": None,
        "status": "PASS" if not errors else "FAIL",
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"CHINA SEO MONITOR {report['status']}: {len(files)} posts; {len(seen_urls)} sitemap URLs; "
          f"{measured['pages_scanned']} rendered pages; {len(warnings)} advisory warnings; "
          f"{len(errors)} errors.")
    for message in warnings:
        print("WARN:", message)
    for message in errors[:30]:
        print("ERROR:", message, file=sys.stderr)
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
