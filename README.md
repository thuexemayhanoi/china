# CHINA — Nguyễn Tú 🇨🇳

Live: https://zh.rentbikehanoi.com/ · Code: https://github.com/thuexemayhanoi/china · Language: zh-CN.

## Architecture — edit once, rebuild all pages
Native Jekyll from GitHub Pages' existing branch build; no custom workflow/dependencies/hosting changes.

- `_data/site.json`: business NAP, hours, canonical domain, feature flags, sitemap base routes.
- `_data/navigation.json`: header dropdown, sidebar and footer navigation.
- `_data/vehicles.json`: published reference rents and calculator (no invented rates).
- `_data/faqs.json`: visible FAQ answers and FAQPage schema.
- `_layouts/default.html`: SEO and shared site structure; `_layouts/post.html`: future posts.
- `_includes/*.html`: reusable header/footer/nav/sidebar/breadcrumbs/schema/CTA/pricing/related posts.
- `assets/site.css`: existing black/white/gold design tokens and responsive UI.
- `assets/site.js`: existing interactions, reading price data embedded from central JSON.

## Current editorial scope
**0 articles published.** Menu allows 200 future Simplified Chinese posts: rental 50, pricing 40, 50cc 35, Old Quarter 35, guides 40. Empty subcategories stay noindex and are excluded from sitemap until reviewed.

## Adding posts later (do not generate empty posts)
Create `_posts/YYYY-MM-DD-unique-slug.md` with front matter `layout: post`, `title`, `description`, `topic`, `subtopic`, `date`, `breadcrumbs`; GitHub Pages/Jekyll generates `/blog/:title/`, blog lists, category related posts, article schema, CTA and sitemap automatically.

## SEO/QA safeguards
Preserve all existing page URLs, titles, descriptions, canonical domain, visible content and design. Canonical: https://zh.rentbikehanoi.com/. Sitemap base: 9 indexed pages. No false prices, waived deposits, fabricated reviews or assumed 50cc license exemptions.

No changes to `CNAME`, DNS, Pages deployment mode or other repositories. Always verify native Jekyll build results and rollback if failing.

## Lightweight QA
Run `python3 scripts/qa.py` before merging/publishing. GitHub Pages' original Jekyll build remains the final build/deployment check. No additional Action workflow is installed.

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
