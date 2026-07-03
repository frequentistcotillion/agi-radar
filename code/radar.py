#!/usr/bin/env python3
"""AGI Radar — renders radar.svg from ../data/radar_scores.csv.

Stdlib only; output is deterministic (byte-stable) so the recipe can pin a
SHA-256. Scale: radial 1.0 = well-educated-adult anchor (Hendrycks). Rings
above the anchor are ORDINAL thresholds (GDM Levels of AGI percentiles, then
Genewein collective rings), not a continuous scale — see the plot footnote.

Usage: python3 radar.py [scores_csv] [out_svg]
"""
import csv
import math
import sys

# radial value for each ordinal ring above the anchor
RING_RADIAL = {"none": None, "anchor": 1.00, "expert": 1.25,
               "virtuoso": 1.50, "team": 1.75, "enterprise": 2.00}
# rings drawn on the chart: (radial, label)
RINGS = [(0.50, "Competent (50th pct)"),
         (1.00, "Well-educated adult (~80th)"),
         (1.25, "Expert (90th)"),
         (1.50, "Virtuoso (99th)"),
         (1.75, "Research team"),
         (2.00, "Enterprise")]
ERAS = [("era1", "GPT-4 era (2023)", "#9db4c8"),
        ("era2", "GPT-5 era (2025)", "#4a7ba6"),
        ("era3", "Mythos-class (mid-2026)", "#c0392b")]

CX, CY, R_UNIT = 460.0, 420.0, 150.0  # px; radial 2.0 -> 300 px


def load(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(r for r in f if not r.startswith("#")):
            radial3 = RING_RADIAL[row["era3_ring"]]
            if radial3 is None:
                radial3 = float(row["era3_score"]) / 100.0
            rows.append({
                "label": row["label"],
                "era1": float(row["era1_gpt4"]) / 100.0,
                "era2": float(row["era2_gpt5"]) / 100.0,
                "era3": radial3,
            })
    # spiral: era-3 descending, highest at 12 o'clock, clockwise;
    # tie-break on label so the sort (and the SVG) is fully deterministic
    rows.sort(key=lambda r: (-r["era3"], r["label"]))
    return rows


def pt(radial, i, n):
    theta = 2.0 * math.pi * i / n  # 0 = 12 o'clock, increasing = clockwise
    x = CX + R_UNIT * radial * math.sin(theta)
    y = CY - R_UNIT * radial * math.cos(theta)
    return f"{x:.2f},{y:.2f}"


def xy(radial, i, n):
    theta = 2.0 * math.pi * i / n
    return (CX + R_UNIT * radial * math.sin(theta),
            CY - R_UNIT * radial * math.cos(theta))


def main():
    scores_csv = sys.argv[1] if len(sys.argv) > 1 else "../data/radar_scores.csv"
    out_svg = sys.argv[2] if len(sys.argv) > 2 else "../radar.svg"
    rows = load(scores_csv)
    n = len(rows)
    s = []
    s.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 880" '
             'font-family="Helvetica,Arial,sans-serif">')
    s.append('<rect width="920" height="880" fill="white"/>')
    s.append('<text x="460" y="40" text-anchor="middle" font-size="24" '
             'fill="#1a1a1a">AGI Radar — CHC domains vs the '
             'well-educated-adult anchor</text>')
    s.append('<text x="460" y="64" text-anchor="middle" font-size="13" '
             'fill="#555">Eras 1–2: Hendrycks et al. Table 1 (arXiv:2510.18212). '
             'Era 3: workshop estimate from public benchmarks, 2026-07-03.</text>')

    # rings (anchor ring emphasized); labels are emitted AFTER the polygons so
    # the inner ones (Competent, anchor) stay legible over the era fills
    ring_labels = []
    for radial, label in RINGS:
        r = R_UNIT * radial
        emph = radial == 1.0
        s.append(f'<circle cx="{CX:.2f}" cy="{CY:.2f}" r="{r:.2f}" fill="none" '
                 f'stroke="{"#333" if emph else "#cccccc"}" '
                 f'stroke-width="{1.6 if emph else 0.8}"'
                 f'{"" if emph else " stroke-dasharray=\"4 3\""}/>')
        ring_labels.append(
            f'<text x="{CX + 6:.2f}" y="{CY - r - 4:.2f}" font-size="10.5" '
            f'fill="{"#1a1a1a" if emph else "#777"}" stroke="white" '
            f'stroke-width="3" paint-order="stroke">{label}</text>')

    # spokes and axis labels
    for i, row in enumerate(rows):
        x, y = xy(2.0, i, n)
        s.append(f'<line x1="{CX:.2f}" y1="{CY:.2f}" x2="{x:.2f}" y2="{y:.2f}" '
                 'stroke="#dddddd" stroke-width="0.8"/>')
        lx, ly = xy(2.14, i, n)
        anchor = "middle"
        if lx > CX + 12:
            anchor = "start"
        elif lx < CX - 12:
            anchor = "end"
        s.append(f'<text x="{lx:.2f}" y="{ly + 4:.2f}" text-anchor="{anchor}" '
                 f'font-size="13" fill="#1a1a1a">{row["label"]}</text>')

    # era polygons, oldest underneath
    for key, _label, color in ERAS:
        pts = " ".join(pt(row[key], i, n) for i, row in enumerate(rows))
        s.append(f'<polygon points="{pts}" fill="{color}" fill-opacity="0.14" '
                 f'stroke="{color}" stroke-width="2"/>')
        for i, row in enumerate(rows):
            x, y = xy(row[key], i, n)
            s.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="3" fill="{color}"/>')

    # ring labels above the polygons
    s.extend(ring_labels)

    # legend
    ly = 790
    for j, (_key, label, color) in enumerate(ERAS):
        lx = 120 + j * 260
        s.append(f'<rect x="{lx}" y="{ly}" width="14" height="14" fill="{color}" '
                 'fill-opacity="0.35" stroke-width="2" stroke="' + color + '"/>')
        s.append(f'<text x="{lx + 20}" y="{ly + 12}" font-size="13" '
                 f'fill="#1a1a1a">{label}</text>')
    s.append('<text x="460" y="836" text-anchor="middle" font-size="11.5" fill="#555">'
             'Rings above the anchor are ordinal thresholds (GDM performance levels; '
             'collective rings from Genewein et al. 2026), not a linear scale.</text>')
    s.append('<text x="460" y="854" text-anchor="middle" font-size="11.5" fill="#555">'
             'Axes ordered by mid-2026 value, highest at 12 o’clock, clockwise. '
             'Note Reasoning (static) vs Reasoning (dynamic).</text>')
    s.append("</svg>")

    with open(out_svg, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(s) + "\n")
    print(f"wrote {out_svg} ({n} axes)")


if __name__ == "__main__":
    main()
