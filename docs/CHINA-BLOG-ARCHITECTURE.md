# CHINA Blog — shared maintenance architecture

Production: https://zh.rentbikehanoi.com · GitHub `thuexemayhanoi/china`.
Keep existing URLs, post content, canonical, schema, sitemap and light/dark design.

| What to change | One central place |
|---|---|
| Brand, contact, address, hours | `_data/site.json → business` |
| Publisher logo and description | `_data/site.json → publisher`, shared `author-box.html` |
| CTA text/destination/variants | `_data/site.json → post_ui.cta`, shared `cta.html` |
| Post footer hook order | `_includes/post-footer.html` |
| Related and previous/next posts | `_includes/related-posts.html`, `post-navigation.html` |
| Three curated silo/topic links | `_data/site.json → post_ui.hub_links`, `post-hub-links.html` |
| Global JSON-LD | `_includes/schema.html` |
| Color / light-dark palettes | `assets/site.css` CSS custom properties |
| Blog component radius and spacing | `assets/blog-enhancements.css` `--blog-*` tokens |
| Optional before/after body promo slots | `_data/site.json → post_ui.slots` and `_includes/post-slot.html` |
| Search | `assets/search/posts.json` generated from real Jekyll `site.posts` |

Features are controlled in `_data/site.json → features`, with `show_post_slots`
**OFF by default** so current appearance does not change. To activate, set it
true and enable `post_ui.slots.before_body.enabled` or `after_body.enabled`.
Each slot has shared eyebrow/title/description/button/href, and its destination
must exist in the site's core sitemap. The slot uses no H1/H2/H3 and never
rewrites Markdown article body.

Internal linking is bounded: Related Posts select genuine Jekyll posts by
exact `seo_silo`, otherwise `topic`. Topic hubs use only curated valid
routes from `sitemap_base`. No arbitrary keyword insertion, bogus post links,
third-party database or heavy dependency.

Run `CHINA Blog UX Build QA` on PR and after merge: source checks, Jekyll
double build (idempotence), rendered SEO and link checks, four disposable
sample articles to exercise silo links/search/CTA/flags. Those fixtures are not
published. Confirm GitHub Pages (main branch) successful deployment and
check sitemap/canonical independently. Search Console indexing is separate.
