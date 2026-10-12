# CHINA AI Search P2 — Batch 08

Production website: https://zh.rentbikehanoi.com/ · Repository `thuexemayhanoi/china`

## Scope

Exactly **10** existing posts edited in their original Jekyll source. No invented FAQ blocks or blanket FAQPage markup. All 300 published articles, URLs, schema, layout, sitemap, CNAME and deployment configuration must remain intact.

| Article | Substantive editorial improvement |
|---|---|
| CN-0024 | Rental documentary proof: contracts and payment records, photos with consent, sensitive document minimization; time stamp alone is not conclusive legal evidence |
| CN-0025 | Return-condition comparison with check-in photos and actual contract; no claim that every scratch dispute can be eliminated |
| CN-0029 | Compare genuine full daily/weekly/monthly quotes and separate deposits; no guarantee monthly saves 50% or produces better vehicle |
| CN-0030 | Fourteen-day dates and explicit store quote; never treat daily×14 or weekly×2 as confirmed transaction price |
| CN-0031 | Maintenance responsibility set by actual mileage, vehicle condition and written agreement; no blanket store obligation |
| CN-0032 | Stop for legal/safety-related faults including turn signal failures; no promised free rescue or replacement |
| CN-0033 | Tyre pressure/depth require proper instruments; do not diagnose uneven wear by a single visual pattern |
| CN-0034 | Renew every substantive contract term, not just price; no guaranteed notice deadline |
| CN-0035 | Correct Honda Wave as commonly semi-automatic rather than manual clutch; rewrite comparison body for factual consistency |
| CN-0036 | Static daily checks do not guarantee roadworthiness; do not use public roads as a brake or steering test area |

Each revised post includes a clear highlighted answer-first introduction, matching Chinese SEO description, `last_modified_at: 2026-10-12`, retained original `date`, `article_id`, H2 subject hierarchy, categories and permalink. Existing topic-hub links stay in place.

## Matrix progress after batch 08

| Category | URLs |
|---|---:|
| P0_IMPLEMENTED | 1 |
| P1_IMPLEMENTED | 3 |
| P1_CONTENT_REVISED | 23 |
| P1_REVIEW_PENDING | 0 |
| P2_ANSWER_FIRST_REVISED | 44 |
| P2_EDITORIAL_REVIEW_PENDING | 201 |
| NO_FORCED_FAQ; KEEP_UNIQUE_CONTENT | 59 |
| **Total** | **331** |

Revised P2 rows deliberately keep `review_required=true` to permit deeper fact checks. No ranking, AI Overviews or citation guarantees.

## Release gates

- CHINA 300 Matrix QA and source integrity PASS.
- Native Jekyll Blog UX Build QA, full rendered links/schema/canonical QA, and synthetic-feature regressions PASS.
- Merge only onto the known latest main HEAD; no force push.
- Deploy GitHub Pages and check representative published content and sitemap live: 331 URLs including 300 posts.
