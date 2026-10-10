# CHINA — 250 bài tiếng Trung / Content Factory

**Scope:** `thuexemayhanoi/china` → `https://zh.rentbikehanoi.com/`. Inspired by the safe parts of `thuexemayhanoi/vanchinh` factory, **not a copy of its articles**. No changes to the French site or Pages deployment.

## Status and editorial allocation

- **250 distinct briefs**, immutable IDs `CN-0001..CN-0250`, **10 batches of 25**: `B01..B10`.
- 50 x `rental`; 50 x `pricing`; 50 x `50cc`; 50 x `old-quarter`; 50 x `guides`.
- Manifest `_data/china-plan.json` is the immutable editorial scope.
- Operational matrix `data/china-matrix.csv` uses states `PLANNED` and `PUBLISHED`. Prepared/QA-ready drafts are **derived from their physical _drafts files**, not asserted by an outdated checkpoint.
- 0 drafted posts or published posts were created as part of workflow installation. They require genuine writing and review.

## No cross-repository copying

`vanchinh` is read-only reference for IDs, matrix, validation, scoped QA and checkpoint-style progress; no template article text, photos or AI-invented facts are imported. The CHINA site speaks original **Simplified Chinese (zh-CN)**. Existing UI switch 中文 / EN does not professionally translate new articles; never present English post translations that do not exist.

## Workflow and safety

```text
250 unique briefs / 10 batches
           |
      Writer drafts CN-xxxx.md
           |
       _drafts/ (NOT published)
           |
   Matrix QA: editorial checks + no duplicates + site's existing QA
           |
   Manual editor review: source accuracy and originality
           |
  Workflow Dispatch: PUBLISH + 1..5 reviewed IDs
           |
     scoped QA again, fail closed
           |
     atomic git commit: _posts + matrix update + remove draft
           |
   existing GitHub Pages native Jekyll build / live canonical URL
```

Only the **manual** `CHINA Publish Reviewed Posts` workflow has `contents: write` permissions; the `CHINA 250 Matrix QA` workflow (push/PR/weekly/manual) is read-only. One publisher run at a time; no silent lease claim, stale content import, force push or external API keys. Race against another writer causes an explicit failure; rerun from new main. No automatic mass publication.

### Using GitHub Actions on a phone

1. GitHub repository → **Actions** → **CHINA 250 Matrix QA** → **Run workflow** (main). Choose `status` to see remaining, or `plan` and batch `B01` to see the next five IDs.
2. A writer/agent drafts one of the listed topics by creating `_drafts/CN-0001.md` in the same repo. Keep it in drafts, not `_posts`!
3. Review facts, legal sources, SEO uniqueness and links. Record human approval in draft front matter.
4. After `CHINA 250 Matrix QA` succeeds, go to **CHINA Publish Reviewed Posts** → Run workflow on `main`, enter `CN-0001` (or up to five IDs separated by commas), and type exactly `PUBLISH`.
5. The publisher QA-checks again; on success it atomically commits the post(s) and matrix, then the original GitHub Pages deploy rebuilds the site. Never run for a PLANNED ID without its validated draft.

## Draft structure (example, NOT a published article)

```markdown
---
article_id: "CN-0001"
layout: "post"
title: "河内首次租踏板车前应该确认的八个问题"
description: "用简体中文清楚解释河内首次租踏板车前应核实的车型、车况、租期、租金、押金、证件、交接时间以及合同条件，帮助旅客做好准备。"
topic: "rental"
subtopic: "scooters"
permalink: "/blog/hanoi-rental-scooters-01/"
reviewed_by: "thuexemayhanoi"
editor_approved: true
---
## 车辆选择与实际需求

[至少 800 个有用汉字的原创正文；最少 3 个 H2 和 2 个有效站内链接。]
 
查看[踏板车租赁分类](/topics/rental/scooters/)以及[价格表](/prices/)。
```

**Important:** `editor_approved: true` and `reviewed_by` must be added **only after a real review**. The example above is a *format example*, not an article. SEO QA scoring is deterministic and is **not** independent fact-checking. Do not promise no deposit, no licence for all 50cc, available inventory, delivery, or unverified prices. Legal claims need source notes from a suitable authoritative current public resource.

## QA requirements

- Exact 250 IDs, 10 batches, unique Chinese titles/slugs/canonical paths; corresponding category hubs exist.
- Substantive Chinese text ≥800 Hanzi, 3+ descriptive H2, distinct internal links (including parent hub), Chinese meta description 40–150 Hanzi.
- Match planned brief and permalink; manually approved; no scripts, harmful embeds, misleading marketing promises.
- For relevant licensing/traffic claims, provide traceable `source_notes` with an official source URL and check it manually.
- A deterministic QA score ≥80 and **zero blocking issues** is required for publication.
- Check `_posts` against matrix statuses and block unregistered posts. No article past 250 can be published by this factory.

## Local commands (optional)

```bash
python3 scripts/china_factory.py status
python3 scripts/china_factory.py plan --batch B01 --limit 5
python3 scripts/china_factory.py validate --drafts
python3 scripts/china_factory.py qa --ids CN-0001
# Used only by the manual GitHub Actions publisher, after real human review:
python3 scripts/china_factory.py publish --ids CN-0001 --confirm PUBLISH
```

## SEO and architecture preserved

All articles go to `https://zh.rentbikehanoi.com/blog/<preplanned-slug>/`; Chinese is the canonical HTML language. The existing `_layouts/post.html`, SEO schema, CTA, related posts, categories, centralized navigation, blog listing, chatbot index and dynamic sitemap update automatically when a legitimate article is published.

Native GitHub Pages build, CNAME, DNS, menu, footer, widget UI and pricing remain unchanged. No scheduled AI text generation: writing requires an external writing agent or editor to actually supply accurate, reviewed content.
