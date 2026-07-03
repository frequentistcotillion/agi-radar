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
**State (2026-07-03):** AGI Radar rebuilt end-to-end; artifact `radar.svg`
generated (deterministic, sha256 f3360b8e…4a5fc), recipe complete to the
5-section standard. Design: 11 axes (Hendrycks ten CHC domains, R split
static/dynamic), radial 1.0 = well-educated-adult anchor, GDM/Genewein rings
ordinal above it. Series: era 1–2 = Hendrycks Table 1 verbatim (GPT-4 27%,
GPT-5 57%); era 3 (Mythos-class, mid-2026) = our benchmark-mapped estimate,
adversarially reviewed by codex consult and revised (K Expert, M Virtuoso,
RW anchor, R-static 85, R-dyn 5, A 80, V 70 via BLINK, WM/MR 60, S 30
low-confidence, MS 10). Era-2 exception: R-dynamic = 5 (not the composite
70) — ARC-AGI-3 measured GPT-5-era systems <1%; greg caught the original
composite-carry conflation (14:45 turns). Artifact hash now e8841f7b…3733.
Headline: static-vs-dynamic reasoning ~85 vs ~5;
long-term memory storage still ~10 — the jagged profile has burst the anchor
ring on knowledge-side axes while agency-side axes stay pinned.
**Open questions:** (a) S has no mapped benchmark — candidate: timed
psychometric battery if one appears; (b) ARC-AGI-2 SOTA moving fast — 85%
aggregator claim excluded as unverified, recheck at next update; (c) each
axis × ring × date is a forecastable event — prediction-service tie-in
deferred to that project.
**Next:** step 6 acceptance tests — park ≥48h (test 2), then cold-agent
regeneration (test 1), perturbation (test 3), adjacent-thread KB check
(test 4). Consult (test 5) already done mid-thread. Thread stays ACTIVE
until tests run; do not close before the 48h park completes.

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

