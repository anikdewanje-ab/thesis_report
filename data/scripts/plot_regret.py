"""Null-policy regret: how many runs responding helped, left level, or harmed.

The point of the figure: the baseline gained nothing by responding (every run
ties the null policy), and the agentic system tied it or did worse. No agentic run of 150 improved on
doing nothing; 68 came out worse.

Regret is R = min(S_system, 1) - S_null, on survival, per run. A run is
"helped" when R > 0, "neutral" when R = 0, and "harmed" when R < 0.

S is capped at 1.0, as everywhere in the thesis. The pack's `regret` cells use
uncapped S, so three qwen3.5 runs that shelter more residents than the
feasibility ceiling admits (S = 1.1, RESULTS sec. 6.2) count there as "helped".
The script finds every run with completeness above 1.0 in scores.jsonl and
moves it from helped to neutral.

Source: thesis-pack/11-results/data/v2.json, key `regret`, one row per
system/model/scenario cell over the five novel disruptions, plus
thesis-pack/11-results/data/scores.jsonl for the cap. Reproduces
thesis-pack/09-method/EVALUATION_PROTOCOL_V2.md sec. 11.1 with S capped at 1.0.
Exploratory: the
instrument was written after the v1 data were seen (Amendment 16).

Writes data/null_policy_regret.csv and pics/critique-regret.pdf.

Run from the thesis_report directory:
    python data/scripts/plot_regret.py
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
V2 = os.path.join(ROOT, "thesis-pack", "11-results", "data", "v2.json")
SCORES = os.path.join(ROOT, "thesis-pack", "11-results", "data", "scores.jsonl")
CSV_OUT = os.path.join(ROOT, "data", "null_policy_regret.csv")
PDF_OUT = os.path.join(ROOT, "pics", "critique-regret.pdf")

FULL_MODELS = {
    "qwen3.5:cloud": "qwen3.5",
    "glm-5.2:cloud": "glm-5.2",
    "deepseek-v4-pro:0813-cloud": "deepseek-v4-pro",
}
ROWS = ["baseline"] + ts.MODEL_ORDER
OUTCOMES = ["helped", "neutral", "harmed"]
OUTCOME_COLOR = {"helped": "#6f9ac4", "neutral": "#e3e3e3", "harmed": "#5a5a5a"}
OUTCOME_TEXT = {"helped": "white", "neutral": "#333333", "harmed": "white"}

# EVALUATION_PROTOCOL_V2 sec. 11.1, after the cap: qwen3.5's three over-ceiling
# runs move from helped to neutral. The script stops if the pack disagrees.
EXPECTED = {
    "baseline": (0, 50, 0),
    "qwen3.5": (0, 33, 17),
    "glm-5.2": (0, 34, 16),
    "deepseek-v4-pro": (0, 15, 35),
}


def read_counts():
    with open(V2, encoding="utf-8") as fh:
        cells = json.load(fh)["regret"]
    counts = collections.defaultdict(collections.Counter)
    regret_sum = collections.defaultdict(float)
    for c in cells:
        if c["system"] == "baseline":
            row = "baseline"
        elif c["model"] in FULL_MODELS:
            row = FULL_MODELS[c["model"]]
        else:
            continue
        for o in OUTCOMES:
            counts[row][o] += c[o]
        counts[row]["n"] += c["n"]
        regret_sum[row] += c["mean_regret"] * c["n"]
    null = {(c["system"], c["model"], c["scenario"]): c["null_survival"] for c in cells}
    apply_cap(counts, regret_sum, null)
    return counts, regret_sum


def apply_cap(counts, regret_sum, null):
    """Cap S at 1.0: an over-ceiling run that beat the null only by the excess
    moves from helped to neutral, and its excess leaves the regret sum."""
    with open(SCORES, encoding="utf-8") as fh:
        runs = [json.loads(line) for line in fh if line.strip()]
    for r in runs:
        if r["completeness"] <= 1.0 or r["model"] not in FULL_MODELS:
            continue
        key = (r["system"], r["model"], r["scenario"].replace("agentic_", "", 1))
        if key not in null:
            continue
        row = FULL_MODELS[r["model"]]
        regret_sum[row] -= r["completeness"] - 1.0
        if 1.0 - null[key] <= 0 < r["completeness"] - null[key]:
            counts[row]["helped"] -= 1
            counts[row]["neutral"] += 1


def check(counts):
    for row, want in EXPECTED.items():
        got = tuple(counts[row][o] for o in OUTCOMES)
        if got != want:
            raise SystemExit("%s: expected %s, found %s" % (row, want, got))


def write_csv(counts, regret_sum):
    with open(CSV_OUT, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["system_model", "n", "mean_regret"] + OUTCOMES)
        for row in ROWS:
            n = counts[row]["n"]
            w.writerow(
                [row, n, "%.3f" % (regret_sum[row] / n)]
                + [counts[row][o] for o in OUTCOMES]
            )
    print("wrote", CSV_OUT)


def main():
    counts, regret_sum = read_counts()
    check(counts)
    write_csv(counts, regret_sum)

    ts.apply()
    fig, ax = plt.subplots(figsize=(ts.TEXTWIDTH_IN, 2.1))

    ys = list(range(len(ROWS)))[::-1]
    for y, row in zip(ys, ROWS):
        left = 0
        for o in OUTCOMES:
            v = counts[row][o]
            if v:
                ax.barh(
                    y,
                    v,
                    left=left,
                    height=0.62,
                    color=OUTCOME_COLOR[o],
                    edgecolor="#333333",
                    linewidth=0.4,
                    zorder=2,
                )
                ax.text(
                    left + v / 2,
                    y,
                    str(v),
                    ha="center",
                    va="center",
                    fontsize=7.5,
                    color=OUTCOME_TEXT[o],
                    zorder=3,
                )
            left += v

    ax.set_yticks(ys)
    ax.set_yticklabels(["workflow baseline"] + ["agentic / " + m for m in ts.MODEL_ORDER])
    ax.set_xlim(0, 50)
    ax.set_xticks([0, 10, 20, 30, 40, 50])
    ax.set_xlabel("Novel-arm runs, out of 50 per row")
    ax.xaxis.grid(True, zorder=0)
    ax.set_axisbelow(True)
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", length=0)

    handles = [
        plt.Rectangle((0, 0), 1, 1, facecolor=OUTCOME_COLOR[o], edgecolor="#333333", linewidth=0.4)
        for o in OUTCOMES
    ]
    labels = [
        "helped (better than doing nothing)",
        "neutral (same as doing nothing)",
        "harmed (worse than doing nothing)",
    ]
    ax.legend(
        handles,
        labels,
        loc="upper center",
        bbox_to_anchor=(0.5, -0.32),
        ncol=3,
        handletextpad=0.5,
        handlelength=1.2,
        columnspacing=1.4,
    )

    ts.save(fig, PDF_OUT)


if __name__ == "__main__":
    main()
