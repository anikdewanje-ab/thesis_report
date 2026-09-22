"""Shared matplotlib style for every figure in the thesis.

Keeps the figures looking like the document: Times serif, 9 pt, no chart junk,
vector PDF output at the 160 mm text width. Import this before plotting.
"""

import os
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# 160 mm text width, in inches.
TEXTWIDTH_IN = 160.0 / 25.4

# Model palette. Ordered best to worst on mean survival, and separated by
# lightness as well as hue so the figures survive a black-and-white printer.
MODEL_COLOR = {
    "qwen3.5": "#1f3b5c",
    "glm-5.2": "#6f9ac4",
    "deepseek-v4-pro": "#9fb6cb",
}
MODEL_ORDER = ["qwen3.5", "glm-5.2", "deepseek-v4-pro"]
MODEL_MARKER = {"qwen3.5": "o", "glm-5.2": "s", "deepseek-v4-pro": "^"}

# Readable short labels for the five novel disruptions.
DISRUPTION_LABEL = {
    "conflicting_evacuation_orders": "Conflicting\nevacuation orders",
    "medical_emergency_in_flight": "Medical emergency\nin flight",
    "bus1_suspension_capacity_reduction": "Bus-1 suspension,\ncapacity reduction",
    "unverified_persons_report": "Unverified\npersons report",
    "sc1_partial_capacity_loss": "SC1 partial\ncapacity loss",
}


def apply():
    plt.rcParams.update(
        {
            "font.family": "serif",
            "font.serif": ["Times New Roman", "Nimbus Roman", "DejaVu Serif"],
            "mathtext.fontset": "stix",
            "font.size": 9,
            "axes.labelsize": 9,
            "axes.titlesize": 9,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
            "legend.fontsize": 8,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.linewidth": 0.6,
            "xtick.major.width": 0.6,
            "ytick.major.width": 0.6,
            "xtick.direction": "out",
            "ytick.direction": "out",
            "lines.linewidth": 1.0,
            "grid.linewidth": 0.4,
            "grid.color": "#cccccc",
            "legend.frameon": False,
            "figure.dpi": 200,
            "savefig.bbox": "tight",
            "savefig.pad_inches": 0.02,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )


def save(fig, path):
    # Drop the PDF creation timestamp. Without this every re-run produces a
    # byte-different file with identical content, so git reports the figures as
    # modified whenever a script is run.
    fig.savefig(path, metadata={"CreationDate": None})
    print("wrote", path)
    # Set THESIS_FIG_PNG to a directory to also drop a raster preview there.
    # Handy for eyeballing a figure without opening the PDF. Never used by the
    # build; the thesis always includes the PDF.
    preview_dir = os.environ.get("THESIS_FIG_PNG")
    if preview_dir:
        name = os.path.splitext(os.path.basename(path))[0] + ".png"
        out = os.path.join(preview_dir, name)
        fig.savefig(out, dpi=180)
        print("preview", out)
