"""Supplementary tables for the appendix: level counts, cut-point sensitivity,
Gate 1 with the Wilcoxon check, and the per-cell secondary measures.

Sources: thesis-pack/11-results/data/summary.md (level distribution, Gate 1
table, sensitivity table) and thesis-pack/11-results/data/scores.jsonl (bus-km,
resource efficiency, rejected messages per run). RESULTS.md is authoritative;
the level-4 counts and risk differences printed here match its sec. 2.

Writes inc/app_supp_tables.tex, which inc/appendix.tex inputs.

Run from the thesis_report directory:
    python data/scripts/supp_tables.py
"""

import collections
import json
import os
import statistics

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
DATA = os.path.join(ROOT, "thesis-pack", "11-results", "data")
SUMMARY = os.path.join(DATA, "summary.md")
SCORES = os.path.join(DATA, "scores.jsonl")
TEX_OUT = os.path.join(ROOT, "inc", "app_supp_tables.tex")

SCENARIOS = [
    ("closed_loop", "S01"),
    ("road_closure", "S02"),
    ("medical_emergency_in_flight", "S04"),
    ("unverified_persons_report", "S05"),
    ("conflicting_evacuation_orders", "S06"),
    ("bus1_suspension_capacity_reduction", "S07"),
    ("sc1_partial_capacity_loss", "S08"),
]
CODE = dict(SCENARIOS)
MODELS = [
    ("", "baseline"),
    ("qwen3.5:cloud", "qwen3.5"),
    ("glm-5.2:cloud", "glm-5.2"),
    ("deepseek-v4-pro:0813-cloud", "deepseek-v4-pro"),
    ("minimax-m3:cloud", "minimax-m3"),
    ("nemotron-3-ultra:cloud", "nemotron-3-ultra"),
    ("kimi-k3:cloud", "kimi-k3"),
    ("gpt-oss:120b-cloud", "gpt-oss"),
    ("kimi-k2.7-code:cloud", "kimi-k2.7-code"),
]
SHORT = dict(MODELS)
ORDER = {m: i for i, (m, _) in enumerate(MODELS)}


def md_table(heading):
    """Return the rows of the first markdown table after a heading line."""
    with open(SUMMARY, encoding="utf-8") as f:
        lines = f.read().splitlines()
    start = next(i for i, l in enumerate(lines) if l.strip() == heading)
    rows, header = [], None
    for l in lines[start + 1:]:
        if not l.startswith("|"):
            if header:
                break
            continue
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        if header is None:
            header = cells
        elif not set(cells[0]) <= {"-", " "}:
            rows.append(dict(zip(header, cells)))
    return rows


def scen_of(name):
    return name.split("_", 1)[1] if name.startswith(("agentic_", "baseline_")) else name


def sort_key(scen, model):
    return ([s for s, _ in SCENARIOS].index(scen), ORDER[model])


def fmt_median(x):
    return f"{float(x):.1f}"


def fmt_signed(x):
    """Two decimals, or three where the source carries a third (-0.245)."""
    v = round(float(x), 3)
    s = f"{v:.3f}"
    if s.endswith("0"):
        s = s[:-1]
    s = s.lstrip("-")
    if v == 0:
        return "0.00"
    return f"${s}$" if v > 0 else f"$-{s}$"


def median_from_counts(counts):
    """The usual median of the runs, as the protocol's reporting template prints it."""
    runs = [lvl for lvl, c in enumerate(counts) for _ in range(c)]
    return statistics.median(runs)


def levels_table():
    dist = {(scen_of(r["scenario"]), r["model"]): r for r in md_table("## Recovery-level distribution")}
    sens = {}
    for r in md_table("### Sensitivity across the cut points"):
        sens[(r["disruption"], "" if r["model"] == "none" else r["model"])] = r
    out = []
    for key in sorted(dist, key=lambda k: sort_key(*k)):
        d, s = dist[key], sens[key]
        flag = "" if s["stable"] == "True" else r"\textsuperscript{*}"
        out.append(
            f"{CODE[key[0]]} & {SHORT[key[1]]} & {d['n']} & "
            + " & ".join(d[f"level_{i}"] for i in range(5))
            + f" & {fmt_median(median_from_counts([int(d[f'level_{i}']) for i in range(5)]))} & "
            + " & ".join(fmt_median(s[f"median@{c}"]) for c in ("0.40", "0.50", "0.60"))
            + f"{flag} \\\\"
        )
    return out