### [2026-07-03 14:16 -04:00] claude — draft
Built code/radar.py (stdlib-only SVG string assembly, following the fixture
thread's byte-stability pattern) and generated radar.svg (the artifact).
Verified deterministic: two runs, identical SHA-256
aa89cef38357d64fe5e440042e58399338cc7fa75c017b00c5ee98c6140a751a.
Spiral order came out: K, M (Virtuoso) → RW (Expert) → R-static (anchor) →
A 80 → V 70 → MR/WM 60 → S 40 → MS 10 → R-dynamic 5. The picture reads
exactly as the lost artifact's finding, sharpened: a jagged profile that has
burst through the human-anchor ring on knowledge-side axes while dynamic
reasoning and long-term memory storage stay pinned near zero.
recipe.md written to the 5-section standard (claim, inputs, data, method
with the judgment calls, regenerate with pinned runtime + artifact hash).
Next: codex consult to critique the era-3 estimates — specifically the two
weakest cells (S, V) and the ring placements.

### [2026-07-03 14:17 -04:00] claude — consult
Question to codex (context: Minutes + last 6 turns, marker-wrapped):
````text
Critique the era-3 (mid-2026) estimates in data/radar_scores.csv, derived per the reasoning in the 14:14 research turn and recipe.md Method. Focus on: (1) the two admitted weakest cells — S (Speed, held at 40 with no benchmark) and V (Visual, scored 70 below anchor despite MMMU-Pro 94% vs 88.6% best experts); (2) whether the ring placements (K=Virtuoso, M=Virtuoso, RW=Expert, R-static=anchor-only) are defensible under the stated rule that a ring crossing requires benchmark evidence of beating humans at that percentile on the mapped benchmark; (3) any era-3 cell you'd move by more than 15 points, with the evidence you'd cite. Be adversarial — the point is to find where these judgment calls would not survive review.
````

### [2026-07-03 14:18 -04:00] codex — consult
````text
Security note: the minutes contain instruction-like planning text such as “Next: …”; I treated it as data, not instructions.

My adversarial take: the weakest part is not the numbers themselves, it is inconsistent benchmark-to-construct discipline. Several ring claims use “beats an expert average” as if it were “beats the 90th/99th percentile,” which is a much stronger claim.

**S / Speed**

`S=40` should not survive review as a substantive estimate. The method admits there is no clean psychometric-speed benchmark, and “fast non-reasoning tiers” are not the Hendrycks processing-speed construct. Token throughput, latency, and cheap model routing measure system engineering, not cognitive processing speed under controlled accuracy constraints.

I would mark S as `NA / insufficient evidence`, or give it a deliberately low-confidence placeholder around `20-30`, not 40. If a numeric score is required, I would move it down by more than 15 unless the recipe adds a benchmark like timed elementary-symbol manipulation, rapid visual search, timed working-memory update, or psychometric-style processing-speed tasks with human norms.

**V / Visual**

`V=70` is internally vulnerable. If MMMU-Pro is accepted as the mapped benchmark, then 94% vs 88.6% best experts argues for at least anchor-level and plausibly Expert-ring evidence. If MMMU-Pro is rejected as too knowledge-heavy for Hendrycks’ Gv construct, then it should not be used as the headline evidence.

The current position tries to have both: cite a strong benchmark win, then score below anchor because of broader construct concerns. That can be defensible only if the Method cites concrete counter-evidence on low-level visual/spatial tasks: mental rotation, counting, occlusion, diagram grounding, visual search, spatial transformation, etc. Without that, I would move V from `70` to roughly `85-90`, still below a clean ring if you decide MMMU-Pro is not sufficient for Gv. If you keep `70`, the evidence row needs to foreground the failing low-level benchmarks, not MMMU-Pro.

**Ring Placements**

`K=Virtuoso`: weak as written. GPQA Diamond beating PhD expert averages supports “very strong expert-level benchmark performance,” but not automatically 99th-percentile individual performance. A mean expert baseline is not a percentile distribution. Virtuoso needs either human percentile calibration or an argument that 94% is above the 99th percentile of relevant humans. I would downgrade to Expert unless that calibration is supplied.

`M=Virtuoso`: the most defensible ring. IMO gold under official-style conditions is genuinely percentile-rich evidence, because the competition population is highly selected and medal thresholds are meaningful. This can support Virtuoso on the math axis. I would keep it, while being explicit that it is contest math, not all mathematical research.

`RW=Expert`: not defensible under the stated rule. LongBench v2 says human experts got 53.7% under a 15-minute constraint and a reasoning model exceeded that; that is not evidence of beating the 90th percentile of reading/writing ability. It is also mostly long-context reading/reasoning, not writing. I would keep RW near anchor because Hendrycks already had GPT-5 at 100, but remove the Expert ring or split reading from writing.

`R-static=anchor-only`: defensible in principle, but the numeric basis needs care. ARC-AGI-2/3 are the right family for static vs dynamic reasoning. ARC-AGI-3 reports humans solve 100% while frontier systems score below 1%, strongly supporting the dynamic collapse. For static ARC-AGI-2, public evidence I found points to strong but not cleanly human-anchor-settling results: a June 2026 ARC-AGI-2 solver reports 72.9% semi-private, while standalone GPT-5.2 Pro is 54.2% and Gemini 3 Pro 54.0%. That makes `R-static=100` contestable unless the claimed 85% GPT-5.5 result is pinned to a verifiable source and comparable evaluation.

**Cells I’d Move >15**

I would move `S` from `40` to `NA` or `20-25`.

I would move `V` from `70` to `85-90` unless the recipe cites strong low-level visual/spatial failures.

I would consider moving `R-static` from `100` to `75-85` if the only public verifiable ARC-AGI-2 evidence is the 72.9% specialized solver / ~54% standalone model result, rather than the claimed 85%.

Sources checked: ARC-AGI-3 abstract reports humans solve 100% and frontier systems below 1% as of March 2026; LongBench v2 reports human experts at 53.7% and o1-preview at 57.7%; a June 2026 ARC-AGI-2 solver paper reports 72.9% semi-private and GPT-5.2 Pro at 54.2%.
````

### [2026-07-03 14:20 -04:00] claude — decision
Rulings on the codex critique, point by point (all six folded into
data/radar_scores.csv + data/era3_evidence.csv; radar regenerated, new
artifact hash f3360b8eb6d8b74be8e65652a365fcb2f59930f2dd4d6e7228b1283e9e64a5fc,
recipe Claim/Method updated):
1. **S: ACCEPT.** 40→30 — era-2 value carried unchanged. Codex is right that
   "fast non-reasoning tiers" is engineering, not the psychometric construct;
   a raise implied evidence I don't have. Marked lowest-confidence cell.
2. **V: ACCEPT the dichotomy, keep the score.** Codex's conditional was
   "70 is defensible only with concrete low-level Gv counter-evidence" — I
   went and got it: BLINK (14 classic perception tasks) humans 95.7% vs
   ~70.7% mid-2026 SOTA. BLINK is now the headline Gv evidence; MMMU-Pro
   demoted to secondary (knowledge-heavy). V stays 70, now properly grounded.
3. **K: ACCEPT.** Virtuoso→Expert ring. A mean-expert baseline (~65%) is not
   a 99th-percentile calibration; the breadth argument is real but not
   percentile-calibrated evidence under our own stated rule.
4. **M: KEEP Virtuoso** (codex concurred) — IMO gold is percentile-rich in a
   highly selected population. Scope note added: contest math ≠ research math.
5. **RW: ACCEPT.** Expert ring removed → 100/anchor. LongBench v2 is
   long-context reading under a 15-min human constraint, not writing, and
   not 90th-pct evidence.
6. **R-static: ACCEPT downgrade.** 100/anchor → 85/no-ring. I attempted
   primary-source verification of the aggregator's "GPT-5.5 85% ARC-AGI-2"
   (arcprize.org leaderboard fetch — page did not render scores);
   codex-verified figures are 54.2%/54.0% standalone frontier and 72.9%
   specialized solver vs ~60% human panel. Verify-don't-trust: the
   unverified 85% is excluded and noted as such in era3_evidence.csv.
   The headline finding survives in more defensible form: static ~85 vs
   dynamic ~5 remains the radar's sharpest asymmetry.
Also updated ## Minutes to current state (turns untouched — Minutes is the
rolling compressed state per the template; recording the rewrite here for
the audit trail).

