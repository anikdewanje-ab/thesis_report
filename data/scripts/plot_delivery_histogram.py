"""Distribution of residents delivered, over the 150 agentic novel runs.

The point of the figure: the loss is quantised. It clusters on a few discrete
values instead of spreading smoothly, which is what a system losing whole
committed legs produces and what a system degrading under load does not.

Source: thesis-pack/11-results/data/scores.jsonl, field `sheltered_residents`,
restricted to the agentic runs on the five novel disruptions from the three
models that completed a full arm. Reproduces the counts in
thesis-pack/09-method/EVALUATION_PROTOCOL_V2.md sec. 11.4: of 150 runs, 102
delivered everyone, 19 delivered exactly 50, 18 delivered exactly 90, 2
delivered none.

Six runs report more arrivals than the feasibility ceiling admits (RESULTS
sec. 6.2). They are folded into the "100 or more" column here, exactly as the
survival tables cap them at 1.0.

Writes data/delivery_distribution.csv and pics/results-delivery-histogram.pdf.

Run from the thesis_report directory:
    python data/scripts/plot_delivery_histogram.py
"""

import collections
import csv
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import thesis_style as ts  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
SCORES = os.path.join(ROOT, "thesis-pack", "11-results", "data", "scores.jsonl")
CSV_OUT = os.path.join(ROOT, "data", "delivery_distribution.csv")
PDF_OUT = os.path.join(ROOT, "pics", "results-delivery-histogram.pdf")

NOVEL = {
    "agentic_medical_emergency_in_flight",
    "agentic_unverified_persons_report",
    "agentic_conflicting_evacuation_orders",
    "agentic_bus1_suspension_capacity_reduction",
    "agentic_sc1_partial_capacity_loss",
}
FULL_MODELS = {
    "qwen3.5:cloud": "qwen3.5",
    "glm-5.2:cloud": "glm-5.2",
    "deepseek-v4-pro:0813-cloud": "deepseek-v4-pro",
}
CEILING = 100


def read_counts():
    counts = collections.defaultdict(collections.Counter)
    n = 0
    with open(SCORES, encoding="utf-8") as fh:
        for line in fh:
            r = json.loads(line)
            if r["system"] != "agentic" or r["scenario"] not in NOVEL:
                continue
            if r["model"] not in FULL_MODELS:
                continue
            delivered = min(r["sheltered_residents"], CEILING)
            counts[delivered][FULL_MODELS[r["model"]]] += 1
            n += 1
    return counts, n


def write_csv(counts):
    with open(CSV_OUT, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["residents_delivered"] + ts.MODEL_ORDER + ["total"])
        for d in sorted(counts):
            row = [counts[d][m] for m in ts.MODEL_ORDER]
            w.writerow([d] + row + [sum(row)])
    print("wrote", CSV_OUT)


def main():
    counts, n = read_counts()
    if n != 150:
        raise SystemExit("expected 150 agentic novel runs, found %d" % n)
    write_csv(counts)

    ts.apply()
    fig, ax = plt.subplots(figsize=(ts.TEXTWIDTH_IN, 3.2))

    xs = sorted(counts)
    width = 4.0
    bottoms = collections.defaultdict(float)
    for m in ts.MODEL_ORDER:
        heights = [counts[x][m] for x in xs]
        ax.bar(
            xs,
            heights,
            width=width,
            bottom=[bottoms[x] for x in xs],
            color=ts.MODEL_COLOR[m],
            edgecolor="#333333",
            linewidth=0.4,
            label=m,
            zorder=2,
        )
        for x, h in zip(xs, heights):
            bottoms[x] += h

    for x in xs:
        total = sum(counts[x].values())
        ax.annotate(
            str(total),
            xy=(x, total + 2),
            ha="center",
            va="bottom",
            fontsize=7.5,
            color="#333333",
        )

    ax.set_xlim(-6, 110)
    ax.set_xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    ax.set_xticklabels(
        ["0", "10", "20", "30", "40", "50", "60", "70", "80", "90", "100+"]
    )
    ax.set_ylim(0, 128)
    ax.set_yticks([0, 25, 50, 75, 100])
    ax.set_xlabel("Residents delivered to a shelter, out of 100")
    ax.set_ylabel("Runs")
    ax.yaxis.grid(True, zorder=0)
    ax.set_axisbelow(True)

    # The two spikes that carry the argument.
    ax.annotate(
        "one whole\nbus-load short",
        xy=(50, 27),
        fontsize=7.5,
        color="#555555",
        ha="center",
        va="bottom",
    )
    ax.annotate(
        "everyone\ndelivered",
        xy=(100, 111),
        fontsize=7.5,
        color="#555555",
        ha="center",
        va="bottom",
    )

    ax.legend(
        loc="upper left",
        bbox_to_anchor=(0.02, 1.0),
        ncol=1,
        handletextpad=0.5,
        handlelength=1.2,
    )

    ts.save(fig, PDF_OUT)


if __name__ == "__main__":
    main()
