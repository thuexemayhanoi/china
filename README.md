# CHINA — Nguyễn Tú 🇨🇳

Live: https://zh.rentbikehanoi.com/ · Code: https://github.com/thuexemayhanoi/china · Language: zh-CN.

## Architecture — edit once, rebuild all pages
Native Jekyll from GitHub Pages' existing branch build; optional editorial QA/publish GitHub Actions (distinct from unchanged Pages deployment), no heavy dependencies/hosting changes.

- `_data/site.json`: business NAP, hours, canonical domain, feature flags, sitemap base routes.
- `_data/navigation.json`: header dropdown, sidebar and footer navigation.
- `_data/vehicles.json`: published reference rents and calculator (no invented rates).
- `_data/faqs.json`: visible FAQ answers and FAQPage schema.
- `_layouts/default.html`: SEO and shared site structure; `_layouts/post.html`: future posts.
- `_includes/post-footer.html`: one ordered shared slot for post navigation, Author Box, CTA, related articles and useful hub links (all independently feature-flagged).
- `_data/site.json → post_ui.cta.default`: single shared banner/CTA text/button/contact destination; optional approved `page.cta_variant`. `post_ui.hub_links`: exactly 3 verified live hub links per topic, never auto-spam or guessed articles.
- `_includes/related-posts.html`: real `site.posts` only, strict same `seo_silo` when present; falls back to same `topic` only when no silo exists. Limit is `features.related_limit`. Existing Previous/Next, schema, post content and URLs remain unchanged.
- `features.show_post_hub_links`, `show_post_cta`, `show_related_posts`: disable any section globally without editing articles. All Chinese UI captions have English keys in `_data/i18n-en.json`.
- `_includes/*.html`: reusable header/footer/nav/sidebar/breadcrumbs/schema/CTA/pricing/related posts.
- `assets/site.css`: existing black/white/gold design tokens and responsive UI.
- `assets/site.js`: existing interactions, reading price data embedded from central JSON.

## Current editorial scope
**Editorial capacity: exactly 250 planned Simplified Chinese articles, in 10 batches × 25.** Allocated equally to rental, pricing, 50cc, Old Quarter and guides (50 each). Actual progress is tracked in `data/china-matrix.csv`; run `python3 scripts/china_factory.py status`. **Installing the factory publishes no posts.**

## Adding posts later (do not generate empty posts)
**Do not write directly to `_posts/`.** Create `_drafts/CN-xxxx.md` for the approved matrix ID and topic; run matrix QA and manual human review, then the `CHINA Publish Reviewed Posts` Action moves it to `_posts/YYYY-MM-DD-<planned-slug>.md` and updates the matrix atomically. Existing Jekyll templates then update `/blog/<planned-slug>/`, blog lists, categories, schema, CTA and sitemap automatically. See `docs/CHINA-FACTORY-250.md`.

## SEO/QA safeguards
Preserve all existing page URLs, titles, descriptions, canonical domain, visible content and design. Canonical: https://zh.rentbikehanoi.com/. Sitemap base: 26 existing index-eligible pages (actual Google indexing is not guaranteed). No false prices, waived deposits, fabricated reviews or assumed 50cc license exemptions.

No changes to `CNAME`, DNS, Pages deployment mode or other repositories. Always verify native Jekyll build results and rollback if failing.

## Lightweight QA
Run `python3 scripts/qa.py` before merging/publishing. GitHub Pages' original Jekyll build remains the final build/deployment check. Editorial Actions added for 250-article matrix QA and explicit manual publishing; native GitHub Pages deployment is unchanged.

## Chinese / English switch (same URLs, Chinese-first SEO)
- Toggle **中文 / EN** in the shared header, across all pages; preference is stored locally and remembered between pages.
- English is a curated on-page translation via `_data/i18n-en.json` + `assets/i18n.js` (no remote translate service).
- Initial server-generated HTML, meta descriptions, canonical tags, sitemap and all page URLs remain in Chinese at `https://zh.rentbikehanoi.com/`.
- The switch changes visible text and accessibility labels, not URLs; `<html lang>` becomes `en` when selected.
- For future published posts, add reviewed English translations to the dictionary or create an appropriate dedicated English content workflow. **Do not** assume new Chinese posts automatically get a professional English translation.
- Existing menu behavior, page designs, CSS tokens, theme, contact information, and prices are preserved.

## About, FAQ, privacy and terms (2026-10-10)
- Navigation and footer share `_data/navigation.json` with exact same top-level labels and order: Home → About → topics → Blog → FAQ → Contact → Privacy → Terms. FAQ was removed from the Guides dropdown to avoid duplicate primary navigation.
- New pages: `/about/`, `/privacy/`, `/terms/`. Existing `/faq/` remains the same canonical and now has 12 grounded questions, shared between visible answers and `FAQPage` JSON-LD.
- `_data/i18n-en.json` includes reviewed English display translations for these pages and new FAQ answers. HTML remains Chinese-first; no English URL or hreflang claims.
- Central sitemap expanded from 9 to 12 URLs; new informational pages use the same Jekyll layout, NAP, SEO and responsive design as the original site.
- New privacy and terms pages are informational notices, not substitutes for professional legal review; do not assert unverified policies or guarantees.
- On laptop-width screens, navigation uses the already working responsive drawer to avoid 12 top-level labels overflowing the header.
- Updated `scripts/qa.py` to expect 26 core HTML pages, 12 FAQs and proper top-menu order.

## Quick Call and local chatbot (adapted from the /french repo)
- UI interaction patterns adapted from `thuexemayhanoi/french` (read-only reference, untouched). Only this /china repository is modified.
- `assets/assistant-cn.css` contains scoped floating widgets using **black / white / gold** design tokens, supporting dark mode, mobile safe areas, and iOS keyboard viewport.
- `assets/assistant-cn.js` mounts two floating widgets: Quick Call (phone, Zalo, WhatsApp, Google Maps) and a **local rules-and-search FAQ assistant** in Simplified Chinese and English.
- No external AI model, account credentials, tracking, third-party script, or API is used. The chatbot **does not invent inventory, prices or licensing exemptions**, does not book or take payments, and reads only publicly published Chinese-site content.
- `assets/chat/site-index.json` is generated automatically by Jekyll from central FAQ, vehicle data, business info, real pages and future published posts, not the French-language 5MB search index.
- Language follows the existing 中文 / EN toggle; script does not change canonical, SEO metadata, URLs, or the initial Chinese HTML.
- All widget data/visibility flags are managed in `_data/site.json` (`features.quick_contact`, `features.local_chatbot`).


## CHINA 250-article workflow — inspired by /vanchinh
- **Guide:** [docs/CHINA-FACTORY-250.md](docs/CHINA-FACTORY-250.md).
- **Manifest:** `_data/china-plan.json`: 250 unique planned Chinese article titles and canonical slugs.
- **Matrix:** `data/china-matrix.csv`: immutable brief identifiers + actual publication state.
- **Manual writer flow:** create `_drafts/CN-xxxx.md` → quality QA → human review → Actions **CHINA Publish Reviewed Posts** with 1–5 IDs and explicit PUBLISH → native Jekyll auto rebuild.
- **Progress/QA from iPhone:** Actions **CHINA 250 Matrix QA** (Run workflow → status/plan/validate).
- **Guardrails:** no posts created by setup, no cross-repo text reuse, no false prices or legal claims, no forced push, max 250 published, CNAME and GitHub Pages mode untouched.