def gate1_table():
    rows = md_table("## Gate 1 -- safety")
    rows.sort(key=lambda r: sort_key(r["disruption"], r["model"]))
    out = []
    for r in rows:
        p = "--" if r["wilcoxon_p"] == "None" else f"{float(r['wilcoxon_p']):.3f}"
        method = {"exact": "exact", "normal_approximation": "normal", "undetermined": "all ties"}[r["wilcoxon_method"]]
        ci = f"[{fmt_signed(r['ci_low'])}, {fmt_signed(r['ci_high'])}]"
        out.append(
            f"{CODE[r['disruption']]} & {SHORT[r['model']]} & {r['arm']} & {r['n_pairs']} & "
            f"{fmt_signed(r['rd'])} & {ci} & {p} & {method} & {r['gate1']} \\\\"
        )
    return out


def secondary_table():
    cells = collections.defaultdict(list)
    with open(SCORES, encoding="utf-8") as f:
        for line in f:
            x = json.loads(line)
            cells[(scen_of(x["scenario"]), x["model"])].append(x)
    out = []
    for key in sorted(cells, key=lambda k: sort_key(*k)):
        runs = cells[key]
        eta = [x["resource_efficiency"] for x in runs if x["resource_efficiency"] is not None]
        eta_s = f"{statistics.mean(eta):.2f}" if eta else "--"
        km = statistics.mean(x["bus_km"] for x in runs)
        rejected = sum(x["invalid_routings"] for x in runs)
        out.append(
            f"{CODE[key[0]]} & {SHORT[key[1]]} & {len(runs)} & {km:.1f} & {eta_s} & {len(eta)} & {rejected} \\\\"
        )
    return out


TEMPLATE = r"""% Generated by data/scripts/supp_tables.py. Do not edit by hand.

\begin{{table}}[htbp]
\centering
\caption[Recovery levels and cut-point sensitivity per cell]{{Recovery levels
and cut-point sensitivity per cell. The level columns count runs. The last
three columns re-read the cell's median level with the level-1/2 cut at 0.40,
0.50 and 0.60. They are read before the promotion to level 4, so a cell can
read 3 there and publish a median of 4. The median of an even number of runs
is the mean of the middle two. An asterisk marks a cell whose median
moves within the cut range.}}
\label{{tab:app:levels}}
\scriptsize
\setlength{{\tabcolsep}}{{4pt}}
\begin{{tabular}}{{llrcccccc@{{\hspace{{10pt}}}}ccc}}
\toprule
 & & & \multicolumn{{5}}{{c}}{{Runs at level}} & & \multicolumn{{3}}{{c}}{{Median at cut}} \\
\cmidrule(lr){{4-8}} \cmidrule(lr){{10-12}}
Scen. & System or model & $n$ & 0 & 1 & 2 & 3 & 4 & Median & 0.40 & 0.50 & 0.60 \\
\midrule
{levels}
\bottomrule
\end{{tabular}}
\end{{table}}

\begin{{table}}[htbp]
\centering
\caption[Gate 1 per cell with the Wilcoxon check]{{Gate~1 per cell with the
Wilcoxon signed-rank check. $RD$ is agentic minus baseline, paired by
replicate, with the 95\,\% bootstrap interval. The Wilcoxon $p$ is two-sided.
Zero differences are dropped from the test, and a cell where every pair ties
has no $p$.}}
\label{{tab:app:gate1}}
\scriptsize
\setlength{{\tabcolsep}}{{4pt}}
\begin{{tabular}}{{lllrrcrll}}
\toprule
Scen. & Model & Arm & $n$ & $RD$ & 95\,\% CI & Wilcoxon $p$ & Method & Gate~1 \\
\midrule
{gate1}
\bottomrule
\end{{tabular}}
\end{{table}}

\begin{{table}}[htbp]
\centering
\caption[Secondary measures per cell]{{Secondary measures per cell. Bus-km is
the mean over all runs. Resource efficiency $\eta = V / K$ is the mean over the
runs that drove at all, counted in the next column. Both are composed
differently in the two systems and are compared only within one system.
Rejected messages are outbound messages the runtime dropped, summed over the
cell.}}
\label{{tab:app:secondary}}
\scriptsize
\begin{{tabular}}{{llrrrrr}}
\toprule
Scen. & System or model & $n$ & Bus-km & $\eta$ & Runs with $\eta$ & Rejected messages \\
\midrule
{secondary}
\bottomrule
\end{{tabular}}
\end{{table}}
"""


def main():
    tex = TEMPLATE.format(
        levels="\n".join(levels_table()),
        gate1="\n".join(gate1_table()),
        secondary="\n".join(secondary_table()),
    )
    with open(TEX_OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(tex)
    print(f"wrote {TEX_OUT}")


if __name__ == "__main__":
    main()
