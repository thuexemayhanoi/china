# CHINA FAQ / AI Search Matrix — Batch 07

Production: https://zh.rentbikehanoi.com/ — repo `thuexemayhanoi/china`. Scope is ten existing URLs with source-specific factual improvements, not generic FAQ insertion.

## P1: Three remaining core pages revised

| URL | Improvement |
|---|---|
| `/about/` | Source-of-truth store identity and location, stock not guaranteed, reference pricing not final contract; existing AboutPage semantics preserved |
| `/contact/` | Three user-focused sections: specific info to ask store, where Long Biên store is, why a phone/Zalo enquiry does not complete an online booking. Shared business phone, location, map and hours untouched |
| `/privacy/` | Differentiates lack of online data-entry form from technical hosting logs, identifies third-party privacy scopes and avoids unverified retention claims; dated 2026-10-12. Not mislabelled a FAQPage |

## P2: Seven actual article edits

| Article | Content corrected |
|---|---|
| CN-0019 | Rental handover checklist vs shop-guaranteed procedures, lawful test driving, no assumed 24-hour emergency service |
| CN-0020 | Distance-based vehicle choice requires legal route/vehicle category, no unverified highway permission and no uniform seat-height rule |
| CN-0021 | Vehicle-specific controls and stationary safe inspection; novice riders should not accelerate/test on public roads |
| CN-0022 | Defective turn signal or lighting may be a safety/legal issue; no assumed free roadside assistance or replacement |
| CN-0026 | Monthly rental only potentially economical depending on actual total costs, no guarantee of always cheaper |
| CN-0027 | Monthly billing duration, exact date/time, early return and extensions are contract-specific, not always 30 days |
| CN-0028 | Fuel, maintenance and accessory terms must be verified; not universally free, included or always charged |

All seven articles preserve their article IDs, canonical URLs, original publishing dates, silos and H2 headings; `description` and `last_modified_at: 2026-10-12` updated to reflect actual changes. All source edits match the existing Matrix. No new FAQPage structured data.

## Exact Matrix after this batch

| Status | URLs |
|---|---:|
| P0_IMPLEMENTED | 1 |
| P1_IMPLEMENTED | 3 |
| P1_CONTENT_REVISED | 23 |
| P1_REVIEW_PENDING | 0 |
| P2_ANSWER_FIRST_REVISED | 34 |
| P2_EDITORIAL_REVIEW_PENDING | 211 |
| NO_FORCED_FAQ; KEEP_UNIQUE_CONTENT | 59 |
| **Total** | **331** |

Thus all 26 P1 topic/core pages have received targeted editorial revisions or earlier implementation, but `review_required=true` flags still indicate further human fact review may be useful. `211` P2 question-intent articles still await actual editorial work. Other 59 URLs are not required to carry FAQ content.

## Release gates

- CHINA 300 Matrix QA passes, including 300/300 exact published article IDs.
- Blog UX build and rendered-site SEO/links/canonical/sitemap checks pass, with feature flag fixtures.
- Production GitHub Pages succeeds, and live examples show updated copy, canonical and expected `dateModified`.
- No change to DNS, CNAME, published post permalinks, sitemap URL count, site styling or layout.
