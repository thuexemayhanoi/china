# CHINA — 300 Chinese articles / continuous queue

Website: https://zh.rentbikehanoi.com/ — only repo `thuexemayhanoi/china`.

## Editorial inventory
- Existing 250 briefs `CN-0001..CN-0250` remain unchanged in `_data/china-plan.json` and `data/china-matrix.csv`.
- New 50 briefs `CN-0251..CN-0300` are in `_data/china-plan-extra.json` and `data/china-matrix-extra.csv`.
- **300 total in 12 batches × 25**, with 60 briefs per parent: rental, pricing, 50cc, old-quarter, guides.
- Five added child category hubs: `rental/electric`, `pricing/monthly`, `50cc/checklist`, `old-quarter/planning`, `guides/maintenance`.
- 31 core site URLs = existing 26 preserved + 5 new category URLs. Blog post paths remain `/blog/<slug>/`.

## How the factory works
Borrowed the recovery-queue pattern, not English content, from `thuexemayhanoi/web`:
1. `data/china-writer-queue.json` always lists the next ten **unpublished** briefs (read-only feed for a writer).
2. External AI/human writer creates `_drafts/CN-xxxx.md` using the approved brief, original Simplified Chinese, factual source notes and no invented offers or prices.
3. A human reviews legal/factual claims, links, meta and originality. **Only after actual approval**, mark `editor_approved: true` and `reviewed_by: "thuexemayhanoi"` in draft front matter.
4. `CHINA Continuous Article Factory` runs on a draft push and has a 15-minute recovery watchdog (GitHub Actions schedules are best effort). It scans all pending draft files and publishes **at most five genuinely reviewed, QA-passing drafts per run**. Nonapproved/invalid drafts stay unpublished.
5. Publishing updates the correct half of the matrix, refills the queue, adds real articles to Jekyll, and runs Jekyll build plus rendered SEO/link checks before a fast-forward push. Native GitHub Pages rebuilds site and sitemap. Repeated watchdog runs without ready content make no commit.
6. `CHINA 300 Matrix QA` performs read-only matrix/source checks; `CHINA Blog UX Build QA` tests Jekyll twice plus disposable fixture articles.

**The workflow does not call an external AI API or synthesize article text.** Connect an external writer separately or upload original drafts. Ubersuggest is for planning/validation; it is not a free automatic 300-article generator.

## Commands (GitHub Actions or local)
```bash
python3 scripts/china_factory.py status
python3 scripts/china_factory.py plan --batch B11 --limit 5
python3 scripts/china_factory.py queue
python3 scripts/china_factory.py refresh-queue
python3 scripts/china_factory.py pending-count
python3 scripts/china_factory.py validate
python3 scripts/china_factory.py validate --drafts
python3 scripts/china_factory.py process
python3 scripts/china_factory.py pause
python3 scripts/china_factory.py resume
```

- In GitHub → Actions → CHINA Continuous Article Factory → Run workflow choose `status`, `process`, `refresh-queue`, `pause`, or `resume`.
- For manual curated publication, use `CHINA Publish Reviewed Posts` with up to five verified IDs and confirmation `PUBLISH`.
- The queue is operational, **not** a claim that drafts exist or have been published.
- Shared edit-once layouts, NAP, theme, Quick Call, chatbot, canonical, blog post metadata and domain are preserved.

## Safety and authenticity
- Never modify `CNAME`, DNS, GitHub Pages deployment mode, /web, /french or unrelated repos.
- Never invent availability, fee, policy, waived deposits, 50cc license exemptions, reviews or traffic figures.
- Automation cannot certify whether a review was genuinely performed. It requires explicit reviewed front matter and deterministic QA, with human editorial responsibility.
- Scheduled checks may be delayed by GitHub Actions; empty queue is not an error.
