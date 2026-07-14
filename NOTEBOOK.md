# Lab notebook — what this chart is and how we built it

*Written for human readers. The machine-checkable version of everything here
lives in [recipe.md](recipe.md) (how to rebuild it) and [AUDIT.md](AUDIT.md)
(how to verify it); the unabridged working log is [THREAD.md](THREAD.md).
This page is the conceptual summary.*

## The idea

"How smart is AI?" is a bad question because the honest answer is *jagged* —
wildly superhuman in some directions, below a child in others. This chart
makes the jaggedness visible. It takes the ten cognitive domains that
psychometrics uses to describe *human* general intelligence
(Cattell-Horn-Carroll theory, via Hendrycks et al.'s
[*A Definition of AGI*](https://arxiv.org/abs/2510.18212)),
and plots where frontier AI stood on each at three moments: GPT-4 (2023),
GPT-5 (2025), and the mid-2026 frontier.

One deviation from Hendrycks: we split his "On-the-Spot Reasoning" domain in
two — **static** reasoning (solve a fixed puzzle put in front of you) and
**dynamic** reasoning (dropped into an unfamiliar interactive environment,
figure out the rules by acting). We split it because the single most
important fact about current AI hides inside that average: static is near
human level; dynamic is close to zero, and has barely moved in three years.

## How to read the scale (honestly)

- **The solid ring = a "well-educated adult."** Hendrycks' anchor. A score
  of 100 means the model covers what that reference adult can do in the
  domain.
- **Below the ring, scores are *coverage*, not rank.** Speed = 30 means the
  model handles 3 of 10 speeded sub-abilities at adult level — it does NOT
  mean "30th-percentile human." We initially drew this ambiguously; a
  recipient's critique caught it and the chart now says what it means.
- **Above the ring, placements are claims, not measurements.** Expert
  (90th) and Virtuoso (99th) rings come from Google DeepMind's
  [*Levels of AGI*](https://arxiv.org/abs/2311.02462); the collective rings
  (research team, enterprise) from their 2026
  [*From AGI to ASI*](https://arxiv.org/abs/2606.12683). An axis only crosses
  a ring when a public benchmark
  shows the model beating humans at roughly that level *on that domain's
  mapped benchmark* — and the two collective rings are currently
  unreachable by any criterion we'd accept, which we say out loud rather
  than quietly implying otherwise.
- **Why not true human percentiles throughout?** Because the data doesn't
  publicly exist: benchmarks report expert *means* or panel *averages*, not
  population distributions. The one genuinely percentile-rich signal we
  have is contest math (IMO medal thresholds). Details: recipe.md, Method 2.

## The axis → evaluation mapping

The heart of the chart. For eras 1–2 we use Hendrycks' own published
per-domain scores. For mid-2026 (no published scores exist), each axis is
carried by the public benchmark(s) we judged closest to the domain's
*construct* — with the judgment calls disclosed.

**Every point on this chart is a three-link claim — a small syllogism:**

1. **an axis** — a cognitive *construct* from the CHC framework (what we're
   trying to measure);
2. **a benchmark** — the public eval we judged best *operationalizes* that
   construct (the bridge from concept to number);
3. **a source** — the *specific published datum*, from a named source of
   stated quality, that sets where the point lands.

A point is only as strong as its weakest link. The table below makes all
three explicit for every axis, including the **source and its grade**
(*primary* = the benchmark's own site / paper / an official leaderboard;
*secondary* = a third-party aggregator or blog re-reporting it). Making the
chain legible is what lets a reader — or a newer model's results — *falsify*
a point. As of the 2026-07-14 audit below, several points are now falsified.

| Axis | Construct (link 1) | Benchmark & datum (link 2) | Source [grade] (link 3) | Plotted score |
|---|---|---|---|---|
| Mathematics | competition & research math | IMO gold (2025); FrontierMath ">40%" | IMO official; FM via bracai.eu **[secondary]** | 100, **Virtuoso ring** — the one axis with true percentile evidence (IMO) |
| General Knowledge | breadth + depth of world knowledge | GPQA Diamond ~94% vs ~65% expert mean | epoch.ai / benchlm.ai **[primary/secondary]** | 100, **Expert ring** (an expert *mean* isn't a 99th-pct calibration) |
| Reading & Writing | comprehension + composition | LongBench v2 64% vs 54% timed experts | llm-stats.com **[secondary]** | 100, at anchor (that's a reading test, not a writing one) |
| Reasoning (static) | solve the fixed puzzle | ARC-AGI-2: ~54% standalone frontier vs ~60% human panel | arcprize.org **[primary]** | 85 — an unverifiable "85%" leaderboard claim was *excluded* (⚠ now superseded — see audit) |
| Auditory | understand sound, speech, music | MMAU ~76% vs ~82% human | mmaubench.github.io **[primary]** | 80 |
| Visual | actually *see* — rotation, counting, correspondence | BLINK ~71% vs ~96% human | BLINK paper (arXiv) **[primary]** | 70 — perception benchmark, not the flattering knowledge-heavy MMMU (94%) |
| Working Memory | hold and manipulate context | MRCR 8-needle @1M: ~76% | awesomeagents.ai **[secondary]** | 60 — huge context ≠ faithful use of it |
| LT Memory Retrieval | recall without confabulating | hallucination 3–9%, halved by extended thinking | digitalapplied.com **[secondary]** | 60 |
| Speed | psychometric processing speed | none exists | — **[no source]** | 30 — era-2 value carried, lowest-confidence cell on the chart |
| LT Memory Storage | *accumulate* knowledge from use | MemoryBench et al.: SOTA "far from satisfying" | MemoryBench/CL-Bench (arXiv) **[primary]** | 10 — the standing bottleneck |
| Reasoning (dynamic) | learn a novel environment by acting | ARC-AGI-3 <1%; BALROG NetHack ~7%; humans breeze both | arcprize.org **[primary]** | 5 — triangulated across three eval families (⚠ now falsified — see audit) |

Full per-point evidence with dates: [data/era3_evidence.csv](data/era3_evidence.csv).
Rows tagged `ADJACENT` there (e.g. METR's 16-hour task horizons) are
deliberately *excluded* from axes — that's fast-rising agentic execution in
familiar tool-rich domains, a different construct than novel-environment
adaptation, and folding it in would blur the chart's key finding.

## Data-quality audit — 2026-07-14 (triggered by GPT-5.6 Sol)

Making the axis → benchmark → source chain explicit did exactly what a good
audit trail should: it surfaced bad points. Two kinds of rot showed up —
**weak sources** (four axes rest on secondary aggregators, not primary
benchmark sources) and **falsified numbers** (a model released *after* our
snapshot, **GPT-5.6 Sol** — OpenAI, 2026-07-09, now the top-ranked model at
[Epoch, ECI 162](https://epoch.ai/models/gpt-5-6-sol)) beats several of our
plotted points. This is **not just staleness**: at least one point was
*mis-stated at the time*.

**The chart image (`radar.svg`) has NOT been re-plotted** — its points are
still the 2026-07-03 numbers. Per this thread's correction discipline, a
correction is logged *before* it is drawn. The re-score is the next step
(scoped at the bottom).

| Axis | Plotted (2026-07-03) | Current data (GPT-5.6 Sol / 2026-07) | Source [grade] | Verdict |
|---|---|---|---|---|
| **R-dynamic** | 5 — "ARC-AGI-3 <1%, hasn't moved" | ARC-AGI-3 **7.78% semi-private / 13.33% public**; **won game ft09 at 87%** (max reasoning) | [arcprize.org](https://arcprize.org/results/openai-gpt-5-6-sol) **[primary]**, 2026-07-09 | **WRONG-as-stated.** Our single sharpest claim ("dynamic reasoning ≈ 0, flat for 3 years") is falsified — the axis is off the floor and one game is essentially solved. Highest-priority fix. |
| **R-static** | 85 — "~54% standalone; we *excluded* an unverified 85%" | ARC-AGI-2 **92.5%** (max reasoning) | [arcprize.org](https://arcprize.org/results/openai-gpt-5-6-sol) **[primary]**, 2026-07-09 | **STALE.** Now at/above the anchor. Ironic: the ~85% we discarded as unverifiable is beaten by a *verified* 92.5%. |
| **M (Math)** | "FrontierMath T1-3 **>40%**" | FrontierMath is version-fragmented: **T1-3 ≈ 89%** (Sol) vs the harder full set **≈ 40–48%** (GPT-5.4 @ 0.476) | benchlm.ai / llm-stats.com **[secondary]**; our datum was from bracai.eu **[weak]** | **WRONG-as-stated / mis-sourced.** ">40%" understates T1-3 by ~half *and* silently conflates two different FrontierMath versions. (The M=100/Virtuoso *conclusion* survives — IMO gold carries it — but the evidence line was bad.) |
| K (Knowledge) | 100/Expert (GPQA ~94.3%) | GPQA Diamond **94.6%** (Sol) | benchlm.ai **[secondary]** | OK — consistent. |

**Source-quality finding (independent of Sol):** four axes — **Reading &
Writing, Working Memory, LT Memory Retrieval,** and the **FrontierMath line
of Mathematics** — are set by *secondary* aggregators (llm-stats.com,
awesomeagents.ai, digitalapplied.com, bracai.eu), not by the benchmark's own
results. Even where the number is right, the provenance is one hop too long.
These are the first re-sourcing targets.

**Scoped next step — a proper re-score (not done here):** (1) re-source every
point to a *primary* benchmark result; (2) re-estimate the era-3 column
against current frontier models (GPT-5.6 Sol, Claude Fable 5, etc.), not the
mid-2026 snapshot; (3) run it through an adversarial consult before locking,
the same discipline that produced the original — then regenerate `radar.svg`
and its hash as a dated new version. The headline finding to re-examine
first: is "dynamic reasoning is the flat, near-zero bottleneck" still true
when a frontier model wins an ARC-AGI-3 game? The gap is narrowing, not
absent — and that is itself the news.

## What the chart says

Three years of frontier progress filled in nearly everything measurable —
knowledge, math, reading, static puzzles, perception are at or through the
human ring. What didn't move: **learning-during-use**. Dynamic reasoning
(~5) and long-term memory storage (~10) are two faces of the same missing
capability — the system doesn't get better at *your* problem while working
on it. Composite "AGI score" trend lines (27% → 57% → ~65%) hide this:
the remaining gap isn't more of the same, it's concentrated in one
qualitatively different capability. Which cuts both ways — steady trends
understate the jump risk if continual learning cracks, and overstate
generality if you extrapolate the composite line naively.

> **⚠ Update (2026-07-14):** this section's central claim — dynamic reasoning
> pinned near zero — is now under revision. A model released after this chart
> (GPT-5.6 Sol) scores 7.78–13.33% on ARC-AGI-3 and won one game outright.
> The bottleneck is *narrowing*, not absent. See the Data-quality audit above;
> the chart image still shows the pre-Sol numbers pending a re-score.

## How it was built (one day, 2026-07-03)

1. Reconstructed from a lost prototype: Hendrycks CHC radar + GDM level
   rings + benchmark-mapped current scores.
2. Pinned the three source papers (checksummed; licenses verified for
   redistribution) and verified Hendrycks' Table 1 against the arXiv source
   by grep, not by trusting a summary.
3. Collected mid-2026 evidence per axis from public leaderboards, dated.
4. Adversarial review by a *different* frontier model (Codex), which moved
   four scores and two ring placements — including forcing the exclusion of
   an ARC-AGI-2 claim we couldn't verify at a primary source.
5. Two errors caught by the human operator, corrected on the record: an
   era-2 dynamic-reasoning conflation (the paper's composite score doesn't
   measure interactive adaptation) and invalid XML in the generated SVG.
6. A recipient critique then forced the scale-honesty rewrite above.

Every step, mistake, and reversal is a timestamped entry in
[THREAD.md](THREAD.md) — corrections are append-only, so the errors remain
visible. The chart regenerates deterministically from
[data/radar_scores.csv](data/radar_scores.csv) via ~150 lines of dependency-
free Python; the SHA-256 in [recipe.md](recipe.md) pins the exact artifact.

## Known weaknesses (our own list)

- **Several points are stale or were mis-sourced** — see the 2026-07-14
  Data-quality audit above. R-dynamic and R-static are superseded by GPT-5.6
  Sol; the FrontierMath evidence line was under-specified and from a secondary
  source; four axes rest on aggregators rather than primary results. A
  re-score is scoped but not yet done.
- **Speed** has no valid public benchmark; its value is a placeholder.
- **Visual** has a construct gap: models ace knowledge-heavy image tests
  while failing "glance" perception; we scored the perception construct.
- **Percentile calibration** below the anchor doesn't exist (see scale
  section) — coverage is the honest unit, and it's a weaker unit.
- **Collective rings** have no crossing criterion yet.
- **Era-3 is our estimate.** The paper's authors haven't scored post-GPT-5
  models; ours is a disclosed, dated, reviewable stand-in, not a
  measurement.
- There's also a dated **end-of-2026 projection**
  ([data/eoy2026_projection.csv](data/eoy2026_projection.csv)) we've
  committed to scoring publicly in January 2027 — including a recipient's
  on-record claim that our central estimates skew low.

## Disagree with a number?

Good — that's the designed use. Find the axis's row in
[data/era3_evidence.csv](data/era3_evidence.csv), bring a better benchmark
or a primary source we missed, and the chart regenerates in one command.
The bar for changing a score is the bar everything here already cleared:
dated, public, verifiable evidence.

## References

The chart's *framework* — its axes, its anchor, and its rings — rests on three
papers, all retrieved from arXiv on 2026-07-03 and pinned in [refs/](refs/) as
text extracts (verbatim source PDFs in `refs/originals/`):

1. **[A Definition of AGI](https://arxiv.org/abs/2510.18212)** — Hendrycks, D.,
   et al. (2025). arXiv:2510.18212v3. License: CC BY 4.0.
   *The Cattell–Horn–Carroll psychometric base: the ten cognitive domains, the
   "well-educated adult" anchor, and the GPT-4 / GPT-5 per-domain scores that
   carry eras 1–2 verbatim.*
2. **[Levels of AGI: Operationalizing Progress on the Path to AGI](https://arxiv.org/abs/2311.02462)**
   — Morris, M. R., et al. (Google DeepMind, 2023). arXiv:2311.02462.
   License: CC BY-NC-ND 4.0.
   *The percentile performance levels — Competent (50th), Expert (90th),
   Virtuoso (99th) — that become the radar's rings.*
3. **[From AGI to ASI](https://arxiv.org/abs/2606.12683)** — Genewein, T., et
   al. (Google DeepMind, 2026). arXiv:2606.12683v1. License: CC BY 4.0.
   *The above-individual-human collective rings (research team, enterprise).*

The chart's *data* — the per-axis benchmark evidence for the mid-2026 era
(GPQA, IMO, ARC-AGI-2/3, LongBench v2, BLINK, MMAU, MRCR, BALROG, and the
rest), each with its score, date, and source link — lives in
[data/era3_evidence.csv](data/era3_evidence.csv), kept there as the single
source of truth rather than duplicated here. Full citations for every input
are also in [recipe.md](recipe.md) (Inputs); the PDF redistribution licenses
are itemized in [refs/LICENSES.md](refs/LICENSES.md).
