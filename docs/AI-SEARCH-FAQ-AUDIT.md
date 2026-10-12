# China AI Search FAQ Audit — full URL Matrix

Audit-only: source Q&A candidates, NOT AI visibility or Google index confirmation.

## Scope

- Repo: thuexemayhanoi/china; live domain: https://zh.rentbikehanoi.com
- Inspected 300 Markdown posts and 31 core HTML pages; 331 unique URLs and complete CN-0001 to CN-0300 IDs.
- The /faq/ page renders 12 central questions from _data/faqs.json; schema_faq is already enabled for that page.
- No new FAQ or schema added. Google retired FAQ rich results in May 2026; do not add generic FAQPage to every blog post.
- Question-heading with adjacent substantive paragraph = candidate Q&A, NOT verified FAQ. A title phrased as a question is classified separately as title answer intent, NOT explicit FAQ. Human review is required.

## Classifications

| Class | Total URLs | Posts | Pages |
|---|---:|---:|---:|
| CURATED_FAQ | 1 | 0 | 1 |
| EXISTING_QA_CANDIDATE | 26 | 0 | 26 |
| QUESTION_WITHOUT_CLEAR_ANSWER | 0 | 0 | 0 |
| TITLE_ANSWER_INTENT | 245 | 245 | 0 |
| NO_EXPLICIT_QA | 59 | 55 | 4 |

- Evidence matrix includes 86 explicit question/adjacent-answer candidate pairs and 245 question-intent article titles with existing opening paragraphs (distinct classes).

## Highest-priority existing question pages

| URL | Q&A candidates | Status |
|---|---:|---|
| [/faq/](https://zh.rentbikehanoi.com/faq/) | 12 | CURATED_FAQ |
| [/topics/pricing/daily/](https://zh.rentbikehanoi.com/topics/pricing/daily/) | 5 | EXISTING_QA_CANDIDATE |
| [/topics/50cc/models/](https://zh.rentbikehanoi.com/topics/50cc/models/) | 4 | EXISTING_QA_CANDIDATE |
| [/topics/50cc/requirements/](https://zh.rentbikehanoi.com/topics/50cc/requirements/) | 4 | EXISTING_QA_CANDIDATE |
| [/topics/guides/contracts/](https://zh.rentbikehanoi.com/topics/guides/contracts/) | 4 | EXISTING_QA_CANDIDATE |
| [/topics/guides/returns/](https://zh.rentbikehanoi.com/topics/guides/returns/) | 4 | EXISTING_QA_CANDIDATE |
| [/topics/guides/safety/](https://zh.rentbikehanoi.com/topics/guides/safety/) | 4 | EXISTING_QA_CANDIDATE |
| [/topics/old-quarter/pickup/](https://zh.rentbikehanoi.com/topics/old-quarter/pickup/) | 4 | EXISTING_QA_CANDIDATE |
| [/topics/pricing/deposits/](https://zh.rentbikehanoi.com/topics/pricing/deposits/) | 4 | EXISTING_QA_CANDIDATE |
| [/topics/pricing/weekly/](https://zh.rentbikehanoi.com/topics/pricing/weekly/) | 4 | EXISTING_QA_CANDIDATE |
| [/about/](https://zh.rentbikehanoi.com/about/) | 3 | EXISTING_QA_CANDIDATE |
| [/topics/50cc/](https://zh.rentbikehanoi.com/topics/50cc/) | 3 | EXISTING_QA_CANDIDATE |
| [/topics/old-quarter/](https://zh.rentbikehanoi.com/topics/old-quarter/) | 3 | EXISTING_QA_CANDIDATE |
| [/topics/old-quarter/directions/](https://zh.rentbikehanoi.com/topics/old-quarter/directions/) | 3 | EXISTING_QA_CANDIDATE |
| [/topics/pricing/](https://zh.rentbikehanoi.com/topics/pricing/) | 3 | EXISTING_QA_CANDIDATE |
| [/topics/rental/](https://zh.rentbikehanoi.com/topics/rental/) | 3 | EXISTING_QA_CANDIDATE |
| [/topics/rental/automatic/](https://zh.rentbikehanoi.com/topics/rental/automatic/) | 3 | EXISTING_QA_CANDIDATE |
| [/topics/rental/monthly/](https://zh.rentbikehanoi.com/topics/rental/monthly/) | 3 | EXISTING_QA_CANDIDATE |
| [/topics/rental/scooters/](https://zh.rentbikehanoi.com/topics/rental/scooters/) | 3 | EXISTING_QA_CANDIDATE |
| [/prices/](https://zh.rentbikehanoi.com/prices/) | 2 | EXISTING_QA_CANDIDATE |
| [/privacy/](https://zh.rentbikehanoi.com/privacy/) | 2 | EXISTING_QA_CANDIDATE |
| [/contact/](https://zh.rentbikehanoi.com/contact/) | 1 | EXISTING_QA_CANDIDATE |
| [/topics/50cc/checklist/](https://zh.rentbikehanoi.com/topics/50cc/checklist/) | 1 | EXISTING_QA_CANDIDATE |
| [/topics/guides/maintenance/](https://zh.rentbikehanoi.com/topics/guides/maintenance/) | 1 | EXISTING_QA_CANDIDATE |
| [/topics/old-quarter/planning/](https://zh.rentbikehanoi.com/topics/old-quarter/planning/) | 1 | EXISTING_QA_CANDIDATE |
| [/topics/pricing/monthly/](https://zh.rentbikehanoi.com/topics/pricing/monthly/) | 1 | EXISTING_QA_CANDIDATE |
| [/topics/rental/electric/](https://zh.rentbikehanoi.com/topics/rental/electric/) | 1 | EXISTING_QA_CANDIDATE |

## Implementation sequence — not executed

1. P0: fact-check 12 central FAQ answers against store policies and official legal sources. Retain current centralized source and visible FAQ.
2. P1: review real on-page question headings and answer excerpts. Prioritize answer-first summaries, unique usefulness and contextual same-topic links. No invented facts.
3. P1: for question headings with weak adjacent answers, review context manually before adding any text.
4. P2/P3: informational posts and core pages with no explicit FAQ are not automatically missing FAQ. Don't inject boilerplate.
5. Structured data: preserve existing WebSite, LocalBusiness, BlogPosting and BreadcrumbList. Do not blanket-inject FAQPage or QAPage.
6. Regression QA for future edits: preserve all 300 posts, 331 sitemap routes, canonical, indexability, language and production Pages deploy.

## Evidence files

- AI-SEARCH-FAQ-URL-MATRIX.csv: all 331 URLs, priorities and review status.
- AI-SEARCH-FAQ-QUESTION-EVIDENCE.csv: existing questions and adjacent answers with source paths.

## Limits

- Source-level inspection, not full live browser crawl of 331 pages. HTML includes are not rendered except /faq/ shared JSON.
- Answers have not been human fact-checked; Google, Baidu, AI Overviews, ChatGPT citations and GSC performance not measured.
