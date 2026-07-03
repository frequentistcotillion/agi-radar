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
