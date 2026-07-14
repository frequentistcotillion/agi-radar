# Axis → Benchmark → Human baseline → Placement

**The authoritative mapping** for the AGI Radar. Every plotted point traces
through this table: a CHC **axis** (construct) → the **benchmark(s)** that
operationalize it → the **human baseline** on that benchmark → the **placement**
on the 0–100 well-educated-adult-anchor scale (calibration bridge, recipe
Method 7).

**Re-score RS-2026-07-14 · SOTA-envelope (APPLIED; radar.svg `6a8d4110…c943`).**
Era-3 = the **best current public result per axis** (any model, named + dated
below), placed via the calibration bridge and adversarially re-consulted
(gemini 2026-07-14; codex 2026-07-09). *Single-lineage on GPT-5.6 Sol was tried
first and dropped* — Sol has confident data on only 4 of 11 axes, so a strict
Sol chart is mostly holes. Eras 1–2 stay GPT-4/GPT-5 (Hendrycks); a chart
footnote flags era-3 as a per-axis frontier envelope, not one system.

## Calibration bridge (how a benchmark number becomes a placement)

A placement is the model's **position relative to the benchmark's human
reference**, NOT the raw benchmark % — and it is a **judgment informed by** that
position, not an arithmetic ratio (gemini, 2026-07-14: 30% where humans get 60%
is not "half the construct"):
- Model **≥** human baseline → **near/at the anchor**; a *single* benchmark
  beating the human **mean** lands **~90 (near), not 100 (at)**, unless a broad
  battery corroborates. A ring (Expert 90th / Virtuoso 99th) needs
  percentile-rich evidence, not beating a mean.
- Model **<** human baseline → placement = the honest **fraction of the anchor**
  covered (low-confidence flagged).
- **No human baseline** → the axis cannot be anchored; explicit low-confidence
  coverage estimate.

## The mapping (era-3 = current SOTA)

| Axis | Construct | Benchmark | Human baseline (source) | Era-3 SOTA (model, date) | Placement | Conf |
|---|---|---|---|---|---|---|
| **K** | knowledge breadth+depth | GPQA Diamond (HLE = harder context) | experts **~65–70%** (GPQA paper; OpenAI PhDs 69.7%) | **94.6%** (GPT-5.6 Sol) | **100 / Expert** | high |
| **M** | competition + research math | FrontierMath T1-3 + T4v2 + IMO | IMO gold ≈ top 0.01%; FM stumps pro mathematicians | T4v2 **88%** (Fable 5), T1-3 **89%** (Sol); IMO gold | **100 / Virtuoso** | high |
| **R-static** | solve the fixed puzzle | ARC-AGI-2 | human panel **~60%** (arcprize) | **92.5%** (Sol, 2026-07-09) | **90** (near anchor, no ring) | high |
| **R-dynamic** | learn a novel env by acting | ARC-AGI-3 (+ BALROG) | humans **~100%** (arcprize) | **13.33% pub / 7.78%** (Sol); won ft09 87% | **12** (far below) | med |
| **RW** | comprehension + composition | LongBench v2/Pro (read) + HelloBench (write) | time-constrained experts **53.7%** (LongBench v2) | Opus 4.5 **64.4%** (LB v2) | **100 / anchor** | med |
| **WM** | hold + manipulate context | MRCR | **none** — no human reads 1M tokens | **~91.5%** (Sol; version unconfirmed) | **70** | low |
| **MS** | accumulate knowledge from use | MemoryBench / continual-learning | humans accumulate continuously (no %) | "far from satisfying" (authors) | **12** | low |
| **MR** | recall *without confabulating* | LongMemEval (primary) / LoCoMo | models lag humans; no clean % | mem-systems **83–86%**; oracle GPT-4o 82.4% | **55** | low |
| **V** | see — perception (Gv) | BLINK | humans **95.7%** (BLINK paper) | **81.4%** (Seed 2.1 Pro) | **78** | med |
| **A** | understand sound/speech/music | MMAU | humans **~82%** (MMAU paper) | **65.6%** (Qwen2.5-Omni-7B) | **70** | low |
| **S** | processing speed | none exists | — | — | **30** (carried) | v.low |

## What the human column reveals

Only **~6 of 11 axes have a real human baseline** (K, M, R-static, R-dynamic, V,
A), so only those are placed *against human performance*. The rest — WM (MRCR
synthetic), MS, MR (agent-memory benches lack a clean human %), S (no benchmark)
— are explicit low-confidence coverage estimates. That is the honest reason the
below-anchor region of the chart is soft, and it is a finding, not a defect.

## Headline (RS-2026-07-14)

Static reasoning is **at the doorstep of the human anchor (~90)** while dynamic
reasoning has **come off the floor (~12) but remains the dominant bottleneck**.
The static-vs-dynamic split (**~90 vs ~12**) is still the chart's sharpest
asymmetry — narrowed from the 2026-07-03 ~85-vs-5 read; the "flat for 3 years"
claim is retired (a frontier model won an ARC-AGI-3 game).
