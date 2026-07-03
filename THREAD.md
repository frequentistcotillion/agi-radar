---
type: research
status: active
opened: 2026-07-03
closed_at: null
commissioned_by: null
due: null
delivered: null
deliverable: []
supersedes: null
---

# AGI Radar

## Minutes
<!-- Rolling compressed state. A cold agent reads this first. Keep current. -->
New thread. KB search results for prior related work: see the opening turns.

## Turns

### [2026-07-03 14:07 -04:00] greg — admin
Instruction being acted on: "workshop pilot pls (session 46 open — chose step 5, the AGI Radar rebuild, over box-as-code maintenance; full recipe reconstruction in spec/5-next-steps.md step 5)"

### [2026-07-03 14:07 -04:00] claude — admin
Opened this thread from templates/thread-research/, added the INDEX.md row (via new_thread.py).
KB search for prior work: `AGI Radar` →
=== RESULT 1 [score: 0.027] ===
Source: Fixture: Toy Radar (regression target) (2026-07-03, workshop-thread)
Section: ## Method
---
- data/toy.csv — fixed values, chosen to echo the real AGI-radar shape
  (knowledge high, agency low). Never update this file; the fixture's value
  is its fixedness.

- Sort axes by score descending; place highest at 12 o'clock, proceed
  clockwise (workshop radar convention, in miniature).
- Radius scales linearly with score; quarter-scale reference rings.
- Rendering is pure string assembly (stdlib only) so output is byte-stable.

