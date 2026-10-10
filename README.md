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
