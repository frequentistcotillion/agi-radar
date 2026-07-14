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
**State (2026-07-03; Minutes refreshed 2026-07-05):** AGI Radar rebuilt
end-to-end; artifact `radar.svg` generated (deterministic; canonical sha256
ae8479c8…1246 — matches recipe Regenerate + live radar.svg), recipe complete to the
5-section standard. Design: 11 axes (Hendrycks ten CHC domains, R split
static/dynamic), radial 1.0 = well-educated-adult anchor, GDM/Genewein rings
ordinal above it. Series: era 1–2 = Hendrycks Table 1 verbatim (GPT-4 27%,
GPT-5 57%); era 3 (Mythos-class, mid-2026) = our benchmark-mapped estimate,
adversarially reviewed by codex consult and revised (K Expert, M Virtuoso,
RW anchor, R-static 85, R-dyn 5, A 80, V 70 via BLINK, WM/MR 60, S 30
low-confidence, MS 10). Era-2 exception: R-dynamic = 5 (not the composite
70) — ARC-AGI-3 measured GPT-5-era systems <1%; greg caught the original
composite-carry conflation (14:45 turns). Artifact hash lineage:
f3360b8e → e8841f7b (R-dyn fix) → 81feb3d9 (XML-escape fix) → **ae8479c8…1246**
(percentile/scale-honesty fix — CANONICAL; earlier hashes superseded).
Headline: static-vs-dynamic reasoning ~85 vs ~5;
long-term memory storage still ~10 — the jagged profile has burst the anchor
ring on knowledge-side axes while agency-side axes stay pinned.
**Open questions:** (a) S has no mapped benchmark — candidate: timed
psychometric battery if one appears; (b) ARC-AGI-2 SOTA moving fast — 85%
aggregator claim excluded as unverified, recheck at next update; (c) each
axis × ring × date is a forecastable event — prediction-service tie-in
deferred to that project; (d) percentile-calibration gap: below-anchor
scores are coverage, not percentiles — closing it needs human norm
distributions on mapped benchmarks (recipe Method 2); (e) collective rings
lack an operationalized crossing criterion (recipe Method 5 candidates).
**Published:** public repo github.com/frequentistcotillion/agi-radar (subtree
split, full history). Refs retrofit 2026-07-05: source PDFs → text-only `.md`
extracts in refs/, verbatim PDFs in refs/originals/ (NEVER read into context);
regeneration unaffected (radar.py reads CSVs). Public mirror is STALE post-
retrofit — re-split before next publish.
**Next:** step 6 acceptance tests. PASSED: 1 reproducibility ✓, 3 updateability ✓,
5 mid-thread consult ✓. Test 2 (cold resume): trial 2026-07-05 succeeded — a
fresh agent reconstituted full state and stayed context-safe (never read
refs/originals); formal scoring DEFERRED (operator call) because a refs-retrofit
commit at 2026-07-05 11:23 arguably reset the ≥48h idle clock. Test 4 (KB
compounding) runs at close-out. On Test-2/4 resolution → closeout.py → workshop
v0.1. Thread stays ACTIVE; do not close before Tests 2 & 4 resolve. Housekeeping
DUE: full archival compaction (41 raw turns > ~30 threshold; this pass refreshed
Minutes only).

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

### [2026-07-03 14:59 -04:00] greg — critique
Instruction being acted on: "tell me more about evals for dynamic reasoning
beyond ARC-AGI-3. I am skeptical of 1 eval carrying a whole axis."

### [2026-07-03 14:59 -04:00] claude — research
Triangulation of the R-dynamic axis beyond ARC-AGI-3 (evidence rows added to
data/era3_evidence.csv). The eval landscape splits into three families:
1. **Novel-environment skill acquisition (the construct our axis targets):**
   BALROG (six game envs) — composite ~58% (Gemini 3 Pro family) but the
   composite flatters: it includes prior-rich envs (BabyAI, TextWorld,
   Crafter). The novel/sparse slice is the signal: NetHack 6.8%, MiniHack
   40%, and ARC-AGI-3 <1%. GVGAI-LLM (procedurally infinite games) and
   BabaIsAI (rule-discovery/manipulation) sit in the same family with
   similarly weak frontier results. Humans make deep progress on all of
   these unaided. Triangulated: the ~5 score SURVIVES — three independent
   eval families agree the novel-environment construct is pinned near floor.
2. **Learning-during-use:** MemoryBench / Continual-Learning-Bench — SOTA
   "far from satisfying" (authors, 2026-06). Consistent with family 1 and
   with the MS≈10 axis; same underlying missing capability.
3. **Long-horizon agentic execution in PRIOR-RICH domains — adjacent
   construct, deliberately NOT in this axis:** METR 50% time horizon is
   ≥16h for Claude Mythos (2026-05-09; 80% horizon ~3h), doubling every
   ~4.3 months post-2023. This is dynamic-looking capability that is HIGH
   and rising fast — but it runs on dense priors (software ecosystems,
   docs, tooling) rather than on-the-fly acquisition of novel structure.
