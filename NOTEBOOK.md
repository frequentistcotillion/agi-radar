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
GPT-5 (2025), and the current frontier (mid-2026 → July 2026 — era-3 is the
best public result per axis, each model named + dated in the sources).

One deviation from Hendrycks: we split his "On-the-Spot Reasoning" domain in
two — **static** reasoning (solve a fixed puzzle put in front of you) and
**dynamic** reasoning (dropped into an unfamiliar interactive environment,
figure out the rules by acting). We split it because the single most
important fact about current AI hides inside that average: static reasoning is
at the doorstep of human level (~90); dynamic reasoning has only just come off
the floor (~12 — a frontier model won its first ARC-AGI-3 game in July 2026)
and remains the single dominant bottleneck.

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

The heart of the chart. Every point is a three-link claim — a small syllogism:
**(1) an axis** (a CHC construct) → **(2) a benchmark** that operationalizes it
→ **(3) a source** (a named datum of stated grade) that sets where it lands. A
point is only as strong as its weakest link. Eras 1–2 use Hendrycks' own
GPT-4/GPT-5 scores; **era-3 (re-score RS-2026-07-14) is the current frontier
SOTA per axis** — best model, named + dated. The full mapping *with human
baselines and source grades* is the authoritative table in
**[MAPPING.md](MAPPING.md)**; the plain-language version:

| Axis | Benchmark | Score | Reading |
|---|---|---|---|
| Mathematics | FrontierMath (all tiers) + IMO | **100 / Virtuoso** | saturating even at research tier (T4v2 88%, Fable 5); IMO gold = true percentile evidence |
| General Knowledge | GPQA Diamond | **100 / Expert** | ~94% vs ~65–70% experts; an expert *mean* isn't a 99th-pct calibration, so Expert not Virtuoso |
| Reading & Writing | LongBench v2 + HelloBench | **100 / anchor** | frontier ≥ time-constrained experts on reading; strong long-form writing |
| Reasoning (static) | ARC-AGI-2 | **90** | 92.5% > ~60% human panel — but ONE benchmark, so *near* not *at* the anchor |
| Visual | BLINK | **78** | Seed 2.1 Pro 81.4% vs 95.7% humans — perception still below the anchor |
| Auditory | MMAU | **70** | best is 65.6% (a 7B audio specialist) vs ~82% humans |
| Working Memory | MRCR | **70** | ~91.5% but **no human baseline exists** — a soft coverage estimate |
| LT Memory Retrieval | LongMemEval | **55** | re-mapped from hallucination-rate; durable multi-session recall lags humans |
| LT Memory Storage | MemoryBench / continual | **12** | the standing bottleneck — SOTA "far from satisfying" |
| Speed | none exists | **30** | no benchmark; lowest-confidence cell |
| Reasoning (dynamic) | ARC-AGI-3 (+ BALROG) | **12** | 7–13% and won one game (ft09 87%); off the floor, still far below ~100% humans |

Full per-point evidence with dates + sources: [MAPPING.md](MAPPING.md) and
[data/era3_evidence.csv](data/era3_evidence.csv). METR's long-horizon task
scores are deliberately *excluded* from R-dynamic — that's agentic execution in
prior-rich domains, a different construct than novel-environment adaptation.

## Data-quality audit — 2026-07-14 (triggered by GPT-5.6 Sol)

