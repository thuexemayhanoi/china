# CHINA AI Search / FAQ Matrix — Batch 11

Repository: `thuexemayhanoi/china` · Production: https://zh.rentbikehanoi.com/

User-approved continuation of the 331-URL AEO content rollout. This batch makes actual source revisions to **10 existing P2 posts** without adding mass `FAQPage` schema or new articles. Original IDs, URLs, publish dates, SEO silos and article H2 topics are retained.

| Article | Improvement |
|---|---|
| CN-0066 | Fuel charging and handover oil levels must reflect each agreement; no invented blanket customer-pays policy |
| CN-0068 | Contact shop for actual model/date inventory, no guaranteed auto reservation or assumed identical Wave/Click driving controls |
| CN-0069 | Compare Honda Wave and Vision's published day/deposit rates and half-automatic versus automatic handling rather than claiming bigger price is always better |
| CN-0070 | Distinguish rental payment, conditionally refundable deposits, actual fuel/equipment and possible damage liability |
| CN-0071 | Delayed returns: contact shop and confirm authorization and actual extra charge; no universal hourly/half-day fee |
| CN-0072 | Ask whether helmets are included, actual condition and price, not a free or fixed-rate promise |
| CN-0073 | Published reference prices vs final vehicle availability, contract time, fuel and service terms |
| CN-0074 | Model, dates, qualification, helmets and budget needed for enquiry; protect sensitive personal documents |
| CN-0076 | Real Wave, Click/Mio, Vision and Air Blade week-price source; no assumed early return/refund or automatic day-rate substitution |
| CN-0078 | Vision official weekly reference and separate deposit, safe/qualified rider check, no assumed refund from week-to-day arithmetic |

The edits include article-specific Chinese lead answers, source-backed factual section rewrites, updated Chinese SEO meta descriptions and accurate `last_modified_at: 2026-10-12`. Prices are derived from existing `_data/vehicles.json` through Liquid rather than inventing or duplicating amounts. 300 existing posts and original routes remain the release target.

## Matrix status after editing

| Category | URLs |
|---|---:|
| P0_IMPLEMENTED | 1 |
| P1_IMPLEMENTED | 3 |
| P1_CONTENT_REVISED | 23 |
| P1_REVIEW_PENDING | 0 |
| P2_ANSWER_FIRST_REVISED | 74 |
| P2_EDITORIAL_REVIEW_PENDING | 171 |
| NO_FORCED_FAQ; KEEP_UNIQUE_CONTENT | 59 |
| **Total** | **331** |

All revised rows still have `review_required=true`; targeted editorial correction does not certify every underlying claim, Google ranking, indexing, AI citation or AI answer inclusion.

## Release gates

1. PR Matrix QA verifies 300 CN articles and 331 Matrix URL rows.
2. Jekyll Blog UX QA validates generated canonical, H1, SEO, JSON-LD, internal links, rendered site and feature toggles.
3. Check `main` has not advanced, squash merge only after PASS, then confirm GitHub Pages Deploy SUCCESS.
4. Verify all 10 live HTML URLs and latest sitemap (331 URLs including 300 posts).

No changes to DNS, CNAME, site title, homepage, theme, permalink, menu or plugin dependencies.