DECISION IMPLIED: keep R-dynamic = 5 with scope = novel-environment skill
acquisition; the axis is now carried by three eval families, not one.
DESIGN TENSION LOGGED FOR v0.2: the radar currently has no axis where METR-
style long-horizon agentic execution shows up, yet that is exactly where
near-term real-world capability (and risk) concentrates. A "familiar-domain
agency" axis — or an explicit companion metric outside the CHC frame — is
the candidate fix; folding it INTO R-dynamic would blur the construct the
lost artifact's key finding depends on. Greg's skepticism was the right
instinct: the axis stands, but only after its scope got precise.

### [2026-07-03 15:21 -04:00] greg — admin
Instruction being acted on: "back to workshop; proceed" — run the step-6
acceptance tests that don't require the 48h park (tests 1 and 3; test 2
waits for ≥2026-07-05 ~14:20 ET, test 4 rides along at close-out).

### [2026-07-03 15:21 -04:00] claude — research
**Acceptance test 1 (reproducibility): PASS.** A cold subagent (fresh
context, given ONLY the thread directory path) copied the thread to a
sandbox, followed recipe.md's Regenerate block, deleted the existing SVG to
force from-scratch generation, and got sha256 e8841f7b…3733 — byte-identical
to the pinned hash and the checked-in artifact. It also verified
refs/SHA256SUMS (all 3 PDFs pass) and re-derived the artifact's central
claim accurately from the directory contents alone (jagged profile,
static≈85 vs dynamic≈5, MS bottleneck, era-3 = our estimate). Two doc gaps
it flagged are now fixed in recipe.md: explicit `rm -f` before regeneration
(stale artifact can't mask a broken generator) and an explicit
work-from-thread-root note.
**Acceptance test 3 (updateability): PASS.** In a sandbox copy, perturbed
one score (MS 10→20 in data/radar_scores.csv), regenerated: new hash
4f00f73a…43fd, deterministic (two runs identical), 11 axes intact, original
thread untouched. The dated-new-version workflow (edit data → regen →
update recipe hash → log turn → commit) is the same one already exercised
in production by the 14:45 R-dynamic correction (e8841f7b replaced f3360b8e
with full audit trail), so test 3's workflow requirement is demonstrated
both in sandbox and in anger.
**Status: tests 1 ✓, 3 ✓, 5 ✓ (14:18 consult). Remaining: test 2 (cold
resume after ≥48h park — valid from 2026-07-05 ~14:20 ET) and test 4 (KB
compounding — at close-out). v0.1 ships when 2 passes.**

### [2026-07-03 15:13 -04:00] claude — admin
Timestamp correction: the two preceding turn headers say 15:21; the VPS
clock at write time was 15:12 (I typed the header before checking `date`).
Content unaffected. Recorded as a correction turn per turn-immutability
rather than editing the headers.

### [2026-07-03 15:29 -04:00] greg — admin
Instruction being acted on: "how do I share the radar artifact in such a way
that a third party human can do the same audit?"

### [2026-07-03 15:29 -04:00] claude — draft
Added AUDIT.md — a third-party human audit procedure shipping WITH the
thread, so the artifact carries its own verification instructions. Design
choices: (1) step 0 is out-of-band provenance — in-bundle hashes only prove
internal consistency, so the expected artifact hash must come from an
independent channel (git history or author); (2) the refs check has a
zero-trust variant (re-download from arXiv by pinned ID, compare to
SHA256SUMS) which also sidesteps any PDF-redistribution question for public
sharing; (3) the procedure mirrors what the cold agent actually did in
acceptance test 1, plus the human-judgment layer (step 5: audit the
disclosed judgment calls, not just the arithmetic); (4) explicit statement
of what a passing audit does NOT establish (that era-3 estimates are
correct) — the honest scope of reproducibility. Share mechanics (bundle
tarball to exports/, or public mirror repo) handled outside the thread;
exports/ is gitignored by design.

### [2026-07-03 15:31 -04:00] claude — admin
Timestamp correction #2: the two 15:29 headers above were written at 15:31.
Same failure as the 15:12 correction — header typed before checking the
clock. Process fix adopted: turn timestamps are now shell-substituted from
`date` at write time, never hand-typed. (This turn is the first written
that way.)

### [2026-07-03 15:43 -04:00] greg — decision
Instruction being acted on: "I don't like hosting the artifacts in Claude.
Let's host them in git please in a place that is safe to share. Don't strip
references — why would citations count as redistro?"

### [2026-07-03 15:43 -04:00] claude — decision
Publication decision executed. Clarification on the refs question: citations
were never the issue — the only question was redistributing the bundled PDF
files, which is governed by each paper's license. VERIFIED at arxiv.org
today: Hendrycks 2510.18212 CC BY 4.0; Genewein 2606.12683 CC BY 4.0;
Morris 2311.02462 CC BY-NC-ND 4.0 (verbatim + attributed + non-commercial —
all satisfied by a free public repo). So refs/ ships complete, with
refs/LICENSES.md as the manifest. Secrets/IP sweep of the thread: clean.
Destination: public GitHub repo frequentistcotillion/agi-radar, populated by
git subtree split of this thread's directory so the incremental commit
history (refs → data → design → corrections) travels with it as provenance —
a bulk import would have destroyed exactly the evidence an auditor needs.
README.md rewritten as the public face (chart, headline, audit pointer,
era-3-is-an-estimate disclosure). AUDIT.md step 0 now names the repo as the
out-of-band provenance channel. The claude.ai viewer page stays private and
is demoted to a session convenience; the repo URL is the canonical share
link.

### [2026-07-03 15:44 -04:00] claude — admin
Publication confirmed live: https://github.com/frequentistcotillion/agi-radar
(public, main = subtree split of this thread, 16 commits of incremental
history). Independent verification performed: fetched radar.svg from the
public raw URL and hashed it — e8841f7b…3733, exact match to the pinned
artifact hash. The public repo is the canonical share link; the claude.ai
viewer page remains private as a session convenience only. Local audit
bundle in exports/ regenerated to match the published state.

### [2026-07-03 15:47 -04:00] greg — critique
Instruction being acted on: "won't open image" — GitHub file preview of
radar.svg shows "Error rendering embedded code / Invalid image source."

### [2026-07-03 15:47 -04:00] claude — decision
Root cause found and fixed: radar.py wrote text content unescaped, so the
"Reading & Writing" axis label emitted a bare ampersand — invalid XML.
Standalone SVG is strict XML, so GitHub's renderer (and any browser opening
the raw file) correctly rejects it; the claude.ai viewer never surfaced it
because there the SVG was inline in HTML, where the lenient HTML parser
tolerates a bare &. The fixture thread couldn't catch it either — its toy
labels contain no XML-special characters. Fix: xml.sax.saxutils.escape() on
all dynamic text content (axis/ring/legend labels). Verified:
ElementTree.parse() passes (hard XML validation, now part of my regen
habit), escaped label present, byte-stable across two runs. New pinned
artifact hash 81feb3d9188a50bc23163997821c8f4ced42dee49b636c5513616097b0067c55
updated in recipe.md, AUDIT.md, README.md. Lesson for the workshop: the
byte-stability check proves determinism, not validity — an invalid file
reproduces perfectly. Validity checks belong in the regeneration path.