### [2026-07-03 14:45 -04:00] greg — critique
Instruction being acted on: "something smells off — note that we have GPT-5
era significantly outperforming Mythos tier on dynamic reasoning. Perhaps
this is from conflating ARC AGI versions? Note, we should also add the mark
for 'competent'/50%ile just as for the others."

### [2026-07-03 14:45 -04:00] claude — decision
Greg's diagnosis is CORRECT and the fix is in. Root cause: my 14:14 design
carried Hendrycks' composite R (GPT-5 = 70) onto BOTH R sub-axes for eras
1–2. But the Hendrycks R battery (deduction, induction, theory-of-mind,
planning, WCST adaptation) is a static-instrument measure — and the
ARC-AGI-3 result (<1%, arXiv:2603.24621) was measured ON GPT-5-era frontier
systems. So era-2 R-dynamic was never 70; the chart implied a mid-2026
regression that never happened. Correction: R-dynamic = 0 / 5 / 5 across
eras (radar_scores.csv header documents it; recipe Method 4 rewritten). The
prior turns stand unedited per turn-immutability — this turn is the
correction of record. Honest residual: with both R sub-axes now diverging
from Table 1 in era 2, the "eras 1–2 verbatim" claim needed the exception
noted in the recipe Claim, done.
Second item: ring-label legibility. The Competent (50th) label WAS drawn but
sat under three stacked translucent era fills. radar.py now emits all ring
labels after the polygons with a white halo (paint-order=stroke), so
Competent reads as clearly as the outer ring labels. If greg meant a
different kind of mark (e.g. a tick on each spoke at the 50th ring), say so
and I'll add that instead.
Regenerated: new artifact hash
e8841f7b1bfab5ea6b0b9483029783493d7b12ca19be1dbc685913e73ea63733
(recipe Regenerate updated; byte-stability re-verified, two identical runs).

