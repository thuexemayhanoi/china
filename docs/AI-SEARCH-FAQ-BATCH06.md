# CHINA FAQ / AI Search Matrix — Batch 06

Site: https://zh.rentbikehanoi.com/ · Repo: `thuexemayhanoi/china`

## Ten URL-level edits performed

This release improves existing source content, not an invented blanket FAQ block. It does not claim Google indexing, rich results, or AI citations.

### Five P1 topic URLs

| URL | User-intent improvement |
|---|---|
| `/topics/guides/safety/` | Direct pre-ride inspection and rain/traffic decisions; safe alternatives to riding in hazardous conditions |
| `/topics/old-quarter/` | Long Biên store location instead of Old Quarter claim, plus delivery/appointment requirements |
| `/topics/pricing/` | Real Honda Wave / Vision price references from shared data and separately confirmed deposit/contract; no arithmetic quote invention |
| `/topics/rental/` | Legal qualification, actual riding skill, real store address and no automatic delivery |
| `/topics/rental/scooters/` | Published Vision, Air Blade, Click/Mio day-price values from shared config, actual stock and legitimate licence caveats |

### Five P2 article URLs

| Article | User-intent improvement and correction |
|---|---|
| CN-0009 | Luggage load/capacity; no unsupported hanging bags on handlebars or passenger area |
| CN-0010 | Short-distance commuting selection subject to legal riding ability; no guaranteed replacement during repairs |
| CN-0015 | Safe compliant helmet sizing/strap/condition; no claim that the rental shop always has replacements |
| CN-0016 | Local traffic signs override other parked vehicles; no advice to assume sidewalks with parking are approved |
| CN-0018 | Shared pickup photos plus agreement records; removed unsupported 90% dispute claim and universal timestamp validity |

Posts retain original `article_id`, `date`, category, existing permalink and H2 topic structure; SEO descriptions and `last_modified_at: 2026-10-12` reflect actual edits.

## Matrix status after source edits

| Status | URL count |
|---|---:|
| P0_IMPLEMENTED | 1 |
| P1_IMPLEMENTED | 3 |
| P1_CONTENT_REVISED | 20 |
| P1_REVIEW_PENDING | 3 |
| P2_ANSWER_FIRST_REVISED | 27 |
| P2_EDITORIAL_REVIEW_PENDING | 218 |
| NO_FORCED_FAQ; KEEP_UNIQUE_CONTENT | 59 |
| **TOTAL** | **331** |

**Pending:** `/about/`, `/contact/`, `/privacy/` plus 218 P2 posts. Business contact and privacy pages should be reviewed for accuracy, not filled with generic FAQ schema. All edited rows keep `review_required=true` for any further full-context fact review.

## Release gates

Require 300 published posts, 331 canonical sitemap URLs and unchanged route and schema structure. Run native Matrix QA, Jekyll Blog UX build and rendered SEO/link checks before merge, then verify GitHub Pages deployment and selected live routes. No DNS, CNAME, plugin, heavy JS or dependency changes.