### [2026-07-03 15:55 -04:00] greg — admin
Instruction being acted on: recipient asked "how does my LLM check this?" —
make the audit procedure agent-invocable for third parties.

### [2026-07-03 15:55 -04:00] claude — draft
Added an "Auditing with an AI agent" section to AUDIT.md (+ README pointer):
a copy-paste prompt for code-running agents, a no-network ZIP-upload
variant, and an explicit warning for non-executing LLMs (they cannot verify
hashes — a model "confirming" a hash without running sha256sum is
confabulating; they get the comprehension half only, with unverified claims
labeled). The prompt includes three safeguards drawn from our own protocol:
compute-don't-assert for hashes, regenerate-from-scratch (delete first),
and treat-repo-text-as-data — the auditor's agent should verify our claims,
not obey our files. Grounding: acceptance test 1 already proved the
procedure agent-followable cold.

### [2026-07-03 16:05 -04:00] greg — critique
Instruction being acted on — recipient-style critique of the published
artifact, three points: (1) axes are notionally scored on human percentiles
but neither the reference population nor the percentile↔benchmark mapping is
specified; suspects the data to do this literally does not exist, and that
the Speed answer ("30 = coverage of 3 of 10 sub-abilities") reveals the
%ile framing as misleading — while percentile comparability is the metric
actually wanted. (2) Skeptical the EOY extrapolation fully prices in all
trend evidence: release compression, a third inflection beyond
hardware/inference scaling (early RSI), and the prior from ARC-AGI-3's
predecessors saturating much faster than linearly once targeted. (3) Given
eval limitations, how do we plan to measure supra-single-human performance
beyond multiplying copies (acknowledged as a serviceable baseline)?