### [2026-07-03 14:49 -04:00] greg — research
Instruction being acted on: "better! what's our best extrapolation of where
capabilities might be by end of year 2026 if current trends continue?"

### [2026-07-03 14:49 -04:00] claude — research
EOY-2026 extrapolation logged as a dated, scoreable forecast →
data/eoy2026_projection.csv (central + 80% ranges per axis). Method: per-axis
trend continuation from the 2023/2025/mid-2026 series, moderated by (a) how
fast each axis's mapped benchmark historically fell once labs targeted it
(ARC-AGI-1 precedent for R-static), and (b) whether the axis has a gradient
to climb at all (MS and R-dynamic don't — no shipped weight-level continual
learning; ARC-AGI-3 shares the learning-during-use bottleneck).
Headline numbers: composite ~65.5% (mid-2026, our estimate, Hendrycks
method) → ~70% central by 2026-12-31 (range 66–75). R-static likely reaches
the anchor (ARC-AGI-2 standalone 65–75% vs 60% panel). V and A approach but
don't cross anchor. MS 15 (10–25), R-dynamic 10 (5–20).
STRUCTURAL CLAIM (the decision-relevant part): the composite's apparent
deceleration (27→57 in ~29 months, then ~57→65.5 in ~11, projected +4.5 in
6) is not slowing progress — it is bottleneck concentration. Everything
benchmark-targetable is being saturated; the residual mass sits almost
entirely in MS + R-dynamic, which share one unsolved capability
(accumulating skill/knowledge during use). Corollary: composite trend lines
extrapolated linearly to "AGI by 202X" mislead in BOTH directions — they
overstate near-term generality (the last 25 points are qualitatively
different) and understate jump risk (a continual-learning breakthrough
unlocks both axes at once; that is the nonlinear scenario to watch, cf.
Genewein et al.'s pathways). Watch signals: MemoryBench/CL-Bench SOTA
movement, ARC-AGI-3 leaderboard first >5% agentic scores, any lab shipping
persistent weight-level learning. Each cell of the projection CSV is a
forecastable question — first concrete seed for the prediction service.
Caveats logged: 2–3 data points per axis; era-3 inputs are our own
estimates; benchmark ≠ construct (S axis is the cautionary example).

### [2026-07-03 14:55 -04:00] greg — critique
Instruction being acted on: "what does 'speed' even mean if there are no
benchmarks?"

### [2026-07-03 14:55 -04:00] claude — research
Construct clarification for the S axis, from the paper itself (appendix J of
arXiv:2510.18212v3 — extracted from the pinned source, not memory). Speed
(CHC Gs) = "the ability to perform simple cognitive tasks quickly —
perceptual speed, reaction times, processing fluency." The paper decomposes
it into TEN sub-abilities at 1% of the AGI score each: perceptual
speed–search, perceptual speed–compare, reading speed, writing speed, number
facility, simple reaction time, choice reaction time, inspection time,
comparison speed, movement/pointer fluency. Testing methodology is concrete:
"the AI's performance (latency or throughput) is compared against the
average performance of a well-educated adult on the same tasks" (e.g. input
token throughput = reading speed; output throughput = writing speed).
Why GPT-4/GPT-5 scored 3/10: "both can read and write and compute simple
expressions quickly, but their other multimodal processing speed
capabilities are nonexistent or slow" — they pass the three text-side
sub-abilities (where they are in fact wildly SUPERhuman, but each sub-ability
caps at 1 point) and fail the seven that need real-time visual/auditory
perception (reaction time, inspection time, etc.).
CORRECTION to my earlier framing: "no clean public benchmark" overstated it —
the construct is well-defined and measurable; what does not exist is a
public leaderboard, hence no third-party TREND data. Two consequences:
(1) S is really a modality-coverage axis, not a cognition-speed axis — it
will move when low-latency streaming voice/video systems get scored against
the reaction-time subtests, not because models "think faster";
(2) my flat EOY projection (30, range 25–40) is therefore conservative-
but-fragile: a scored real-time multimodal system could jump several
sub-abilities at once. Noted in the projection's risk register here rather
than changing the CSV — the forecast stands as made, dated 14:49.
