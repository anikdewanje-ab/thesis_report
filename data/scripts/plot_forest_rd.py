"""Forest plot of the 15 novel-arm risk differences.

Source: thesis-pack/11-results/data/summary.md, the generated reporting-template
table (protocol sec. 14). Every value was checked against
thesis-pack/00-start-here/RESULTS.md sec. 2, which is authoritative.

Writes data/novel_risk_differences.csv so the plotted numbers can be read
without running the script, and pics/results-forest-rd.pdf.

Run from the thesis_report directory:
    python data/scripts/plot_forest_rd.py
"""

import csv
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import thesis_style as ts  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
SUMMARY = os.path.join(ROOT, "thesis-pack", "11-results", "data", "summary.md")
CSV_OUT = os.path.join(ROOT, "data", "novel_risk_differences.csv")
PDF_OUT = os.path.join(ROOT, "pics", "results-forest-rd.pdf")

NOVEL = [
    "conflicting_evacuation_orders",
    "medical_emergency_in_flight",
    "bus1_suspension_capacity_reduction",
    "unverified_persons_report",
    "sc1_partial_capacity_loss",
]
FULL_MODELS = {
    "qwen3.5:cloud": "qwen3.5",
    "glm-5.2:cloud": "glm-5.2",
    "deepseek-v4-pro:0813-cloud": "deepseek-v4-pro",
}


def read_cells():
    """Pull the (disruption, model, rd, lo, hi) rows out of summary.md."""
    cells = {}
    with open(SUMMARY, encoding="utf-8") as fh:
        for line in fh:
            if not line.startswith("| "):
                continue
            col = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(col) < 10:
                continue
            disruption, system, model = col[0], col[1], col[2]
            if system != "agentic" or disruption not in NOVEL:
                continue
            if model not in FULL_MODELS:
                continue
            rd, ci = col[8], col[9]
            m = re.match(r"\[\s*(-?[\d.]+)\s*,\s*(-?[\d.]+)\s*\]", ci)
            if not m:
                continue
            cells[(disruption, FULL_MODELS[model])] = (
                float(rd),
                float(m.group(1)),
                float(m.group(2)),
            )
    return cells


def write_csv(cells):
    with open(CSV_OUT, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["disruption", "model", "risk_difference", "ci_low", "ci_high"])
        for d in NOVEL:
            for m in ts.MODEL_ORDER:
                rd, lo, hi = cells[(d, m)]
                w.writerow([d, m, rd, lo, hi])
    print("wrote", CSV_OUT)


def main():
    cells = read_cells()
    missing = [(d, m) for d in NOVEL for m in ts.MODEL_ORDER if (d, m) not in cells]
    if missing:
        raise SystemExit("missing cells in summary.md: %r" % (missing,))
    write_csv(cells)

    ts.apply()
    fig, ax = plt.subplots(figsize=(ts.TEXTWIDTH_IN, 3.9))

    # One block of three model rows per disruption, top to bottom in the order
    # the results chapter lists them.
    row_gap, block_gap = 1.0, 1.0
    y, yticks, ylabels = [], [], []
    pos = 0.0
    for d in NOVEL:
        block = []
        for m in ts.MODEL_ORDER:
            block.append(pos)
            y.append((d, m, pos))
            pos -= row_gap
        yticks.append(sum(block) / len(block))
        ylabels.append(ts.DISRUPTION_LABEL[d])
        pos -= block_gap

    ax.axvline(0.0, color="#333333", lw=0.9, zorder=1)

    seen = set()
    for d, m, p in y:
        rd, lo, hi = cells[(d, m)]
        c = ts.MODEL_COLOR[m]
        ax.plot([lo, hi], [p, p], color=c, lw=1.6, solid_capstyle="butt", zorder=2)
        for x in (lo, hi):
            ax.plot([x, x], [p - 0.14, p + 0.14], color=c, lw=1.0, zorder=2)
        ax.plot(
            rd,
            p,
            ts.MODEL_MARKER[m],
            color=c,
            markersize=4.5,
            markeredgecolor="#333333",
            markeredgewidth=0.5,
            zorder=3,
            label=m if m not in seen else None,
        )
        seen.add(m)

    ax.set_yticks(yticks)
    ax.set_yticklabels(ylabels)
    ax.set_ylim(pos + block_gap - 0.4, 0.8)
    ax.set_xlim(-0.62, 0.12)
    ax.set_xticks([-0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1])
    ax.set_xlabel(
        "Risk difference in survival, agentic minus baseline "
        "(positive favours the agentic system)"
    )
    ax.xaxis.grid(True, zorder=0)
    ax.set_axisbelow(True)
    ax.tick_params(axis="y", length=0)

    # The region a superiority result would have had to reach. No interval
    # enters it, which is the whole point of the figure.
    ax.axvspan(0.0, 0.12, color="#f0f0f0", zorder=0)
    ax.annotate(
        "superiority region",
        xy=(0.06, 0.55),
        xycoords=("data", "axes fraction"),
        ha="center",
        va="center",
        rotation=90,
        fontsize=7.5,
        color="#777777",
    )

    handles, labels = ax.get_legend_handles_labels()
    order = [labels.index(m) for m in ts.MODEL_ORDER if m in labels]
    ax.legend(
        [handles[i] for i in order],
        [labels[i] for i in order],
        loc="upper left",
        bbox_to_anchor=(0.0, 1.13),
        ncol=3,
        handletextpad=0.4,
        columnspacing=1.6,
    )

    ts.save(fig, PDF_OUT)


if __name__ == "__main__":
    main()