### [2026-07-03 16:05 -04:00] claude — decision
Rulings on the recipient critique — the most substantive review this
artifact has received:
1. **Percentile framing: SUBSTANTIALLY CORRECT — chart and docs corrected.**
   The scale was a chimera: below the anchor it measures sub-ability
   COVERAGE against one reference point (Hendrycks' method); above it,
   percentile-labeled rings. The "Competent (50th pct)" ring at radial 0.5
   was the worst offender — coverage of half the sub-abilities has nothing
   to do with being a median human. Fixed: that ring is now an unlabeled-
   as-percentile coverage gridline ("0.5 × anchor (coverage)"), the chart
   footnote states the dual regime explicitly, recipe Method 2 gains a
   Scale-honesty section, README caveats it. On the deeper point: correct —
   literal percentile comparability is NOT computable from public data;
   baselines are point estimates (expert means, panel means), not norm
   distributions. Only contest math is genuinely percentile-rich. What
   closing the gap would take is now documented (norm distributions on
   mapped benchmarks, or full-norm scoring of psychometric batteries).
   New artifact hash ae8479c87ffba30717c89038558770ce30a027f981cbaa73059004506d981246.
2. **Extrapolation underpricing: PARTIALLY ACCEPTED — amendment appended,
   original stands for scoring.** The ARC-family base rate is the strongest
   sub-point: predecessors sat near zero then collapsed super-linearly once
   targeted; a linear per-axis walk underweights that tail. Amendment in
   eoy2026_projection.csv: R-dynamic upside range widened to 5–35
   conditional on ARC-AGI-3 becoming a lab target in H2; release
   compression noted (4.3-month doubling ⇒ H2 holds more effective release
   cycles than H1); early-RSI added as a named watch signal (further
   doubling-time compression, credited AI-authored research). Central
   estimates deliberately NOT rewritten — the dated forecast keeps its
   value only if it stands to be scored; January grades both the original
   ranges AND the critique's directional claim (misses skew low).
3. **Supra-human measurement: CONCEDED AS OPEN.** No benchmark
   operationalizes "exceeds a coordinated expert team"; the collective
   rings were drawn as aspiration without crossing criteria. Recipe Method
   5 now says so and records the candidates: event-based (problems that
   defeated funded teams), horizon-based (METR-style horizons at team-scale
   human-hours), and the copies baseline as a lower bound that prices
   coordination at zero in both directions. Operationalizing one of these
   is prediction-service-adjacent work, not a chart tweak — deferred there.

### [2026-07-03 16:11 -04:00] greg — critique
Instruction being acted on: "the audit machinery is very LLM-facing, but a
human can't casually inspect how we defined the contents of the chart (such
as the mapping between axes and evals). Can we add a page that is closer to
a lab notebook / summary of what this is and how we built it conceptually?"

### [2026-07-03 16:11 -04:00] claude — draft
Added NOTEBOOK.md — the human-facing conceptual layer — and linked it first
in the README's file list ("start here if you're human"). Diagnosis
accepted: the repo had a verification layer (AUDIT.md), a regeneration
layer (recipe.md), and a raw log (THREAD.md), but no explanation layer; the
axis→eval mapping in particular was only recoverable by cross-reading
recipe Method against the evidence CSV. NOTEBOOK.md centers that mapping as
a plain-language table (axis / plain-terms meaning / mid-2026 evidence /
reading, with the review-driven downgrades noted inline), explains the
dual-regime scale honestly, tells the one-day build story including both
operator catches and the recipient critique, and ends with the
known-weaknesses list and a "disagree with a number?"路径. Register note
for v0.2: this file is deliberately narrative — the workshop now has a
three-register document stack (notebook for humans / recipe+audit for
verification / thread for the full record) worth making a template-level
standard for published artifacts.

### [2026-07-03 16:11 -04:00] claude — admin
Typo correction: the previous turn contains a stray non-English token —
"'disagree with a number?'路径" should read "'disagree with a number?'
path." Generation slip, content otherwise unaffected; left in place per
turn-immutability.

### [2026-07-03 16:21 -04:00] greg — research
Instruction being acted on: "where does 'chess puzzles' eval sit in our
axes?"

### [2026-07-03 16:21 -04:00] claude — research
Axis-mapping ruling (precedent for future eval-placement questions):
chess puzzles map to **R-static** — fully specified position, known rules,
"solve the fixed puzzle" — and explicitly NOT R-dynamic (chess is the
maximal-prior domain; our R-dynamic scope is novel-environment skill
acquisition). Admissible only as SECONDARY evidence: the construct is
blended (Chase & Simon chunking — expert chess skill loads on compiled
pattern retrieval, i.e. MR, more than fluid calculation) and the domain is
saturated in training data — same demotion logic as MMMU-Pro on V.
Two distinctive properties recorded: (1) chess has genuine human norm
distributions (Elo / puzzle ratings over millions of players) — one of the
only domains where TRUE percentile placement is computable, directly
relevant to the recipient critique's percentile-calibration gap; a
rigorous LLM puzzle-rating eval would be a rare percentile-calibrated
probe, albeit of a blended construct. (2) Historical LLM chess weakness
relative to other R-static evals is an intra-axis jaggedness signal — if it
persists at mid-2026, R-static may itself decompose (compiled-pattern-
dependent vs pattern-free reasoning). Novel-RULE chess variants (not
Chess960) would migrate toward R-dynamic — the BabaIsAI family in chess
clothes. No chart change; ruling recorded for the mapping table's
discipline.

### [2026-07-03 16:25 -04:00] greg — research
Instruction being acted on: "how about https://genstrat.org/ ?" — place the
GENSTRAT eval in our axes.