### [2026-07-03 14:08 -04:00] claude — research
Pinned the three anchor refs into refs/ (SHA256SUMS alongside). Identification
reasoning: (1) Hendrycks et al., *A Definition of AGI*, arXiv:2510.18212v3 —
the CHC psychometric base; confirmed it defines ten cognitive domains
normalized to a well-educated adult. (2) Morris et al. (GDM), *Levels of AGI:
Operationalizing Progress on the Path to AGI*, arXiv:2311.02462 — source of
the percentile performance levels (Competent=50th, Expert=90th,
Virtuoso=99th) that become the radar's rings; Hendrycks' "well-educated
adult" anchor sits near the ~80th-percentile band between Competent and
Expert. (3) The "AGI→ASI collective-capability ceiling" ref from the lost
GPT artifact matches Genewein et al. (GDM), *From AGI to ASI*,
arXiv:2606.12683v1 (June 2026): AGI = median-human general system; ASI =
system/collective exceeding large coordinated expert organizations —
supplies the above-individual-human collective rings (research team,
enterprise). Retrieved 2026-07-03 from arxiv.org.
Next: extract the ten CHC domains + the paper's own GPT-4/GPT-5 per-domain
scores from Hendrycks (those are the first two eras' data floor), then
re-derive the benchmark-per-domain mapping for the current (Mythos-class) era.

### [2026-07-03 14:10 -04:00] claude — research
Extracted and VERIFIED Hendrycks Table 1 against the arXiv HTML (grep on the
raw text, not a model summary — summaries can hallucinate numbers): ten
domains K/RW/M/R/WM/MS/MR/V/A/S, each weighted 10%; per-domain contributions
GPT-4 = 8/6/4/0/2/0/4/0/0/3 (Σ27%), GPT-5 = 9/10/10/7/4/0/4/4/6/3 (Σ57%).
Written to data/hendrycks_table1.csv with both contribution and normalized
0–100 domain scores (100 = the well-educated-adult anchor). These are the
GPT-4-era and GPT-5-era series verbatim — using the paper's own numbers for
eras 1–2 keeps those series defensible and pins our era-3 estimates to the
same scale. Checked agidefinition.ai for post-GPT-5 scores: none published
(still only GPT-4 27% / GPT-5 57%, no leaderboard). Consequence: the
Mythos-class (mid-2026 frontier) series must be OUR estimate, derived from a
benchmark-per-domain mapping — which is precisely the lost artifact's
improvement 2, so nothing is lost by the absence.

### [2026-07-03 14:10 -04:00] claude — decision
Radar design decisions (re-deriving the lost artifact, recorded here so the
recipe's Method section has its rationale):
1. **Axes = Hendrycks' ten domains, with R split into R-static and
   R-dynamic → 11 axes.** The preserved finding from the lost version is
   that blended reasoning decomposes: static reasoning (fixed puzzles,
   deduction/induction — LogiQA, ARC-AGI-1/2) is near/at human level while
   dynamic reasoning (interactive, adapt-on-the-fly — ARC-AGI-3) is far
   below. Averaging them into one R hides the single most decision-relevant
   gap. Other domains stay whole: no equally clean public split exists.
2. **Radial scale = fraction of the well-educated-adult anchor (0–100),
   Hendrycks' own scale**, so eras 1–2 need no rescaling. GDM rings sit ON
   this scale: Competent/50th ≈ interior ring below 100; anchor=100 (~80th
   pct, Morris' "well-educated adult" ≈ between Competent and Expert);
   Expert/90th, Virtuoso/99th above it; then Genewein's collective rings
   (research team, enterprise) as ORDINAL rings — equal visual spacing,
   explicitly not a continuous percentile scale above 100. A legend note
   must say the above-anchor rings are ordinal thresholds, not linear.
3. **Above-anchor placement is benchmark-evidenced**: an axis only crosses a
   ring if a public benchmark shows the model beating humans at that
   percentile on that domain's mapped benchmark (e.g. IMO gold ⇒ M crosses
   Virtuoso). Judgment calls per axis go in recipe Method.
4. **Axis order: score-descending from 12 o'clock, clockwise (the spiral)**,
   ordered by the LATEST era's scores — matches the fixture-radar convention
   and the lost artifact.
Next: per-axis benchmark mapping + era-3 SOTA collection into data/.

### [2026-07-03 14:14 -04:00] claude — research
Era-3 (Mythos-class, mid-2026) evidence collected per axis → data/era3_evidence.csv;
derived series → data/radar_scores.csv. Headline evidence and the reasoning
behind each estimate (0–100 = anchor scale; rings only where benchmark-evidenced):
- **K = 100/Virtuoso.** GPQA Diamond ~94% (Gemini 3.1 Pro; Opus 4.7/4.8 and
  GPT-5.2 within 2pts) vs ~65% for PhD domain experts — and breadth across all
  domains simultaneously, which no individual human has. Virtuoso (99th pct),
  not team-level: knowledge breadth ≠ producing new knowledge.
- **M = 100/Virtuoso.** IMO gold 2025 (Gemini Deep Think 35/42, official
  conditions) ≈ 99.99th-pct individual performance; FrontierMath T1–3 >40%
  (early 2026), AIME saturated. Not Team ring: FrontierMath is still <50% and
  open-problem output remains sporadic.
- **RW = 100/Expert.** LongBench v2 64.4% (Opus 4.5, 2026-06-18) vs 53.7%
  time-constrained human experts; era-2 already hit the anchor (Hendrycks
  RW=10/10). Expert, not Virtuoso — long-form authorship quality vs the best
  human writers is still contested and I found no clean benchmark win there.
- **R-static = 100/anchor.** ARC-AGI-2 85% (GPT-5.5, 2026-06-18) vs ~60%
  human-panel average — above the typical human on exactly the fixed-puzzle
  fluid-reasoning family that stumped GPT-4 (~0%). THE PRESERVED FINDING
  HOLDS AND HAS SHARPENED:
- **R-dynamic = 5, no ring.** ARC-AGI-3 (interactive: explore, acquire goals,
  adapt) — ALL frontier systems <1% as of 2026-03 (arXiv:2603.24621) while
  humans complete most games unaided. The static/dynamic split is now ~100 vs
  ~5, the radar's single most decision-relevant asymmetry.
- **WM = 60.** MRCR v2 8-needle at 512K–1M: 76% (Opus 4.6) / 74% (GPT-5.5) —
  only two models reliably use 1M; RULER-style multi-hop shows 50–65%
  effective window. Above era-2 (40) but attention fidelity still lossy.
- **MS = 10.** Still the bottleneck: MemoryBench / Continual Learning Bench
  authors (2026) call SOTA "far from satisfying." Small credit above
  Hendrycks' 0: production persistent-memory features now exist and partially
  work, but they are retrieval contortions, not weight-level accumulation.
- **MR = 60.** Frontier hallucination on SimpleQA-family: 3–9%, roughly
  halved by extended thinking (GPT-5.5 Pro 4.2%, Opus 4.7 5.1%) vs era-2 ~40
  domain score. Improved precision, still below human confabulation floor.
- **V = 70.** MMMU-Pro 94% (GPT-5.4 Pro) / 92.7% (Mythos 5, Fable 5) vs
  76–88.6% human experts — but MMMU-Pro is knowledge-heavy; Hendrycks' Gv
  (low-level perception: rotation, visual search, counting) still shows
  failures, so the domain composite stays below anchor despite the benchmark
  win. This axis has the widest benchmark-vs-construct gap; flag for consult.
- **A = 80.** MMAU ~75.6% vs ~82% human accuracy; speech understanding
  near-human, music/complex-scene reasoning behind.
- **S = 40.** No clean public psychometric-speed benchmark; token throughput
  is not Hendrycks' construct. Held near era-2 with small credit for fast
  non-reasoning tiers. Weakest-evidenced cell in the table; flag for consult.
Era 1–2 note: both R sub-axes carry the Hendrycks composite (0, 70) since no
era-1/2 static/dynamic decomposition was published — the split is only
evidenced in era 3. Documented in radar_scores.csv header.
