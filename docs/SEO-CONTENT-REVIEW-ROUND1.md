# CHINA — SEO Content Review Round 1 (2026-10-12)

Scope: `thuexemayhanoi/china`. Based on actual GitHub Actions audit artifact **china-seo-audit** from run [38279760155](https://github.com/thuexemayhanoi/china/actions/runs/38279760155), plus manually inspected live source articles. This is **not** a report of Baidu/Google indexing.

## Priority content fixes completed in this round

- **CN-0120** `/blog/hanoi-fifty-models-20/`: removed unsafe assertions that inexperienced riders can quickly begin riding a 50cc and that 30 minutes of practice is sufficient. Reframed with applicable legal-category requirements, training and safer alternatives. Article title and URL remain unchanged; Chinese meta description updated.
- **CN-0070** `/blog/hanoi-pricing-daily-20/`: changed a Vietnamese meta description to Chinese, removed unsupported universal fuel payment assumptions, and linked to the article explicitly explaining how contract-specific fuel rules work. Title and URL unchanged.

These are specific, evidenced edits; there is no automatic word-count padding, rewriting of all 300 articles, or deletion.

## 12 articles flagged below 800 Hanzi in initial scan

| Article | Topic | Hanzi in body at baseline (approx.) | Editorial triage |
|---|---|---:|---|
| CN-0051 | daily price overview | 745 | Review whether comparison/pricing explanation is complete |
| CN-0055 | Honda Click daily quote | 781 | Verify scope of included costs |
| CN-0058 | daily pricing across models | 755 | Distinguish it from price-overview intent |
| CN-0061 | deposit vs daily rent | 765 | Validate return conditions |
| CN-0066 | fuel allocation | 751 | Cross-check fuel clauses against store policy |
| CN-0068 | inventory before short rental | 780 | Distinguish from booking availability |
| CN-0069 | daily price vs upgraded model | 688 | May need an evidence-backed decision example |
| CN-0070 | rent/deposit/fees contract | 741 | **Specific factual/language issue repaired** |
| CN-0072 | helmet equipment fees | 765 | Check equipment vs fee scope |
| CN-0073 | reference price vs final quote | 712 | Check contract vs reference rate distinction |
| CN-0078 | Honda Vision weekly rent | 746 | Review weekly vs monthly comparison |
| CN-0120 | 50cc riding experience | 766 | **Safety framing repaired** |

Minimum word count is an editorial signal, not an SEO ranking threshold. All 12 had five or more H2 sections. Remaining posts are **review candidates**, not automatically invalid.

## 17 repeated primary-keyword groups (actual published front matter)

These are keyword **clusters**, not 17 proven cases of duplicate articles. Common headings with different sub-intent may be valid.

| Published primary keyword | Posts |
|---|---:|
| 河内50cc驾驶要求 | 25 |
| 河内摩托车周租价格 | 25 |
| 河内摩托车日租价格 | 25 |
| 河内摩托车月租 | 25 |
| 河内摩托车骑行安全 | 25 |
| 河内租摩托车合同押金 | 25 |
| 河内老城区取车还车 | 25 |
| 河内踏板车租赁 | 25 |
| 河内老城区附近租摩托车 | 20 |
| 河内50cc踏板车租赁 | 15 |
| 河内50cc摩托车检查 | 10 |
| 河内50cc摩托车租赁 | 10 |
| 河内摩托车月租价格 | 10 |
| 河内摩托车车况检查 | 10 |
| 河内电动车租赁 | 10 |
| 河内老城区租摩托车 | 10 |
| 河内老城区租车路线 | 5 |

**Why these groups exist:** article-matrix `primary_keyword` labels are broad parent targets; multiple subquestions reuse one label intentionally. Plan-matrix working keywords and published front-matter keywords sometimes differ (e.g., `CN-0078` uses narrower weekly pricing target than the plan); do not assume the two sources are identical.

### Verification before further editing

1. Inspect pairs competing for *the same answer and target audience*, not just identical `primary_keyword`. Highest priority: `CN-0051` vs `CN-0058` vs `CN-0073`, and `CN-0061` vs `CN-0070`.
2. Review the eight other short articles for genuinely missing examples/sources. Keep concise pages that already answer a unique question.
3. Once GSC is connected, join **actual query → landing page** results to identify keyword cannibalization. Do not merge, noindex, redirect, or change published URLs without supporting query-level evidence.
4. Monitor `non_chinese_meta_description_ids` from `scripts/seo_monitor.py` on the next scheduled run; check Chinese-language SEO snippets.
5. Validate Baidu crawl/index access from actual mainland-China infrastructure or Baidu Search Resource Platform. GitHub Pages HTTP 200 from outside China is not proof of Baidu accessibility.

## Access status

The connected SEO accounts currently expose GSC properties for the Nguyễn Tú main domain and chatbot, **not** `https://zh.rentbikehanoi.com/`. Google property addition/ownership and Bing/Baidu console submission require the relevant authorized account and cannot be marked complete from this repository audit. The public `https://zh.rentbikehanoi.com/sitemap.xml` returns 200 with 331 URLs.

No DNS, CNAME, theme or factory workflow changed in this review.
