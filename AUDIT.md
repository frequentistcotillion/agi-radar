# How to audit this artifact (third-party procedure)

You have received a directory (or archive) containing `radar.svg` — a chart
claiming to show frontier-AI capability across human cognitive domains as of
mid-2026 — plus everything needed to verify it. You do not need to trust the
author. This file tells you what to check and what each check proves.

**Prerequisites:** any Linux/macOS machine with Python ≥3.11 (standard
library only) and `sha256sum` (macOS: `shasum -a 256`).

## 0. Establish provenance (do this first)

Hashes *inside* a bundle only prove internal consistency — a tamperer could
change data and hashes together. Get the expected artifact hash from a
channel independent of this bundle (the author's git history, a signed
message, or the author directly):

```
expected: radar.svg sha256 = 81feb3d9188a50bc23163997821c8f4ced42dee49b636c5513616097b0067c55
```

The canonical public home of this artifact is
https://github.com/frequentistcotillion/agi-radar — if you received this as
an archive, compare against that repository. If you are reading this inside
a git repository, the commit history is itself the provenance record — check that the history shows
incremental work (it does: refs → data → design → corrections), not a
single bulk import.

## 1. Verify the input papers are what the recipe says they are

```
cd refs/
sha256sum -c SHA256SUMS
```

Stronger version (removes trust in the bundled PDFs entirely): re-download
the three papers yourself from arxiv.org using the IDs in the filenames
(2510.18212v3, 2311.02462, 2606.12683v1) and compare hashes. Note
2311.02462 is pinned at whatever arXiv revision was current 2026-07-03; if
arXiv has since revised it, hashes will differ — compare against the v-tag
that was live then.

## 2. Regenerate the artifact from data alone

```
cd code
rm -f ../radar.svg
python3 radar.py
sha256sum ../radar.svg     # must equal the hash from step 0
```

This proves: the chart is a pure function of `data/radar_scores.csv` +
~150 lines of readable stdlib Python. No hidden inputs, no manual editing.
Read `radar.py` — it's short by design.

## 3. Verify the era-1/era-2 data against the published source

`data/hendrycks_table1.csv` claims to be Table 1 of arXiv:2510.18212v3.
Open the paper (or https://arxiv.org/html/2510.18212v3) and check the
per-domain rows: GPT-4 = 8/6/4/0/2/0/4/0/0/3 (total 27%), GPT-5 =
9/10/10/7/4/0/4/4/6/3 (total 57%). One deliberate exception is documented
in `recipe.md` Method 4: era-2 "Reasoning (dynamic)" uses 5 (from ARC-AGI-3
measurements of GPT-5-era systems), not the paper's composite 70.

## 4. Spot-check the era-3 evidence

`data/era3_evidence.csv` lists, per axis: the mapped benchmark, the claimed
mid-2026 SOTA, the human baseline, and the source. These are point-in-time
leaderboard readings from 2026-07-03 — follow any row's source and confirm
the number was plausible as of that date. Rows marked `-ADJACENT` or
`-secondary` are context, not axis evidence. One aggregator claim (ARC-AGI-2
"85%") is explicitly EXCLUDED as unverifiable at a primary source — the
conservative verified figures were used instead.

## 5. Audit the judgment, not just the arithmetic

The era-3 scores are estimates, not measurements — the honest question is
whether the judgment calls were reasonable and disclosed:

- `recipe.md` → **Method** lists every judgment call and its rationale
  (ring placements, the R split, scope decisions, weakest cells).
- `THREAD.md` is the complete, timestamped work log: every decision, an
  adversarial review by a second model (which moved four scores and two
  ring placements), two operator-caught errors and their corrections.
  Turns are append-only by protocol — corrections appear as new entries,
  never edits, so mistakes remain visible.
- Known weakest cells, per the log itself: Speed (no public benchmark;
  era-2 value carried) and the era-3 estimates for WM/MR (judgment-heavy).

## What a passing audit establishes

1. The chart is exactly reproducible from the included data (steps 0+2).
2. The inputs are the published papers they claim to be (steps 1+3).
3. The era-3 numbers trace to dated public sources or are flagged as
   judgment (step 4).
4. The reasoning trail is complete and self-critical (step 5).

What it does NOT establish: that the era-3 estimates are *correct* — they
are one team's disclosed, dated, benchmark-grounded judgment, offered for
exactly this kind of scrutiny. Disagreements should be arguable row-by-row
against `data/era3_evidence.csv`.
