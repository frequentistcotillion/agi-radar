<!-- Write as you work, not retroactively. closeout.py refuses without all 5. -->
## Claim

`radar.svg` asserts: measured on Hendrycks et al.'s ten CHC cognitive domains
(with On-the-Spot Reasoning split into static vs dynamic), frontier AI in
mid-2026 (Mythos-class) is at or above the well-educated-adult anchor on
Mathematics (Virtuoso ring), Knowledge (Expert ring), and Reading & Writing
(anchor), with static reasoning just below the anchor (~85) — while
remaining far below the anchor on dynamic reasoning (~5/100, ARC-AGI-3),
long-term memory storage (~10/100, the standing bottleneck), and materially
below it on working memory, memory retrieval, visual, auditory, and speed. The capability profile is jagged and
the static/dynamic reasoning split (~85 vs ~5) is its sharpest asymmetry.
Era-1/2 series (GPT-4 27%, GPT-5 57%) are the paper's own scores — with one
exception: era-2 Reasoning (dynamic) is 5, from ARC-AGI-3 measurements of
GPT-5-era systems, NOT the paper's composite R (see Method 4). The era-3
series is this thread's benchmark-mapped estimate, not a published score.

## Inputs

- Hendrycks, D. et al. (2025). *A Definition of AGI*. arXiv:2510.18212v3.
  → `refs/hendrycks-2025-a-definition-of-agi-2510.18212v3.pdf`
- Morris, M. R. et al. (Google DeepMind, 2023). *Levels of AGI:
  Operationalizing Progress on the Path to AGI*. arXiv:2311.02462.
  → `refs/morris-2023-levels-of-agi-2311.02462.pdf`
- Genewein, T. et al. (Google DeepMind, 2026). *From AGI to ASI*.
  arXiv:2606.12683v1. → `refs/genewein-2026-from-agi-to-asi-2606.12683v1.pdf`
- All three retrieved 2026-07-03 from arxiv.org; SHA-256 in `refs/SHA256SUMS`.
- Era-3 benchmark scores: public leaderboards/reports retrieved 2026-07-03,
  itemized with sources in `data/era3_evidence.csv`.

## Data

- `data/hendrycks_table1.csv` — Table 1 of arXiv:2510.18212v3 (per-domain
  contributions for GPT-4 and GPT-5), verified 2026-07-03 by grep against
  arxiv.org/html/2510.18212v3 (not a model summary). Retrieval date and URL
  in file header.
- `data/era3_evidence.csv` — per-axis mid-2026 SOTA evidence: benchmark,
  score, model, as-of date, human baseline, source. Retrieved 2026-07-03.
- `data/radar_scores.csv` — the derived plotting series (input to
  `code/radar.py`): eras 1–2 from hendrycks_table1 (×10 to the 0–100 anchor
  scale), era 3 estimated from era3_evidence per the Method judgment calls.

## Method

1. Axes = Hendrycks' ten CHC domains with R split into R-static / R-dynamic
   (11 axes). Rationale (THREAD.md decision turn 2026-07-03 14:10): the
   static/dynamic gap is the most decision-relevant finding and averaging
   hides it; no other domain has an equally clean public decomposition.
   R-dynamic scope (sharpened 14:59): novel-environment skill acquisition,
   triangulated across three eval families (ARC-AGI-3, BALROG novel-env
   slice, continual-learning benches) — explicitly NOT long-horizon agentic
   execution in prior-rich domains (METR time horizons), which is high,
   rising fast, and outside this axis by design.
2. Radial scale: 1.0 = Hendrycks' well-educated-adult anchor, so eras 1–2
   plot verbatim. Above the anchor, GDM performance levels (Morris:
   Expert=90th pct, Virtuoso=99th) and Genewein collective levels (research
   team, enterprise) are ORDINAL rings at 1.25/1.50/1.75/2.00 — equal visual
   spacing, explicitly not linear. Competent (50th) drawn at 0.5 as an
   interior reference.
3. Ring placement rule: an era-3 axis crosses a ring only on benchmark
   evidence of beating humans at that percentile on the mapped benchmark.
   After adversarial codex consult (turns of 2026-07-03 14:18–14:20):
   M = Virtuoso (IMO gold — percentile-rich selected population; contest
   math, not research math); K = Expert, downgraded from Virtuoso (GPQA-D
   94% vs ~65% mean-expert baseline is not a 99th-percentile calibration);
   RW = anchor, Expert ring removed (LongBench v2 is long-context reading
   under time constraint, not writing, and not 90th-pct evidence);
   R-static = 85 no ring, downgraded from anchor (the 85% ARC-AGI-2
   aggregator claim could not be verified at a primary source; verified
   figures are 54.2% standalone frontier / 72.9% specialized solver vs ~60%
   human panel); V = 70 with BLINK as the Gv-construct headline (humans
   95.7% vs ~70.7% SOTA — MMMU-Pro demoted to secondary as knowledge-heavy);
   S = 30, era-2 value carried unchanged (no benchmark, no evidence of
   change — lowest-confidence cell).
4. Era-1/2 values for R-static carry the paper's composite R (0, 70): the
   Hendrycks R battery (deduction, induction, ToM, planning, WCST) is a
   static-instrument measure. R-dynamic does NOT inherit the composite —
   doing so (as this recipe's first version did) painted GPT-5-era dynamic
   reasoning at 70 and made mid-2026 look like a regression. ARC-AGI-3
   (arXiv:2603.24621) measured GPT-5-era frontier systems at <1%, so
   R-dynamic is 0 / 5 / 5 across the eras. Corrected 2026-07-03 after the
   operator caught the conflation (decision turn 14:45).
5. Rendering (`code/radar.py`, stdlib-only string assembly for byte
   stability): axes sorted by era-3 radial descending (tie-break: label),
   highest at 12 o'clock, clockwise — the spiral. Three translucent era
   polygons, anchor ring emphasized, ordinality footnoted on the chart.
   Ring labels (incl. Competent/50th) render above the polygons with a
   white halo so the inner ones stay legible over the era fills.

## Regenerate
```
# from the thread root (this directory)
cd code
rm -f ../radar.svg          # ensure a stale artifact can't mask a broken generator
python3 radar.py            # reads ../data/radar_scores.csv, writes ../radar.svg
sha256sum ../radar.svg      # 81feb3d9188a50bc23163997821c8f4ced42dee49b636c5513616097b0067c55
```
Runtime: Python 3.12.3 (Ubuntu 24.04), stdlib only (csv, math, sys, xml.sax.saxutils). Output
`radar.svg` is deterministic; the SHA-256 above is the pinned artifact hash.
