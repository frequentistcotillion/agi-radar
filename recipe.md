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
  → `refs/hendrycks-2025-a-definition-of-agi-2510.18212v3.md` (text extract;
  source PDF at `refs/originals/`)
- Morris, M. R. et al. (Google DeepMind, 2023). *Levels of AGI:
  Operationalizing Progress on the Path to AGI*. arXiv:2311.02462.
  → `refs/morris-2023-levels-of-agi-2311.02462.md` (text extract; PDF at `refs/originals/`)
- Genewein, T. et al. (Google DeepMind, 2026). *From AGI to ASI*.
  arXiv:2606.12683v1. → `refs/genewein-2026-from-agi-to-asi-2606.12683v1.md`
  (text extract; PDF at `refs/originals/`)
- All three retrieved 2026-07-03 from arxiv.org; source PDFs preserved under
  `refs/originals/` (never read into context — read the text extract), SHA-256
  in `refs/SHA256SUMS`. Ingested to text-only extracts 2026-07-05 via
  ingest_ref.py to keep them out of the context-window read path.
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
   spacing, explicitly not linear.
   **Scale honesty (added 2026-07-03 after recipient critique):** the scale
   is dual-regime and the two regimes measure different things. BELOW the
   anchor, a score is sub-ability COVERAGE relative to one reference point
   (fraction of adult-anchor sub-abilities attained — e.g. Speed 30 = 3 of
   10 speeded sub-abilities at adult level), NOT a placement in the human
   percentile distribution. A model at 50 is not "median human." The
   original 0.5 ring was labeled "Competent (50th pct)", which implied
   percentile continuity below the anchor; that label is removed (now a
   coverage gridline). True percentile comparability — what a reader
   naturally wants — would require human norm distributions ON the mapped
   benchmarks, which mostly do not exist publicly: available baselines are
   point estimates (GPQA expert mean ~65%, ARC-AGI-2 panel mean ~60%,
   MMMU expert range), not distributions. The only genuinely
   percentile-rich evidence in this dataset is contest math (IMO medal
   thresholds over a selected population). ABOVE the anchor, ring crossings
   are therefore evidence-gated ordinal claims, not measured percentiles.
   Closing this gap requires either administering normed psychometric
   batteries to models (Hendrycks' approach, but scored against the full
   norm distribution rather than one anchor) or collecting representative
   human samples on the AI benchmarks. Neither is available to this thread.
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
5. **Collective rings are drawn but not yet operationalized (acknowledged
   2026-07-03):** no axis can currently reach Research-team/Enterprise
   because no benchmark operationalizes "exceeds a coordinated expert
   team." Candidate crossing criteria, unresolved: (a) event-based — the
   system solves problems that defeated funded expert teams (open
   conjectures, validated novel therapeutics); (b) horizon-based — METR-
   style task-completion horizons reaching team-scale effort (hundreds of
   coordinated human-hours) by a single system instance; (c) the copies
   baseline — N parallel instances ≈ N-person team — is a serviceable
   lower bound but prices coordination at zero in both directions. Until
   one is adopted, the top two rings are honest aspiration markers only.
6. Rendering (`code/radar.py`, stdlib-only string assembly for byte
   stability): axes sorted by era-3 radial descending (tie-break: label),
   highest at 12 o'clock, clockwise — the spiral. Three translucent era
   polygons, anchor ring emphasized, ordinality footnoted on the chart.
   Ring labels (incl. Competent/50th) render above the polygons with a
   white halo so the inner ones stay legible over the era fills.
7. **Re-score RS-2026-07-14 — single-lineage + calibration bridge (PROPOSED,
   pending operator OK; not yet applied to radar_scores.csv).** The era-3
   column is being re-derived from the **GPT-4 → GPT-5 → GPT-5.6 Sol** lineage
   (operator decision 2026-07-14; consistent with eras 1–2, which are the
   GPT line in Hendrycks Table 1). Rules governing every re-scored point:
   a. **Single-lineage lock.** Era-3 = GPT-5.6 Sol's OWN published result on
      each axis's mapped benchmark. Where Sol has no published result on that
      benchmark, the point is carried from era-2 with a `no-Sol-data` flag, or
      the axis is marked provisional — NEVER back-filled with a different
      model (the model-snapshot conflation codex flagged 2026-07-14).
   b. **Primary-sets-the-point.** Only a primary source (benchmark's own
      site / paper / official leaderboard) may SET a point; secondary
      aggregators may only flag a lead to verify at primary. Each point logs
      benchmark + version + tier + metric + Sol score + eval date + URL +
      grade in era3_evidence.csv.
   c. **Calibration bridge — the score is NOT the raw benchmark %.** An axis
      score is Sol's position RELATIVE to the benchmark's human reference, on
      the coverage/anchor semantics of Method 2:
      • If Sol ≥ the benchmark's human-anchor reference (well-educated adult /
        the benchmark's stated human baseline), the axis is AT the anchor
        (100). A ring crossing (Expert 90th / Virtuoso 99th) still needs the
        percentile-rich evidence of Method 3, not merely beating a mean.
        → e.g. ARC-AGI-2 92.5% vs ~60% human panel puts R-static ≈ 100/anchor,
        NOT 92 (correcting codex's direct-% mapping).
      • If Sol < the human reference, the score is the honest fraction of the
        anchor the benchmark shows Sol covering (coverage), low-confidence
        flagged. → ARC-AGI-3: Sol 7–13% and loses games humans complete →
        still far below anchor; the ft09 87% win is spiky, noted but NOT
        anchor-crossing.
   d. **Construct integrity over convenience.** Where the mapped benchmark is
      a poor proxy for the CHC construct (codex: MR ← hallucination-rate is
      factuality, not durable retrieval), FIX the mapping — pick a better
      benchmark or mark the axis unmeasurable — do not re-source a wrong proxy.
   e. **Change control.** Any axis moving >10 points from its 2026-07-03 value,
      or any headline change, triggers a mandatory adversarial re-consult
      before radar.svg is regenerated. The plotted set (radar_scores.csv)
      becomes single-source + dated; era3_evidence.csv stays append-only raw
      evidence. On OK: execute axis-by-axis → re-plot as a dated new version
      (new hash, old artifact superseded not deleted) → final re-audit →
      republish (human gate).

## Regenerate
```
# from the thread root (this directory)
cd code
rm -f ../radar.svg          # ensure a stale artifact can't mask a broken generator
python3 radar.py            # reads ../data/radar_scores.csv, writes ../radar.svg
sha256sum ../radar.svg      # ae8479c87ffba30717c89038558770ce30a027f981cbaa73059004506d981246
```
Runtime: Python 3.12.3 (Ubuntu 24.04), stdlib only (csv, math, sys, xml.sax.saxutils). Output
`radar.svg` is deterministic; the SHA-256 above is the pinned artifact hash.
