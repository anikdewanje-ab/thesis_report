"""The sixteen held-out rubric criteria, grouped by how the two sides compare.

The results chapter tabulates the same sixteen criteria as a grid of numbers.
This figure puts them in reading order, so the split the prose describes is
visible without scanning four columns per row.

Grouping rule, and the reason it stops where it does. RESULTS.md section 4
names three groups and calls out a fourth case, which together cover 14 of the
16 criteria. It never classifies `verification_requested` or
`reserve_committed_in_time`, so those two are drawn in their own group and
labelled as unclassified rather than pushed into a band the source does not
give them.

The four groups drawn here are defined mechanically, so the figure can be
checked against the table:

  parity          the agentic models that RESULTS calls level match 10/10
  baseline ahead  the baseline scores above every agentic model
  baseline at 0   the baseline itself scores 0, so the criterion says more
                  about the scenario than about either architecture
  unclassified    everything the source leaves unplaced

Source: thesis-pack/00-start-here/RESULTS.md section 4, parsed rather than
retyped. Writes data/rubric_split.csv and pics/results-rubric-split.pdf.

Run from the thesis_report directory:
    python data/scripts/plot_rubric_split.py
"""

import csv
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import thesis_style as ts  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
RESULTS = os.path.join(ROOT, "thesis-pack", "00-start-here", "RESULTS.md")
CSV_OUT = os.path.join(ROOT, "data", "rubric_split.csv")
PDF_OUT = os.path.join(ROOT, "pics", "results-rubric-split.pdf")

# The two the source never places. Named here so the figure fails loudly if
# RESULTS is ever revised to classify them.
UNCLASSIFIED = ("verification_requested", "reserve_committed_in_time")

GROUPS = [
    ("parity", "Parity with the baseline"),
    ("baseline", "Baseline ahead"),
    ("zero", "Baseline scores 0 as well"),
    ("unclassified", "Not classified in the source"),
]

SHORT_DISRUPTION = {
    "bus1_suspension": "bus1",
    "conflicting_orders": "conflicting",
    "medical_emergency": "medical",
    "unverified_persons": "unverified",
    "sc1_capacity_loss": "sc1",
}


def parse_rubric():
    text = io.open(RESULTS, encoding="utf-8").read()
    seg = text.split("**Held-out decision rubric**")[1].split("Read across all sixteen")[0]
    rows, disruption = [], None
    for line in seg.split("\n"):
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip().strip("*").replace("`", "") for c in line.strip().strip("|").split("|")]
        if len(cells) != 6 or cells[1] in ("criterion", "---"):
            continue
        if set(cells[1]) <= set("- "):
            continue
        if cells[0]:
            disruption = cells[0]
        try:
            vals = [int(x) for x in cells[2:6]]
        except ValueError:
            continue
        rows.append({
            "disruption": disruption, "criterion": cells[1],
            "baseline": vals[0], "qwen3.5": vals[1],
            "glm-5.2": vals[2], "deepseek-v4-pro": vals[3],
        })
    return rows


# The grouping is RESULTS.md section 4's own, taken from its prose, because it
# is editorial rather than mechanical: `authority_informed` is called parity at
# 10 / 10 / 9, and `full_evacuation_kept` is called a baseline win at
# 10 / 9 / 10. A rule derived from the numbers alone reproduces neither, so the
# source's calls are listed here and the remainder is left unclassified.
PARITY = (                      # "Parity, on five criteria."
    "authority_informed",       # named for both disruptions, so two rows
    "reserve_committed",
    "whole_population_planned",
    "stood_down_after_retraction",
)
BASELINE_AHEAD = (              # "The baseline wins on five."
    "facility_answered_in_time",
    "no_order_raises_shelter_above_beds",
    "facility_runs_untouched",
    "in_flight_leg_lands_where_ordered",
    "full_evacuation_kept",
)
ZERO = (                        # "Three criteria indict the scenario", plus
    "bus_load_within_cap",      # shelter_set_down_within_beds, which the same
    "medic_sent_to_the_bus_destination",   # paragraph calls out as a place the
    "everyone_bedded_at_the_reduced_capacity",  # agentic side beats the
    "shelter_set_down_within_beds",              # baseline. All four sit at 0.
)


def classify(r):
    if r["criterion"] in PARITY:
        return "parity"
    if r["criterion"] in BASELINE_AHEAD:
        return "baseline"
    if r["criterion"] in ZERO:
        return "zero"
    return "unclassified"


