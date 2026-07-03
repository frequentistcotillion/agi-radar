# AGI Radar

![AGI Radar](radar.svg)

Three model eras — GPT-4 (2023), GPT-5 (2025), and the mid-2026 frontier —
plotted across Hendrycks et al.'s ten CHC cognitive domains, with reasoning
split into static vs dynamic. Radial scale: 100 = the "well-educated adult"
anchor. Below the anchor, scores measure sub-ability *coverage* against that
single reference point — not placement in the human percentile distribution
(the data to do percentiles properly doesn't publicly exist; see recipe.md
Method 2). Above it, rings are ordinal, evidence-gated thresholds (GDM
performance levels, then collective levels — the latter drawn but not yet
reachable by any operationalized criterion). Axes ordered by mid-2026 value,
highest at 12 o'clock.

**The headline:** the capability profile is jagged. Mathematics and knowledge
have burst through the human anchor (Virtuoso / Expert rings) while dynamic
reasoning (~5/100, ARC-AGI-3 family) and long-term memory storage (~10/100)
stay pinned near the floor — three years of frontier progress with almost no
movement on either.

**Era 1–2 values are the published Hendrycks Table 1 scores. Era 3 is our
benchmark-mapped estimate, not a published score** — dated 2026-07-03,
adversarially reviewed, and offered for scrutiny.

## Audit it — don't trust it

Everything needed to verify this chart is in this repository:

- **[NOTEBOOK.md](NOTEBOOK.md)** — start here if you're human: the lab
  notebook. What the chart means, how each axis maps to an evaluation, how
  it was built, and its known weaknesses — in plain language.
- **[AUDIT.md](AUDIT.md)** — the third-party verification procedure (5 steps,
  ~10 minutes, needs only Python ≥3.11 stdlib). Includes a copy-paste prompt
  for auditing via your own AI agent.
- **[recipe.md](recipe.md)** — claim, inputs, data, method (every judgment
  call disclosed), and exact regeneration commands. Pinned artifact hash:
  `ae8479c87ffba30717c89038558770ce30a027f981cbaa73059004506d981246`.
- **[THREAD.md](THREAD.md)** — the complete append-only work log: sources
  verified at origin, an adversarial second-model review that moved four
  scores, two operator-caught errors and their on-the-record corrections.
- **[data/](data/)** — verified Table 1 extract, per-axis mid-2026 evidence
  with sources and dates, the plotting series, and a dated EOY-2026
  projection (scoreable against reality in January 2027).
- **[refs/](refs/)** — the three anchor papers (redistribution licenses in
  [refs/LICENSES.md](refs/LICENSES.md)), checksummed.
- **[code/radar.py](code/radar.py)** — ~150 lines of stdlib Python; the SVG
  is a pure, deterministic function of the data CSV.

This repository is the published mirror of a thread in a private analytical
workspace; its git history is the incremental provenance record (subtree
split of the original thread commits, verbatim).

---
*Workshop-internal notes: THREAD.md protocol lives in the private repo's
AGENTS.md; pandoc exports go to `exports/` (untracked).*
