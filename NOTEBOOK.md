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
*construct* — with the judgment calls disclosed:

| Axis | In plain terms | Mid-2026 evidence | Reading |
|---|---|---|---|
| Mathematics | competition & research math | IMO gold (2025); FrontierMath >40% | 100, **Virtuoso ring** — the one axis with true percentile evidence |
| General Knowledge | breadth + depth of world knowledge | GPQA Diamond ~94% vs ~65% expert mean | 100, **Expert ring** (downgraded from Virtuoso in review — an expert *mean* isn't a 99th-pct calibration) |
| Reading & Writing | comprehension + composition | LongBench v2 64% vs 54% timed experts | 100, at anchor (Expert ring removed in review — that's a reading test, not a writing one) |
| Reasoning (static) | solve the fixed puzzle | ARC-AGI-2: ~54% standalone frontier vs ~60% human panel | 85 — an unverifiable "85%" leaderboard claim was *excluded*; we used the conservative verified numbers |
| Auditory | understand sound, speech, music | MMAU ~76% vs ~82% human | 80 |
| Visual | actually *see* — rotation, counting, correspondence | BLINK ~71% vs ~96% human | 70 — we deliberately use a perception benchmark, not the flattering knowledge-heavy MMMU (94%) |
| Working Memory | hold and manipulate context | MRCR 8-needle @1M: ~76% | 60 — huge context ≠ faithful use of it |
| LT Memory Retrieval | recall without confabulating | hallucination 3–9%, halved by extended thinking | 60 |
| Speed | psychometric processing speed | none exists | 30 — era-2 value carried, lowest-confidence cell on the chart |
| LT Memory Storage | *accumulate* knowledge from use | MemoryBench et al.: SOTA "far from satisfying" | 10 — the standing bottleneck |
| Reasoning (dynamic) | learn a novel environment by acting | ARC-AGI-3 <1%; BALROG NetHack ~7%; humans breeze both | 5 — triangulated across three eval families after a reviewer challenged single-eval reliance |

Full sources with dates: [data/era3_evidence.csv](data/era3_evidence.csv).
Rows tagged `ADJACENT` there (e.g. METR's 16-hour task horizons) are
deliberately *excluded* from axes — that's fast-rising agentic execution in
familiar tool-rich domains, a different construct than novel-environment
adaptation, and folding it in would blur the chart's key finding.

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
