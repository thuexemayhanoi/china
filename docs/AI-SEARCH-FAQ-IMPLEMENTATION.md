# CHINA — AI Search / FAQ content rollout (phase P0 + verified P1)

Project: `thuexemayhanoi/china` · `https://zh.rentbikehanoi.com`

## Baseline and content scope

- Baseline main: `abbdb646282e3b4e16580b0bd909228571b82134`.
- Original audit: `docs/AI-SEARCH-FAQ-URL-MATRIX.csv` (331 URLs), `docs/AI-SEARCH-FAQ-QUESTION-EVIDENCE.csv`.
- This release updates **one core FAQ source (12 Q&A)**, **three pre-existing page answers**, and central source/schema/QA templates. No changes to the 300 post Markdown files.
- Do not claim that publishing content yields indexing, AI citations, AI Overviews visibility or Google FAQ rich results. Google ended FAQ rich results in May 2026.
- For the remaining 23 P1 Q&A pages, 245 P2 title-answer posts and 59 no-explicit-QA URLs, see `AI-SEARCH-FAQ-IMPLEMENTATION-MATRIX.csv`. These are **not falsely marked optimized**.

## Shared answer architecture (one change → all uses)

- 12 curated questions, fallback textual answers and topic links: `_data/faqs.json`.
- Published contact details, brand and opening hours: `_data/site.json`.
- Published reference rent per model: `_data/vehicles.json`.
- Dynamic truthful answer text is rendered once through `_includes/faq-answer.html`, reused by **visible** `_includes/faqs.html` and **FAQPage JSON-LD** in `_includes/schema.html`. No separate static schema answers that can go stale.
- Every answer links to a relevant existing deep guide; legally-sensitive 50cc Q&A includes an official statute source.
- Keep normal WebPage / BlogPosting markup for every other page; do not add boilerplate FAQPage to other URLs.

## P0 — 12 current questions on /faq/

- Updated all 12 to lead with explicit, scoped answers, avoiding unverified policies, guaranteed stock, free delivery, and fixed deposit refunds.
- Price, contact, address, opening hours and route answers now render actual shared data, not redundant hard-coded strings.
- Legal answer now distinguishes properly-classified mopeds (`xe gắn máy`) from merely advertised 50cc models: Article 56 licence exception, minimum 16 years and competency conditions under Article 59 and Article 56(4), official Law 36/2024/QH15.
- Government reference: https://vbpl.vn/TW/Pages/vbpq-toanvan.aspx?ItemID=170620. Store policies and live availability remain explicitly subject to store confirmation.

## P1 — answer-first improvements already applied

- `/topics/50cc/requirements/`: explicit answer in the existing heading section, source-backed legal distinction and age criteria; original references preserved.
- `/topics/pricing/daily/`: immediately states reference daily rates pulled from `_data/vehicles.json`, with deposits separately qualified.
- `/topics/pricing/deposits/`: immediately states examples of deposits from central vehicle data and that refunds follow actual contracts.

## QA required before merge

- `python3 scripts/qa.py` → 31 pages, 300 posts, validated central FAQ keys, all curated links and valid official source.
- `python3 scripts/china_factory.py validate` → original 300/300 articles and Matrix consistency.
- Jekyll build + `python3 scripts/qa_rendered_site.py` → unchanged 331 HTML canonical/sitemap routes, H1, zh-CN, indexability and valid JSON-LD.
- Custom parity QA on `/faq/` compares every one of the 12 **visible** answers directly with `FAQPage` JSON-LD; verifies centrally rendered address, hours, phone and model prices.
- Existing multi-build disposable-fixture Blog UX QA should still pass.

## Pending editorial work

- **23 additional P1 pages** already have question headings and meaningful paragraphs. Review their factual accuracy and clarity individually, without duplicating existing answers.
- **245 P2 article titles** are question-intent, but an introductory paragraph does not make a vetted FAQ. Review in logical silos; use each existing article as the answer source. Rewrite the original first paragraph *only when it fails to answer the specific user query*, with reference checks for legal/commercial claims.
- **59 other URLs** should not acquire empty or generic FAQ blocks. Retain original purpose and content.
- Re-run `scripts/china_faq_ai_audit.py` on a review branch after substantive future edits, but do not overwrite this implementation status table without actually completing and QA-testing a row.

The deployment of this phase does **not** complete all 331 editorial reviews.