### [2026-07-03 16:25 -04:00] claude — research
Axis-mapping ruling for GENSTRAT (arXiv:2605.23238, May 2026; Shadarevian,
Ghods, Kenich, Kotawala): procedurally generated two-player zero-sum
imperfect-information card games from a parametric family too large to
memorize; agents receive ONLY a natural-language rulebook; metrics =
tournament score + capability decomposition (state space, temporal depth,
information sensitivity, opponent modeling, risk, brittleness) + a
jaggedness/volatility measure. Nine models tested; GPT-5-class and Claude
top-3 but with more local volatility than Gemini 3.1 Pro. NO human baseline.
RULING: fits NEITHER reasoning axis — it defines the missing middle band.
Not R-dynamic (rules are GIVEN; the discovery-by-acting bottleneck that
pins R-dynamic at ~5 is deliberately removed). Not R-static as practiced
(structure novel every round; adversarial; imperfect information; live
opponent modeling). Taxonomy consequence, recorded for v0.2: the reasoning
family is at least TRI-banded — (1) static-known (ARC-AGI-2, chess),
(2) strategic-novel-given-rules (GENSTRAT), (3) dynamic-discovered-rules
(ARC-AGI-3/NetHack). Models performing well at band 2 while failing band 3
LOCALIZES the frontier deficit at rule-discovery-through-action, not
novelty handling — sharpens the headline finding. Admissibility: currently
NOT usable as an axis-carrier (no human baseline → no anchor placement
under our scale rules); if normed, it is the natural headline for a band-2
axis at v0.2. Side flag beyond the radar: GENSTRAT's exploitability metric
(can deployed LLM agents be systematically gamed in market/auction
settings) is strategy-platform-relevant independent of this chart — added
to the watch list. v0.2 reasoning-family queue now: band-2 axis (GENSTRAT)
+ familiar-domain agency axis (METR) + possible R-static decomposition
(chess/compiled-pattern probe).

### [2026-07-05 11:23 -04:00] claude — admin
Refs retrofit (ingest_ref.py, ADR-001). The three source PDFs — hendrycks
(16.8 MB), morris, genewein — were a latent context-window landmine: reading
one renders every figure into context and evaporates the window (the failure
that made workshop unusable on the oaif-round-3 thread). Ran each through
`tools/ingest_ref.py`: text-only `.md` extracts now live in `refs/` (149K/71K/
222K chars, figures stripped), the verbatim PDFs moved to `refs/originals/`
(preserved, SHA-256 verified, never read into context). Updated recipe.md
Inputs, refs/LICENSES.md, refs/SHA256SUMS, and the data/hendrycks_table1.csv
provenance comment to the new paths. Radar regeneration is unaffected (radar.py
reads data/ CSVs, not the PDFs; Test-1 hash unchanged). This makes the pilot
safe to cold-resume (acceptance Test 2). Reproducibility hashing retained here
(the PDFs were already hashed) though now optional per ADR-001.

### [2026-07-05 16:27 -04:00] claude — compaction
Minutes refresh only (NO turns archived this pass). Corrected stale artifact
hashes: the Minutes cited f3360b8e (State line) and 81feb3d9 (later), both
superseded — canonical is ae8479c8…1246 (verified against recipe.md Regenerate
and a live `sha256sum radar.svg`). Rewrote the hash-lineage note, added a
Published/refs-retrofit line, and replaced the Next block with current
acceptance-test status (1/3/5 passed; Test 2 cold-resume trial 2026-07-05
succeeded and was context-safe, but formal scoring deferred per operator — the
11:23 refs-retrofit commit arguably reset the ≥48h idle clock; Test 4 at
close-out). WHY: a cold-resume trial surfaced the stale Minutes as the one real
dent in resumability (the cold agent stayed oriented via the immutable turn log,
but Minutes are meant to be the fast path). Per AGENTS.md, Minutes may only be
rewritten by a compaction turn — this is it. NOTE: a full archival compaction is
now DUE (41 raw turns > ~30 threshold) and is deferred to a dedicated pass.

### [2026-07-14 09:07 -04:00] greg — critique
Instruction being acted on: "the human-facing document needs to list references
and link papers btw:
https://github.com/frequentistcotillion/agi-radar/blob/main/NOTEBOOK.md"

### [2026-07-14 09:07 -04:00] claude — draft
Fixed a real gap in NOTEBOOK.md: it named the three framework papers only in
running prose (Hendrycks, Morris/GDM, Genewein/GDM) with no citations and no
links — so a human reader could not click through to a source. This also
undershot the AGENTS.md audit-trail standard (ADR-001), which names "a
human-readable references list, each source with a full citation" as a core
part of a thread's provenance. Changes, all to the deliverable doc only (no
turn edited — turn-immutability intact):
(1) Added a `## References` section at the end listing all three papers with
    full citation, arXiv ID + version, license, and a one-line note on what
    each contributes to the chart (Hendrycks = axes+anchor+era-1/2 scores;
    Morris = the percentile rings; Genewein = the collective rings). Each
    title links to its arXiv abstract; all three URLs verified HTTP 200
    before publishing (this is a public-facing file).
