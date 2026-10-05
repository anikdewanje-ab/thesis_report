# Data

Evaluation data and the scripts that turn it into figures for the thesis.

Keep raw results (CSV or JSON) and the plotting scripts here so every figure in
the thesis can be reproduced, not just pasted as an image. Save generated
figures into `../pics/`.

Layout:

- `scripts/`  — Python scripts (matplotlib) that build the figures.
- `*.csv`     — the exact numbers each figure plots, written by its script, so
  a value can be checked without running anything.

The raw evaluation output is not copied here. The scripts read it from
`../thesis-pack/11-results/data/`, which is the pack's copy of
`evaluation/results/` and the only copy outside the machine that produced it.
Back that directory up. If the pack is ever rebuilt, re-run the scripts.

## Building the figures

Run from the `thesis_report` directory, not from here:

```sh
python data/scripts/plot_forest_rd.py
python data/scripts/plot_delivery_histogram.py
python data/scripts/plot_regret.py
```

Each script writes its CSV into `data/` and its figure into `../pics/`. Set
`THESIS_FIG_PNG` to a directory to also get a PNG preview; the thesis always
includes the PDF.

| Script | Figure | CSV | Source |
| --- | --- | --- | --- |
| `plot_forest_rd.py` | `pics/results-forest-rd.pdf` | `novel_risk_differences.csv` | `summary.md` reporting template, checked against `RESULTS.md` §2 |
| `plot_delivery_histogram.py` | `pics/results-delivery-histogram.pdf` | `delivery_distribution.csv` | `scores.jsonl`, field `sheltered_residents` |
| `plot_rubric_split.py` | `pics/results-rubric-split.pdf` | `rubric_split.csv` | `RESULTS.md` §4, parsed |
| `plot_commitment_scatter.py` | `pics/results-commitment-scatter.pdf` | `commitment_per_run.csv` | `scores.jsonl` **plus the event log**, see below |

### The one script that needs the database

`plot_commitment_scatter.py` is the exception to "everything comes from the
pack". Per-run plan revisions are not in `thesis-pack/`: `v2.json` carries only
the five aggregate bands. They are counted from the event log in the running
Postgres container, using the rule in `evaluation/v2/thresholds_v2.py`
(`PLAN_REVISION_MESSAGE_TYPES`) of the RescueSim repository.

Start the container first, from the RescueSim repo:

```sh
docker compose up -d
```

The script then writes `commitment_per_run.csv` and plots from it. Later
rebuilds fall back to that CSV automatically and print that they did, so the
figure stays reproducible once the container is gone.

It refuses to plot unless banding the result reproduces the published counts
(61 / 22 / 15 / 11 / 41), which is how a silent change in the event log or in
the counting rule gets caught.
| `plot_regret.py` | `pics/critique-regret.pdf` | `null_policy_regret.csv` | `v2.json`, key `regret` (exploratory, Protocol v2) |

`scripts/thesis_style.py` holds the shared look: Times serif at 9 pt, the
160 mm text width, and one model palette separated by lightness as well as hue
so the figures still read in black and white. Import it from any new script
rather than restyling by hand.

Each script asserts its own provenance. `plot_delivery_histogram.py` stops if
it does not find exactly 150 agentic novel runs, and `plot_forest_rd.py` stops
if any of the 15 cells is missing from the summary table. `plot_regret.py` stops
if the helped / neutral / harmed totals differ from `EVALUATION_PROTOCOL_V2.md` §11.1 after
`S` is capped at 1.0, which moves qwen3.5's three over-ceiling runs from helped to neutral. A silent change in
the pack therefore fails loudly instead of redrawing a wrong figure.

## The agent prompts (Appendix C)

`scripts/render_prompts.py` writes the Bus-Driver-1 system prompt into
`prompts/` as three files: `bus_driver_persona.txt`, `bus_driver_contract.txt`
and `bus_driver_playbook_message.txt`. It imports the RescueSim repo's own
`bootstrap_state` and `render_system`, so the addressbook and message types come
out as the model saw them. It stops unless the prompt sources in the repo match
tag `prereg-amendment-1` (commit `7a4d7cc`). The only edit is a shorter indent
on the deeply indented `inform_escort` lines, which the appendix discloses.
Never edit the `.txt` files by hand; re-run the script.
