# REUSABLE SEO STANDARD — GitHub static blog starter v1

Copy this document's *requirements*, not CHINA's names or paths, into each new repository. Choose a site generator (Jekyll/static/WordPress) and adapt scripts after confirming its real output. Keep one canonical domain, one URL convention and one source of truth; never clone content for multiple languages.

## Nine working modules
1. **Technical SEO:** HTTPS, robots, XML sitemap, redirects, error statuses, indexability, self canonicals.
2. **Information architecture:** parent hubs, child silos, breadcrumbs, no orphan pages; verified internal links.
3. **On-page SEO:** unique title/description/H1; default language, OG metadata, alt and accessible HTML.
4. **Content quality:** useful firsthand answers, original value, source verification, no unsafe claims; near-identical search intent is a review flag.
5. **Mobile performance:** viewport, mobile usability, lab LCP/CLS/TBT, real-user LCP/INP/CLS when available.
6. **Measurement:** Google Search Console, Bing Webmaster Tools, optional local search engines; separate submitted/discovered/indexed statuses.
7. **AEO/GEO and structured data:** schema matching visible facts; FAQ only for real displayed Q&A, stable brand identifiers, quote-ready concise factual explanations.
8. **Operational QA:** dependency-light scheduled/PR/manual build audits; evidence artifacts; safe publishing and rollback; no write privilege for monitors.
9. **Authority/international reach:** canonical NAP, earned citations, quality outbound sources, local search engine accessibility, Chinese/Baidu checks when relevant.

These are **workstreams**, not nine independent Google ranking factors.

## Contract before publishing
- A source-of-truth config defines name, phone, address, business map, domain and contact links.
- Generator outputs exactly one intended canonical per indexable URL; robots and sitemap agree.
- Live route returns HTTP 200, initial HTML contains meaningful content, and supported JSON-LD parses.
- Article IDs, permalinks, and normalized titles unique. Similar keyword/search intent prompts **human review**, not automated deletion.
- All prices, vehicle availability, license rules, policies and source claims are verified; unknown facts are labeled unknown.
- Monitor jobs may only **read** data; writer workflow requires separate permissions and quality gates.
- Run source QA → native site build → rendered QA → check Pages deployment → spot-check live URLs.
- Tracking through GSC/Bing/Baidu is a separate verified service; NEVER infer indexing from sitemap count.
- PageSpeed lab tests are not the same as Core Web Vitals field data.
- Main language, market, local search engines and China-network access must be confirmed per project.

## Adapting the CHINA workflow
Keep \`.github/workflows/china-seo-monitor.yml\` and \`scripts/seo_monitor.py\` as **reference implementations only**. They use Jekyll, the \`_posts\` directory, the \`_site\` build destination, and CHINA's JSON config. For a different repo, parameterize those paths, URL patterns, targets and market-language checks *before* enabling a copied workflow. Do not push Chinese business data or invented schema into another brand.
