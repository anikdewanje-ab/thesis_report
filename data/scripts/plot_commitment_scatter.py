"""Plan revisions against delivery, one point per agentic novel run.

The banded table in the results chapter gives five aggregate rows. This figure
gives the 150 runs behind them, so the spread inside each band is visible: runs
at the revision floor sit on full delivery, and the six-or-more band scatters
down the whole range.

Sources, and why there are two of them:

- Residents delivered comes from thesis-pack/11-results/data/scores.jsonl
  (field `sheltered_residents`, capped at the feasibility ceiling).
- Plan revisions are not in the pack. v2.json carries only the five aggregate
  bands. They are derived from the event log in the running Postgres container
  by counting `event_received` rows whose `msg_type` is one of
  PLAN_REVISION_MESSAGE_TYPES, the rule in
  evaluation/v2/thresholds_v2.py of the RescueSim repository, applied in
  facts_v2.py. Banding the result reproduces the published counts exactly
  (61 / 22 / 15 / 11 / 41), which is the check this script enforces.

The database is needed once. The script writes data/commitment_per_run.csv and
plots from it, so later rebuilds need no container.

Run from the thesis_report directory:
    python data/scripts/plot_commitment_scatter.py
"""

import collections
import csv
import json
import os
import random
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import thesis_style as ts  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
SCORES = os.path.join(ROOT, "thesis-pack", "11-results", "data", "scores.jsonl")
CSV_OUT = os.path.join(ROOT, "data", "commitment_per_run.csv")
PDF_OUT = os.path.join(ROOT, "pics", "results-commitment-scatter.pdf")

CONTAINER = "rescuesim-postgres"
PLAN_REVISION_MESSAGE_TYPES = ("transport_plan", "dispatch_buses")

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
# The published banding, evaluation/v2 -> v2.json "commitment_bands".
EXPECTED_BANDS = {"2": 61, "3": 22, "4": 15, "5": 11, "6+": 41}


def read_scores():
    out = {}
    with open(SCORES, encoding="utf-8") as fh:
        for line in fh:
            r = json.loads(line)
            if r["system"] != "agentic" or r["scenario"] not in NOVEL:
                continue
            if r["model"] not in FULL_MODELS:
                continue
            out[r["run_id"]] = {
                "model": FULL_MODELS[r["model"]],
                "disruption": r["scenario"].replace("agentic_", ""),
                "delivered": min(r["sheltered_residents"], CEILING),
                "completeness": r["completeness"],
            }
    return out


def plan_revisions_from_db(run_ids):
    """Count plan-revision messages per run, straight out of the event log."""
    quoted = ",".join("'" + r + "'" for r in run_ids)
    types = ",".join("'" + t + "'" for t in PLAN_REVISION_MESSAGE_TYPES)
    sql = (
        "SELECT run_id, count(*) FILTER (WHERE kind='event_received' "
        "AND details->>'msg_type' IN (%s)) FROM event_log "
        "WHERE run_id IN (%s) GROUP BY run_id;" % (types, quoted)
    )
    proc = subprocess.run(
        ["docker", "exec", CONTAINER, "psql", "-U", "rescuesim", "-d", "rescuesim",
         "-t", "-A", "-F", "|", "-c", sql],
        capture_output=True, text=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "psql failed")
    out = {}
    for line in proc.stdout.splitlines():
        if "|" not in line:
            continue
        run_id, n = line.split("|", 1)
        out[run_id.strip()] = int(n.strip())
    return out


def band_of(revisions):
    return "6+" if revisions >= 6 else str(revisions)


