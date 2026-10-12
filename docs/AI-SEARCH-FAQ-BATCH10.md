# CHINA AI Search / AEO Editorial Matrix — Batch 10

Repository: `thuexemayhanoi/china`. Production: https://zh.rentbikehanoi.com/

This user-approved release revises **10 existing P2 articles**, based on actual page content and the site's published vehicle data. It does not automatically insert FAQPage schema, and it does not promise Google indexing, AI citations or traffic.

| Article | URL | Verified editorial improvements |
|---|---|---|
| CN-0050 | /blog/hanoi-rental-longterm-25/ | Deposit settlement: contract, payment proof, shared inspection, deduction basis and refund arrangements, without blanket full/same-day refund guarantee |
| CN-0051 | /blog/hanoi-pricing-daily-01/ | All published model day rates come from `_data/vehicles.json`; correct rental-vs-deposit distinction, no universal fuel or accessory policy |
| CN-0054 | /blog/hanoi-pricing-daily-04/ | Air Blade published day reference/deposit, rider qualification, dated quote and real stock; no invented inspection, pricing or booking guarantees |
| CN-0055 | /blog/hanoi-pricing-daily-05/ | Click/Mio day/week/month/deposit reference from shared data, actual accessory/fuel and late-return contract terms |
| CN-0058 | /blog/hanoi-pricing-daily-08/ | Compare 5 model day-price tiers, different deposits, real vehicle condition and 50cc legal classification; no treating deposit as spent rental cost |
| CN-0059 | /blog/hanoi-pricing-daily-09/ | Clarifies absence of universal 24-hour/natural-day and overtime-price shop policy |
| CN-0060 | /blog/hanoi-pricing-daily-10/ | Explains possible extras without assuming cleaning or delivery fees actually exist; deposit, fuel, damage and timing separately confirmed |
| CN-0063 | /blog/hanoi-pricing-daily-13/ | No publicly fixed half-day policy; avoids claims every half-day is billed full day or that customers must ride longer to get value |
| CN-0064 | /blog/hanoi-pricing-daily-14/ | Actual one/two-day counting and explicit handover times; multiplying reference price is not a formal quote |
| CN-0065 | /blog/hanoi-pricing-daily-15/ | Holiday price and inventory confirmed case by case; no unsupported universal surcharge, reservation or extra service commitments |

Each source preserves the article ID, original publishing date, permalink, SEO silo and original H2 headings. Its opening answers the target question directly, descriptions and a genuine `last_modified_at: 2026-10-12` reflect the edit, and key body sections and conclusions have been aligned. Shared Liquid `site.data.vehicles` powers the applicable displayed prices and deposits. Original internal topic references stay in place.

## Exact implementation Matrix after batch 10

| Status | URL count |
|---|---:|
| P0_IMPLEMENTED | 1 |
| P1_IMPLEMENTED | 3 |
| P1_CONTENT_REVISED | 23 |
| P1_REVIEW_PENDING | 0 |
| P2_ANSWER_FIRST_REVISED | 64 |
| P2_EDITORIAL_REVIEW_PENDING | 181 |
| NO_FORCED_FAQ; KEEP_UNIQUE_CONTENT | 59 |
| **TOTAL** | **331** |

`review_required=true` remains on edited posts, since precise targeted editorial work is not a blanket human certification of every remaining statement.

## Required release checks

- Preserve exactly 300 published CN-0001..CN-0300 Markdown posts.
- Preserve sitemap's 331 original URL routes and canonical links.
- PR Matrix QA and Blog UX Jekyll rendered-site SEO + internal links + feature fixtures must both PASS before merging.
- On successful Pages deployment, verify 10 live source URLs, metadata and sitemap; do not claim success if production is not verified.
- Do not change DNS, CNAME, SEO template schema, theme, site title, menu or URL structure.