Making the axis → benchmark → source chain explicit did exactly what a good
audit trail should: it surfaced bad points. Two kinds of rot showed up —
**weak sources** (four axes rest on secondary aggregators, not primary
benchmark sources) and **falsified numbers** (a model released *after* our
snapshot, **GPT-5.6 Sol** — OpenAI, 2026-07-09, now the top-ranked model at
[Epoch, ECI 162](https://epoch.ai/models/gpt-5-6-sol)) beats several of our
plotted points. This is **not just staleness**: at least one point was
*mis-stated at the time*.

**RESOLVED — the chart was re-plotted (RS-2026-07-14, hash `6a8d4110…c943`).**
Per this thread's discipline the corrections below were logged *before* they
were drawn; they are now applied. R-static 85→90, R-dynamic 5→12, plus a
SOTA-envelope re-source of the other axes — full detail in
[MAPPING.md](MAPPING.md).

| Axis | Plotted (2026-07-03) | Current data (GPT-5.6 Sol / 2026-07) | Source [grade] | Verdict |
|---|---|---|---|---|
| **R-dynamic** | 5 — "ARC-AGI-3 <1%, hasn't moved" | ARC-AGI-3 **7.78% semi-private / 13.33% public**; **won game ft09 at 87%** (max reasoning) | [arcprize.org](https://arcprize.org/results/openai-gpt-5-6-sol) **[primary]**, 2026-07-09 | **WRONG-as-stated.** Our single sharpest claim ("dynamic reasoning ≈ 0, flat for 3 years") is falsified — the axis is off the floor and one game is essentially solved. Highest-priority fix. |
| **R-static** | 85 — "~54% standalone; we *excluded* an unverified 85%" | ARC-AGI-2 **92.5%** (max reasoning) | [arcprize.org](https://arcprize.org/results/openai-gpt-5-6-sol) **[primary]**, 2026-07-09 | **STALE.** Now at/above the anchor. Ironic: the ~85% we discarded as unverifiable is beaten by a *verified* 92.5%. |
| **M (Math)** | "FrontierMath T1-3 **>40%**" | FrontierMath is saturating across *all* tiers: **T1-3 ≈ 89%** (Sol); even **Tier 4 v2** — research-level, error-corrected — is **88%** (Claude Fable 5), Sol ≈ 83%, and has been **>40% since GPT-5.2** | [Epoch, Tier 4 v2](https://epoch.ai/benchmarks/frontiermath-tier-4-v2) **[primary]** (eval 2026-06-12); T1-3 via benchlm.ai **[secondary]** | **WRONG-as-stated.** ">40%" (from bracai.eu **[weak]**) treats a *saturating* benchmark as a hard ceiling — even the hardest tier is ~88%. (M=100/Virtuoso is now over-determined: IMO gold *and* FrontierMath.) |
| K (Knowledge) | 100/Expert (GPQA ~94.3%) | GPQA Diamond **94.6%** (Sol) | benchlm.ai **[secondary]** | OK — consistent. |

*Correction (this audit ate its own dog food): a first pass of the Math row
mis-cited FrontierMath's hard tier as "~40–48%" from a stale figure (GPT-5.4
@ 0.476) — itself a version error, the exact failure this audit exists to
catch. The hard tier (Tier 4 v2) is ~88%. Fixed above; logged as a correction
turn in THREAD.md, 2026-07-14. The lesson holds twice over: a source-discipline
audit still needs its own sources checked.*

**Source-quality finding (independent of Sol):** four axes — **Reading &
Writing, Working Memory, LT Memory Retrieval,** and the **FrontierMath line
of Mathematics** — are set by *secondary* aggregators (llm-stats.com,
awesomeagents.ai, digitalapplied.com, bracai.eu), not by the benchmark's own
results. Even where the number is right, the provenance is one hop too long.
These are the first re-sourcing targets.

**The re-score (DONE — RS-2026-07-14):** every point re-sourced toward primary;
era-3 re-set to current frontier SOTA per axis (a *SOTA-envelope* — single-
lineage on GPT-5.6 Sol was tried first but Sol has confident data on only 4 of
11 axes); adversarially re-consulted (gemini + codex), which pulled R-static
back from a too-aggressive 100 to **90** and confirmed R-dynamic at **12**; then
`radar.svg` regenerated as a dated new version (hash `6a8d4110…c943`). The
headline answer: **"dynamic reasoning is the flat, near-zero bottleneck" is
retired** — a frontier model won an ARC-AGI-3 game; the gap is narrowing, not
absent, and that is the news.

## What the chart says

Three years of frontier progress filled in nearly everything measurable —
knowledge, math and reading are at or through the human ring; static reasoning
(~90) and perception (~78) sit just beneath it. What didn't move:
**learning-during-use**. Dynamic reasoning (~12) and long-term memory storage
(~12) are two faces of the same missing capability — the system doesn't get
better at *your* problem while working on it. Composite "AGI score" trend lines (27% → 57% → ~65%) hide this:
the remaining gap isn't more of the same, it's concentrated in one
qualitatively different capability. Which cuts both ways — steady trends
understate the jump risk if continual learning cracks, and overstate
generality if you extrapolate the composite line naively.

> **✓ Updated 2026-07-14 (RS re-score applied):** dynamic reasoning is no
> longer "pinned near zero" — GPT-5.6 Sol scores 7.78–13.33% on ARC-AGI-3 and
> won one game (ft09) outright, so the axis moved **5 → 12** and "flat for 3
> years" is retired. It stays the dominant bottleneck (~⅛ of the human anchor).
> The chart now shows the re-scored numbers.

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

- **The below-anchor region is soft.** Only ~6 of 11 axes have a real human
  baseline (K, M, R-static, R-dynamic, V, A); the rest (Working Memory, both
  memory axes, Speed) are low-confidence coverage estimates by the nature of
  their benchmarks. The 2026-07-14 re-score fixed the stale/mis-sourced points
  and re-set era-3 to current SOTA, but it cannot manufacture human baselines
  that do not exist — see [MAPPING.md](MAPPING.md).
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
