# CHINA — AI Search FAQ / Answer-first implementation, Batch 05

Repo: `thuexemayhanoi/china` · Production: https://zh.rentbikehanoi.com/

## Actual editorial changes

This batch revises exactly 10 URLs: five existing P1 core pages and five existing P2 zh-CN articles. No new FAQ markup was forced onto generic posts, and no URLs, original post dates, permalinks, CNAME, DNS or GitHub Pages configuration changed.

### P1 — five page answers

| URL | Improvement |
|---|---|
| `/prices/` | One data-driven day-rent answer covers all five priced vehicles; clarifies unpublished 50cc/electric packages, deposit handling and contract-specific refund conditions; adds genuine visible refund Q&A |
| `/topics/old-quarter/directions/` | Store address/hours from shared site configuration, actual origin and live Google Maps navigation; no guaranteed route, transit time or stock |
| `/topics/old-quarter/pickup/` | Clear Long Biên store location and no assumptions of free hotel delivery, online booking or automatic pickup |
| `/topics/rental/automatic/` | Automatic/semiautomatic versus licence/experience distinction and actual shared per-model prices; no implication untrained riders can ride |
| `/topics/rental/monthly/` | Data-driven monthly rate summary, separate deposits, no auto-assumed 30-day contractual term or prorated refund |

### P2 — five existing articles

| Article | Improvement |
|---|---|
| CN-0006 | Safe rain riding: defer riding during severe weather, do not test brakes in traffic or presume rain-damage charge policy |
| CN-0007 | Evaluate seat height from actual stable handling; no universal flat-feet claim or guaranteed alternative vehicle stock |
| CN-0008 | Check legal passenger capacity, both helmets, separate driver's eligibility, actual tyre pressure and safe passenger test |
| CN-0012 | Honda Vision published daily rent and deposit read from shared data; no assumed hourly overage or same-day refundable deposit |
| CN-0014 | Automatic scooters are not safe for completely untrained riders; no universal half-hour learning guarantee or practising in public streets |

All five P2 source documents retain original published dates and article IDs, and now have answer-first highlighted Chinese introductions, updated meta descriptions and `last_modified_at: 2026-10-12`. Existing H2 structure is maintained. The site remains the canonical source for pricing, deposits, store location and hours. No new SEO dependency or FAQPage schema injection.

## 331-URL rollout accounting after this batch

| Status | URL count |
|---|---:|
| P0_IMPLEMENTED | 1 (central 12-question FAQ) |
| P1_IMPLEMENTED | 3 |
| P1_CONTENT_REVISED | 15 |
| P1_REVIEW_PENDING | 8 |
| P2_ANSWER_FIRST_REVISED | 22 |
| P2_EDITORIAL_REVIEW_PENDING | 223 |
| NO_FORCED_FAQ; KEEP_UNIQUE_CONTENT | 59 |
| **Total** | **331** |

Changed rows still retain `review_required=true` where comprehensive fact-checking of all surrounding content remains warranted. Matrix status denotes editorial work, not Google indexing, rankings or AI answer appearances.

## Required release gates

1. Exactly 300 published CN-0001..CN-0300 and 331 sitemap/canonical URLs preserved.
2. `scripts/qa.py` source QA supports both existing `div.inner-panel` core layouts and `section.inner-panel` topic layouts.
3. CHINA Matrix QA and native Blog UX Jekyll rendered SEO, links, schema and feature-flag tests all succeed.
4. Merge on current main SHA only after QA success and confirm live GitHub Pages deployment and representative URL content.

Remaining: 8 P1 pages and 223 P2 articles. These are not marked completed until actual source edits pass regression tests.
