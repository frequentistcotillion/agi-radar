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
