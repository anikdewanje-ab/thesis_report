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
```

Each script writes its CSV into `data/` and its figure into `../pics/`. Set
`THESIS_FIG_PNG` to a directory to also get a PNG preview; the thesis always
includes the PDF.

| Script | Figure | CSV | Source |
| --- | --- | --- | --- |
| `plot_forest_rd.py` | `pics/results-forest-rd.pdf` | `novel_risk_differences.csv` | `summary.md` reporting template, checked against `RESULTS.md` §2 |
| `plot_delivery_histogram.py` | `pics/results-delivery-histogram.pdf` | `delivery_distribution.csv` | `scores.jsonl`, field `sheltered_residents` |

`scripts/thesis_style.py` holds the shared look: Times serif at 9 pt, the
160 mm text width, and one model palette separated by lightness as well as hue
so the figures still read in black and white. Import it from any new script
rather than restyling by hand.

Both scripts assert their own provenance. `plot_delivery_histogram.py` stops if
it does not find exactly 150 agentic novel runs, and `plot_forest_rd.py` stops
if any of the 15 cells is missing from the summary table. A silent change in
the pack therefore fails loudly instead of redrawing a wrong figure.