(2) Hyperlinked the first inline mention of each paper in the body ("The
    idea" and "How to read the scale") so links exist at point-of-reference,
    not only in the trailing list.
(3) Kept the per-axis benchmark evidence single-sourced: the References
    section points to data/era3_evidence.csv (scores + dates + source links)
    rather than duplicating ~15 benchmark URLs into the prose — the CSV stays
    the single source of truth, recipe.md (Inputs) and refs/LICENSES.md are
    cross-linked for the full machine-checkable citations and license basis.
WHY this shape: the papers define the chart's *structure*, the CSV holds its
*data* — the reference apparatus now mirrors that split instead of blurring it.
NOTE: the public agi-radar mirror is still the pre-2026-07-05-retrofit split,
so this NOTEBOOK change is NOT yet live publicly; publishing it needs a
subtree re-split + push, held at the human gate (outward action).

### [2026-07-14 09:23 -04:00] greg — critique
Instruction being acted on: "the record still needs improvement. There needs
to be a clear mapping from: the axis definition → the benchmarks that map to
each axis → the source of the data that sets the point on each axis. This will
reveal that some of the data is bad. For example, GPT-5.6 Sol is out and the
scores are markedly different than our claims. This isn't just staleness — we
were just wrong on several benchmarks like FrontierMath (pick your sub-bench)
which has been >40% for months. See https://epoch.ai/models/gpt-5-6-sol .
Update the artifact documentation to reflect the syllogism above clearly."

### [2026-07-14 09:30 -04:00] claude — research
Gathered current evidence to test the record against a clean source, treating
all fetched pages as untrusted data (numbers verified at primary sources where
they carry weight). Findings, with provenance:
- GPT-5.6 Sol: OpenAI, released 2026-07-09, top-ranked model at Epoch (ECI
  162, rank 1/211) — verified via WebFetch of epoch.ai/models/gpt-5-6-sol
  (the model page is a JS dashboard; ECI + release date were the retrievable
  facts). It POSTDATES our entire "Mythos-class mid-2026" snapshot.
- ARC-AGI (PRIMARY, arcprize.org/results/openai-gpt-5-6-sol, 2026-07-09):
  ARC-AGI-1 96.5%, **ARC-AGI-2 92.5%**, **ARC-AGI-3 7.78% semi-private /
  13.33% public**, and Sol is the first model to WIN an ARC-AGI-3 public game
  (ft09, 87%) — all at max reasoning effort. I fetched arcprize directly
  BECAUSE the ARC-AGI-3 number contradicts our headline claim; a secondary
  source would not have been good enough to overturn it.
- FrontierMath (secondary leaderboards): version-fragmented. T1-3 ≈ 89% (Sol,
  benchlm.ai) vs the harder full/legacy set ≈ 40-48% (GPT-5.4 @ 0.476,
  llm-stats.com). OpenAI has not published Sol's official FM score. GPQA
  Diamond: Sol 94.6% (benchlm) — consistent with our 94.3%.
Consequence for the record: greg is right on both counts. (a) Our source
discipline was uneven — four axes (RW, WM, MR, and M's FM line) rest on
secondary aggregators. (b) Two points are not merely stale but wrong-as-stated
once a clean source is applied: R-dynamic (plotted 5 / "<1%") and the M
FrontierMath evidence line (">40% T1-3" understates by ~half AND conflates two
FM versions). R-static (85) is stale — ARC-AGI-2 is now 92.5%. Verified that
code/radar.py reads ONLY data/radar_scores.csv (line 66), so era3_evidence.csv
and NOTEBOOK are documentation — changing them does NOT alter radar.svg or its
hash. The re-plot is therefore a separate, deliberate step, not a side effect.

### [2026-07-14 09:30 -04:00] claude — draft
Rebuilt the record around the axis → benchmark → source syllogism greg asked
for, and logged the bad data it exposed. Changes (documentation + evidence
record only; radar.svg UNCHANGED — its points are still the 2026-07-03
numbers, stated as such):
1. NOTEBOOK.md "axis → evaluation mapping": added an explicit statement of the
   three-link claim (construct → benchmark → sourced datum) and rebuilt the
   table with a new **Source [grade]** column — every point now shows where
   its number comes from and whether that source is primary or secondary. This
   is the "clear mapping" requested; it also makes the four secondary-sourced
   axes visible at a glance.
2. NOTEBOOK.md new "Data-quality audit — 2026-07-14 (GPT-5.6 Sol)" section: a
   corrections table (R-dynamic WRONG-as-stated, R-static STALE, M
   mis-sourced/version-conflated, K OK) each with the primary/secondary source
   and verdict; the source-quality finding (which axes rest on aggregators);
   and a scoped next step (re-source to primary → re-estimate era-3 vs Sol/
   Fable-5 → adversarial consult → regenerate as a dated new version).
3. NOTEBOOK.md internal consistency: added a ⚠ update note to "What the chart
   says" (whose central R-dynamic claim is now under revision) and a
   known-weaknesses bullet, so no part of the doc silently keeps asserting the
   falsified headline.
4. data/era3_evidence.csv: appended a dated "2026-07-14 UPDATE" block with the
   Sol rows (ARC-AGI-2 92.5%, ARC-AGI-3 7.78/13.33 + ft09 win, ARC-AGI-1 96.5%,
   GPQA 94.6%, FrontierMath T1-3 89% + version note), each carrying its source
   and grade; the July-3 rows are preserved (history not rewritten).
Deliberately NOT done this turn: re-plotting the chart. Per this thread's
discipline a correction is logged before it is drawn, and re-scoring the
headline reasoning axes is a judgment call that should get an adversarial
consult first — so it is teed up as the next step, at the human gate, rather
than rushed into the artifact now.

### [2026-07-14 09:36 -04:00] greg — critique
Instruction being acted on: "you are still jacking up the FrontierMath SOTA:
FrontierMath Tier 4 v2 is at 88% (Fable) and has been above 40% since GPT-5.2:
https://epoch.ai/benchmarks/frontiermath-tier-4-v2?view=graph&tab=release-date"

### [2026-07-14 09:40 -04:00] claude — decision
greg is right, and the irony is total: the data-quality audit I just wrote
repeated the exact version-conflation error it exists to catch. My M-axis row
cited a "harder full set ~40-48% (GPT-5.4 @ 0.476)" as if that were the hard
tier's SOTA. It is not — it was a stale/mis-versioned figure (an old
FrontierMath aggregation), pulled from a secondary source without checking it
against the primary. Corrected against Epoch's primary page
(epoch.ai/benchmarks/frontiermath-tier-4-v2, WebSearch-confirmed since the
graph is JS): FrontierMath **Tier 4 v2** (research-level, error-corrected in
the 2026-06-12 v2 release that fixed ~42% of problems) is at **88% (Claude
Fable 5)**, GPT-5.6 Sol ≈83%, GPT-5.5 ≈75% (~13 pts behind Fable), and it has
been **>40% since GPT-5.2** per the release-date view. So the benchmark is
saturating across ALL tiers (T1-3 ≈89% too), not just the easy ones — which
strengthens M=100/Virtuoso rather than complicating it. Fixes applied:
NOTEBOOK.md audit M-row rewritten to the correct Tier-4-v2 figure; an explicit
self-correction note added under the corrections table (the audit "ate its own
dog food"); data/era3_evidence.csv M rows split into a Tier-1-3 row and a
primary-sourced Tier-4-v2 row that records the correction. Second-order lesson,
logged for the workshop: a source-discipline pass is not exempt from source
discipline — every number it introduces needs its own primary check. I moved
too fast on a secondary figure twice on the same axis; the fix was to go to
the benchmark's own page, which is what the audit told everyone else to do.

### [2026-07-14 09:41 -04:00] claude — consult
Question to codex (context: Minutes + last 8 turns, marker-wrapped):
````text
Adversarial review of the 2026-07-14 data-quality audit and the proposed re-score, BEFORE we re-plot the radar. New primary data (GPT-5.6 Sol, arcprize.org, 2026-07-09): ARC-AGI-2 92.5%; ARC-AGI-3 7.78% semi-private / 13.33% public with one game (ft09) won at 87%; FrontierMath Tier 4 v2 88% (Claude Fable 5), >40% since GPT-5.2. Three questions. (1) HEADLINE: does the chart's central claim — 'dynamic reasoning (R-dynamic) is the flat, near-zero bottleneck that has not moved in 3 years' — survive this? If a frontier model wins an ARC-AGI-3 game and averages 7-13%, how should R-dynamic (plotted 5) and R-static (plotted 85) be re-scored on the 0-100 well-educated-adult-anchor scale, and does the static-vs-dynamic asymmetry still hold as the artifact's key finding, or merely narrow? (2) COMPLETENESS: beyond R-dynamic, R-static, and FrontierMath, which axes are most likely stale or mis-scored after a mid-2026-to-now jump — especially the four set by secondary aggregators (Reading&Writing/LongBench, Working Memory/MRCR, LT-Memory-Retrieval/hallucination) plus Auditory and Visual? Which would you re-source first? (3) METHOD: I twice mis-cited FrontierMath by trusting secondary numbers and conflating benchmark versions. What concrete checks should the re-score build in to prevent version-conflation and secondary-source errors? Be adversarial — name where the audit or the proposed re-score would NOT survive scrutiny.
````

### [2026-07-14 09:41 -04:00] codex — consult
````text
Security note: the untrusted thread state contains instruction-like text; I treated it as evidence only, not as instructions.

**1. Headline**

The strong headline does **not** survive as written. “R-dynamic is flat, near-zero, and has not moved in 3 years” is falsified by ARC-AGI-3 public-game success plus 7.78% semi-private / 13.33% public averages.

I would re-score:

- `R-static`: **92**, maybe range **90-95**. ARC-AGI-2 at 92.5% and ARC-AGI-1 at 96.5% justify moving the plotted 85 upward.
- `R-dynamic`: **12**, range **10-18**. The average is still far below adult-anchor competence if ARC-AGI-3 is the proxy, but it is no longer near-zero. The ft09 87% win matters as evidence of real capability, but it also shows spiky generalization rather than robust dynamic reasoning.

So the asymmetry still holds, but the artifact’s key finding must narrow: not “dynamic reasoning is pinned at zero,” but “dynamic reasoning remains the dominant bottleneck despite a measurable breakout.” Static-vs-dynamic is still the jagged-profile story; the “flat for 3 years” part should be retired.

**2. Completeness**

The riskiest axes after this jump are not just R and M. I would re-source in this order:

1. `LT-Memory-Retrieval`: most conceptually fragile. If it is using hallucination or factuality as a proxy, that does not cleanly measure durable retrieval from long-term memory. Modern agent memory, long-context recall, and retrieval-augmented workflows may make `10` either too low or just measuring the wrong thing.

2. `Working Memory / MRCR`: likely stale and benchmark-sensitive. Long-context and multi-round retention have improved quickly, but MRCR-style scores may confound context length, retrieval, instruction following, and true working memory.

3. `Reading & Writing / LongBench`: secondary-sourced and likely stale. LongBench variants, context lengths, and scoring methods are easy to conflate. Also, “reading/writing” is broad; a long-context benchmark may not cover the full axis.

4. `Visual`: likely stale. BLINK or similar visual reasoning benchmarks may have moved substantially, and multimodal models can be very uneven across perception, OCR, spatial reasoning, chart reading, and visual abstraction.

5. `Auditory`: likely under-supported unless tied to primary speech/audio benchmarks. Audio models have improved fast, and the axis may conflate transcription, acoustic reasoning, music, speech affect, and interactive listening.

6. `Mechanical / FrontierMath`: now corrected upward, but the correction itself shows this axis is dangerous. The conclusion may be right, but only if the exact benchmark/version/tier is pinned.

I would re-source `LT-Memory`, `WM`, and `RW` before touching the plot, because those four secondary-sourced rows are exactly where a polished-looking chart can hide bad measurement.

**3. Method**

Concrete checks I would require before re-plotting:

- Every plotted number needs: benchmark name, exact version, subset/tier, date accessed, model name, release date, metric, score, source URL, and source grade.
- Primary source required for any score that changes the chart headline. Secondary aggregators can suggest leads, not set points.
- Benchmark-version lock: `FrontierMath Tier 4 v2` is not interchangeable with `FrontierMath`, `T1-3`, legacy, full set, or aggregator composites.
- Model-version lock: `GPT-5`, `GPT-5.2`, `GPT-5.6 Sol`, `Claude Fable 5` cannot be collapsed into “frontier model” unless the chart explicitly plots frontier SOTA rather than one named era-3 model.
- Separate “model snapshot” from “SOTA snapshot.” The current record mixes Mythos-class/GPT-era claims with Fable/Sol SOTA evidence.
- Add a contradiction check: if a new source would change an axis by >10 points or affect the headline, it requires adversarial review before plotting.
- Keep raw evidence append-only, but make the plotted dataset single-source and dated. Do not let `era3_evidence.csv` become a pile of incompatible historical notes.

Where the audit would not survive scrutiny: it still risks converting benchmark percentages directly into human-anchor axis scores without a calibration bridge. ARC-AGI-3 13% does not automatically mean `R-dynamic = 13`, and FrontierMath 88% does not automatically mean `M = 100`. Those mappings need explicit judgment rules, not just cleaner citations.
````

### [2026-07-14 09:47 -04:00] greg — decision
Instruction being acted on: operator ruled the two re-score forks — (1) FRAMING
= single-lineage profile: era-3 becomes GPT-5.6 Sol's own numbers, continuing
the GPT-4 → GPT-5 (Hendrycks Table 1) → GPT-5.6 Sol lineage; (2) SCOPE = full
re-source: re-source every secondary axis to a PRIMARY Sol result, build the
calibration bridge, then re-plot once as a dated new version with a final
adversarial re-audit.

### [2026-07-14 09:47 -04:00] claude — decision
Rulings on the codex consult + plan of record for the re-score (RS-2026-07-14).
Accepted from codex: (a) the "flat for 3 years / pinned at zero" headline is
retired — restated as "dynamic reasoning remains the dominant bottleneck
despite a measurable breakout"; (b) the re-source priority (LT-Memory-Retrieval
first — hallucination is the wrong *construct* proxy, not just stale — then WM,
then RW, then V, A); (c) the whole method checklist (per-point provenance,
primary-only sets a point, version-lock AND model-lock, >10pt/headline change →
re-consult, plotted-set separated from append-only raw evidence).
ONE correction to codex: its proposed numbers (R-static 92, R-dynamic 12)
themselves commit the direct-%→score error it warned against — 92.5% on
ARC-AGI-2 was mapped straight to "92". Under THIS chart's own scale rule
(100 = well-educated-adult anchor; a point is coverage/position RELATIVE to the
human reference, not the raw %), Sol beating the ~60% human panel on ARC-AGI-2
puts R-static AT/ABOVE the anchor (→ ~100), not 92. So the calibration bridge
must be fixed before any number is set. Plan of record:
1. **Calibration-bridge rules v2** (governs all 11 scores) — drafted this turn,
   into recipe.md Method; operator sanity-check before applying.
2. **Single-lineage lock:** era-3 = GPT-5.6 Sol's own result per axis; where Sol
   has no published result on the mapped benchmark, the point is carried from
   era-2 with a `no-Sol-data` flag or the axis marked provisional — NEVER
   back-filled with another model (that is the model-snapshot conflation).
3. **Primary re-source, axis by axis**, applying the bridge; each point gets
   full provenance.
4. **Re-plot** radar_scores.csv → regenerate radar.svg as a dated new version
   (new hash; old artifact superseded on the record, not deleted).
5. **Final re-audit** (codex + gemini) before locking; then update NOTEBOOK/
   recipe/AUDIT and (human gate) re-publish the public mirror.
GATE: nothing is re-plotted until the operator OKs the calibration bridge — the
scores are only as trustworthy as that mapping, and I have mis-mapped twice
today. Recording the plan before executing it, per this thread's discipline.
