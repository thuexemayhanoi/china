# CHINA 300 — automatic QA publication using an external writer

Production: https://zh.rentbikehanoi.com/ · Repo: `thuexemayhanoi/china` only.

## Policy

- Target exactly 300 original zh-CN posts, in 12 batches × 25.
- `data/china-factory-state.json`: `manual_review_required: false`, `publication_mode: automatic_qa`, `publisher: external_writer`.
- This is the owner's authorization to **automatically publish when deterministic QA passes**. The pipeline does NOT represent AI QA as a human editor's review, never writes `editor_approved: true`, and marks published metadata `publication_method: automated_qa`.
- This is not AI fact-checking: legal claims require verifiable official source notes; uncertain prices, waivers, guaranteed availability, and unsafe claims are blocked or should be verified before writing.
- Original 250-row manifest/matrix + 50-row additional manifest/matrix remain the immutable content plan.
- All 31 core website URLs, 5 parent hubs, 19 child categories, CNAME, canonical, and native Pages build stay unchanged.

## Correct writer-owned transaction

**Important GitHub Pages behavior:** pushes from GitHub Actions made using `GITHUB_TOKEN` do **not** trigger native branch-based Pages deploy. Therefore **do not create _posts using an Actions self-push.** Mistral or another writer must generate, QA, promote and push with its **own authenticated GitHub connection**, all in one commit. The watchdog workflow is read-only, preventing stale-site false positives.

Every batch:

1. Synchronize latest `main` and inspect current `_drafts`, `_posts`, both matrices, `data/china-writer-queue.json`.
2. Use `python3 scripts/china_factory.py queue` to receive briefs whose draft is **not yet staged**. Repair staged drafts if they fail QA; never overwrite IDs.
3. Write up to five original drafts into `_drafts/CN-xxxx.md`. Respect title, topic, subtopic, URL, at least 800 useful Chinese characters, ≥3 H2, 40–150 Hanzi description, ≥2 valid internal links including parent topic, source requirements and safe factual claims.
4. Run `python3 scripts/china_factory.py validate --drafts`; if any draft fails, fix it. Source QA is a deterministic gate, NOT proof of truth.
5. Run `python3 scripts/china_factory.py process`. This publishes **up to five** passing staged drafts to `_posts`, updates the right matrix (including QA score/date/method), removes the draft and replenishes the queue. Run again if more eligible staged drafts remain; review any blocks instead of bypassing QA.
6. Run `python3 scripts/china_factory.py validate`, `python3 scripts/qa.py` and, where the writer environment supports GitHub Pages Jekyll, `bundle exec jekyll build` followed by `python3 scripts/qa_rendered_site.py`. If build cannot run locally, verify native Pages and rendered QA after the push and treat failures as blockers.
7. Review `git diff --check` and scope; commit **_posts, removed _drafts, both matrices and updated writer queue together**, then push using the authenticated writer identity. Never force push or bypass stale-head checks.
8. Check GitHub Pages native deployment and the live URLs; only then report PUBLISHED/ONLINE. On QA or build failure, pause the next batch and repair.

Commands:

```bash
python3 scripts/china_factory.py status
python3 scripts/china_factory.py queue
python3 scripts/china_factory.py validate --drafts
python3 scripts/china_factory.py process
python3 scripts/china_factory.py validate
python3 scripts/qa.py
git diff --check
git add -A -- _drafts _posts data/china-matrix.csv data/china-matrix-extra.csv data/china-writer-queue.json
git commit -m "china: QA publish next five zh-CN posts"
git push origin HEAD:main
```

Batch of 5 is the per-command safety limit, not an expectation that content from all 300 should be mass-produced without verification. `process` skips invalid drafts, and `queue` skips staged/published IDs to prevent writer duplication. During a queue backlog the writer should drain ready drafts before creating more.

## Workflows

- `CHINA 300 Matrix QA` checks matrix integrity and all staged drafts on PR or push.
- `CHINA Blog UX Build QA` checks Jekyll build, canonical, schema, sitemap, indexability, links and synthetic fixtures.
- `CHINA Continuous Article Factory` is a read-only QA and queue watchdog (15-minute schedule). Its success does not mean an article has been published.
- `CHINA Scoped Article QA` is optional manual read-only testing for chosen IDs.
- The external writer is the **actual publication engine**, and no API key or new subscription is required by this repository.

## Safety

Never change `/web`, other repos, Hostinger DNS, CNAME, Pages source, shared NAP or publicly verified prices during article production. Never claim fake human approval, online delivery, licence exemptions, deposits waived, fabricated legal sources, or unverified SEO volumes. Inspect actual GitHub commit SHA, Matrix, Actions, rendered sitemap and live article URL before confirming publication.
