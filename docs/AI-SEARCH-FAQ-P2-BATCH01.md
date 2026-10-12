# AI Search Answer-First: P2 batch 01 (7 actual zh-CN posts)

Source audit: `docs/AI-SEARCH-FAQ-URL-MATRIX.csv` and `docs/AI-SEARCH-FAQ-QUESTION-EVIDENCE.csv`.

This is a targeted correction of existing content, not insertion of generic questions/FAQPage schema. Each revised post retains its article ID, canonical permalink, publication date, silo, internal links and topic context. Updated `description` is aligned with the answer and `last_modified_at: "2026-10-12"` reflects the editorial update date.

| Article | Focus | Main factual correction |
|---|---|---|
| CN-0105 | 50cc daily rent versus deposit | Price/deposit sourced from shared vehicle data; no automatic or unconditional deposit refund |
| CN-0127 | 50cc licence | Legal moped classification requires more than advertised displacement; minimum age and skills |
| CN-0130 | Minimum age / contracting | 16-year minimum for qualifying mopeds is not a promise that any shop rents to under-18s |
| CN-0133 | Foreign driving licence | No universal recognition of foreign IDP/licence; verify convention, country, category and law |
| CN-0204 | Deposit versus prepaid rent | Distinguish collateral from rent, with contract-specific settlement conditions |
| CN-0218 | When deposit is returned | No verified uniform shop policy or fixed processing time; written confirmation needed |
| CN-0085 | Electric weekly rent | Site does not publish a weekly quote; no evidence for asserting the shop's pricing rationale |

Official legal source: https://vbpl.vn/TW/Pages/vbpq-toanvan.aspx?ItemID=170620 (Law 36/2024/QH15, Articles 34, 56, 59).

The live operational terms of the user's rental business (refund, ID documents accepted, stock, delivery, booking and charges) must still be confirmed by the store; no fabricated policies were introduced.

## Matrix and QA

- 7 URLs now carry `P2_ANSWER_FIRST_REVISED` in `AI-SEARCH-FAQ-IMPLEMENTATION-MATRIX.csv`.
- `review_required=true` intentionally remains on those rows: rewriting a lead and fixing identified body statements does not certify all surrounding content as fully human reviewed.
- Remaining original audit rows and evidence are unchanged; **no** FAQ schema is injected into ordinary article pages.
- `scripts/qa.py` validates metadata and answer-first labels on these seven source posts; build and rendered Jekyll QA cover all 331 unchanged routes.
- Only merge after CHINA Matrix QA and Blog UX Build QA both succeed, then confirm GitHub Pages deploy and live article URLs.

Next iteration: continue with factual-sensitive titles in the 238 unrevised P2 articles, then revisit the 23 still-open P1 core pages. Don't bulk-insert duplicated FAQ sections.
