<!-- Write as you work, not retroactively. closeout.py refuses without all 5. -->
## Claim

`radar.svg` asserts: measured on Hendrycks et al.'s ten CHC cognitive domains
(On-the-Spot Reasoning split into static vs dynamic), CURRENT FRONTIER AI
(era-3 = SOTA per axis, mid-2026 → 2026-07) is at or above the
well-educated-adult anchor on Mathematics (Virtuoso — IMO gold + FrontierMath
saturating every tier), Knowledge (Expert — GPQA-D ~94% vs ~65–70% experts),
and Reading & Writing (anchor); **at the doorstep of the anchor on static
reasoning (~90** — ARC-AGI-2 92.5% vs ~60% human panel, but ONE benchmark so
near-not-at); and far below the anchor on **dynamic reasoning (~12/100** —
ARC-AGI-3 ~8–13% plus one game won: off the floor, still the dominant
bottleneck) and long-term memory storage (~12/100). Working memory, memory
retrieval, visual and auditory sit materially below the anchor as
LOW-CONFIDENCE coverage estimates (most lack a human baseline). The profile is
jagged; the static-vs-dynamic reasoning split (**~90 vs ~12**) is its sharpest
asymmetry — narrowed from the 2026-07-03 ~85-vs-5 read but intact, and the
"flat for 3 years" framing is retired. Eras 1–2 (GPT-4 27%, GPT-5 57%) are
Hendrycks' own scores (era-2 R-dynamic = 5 excepted, per Method 4); era-3 is
this thread's SOTA-envelope benchmark-mapped estimate (best model per axis,
named + dated in era3_evidence.csv / MAPPING.md), not a single published score.

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
7. **Re-score RS-2026-07-14 — SOTA-envelope + calibration bridge (APPLIED
   2026-07-14; radar.svg hash 6a8d4110…c943).** FRAMING NOTE: the re-score
   first tried single-lineage (GPT-5.6 Sol), but the re-consult surfaced that
   Sol has confident data on only 4 of 11 axes — a strict Sol chart is mostly
   holes. Operator ruled SOTA-envelope instead: **era-3 = the best current
   result per axis, each model named + dated** (eras 1–2 stay GPT-4/GPT-5 from
   Hendrycks; a chart footnote states era-3 is a per-axis frontier envelope,
   not one system). Rules governing every re-scored point:
   a. **SOTA-envelope.** Era-3 = the best current public result per axis (any
      model), each named + dated in era3_evidence.csv. (Single-lineage on
      GPT-5.6 Sol was tried and dropped — Sol has confident data on only 4 of
      11 axes, so a strict Sol chart is mostly holes.) Model-version AND
      benchmark-version still locked per point; no collapsing distinct
      models/versions into a vague "frontier".
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
      • If the model < the human reference, the score is the honest fraction of
        the anchor the benchmark shows it covering (coverage), low-confidence
        flagged. → ARC-AGI-3: 7–13% and loses games humans complete → still far
        below anchor; the ft09 87% win is spiky, noted but NOT anchor-crossing.
      • **REFINED (gemini re-consult 2026-07-14):** position-vs-human is a
        JUDGMENT informed by the ratio, NOT equal to it — 30% where humans get
        60% is not "half the construct." A single benchmark beating the human
        MEAN lands NEAR the anchor (~90), not AT it, unless a battery
        corroborates (this is why R-static = 90, not 100).
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
sha256sum ../radar.svg      # 6a8d4110decbe60bab459773c07b130eed46b2e9ac7d0b9ba6a61c4852ebc943
```
Runtime: Python 3.12.3 (Ubuntu 24.04), stdlib only (csv, math, sys, xml.sax.saxutils). Output
`radar.svg` is deterministic; the SHA-256 above is the pinned artifact hash.
**Hash lineage:** ae8479c8…1246 (2026-07-03 original) → **6a8d4110…c943 (RS-2026-07-14
re-score, CURRENT).** The prior artifact is superseded on the record, not deleted.