def load_or_build():
    """Prefer the database; fall back to the CSV a previous run wrote."""
    scores = read_scores()
    try:
        revs = plan_revisions_from_db(sorted(scores))
        source = "event log"
    except Exception as exc:  # container down, docker missing, anything
        if not os.path.exists(CSV_OUT):
            raise SystemExit(
                "no database (%s) and no %s to fall back on" % (exc, CSV_OUT)
            )
        print("database unavailable (%s); plotting from %s" % (exc, CSV_OUT))
        rows = list(csv.DictReader(open(CSV_OUT, encoding="utf-8")))
        return [
            {
                "run_id": r["run_id"], "model": r["model"],
                "disruption": r["disruption"],
                "plan_revisions": int(r["plan_revisions"]),
                "delivered": int(r["delivered"]),
                "completeness": float(r["completeness"]),
            }
            for r in rows
        ], "CSV"

    rows = []
    for run_id, s in scores.items():
        if run_id not in revs:
            raise SystemExit("run %s has no event-log rows" % run_id)
        rows.append(dict(run_id=run_id, plan_revisions=revs[run_id], **s))
    rows.sort(key=lambda r: (r["model"], r["disruption"], r["run_id"]))
    with open(CSV_OUT, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["run_id", "model", "disruption", "plan_revisions",
                    "delivered", "completeness"])
        for r in rows:
            w.writerow([r["run_id"], r["model"], r["disruption"],
                        r["plan_revisions"], r["delivered"], r["completeness"]])
    print("wrote", CSV_OUT)
    return rows, source


def main():
    rows, source = load_or_build()
    if len(rows) != 150:
        raise SystemExit("expected 150 agentic novel runs, found %d" % len(rows))

    bands = collections.Counter(band_of(r["plan_revisions"]) for r in rows)
    if dict(bands) != EXPECTED_BANDS:
        raise SystemExit(
            "banding does not match the published counts.\n  got      %r\n  expected %r"
            % (dict(bands), EXPECTED_BANDS)
        )
    print("source: %s; banding matches the published counts" % source)

    order = ["2", "3", "4", "5", "6+"]
    xof = {b: i for i, b in enumerate(order)}

    ts.apply()
    fig, ax = plt.subplots(figsize=(ts.TEXTWIDTH_IN, 3.4))

    ax.axhline(CEILING, color="#bbbbbb", lw=0.8, zorder=1)

    rnd = random.Random(20260922)  # fixed, so the jitter is reproducible
    for m in ts.MODEL_ORDER:
        pts = [r for r in rows if r["model"] == m]
        xs = [xof[band_of(r["plan_revisions"])] + rnd.uniform(-0.26, 0.26) for r in pts]
        # No vertical jitter: 100 is the ceiling, and nudging points past it
        # would draw deliveries that cannot happen.
        ys = [r["delivered"] for r in pts]
        ax.scatter(
            xs, ys, s=15, color=ts.MODEL_COLOR[m], edgecolor="#333333",
            linewidth=0.3, alpha=0.85, label=m, zorder=3,
        )

    # Full-delivery rate per band, printed where the reader is already looking.
    for b in order:
        inband = [r for r in rows if band_of(r["plan_revisions"]) == b]
        rate = sum(1 for r in inband if r["delivered"] >= CEILING) / len(inband)
        ax.annotate(
            "%d%%" % round(rate * 100),
            xy=(xof[b], 118), ha="center", va="center",
            fontsize=8.5, color="#333333",
        )
        ax.annotate(
            "n=%d" % len(inband),
            xy=(xof[b], 109), ha="center", va="center",
            fontsize=7.5, color="#777777",
        )

    ax.set_xticks(range(len(order)))
    ax.set_xticklabels(["2\n(the minimum)", "3", "4", "5", "6 or more"])
    ax.set_xlim(-0.5, len(order) - 0.5)
    ax.set_ylim(-8, 132)
    ax.set_yticks([0, 25, 50, 75, 100])
    ax.set_xlabel("Plan revisions in the run")
    ax.set_ylabel("Residents delivered")
    ax.yaxis.grid(True, zorder=0)
    ax.set_axisbelow(True)
    ax.legend(loc="lower left", bbox_to_anchor=(0.0, -0.02), ncol=3,
              handletextpad=0.2, columnspacing=1.2, scatterpoints=1)

    ts.save(fig, PDF_OUT)


if __name__ == "__main__":
    main()
