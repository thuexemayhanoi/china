# CHINA — SEO Foundation Matrix (audited 2026-10-12)

**Scope:** thuexemayhanoi/china → https://zh.rentbikehanoi.com/ only.

| Priority | Area | Baseline and evidence | Next action | Acceptance |
|---|---|---|---|---|
| P0 | Publication inventory | _posts contains 300 real Chinese Markdown posts; factory queue reports TARGET_REACHED, 0 remaining | Keep existing writer at target; audit instead of inventing 300 new posts | Post IDs and published HTML routes both 300 |
| P0 | Robots and sitemap | Production robots/sitemap fetch HTTP 200; sitemap lists 331 URLs (31 core + 300 posts) | Read-only scheduled monitoring | Unique absolute URLs, exactly match rendered indexable routes |
| P0 | Canonical/indexability | Sample home and post show self canonical plus index,follow | Run rendered QA across whole site on schedule | 331 rendered routes, canonical self, no accidental noindex |
| P0 | Structured data | Shared Jekyll schema emits WebSite, LocalBusiness, BreadcrumbList, BlogPosting, FAQPage where visible | Parse all emitted JSON-LD and compare to pages | Valid JSON-LD; required types present; FAQ answers visible and matching |
| P1 | Duplicate search intent | Factory checks publication; no portfolio-wide semantic equivalence guarantee | Monitor exact titles, normalized intent-keyword clusters; human review before merging content | No duplicate post ID, permalink, or normalized title; intent flags reviewed, not automatic deletions |
| P1 | Simplified Chinese quality | Site is zh-CN; publication gate enforces length/structure | Track Hanzi and H2 counts, plus editorial sample review | 300 genuine Chinese articles; sources checked for factual/legal claims |
| P1 | Mobile performance | Ubersuggest mobile lab: FCP 1.3s, LCP 1.6s, CLS 0, TBT 24ms, Speed Index 6.9s (2026-10-12) | Investigate 630ms redirect opportunity and measure field INP/Core Web Vitals | No mobile regression; field performance separately measured |
| P1 | GSC and Bing | Google Search Console property for zh subdomain not exposed by connected SMEPost integration | Add/verify the exact zh site property; submit sitemap; inspect URL coverage | Console reports indexed/excluded counts; sitemap processing success |
| P1 | Baidu/China access | Robots allow general crawling; this does not establish reachability from mainland China | Test from mainland-China network, Baidu verification + sitemap, log crawl reliability | Real mainland/Baidu response and official crawl/index evidence |
| P2 | Authority and GEO | Brand/entity/NAP in shared config; llms.txt present | Review first-party and independent sources, cited statements and earned links | Correct NAP; no fake testimonials/backlinks or fabricated citations |

## Monitoring contract

The independent workflow \`.github/workflows/china-seo-monitor.yml\` runs weekly, on relevant pushes/PRs and manually. It builds the real Jekyll output with the repository's existing Pages tooling, runs the existing source/rendered tests, then writes a JSON audit artifact using \`scripts/seo_monitor.py\`.

This workflow **does not** generate, rewrite, delete, or publish articles and **does not** modify GitHub Pages settings or deployment source. Monitoring results are not Google indexing numbers. Core Web Vitals and Baidu access require separate external measurements; no false success claim.

## Next priorities
1. Get Google Search Console + Bing Webmaster Tools verified for the **zh** subdomain; submit \`https://zh.rentbikehanoi.com/sitemap.xml\`.
2. Inspect repeated keyword-intent groups against actual articles before any merge or rewrite.
3. Measure mobile field data and check redirects using exact request chains, not guesses.
4. Investigate mainland China / Baiduspider access without changing DNS on speculation.
