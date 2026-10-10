# CHINA · Nguyễn Tú 中文租车网站 🇨🇳

**Production:** https://zh.rentbikehanoi.com/  
**Repository:** https://github.com/thuexemayhanoi/china  
**Language:** 简体中文（zh-CN）  
**Deployment:** GitHub Pages using the **existing** repository settings. This project does not add or change any Actions workflow.

## Scope and design
- Static HTML + CSS + vanilla JavaScript; no WordPress, build tool, package dependencies, backend or external font.
- Apple-inspired minimal visual style, **black / white / gold**; responsive mobile, tablet and desktop.
- Header and footer share the same top-level menu labels and matching category taxonomy.
- Light/dark toggle remembers the user's preference; mobile navigation closes on link click, backdrop, Escape or desktop resize.
- Sidebar collapses on mobile and is shown on desktop.
- Homepage has **no hero image**. Its hero includes an instant reference-price calculator using published Nguyễn Tú rates.
- Every page has its own canonical URL under **https://zh.rentbikehanoi.com** (never github.io for SEO).

## Site map
- `/` – 首页 & hero 计算器
- `/blog/` – 博客首页（**0 篇文章**, no fake links; noindex until content goes live）
- `/prices/` – 完整参考价格表
- `/faq/` – 常见问题
- `/contact/` – 联系我们
- `/topics/<parent>/` – 五个父分类（可索引）
- `/topics/<parent>/<child>/` – 子分类（目前 noindex,follow，扩充有用内容后再审核开放索引）

### 200-post editorial capacity (NOT 200 published posts)

| Parent category | Future article allocation | Children |
| --- | ---: | --- |
| 租赁服务 (`rental`) | 50 | `scooters`, `monthly`, `automatic` |
| 租车价格 (`pricing`) | 40 | `daily`, `weekly`, `deposits` |
| 50cc 摩托车 (`50cc`) | 35 | `models`, `requirements` |
| 老城区附近 (`old-quarter`) | 35 | `directions`, `pickup` |
| 租车指南 (`guides`) | 40 | `contracts`, `safety`, `returns` |
| **TOTAL** | **200** | **Currently published: 0** |

**Important:** These are editorial allocations, not article URLs or published posts. Do not mass-publish empty or duplicated pages. Write original, accurate Simplified Chinese content and review before publication.

## How to add one new article later
1. Choose an existing parent and child topic.
2. Create `/blog/<unique-descriptive-slug>/index.html` using the shared site header/footer and CSS/JS assets.
3. Write helpful original Chinese content, factual SEO title/description, unique canonical on https://zh.rentbikehanoi.com, and trustworthy internal links.
4. Add its link to the appropriate category/blog listing; then add its URL to `sitemap.xml`.
5. Update article count **only after publication and QA**. Do not change the domain CNAME.

## SEO guardrails
- `<html lang="zh-CN">`, unique title, meta description and canonical URL on each page.
- `robots.txt` and `sitemap.xml` point to https://zh.rentbikehanoi.com.
- 5 parent-topic pages + homepage + prices + FAQ + contact are included in the sitemap.
- Empty blog and thin child category shells are `noindex,follow` until populated.
- There are no fabricated articles, article dates, ratings, reviews or testimonials.
- All prices are indicative; do not advertise deposit-free renting.
- Don't assert 50cc licensing exemptions or Old Quarter delivery without independent confirmation.

## Business data (single source of truth)
- Brand: **Cho Thuê Xe Máy Nguyễn Tú**
- Google Business Profile: **Thuê xe máy ở Hà Nội - Nguyễn Tú**
- Address: **112 Nguyễn Văn Cừ, Bồ Đề, Long Biên, Hà Nội, Việt Nam**
- Phone/Zalo: **0942 467 674** / **+84 942 467 674**
- Opening hours: **09:00–21:00 daily**
- Business website: https://thuexemaynguyentu.com/
- Chinese canonical domain: https://zh.rentbikehanoi.com

## Operations / safety
- **Do not change** `CNAME`, custom-domain settings, GitHub Pages source, DNS or Hostinger configuration for routine content updates.
- Use the existing GitHub Pages deployment workflow/mode. No new build process is necessary.
- For rollback, revert the website commit in this repo, not the DNS or `CNAME`.
- Pricing and deposit terms must be reconfirmed with the shop before booking.
