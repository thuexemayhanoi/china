# CHINA Blog — shared maintenance architecture

Production: https://zh.rentbikehanoi.com · GitHub `thuexemayhanoi/china`.
Keep existing URLs, post content, canonical, schema, sitemap and light/dark design.

| What to change | One central place |
|---|---|
| Brand/header/footer labels | `_data/site.json → branding` (mark, wordmark, subtitles) |\n| Contact, address, hours | `_data/site.json → business` |
| Publisher logo and description | `_data/site.json → publisher`, shared `author-box.html` |
| CTA text/destination/variants | `_data/site.json → post_ui.cta`, shared `cta.html`; publisher contact link follows default CTA |
| Post footer hook order | `_includes/post-footer.html` |
| Related and previous/next posts | `_includes/related-posts.html`, `post-navigation.html` |
| Three curated silo/topic links | `_data/site.json → post_ui.hub_links`, `post-hub-links.html` |
| Global JSON-LD | `_includes/schema.html` |
| AI discovery file | `llms.txt` generated from `_data/navigation.json` and `_data/site.json`; `_layouts/default.html` advertises it |
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

## AI discovery and regression checks

`llms.txt` is a small Jekyll-rendered discovery guide, not a replacement for the 300 post HTML pages or sitemap. It uses shared navigation and contact data; no third-party package, new crawler restrictions, Content-Signal policy, A2A agent card or AI scraping opt-in is added. The default site template advertises the root file with one `text/plain` alternate link. `scripts/qa.py` and `scripts/qa_rendered_site.py` validate the source and final build, including shared branding and 331 unchanged HTML canonical/sitemap routes.