def main():
    rows = parse_rubric()
    if len(rows) != 16:
        raise SystemExit("expected 16 rubric criteria, parsed %d" % len(rows))
    for r in rows:
        r["group"] = classify(r)

    counts = {g: sum(1 for r in rows if r["group"] == g) for g, _ in GROUPS}
    expected = {"parity": 5, "baseline": 5, "zero": 4, "unclassified": 2}
    if counts != expected:
        raise SystemExit("grouping changed.\n  got      %r\n  expected %r" % (counts, expected))
    left = sorted(r["criterion"] for r in rows if r["group"] == "unclassified")
    if tuple(left) != tuple(sorted(UNCLASSIFIED)):
        raise SystemExit("the source now places %r; revisit the grouping" % (left,))
    if any(r["baseline"] != 0 for r in rows if r["group"] == "zero"):
        raise SystemExit("a criterion grouped under a zero baseline is not zero")

    with open(CSV_OUT, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["group", "disruption", "criterion", "baseline",
                    "qwen3.5", "glm-5.2", "deepseek-v4-pro"])
        for g, _ in GROUPS:
            for r in [x for x in rows if x["group"] == g]:
                w.writerow([g, r["disruption"], r["criterion"], r["baseline"],
                            r["qwen3.5"], r["glm-5.2"], r["deepseek-v4-pro"]])
    print("wrote", CSV_OUT)

    ts.apply()
    fig, ax = plt.subplots(figsize=(ts.TEXTWIDTH_IN, 5.0))

    y, ylabels, seps, headers = [], [], [], []
    pos = 0.0
    for gi, (g, title) in enumerate(GROUPS):
        members = [r for r in rows if r["group"] == g]
        headers.append((pos + 0.9, title, len(members)))
        for r in members:
            y.append((r, pos))
            d = SHORT_DISRUPTION.get(r["disruption"], r["disruption"])
            ylabels.append((pos, "%s  (%s)" % (r["criterion"], d)))
            pos -= 1.0
        if gi < len(GROUPS) - 1:
            seps.append(pos + 0.5)
            pos -= 1.0

    for r, p in y:
        ax.plot([0, 10], [p, p], color="#eeeeee", lw=0.8, zorder=0)
        ax.plot(r["baseline"], p, marker="|", markersize=11, color="#333333",
                markeredgewidth=1.6, zorder=4,
                label="baseline" if p == 0 else None)
        # Nudge each model onto its own line within the row. y is categorical,
        # so this costs no accuracy and keeps shared values readable, which
        # matters most in the parity group where everything sits on 10.
        for oi, m in enumerate(ts.MODEL_ORDER):
            ax.plot(r[m], p + (oi - 1) * 0.19, marker=ts.MODEL_MARKER[m], markersize=4.6,
                    color=ts.MODEL_COLOR[m], markeredgecolor="#333333",
                    markeredgewidth=0.4, zorder=3,
                    label=m if p == 0 else None)

    for s in seps:
        ax.axhline(s, color="#cccccc", lw=0.6, zorder=1)
    for py, title, n in headers:
        ax.annotate("%s (%d)" % (title, n), xy=(-0.3, py), ha="left", va="center",
                    fontsize=8, color="#333333", annotation_clip=False)

    ax.set_yticks([p for p, _ in ylabels])
    ax.set_yticklabels([t for _, t in ylabels], fontsize=7)
    ax.set_ylim(pos + 0.5, 1.8)
    ax.set_xlim(-0.3, 10.6)
    ax.set_xticks(range(0, 11, 2))
    ax.set_xlabel("Runs judged “yes”, out of 10")
    ax.xaxis.grid(True, zorder=0)
    ax.set_axisbelow(True)
    ax.tick_params(axis="y", length=0)

    handles, labels = ax.get_legend_handles_labels()
    want = ["baseline"] + ts.MODEL_ORDER
    idx = [labels.index(w) for w in want if w in labels]
    ax.legend([handles[i] for i in idx], [labels[i] for i in idx],
              loc="lower right", bbox_to_anchor=(1.0, 1.0), ncol=4,
              handletextpad=0.3, columnspacing=1.3, numpoints=1)

    ts.save(fig, PDF_OUT)


if __name__ == "__main__":
    main()
