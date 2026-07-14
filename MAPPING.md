# Axis → Benchmark → Human baseline → Placement

**The authoritative mapping** for the AGI Radar. Every plotted point traces
through this table: a CHC **axis** (construct) → the **benchmark(s)** that
operationalize it → the **human baseline** on that benchmark → the **placement**
on the 0–100 well-educated-adult-anchor scale (via the calibration bridge,
recipe.md Method 7).

**Re-score RS-2026-07-14 · single lineage = GPT-4 → GPT-5 → GPT-5.6 Sol.**
Era-3 uses GPT-5.6 Sol's *own* result where one exists; where Sol is unscored on
the mapped benchmark, the point is **carried/provisional** (never back-filled
with another model). Status below is for the DRAFT re-score — placements marked
`prov` are not yet locked and several await final primary numbers + the mandated
re-consult (recipe Method 7e) before radar.svg is regenerated.

## Calibration bridge (how a benchmark number becomes a placement)

A placement is the model's **position relative to the benchmark's human
reference**, NOT the raw benchmark %:
- Sol **≥** the human baseline → axis is **at the anchor (100)**; a ring
  (Expert 90th / Virtuoso 99th) needs percentile-rich evidence, not beating a mean.
- Sol **<** the human baseline → placement is the honest **fraction of the
  anchor** the benchmark shows Sol covering (low-confidence flagged).
- **No human baseline** → the axis cannot be anchored; it stays an explicit
  coverage-estimate (low confidence), by nature of the benchmark.

## The mapping

| Axis | Construct | Benchmark (leaderboard) | Human baseline (source) | Sol (single-lineage) | Placement | Conf |
|---|---|---|---|---|---|---|
| **K** | knowledge breadth+depth | GPQA Diamond (HLE = harder frontier context) | experts **~65–70%** (GPQA paper; OpenAI PhDs 69.7%) | **94.6%** | **100 / Expert** | high |
| **M** | competition + research math | FrontierMath T1-3 + **T4v2** + IMO | IMO gold ≈ top 0.01%; FM stumps pro mathematicians | T1-3 **89%**, T4v2 **83%**; IMO gold | **100 / Virtuoso** | high |
| **R-static** | solve the fixed puzzle | ARC-AGI-2 | human panel **~60%** (arcprize) | **92.5%** (primary) | **100 / anchor** | high |
| **R-dynamic** | learn a novel env by acting | ARC-AGI-3 (+ BALROG novel-env slice) | humans **~100%** (arcprize) | **7.78% semi-priv / 13.33% pub**; won ft09 87% | **12** (far below) | med |
| **RW** | comprehension + composition | **LongBench Pro** (comp) + **HelloBench** (writing) *(was LongBench v2 — stale)* | TBD — needs primary | Sol unscored | **prov** (carry) | low |
| **WM** | hold + manipulate context | MRCR | **none** — no human reads 1M tokens | **91.5%** *(version unconfirmed)* | **prov** (no anchor) | low |
| **MS** | accumulate knowledge from use | MemoryBench / continual-learning | humans accumulate continuously (no %) | Sol unscored | **~10–12** | low |
| **MR** | recall *without confabulating* | **LongMemEval** (primary) / LoCoMo *(was hallucination-rate — wrong proxy)* | models lag humans; no clean % | Sol unscored | **prov** | low |
| **V** | see — perception (Gv) | BLINK *(benchmark current; our old # was stale)* | humans **95.7%** (BLINK paper) | Sol unscored on BLINK (has MMMU-Pro 83%) | **prov ~70** | low |
| **A** | understand sound/speech/music | MMAU | humans **~82%** (MMAU paper) | Sol unscored (no audio) | **prov** (carry) | low |
| **S** | processing speed | none exists | — | n/a | **30** (carried) | v.low |

## What the human column reveals

Filling the human-baseline column exposes that the 11 axes split three ways:
- **Human-anchored (6):** K, M, R-static, R-dynamic, V, A — a real human number
  exists, so placement is rigorous.
- **No human baseline (4):** WM (MRCR synthetic), MS, MR (agent-memory benches),
  and the below-anchor memory region generally — placement is an explicit
  coverage-estimate, not a human-relative measurement.
- **No benchmark (1):** S.

So only ~6 of 11 points can be placed *against human performance*; the rest are
soft by construction. This is the honest reason the below-anchor region of the
chart carries low confidence.

## Field SOTA (context only — NOT plotted; single-lineage plots Sol)

Where Sol is unscored, the current best public number (any model) is recorded so
readers know where the frontier sits — but it does not set the point:
- V / BLINK: **Seed 2.1 Pro 0.814** (still < the 95.7% human anchor)
- A / MMAU: **Qwen2.5-Omni-7B 0.656** (a 7B specialist; < ~82% human)
- MR / LongMemEval: ~94.4% (top system) · LoCoMo ~92.5%

## Open items before lock

1. RW: fetch primary LongBench Pro + HelloBench human baselines & any Sol number.
2. WM: version-lock the Sol MRCR 91.5% (needle count / context length) vs our old 76%.
3. MR: confirm LongMemEval human ceiling (if any) and any Sol number.
4. Mandatory re-consult (Method 7e) — R-static +15 and the R-dynamic headline
   change both trip the >10pt / headline-change gate — before radar.svg is regenerated.
