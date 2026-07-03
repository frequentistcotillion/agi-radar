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
