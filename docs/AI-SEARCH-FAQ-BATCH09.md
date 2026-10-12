# CHINA AI Search P2 — Batch 09

Production site: https://zh.rentbikehanoi.com/ · Repository `thuexemayhanoi/china`. User-approved continued AEO matrix editing. This release edits existing source answers; **it does not add generic FAQPage markup or claim AI citation/ranking gains**.

| Article | Editorial work |
|---|---|
| CN-0038 | Honda Vision published monthly rate/deposit from shared Liquid data; no unverified flagship fleet or replacement promises |
| CN-0041 | Temporary lack of stock: ask real availability and replacement terms, no invented discounts or free transition vehicle |
| CN-0042 | Contract terms covering rent, deposit, legal eligibility and damage; remove fabricated 80% risk statistic and unconditional legal validity of chat logs |
| CN-0043 | Mid-term vehicle swap: separately document both vehicles, contract dates, deposits and possible charge changes; never assume free swap |
| CN-0044 | Monthly returns: check handover, fuel, accessories, wear, paid amounts and actual refunds; records help but do not guarantee no disputes |
| CN-0045 | Handover photos: preserve original records, distinguish received from agreed and avoid false absolute timestamp/legal evidence claims |
| CN-0046 | Real store address/hours from shared site data; no unverified 60–90-minute guaranteed pickup windows |
| CN-0047 | Security deposits separate from rent; no invented 50% of disputes statistic, unconditional same-day/full refund promise |
| CN-0048 | Extensions use store-confirmed total charge, date/time, deposits and terms, not unverified automatic proration |
| CN-0049 | Urban commute suitability depends on driving qualification, true journey, parking, weather, cost; no fixed distance thresholds or zero-cost bus assumption |

Every revised Markdown post retains original article ID, permalink, primary keyword, original published date, H2 subject headings and relevant internal links. Answer-first intro and matching Chinese SEO description have been added, alongside `last_modified_at: 2026-10-12` for genuinely revised content.

## Matrix accounting

| Status | URLs |
|---|---:|
| P0_IMPLEMENTED | 1 |
| P1_IMPLEMENTED | 3 |
| P1_CONTENT_REVISED | 23 |
| P1_REVIEW_PENDING | 0 |
| P2_ANSWER_FIRST_REVISED | 54 |
| P2_EDITORIAL_REVIEW_PENDING | 191 |
| NO_FORCED_FAQ; KEEP_UNIQUE_CONTENT | 59 |
| **Total** | **331** |

All changed rows retain `review_required=true` to avoid presenting limited content corrections as exhaustive fact validation. These labels represent editorial source work, not verified AI search inclusion.

## Release gate

1. Exactly 300 original published posts and 331 canonical routes/sitemap URLs retained.
2. Matrix QA and Jekyll Blog UX QA (rendered SEO, links, schema, UX feature flag fixtures) must pass on the PR HEAD.
3. Merge PR without overwriting unrelated commits; GitHub Pages must report deployment success.
4. Scrape representative production routes and verify new copy, canonical, H1 and dateModified.
