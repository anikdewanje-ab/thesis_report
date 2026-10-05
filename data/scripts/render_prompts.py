"""Render the Bus-Driver-1 system prompt for the Agent Prompts appendix.

Uses the RescueSim repo's own bootstrap and render code, so the addressbook and
message types come out as the model saw them. Refuses to run if the prompt
sources differ from the campaign tag. Read-only on the repo.

    python data/scripts/render_prompts.py
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

REPO = Path(r"e:/Anik/rescue-sim-thesis/RescuemateEvacuationWithAgents")
TAG = "prereg-amendment-1"
SOURCES = [
    "agentic/bus_driver/prompts.py",
    "agentic/bus_driver/agent.py",
    "agentic/bus_driver/identity.yaml",
]
OUT = Path(__file__).resolve().parent.parent / "prompts"

# The inform_escort entry in the contract continues on lines indented by 78
# spaces, which wrap into a zigzag on the page. Only the indent is shortened;
# the appendix text says so. Every other character is left as rendered.
DEEP_INDENT = re.compile(r"^ {40,}", re.MULTILINE)
PAGE_INDENT = 6


def main() -> None:
    diff = subprocess.run(
        ["git", "diff", "--quiet", TAG, "HEAD", "--", *SOURCES], cwd=REPO
    )
    if diff.returncode != 0:
        sys.exit(f"prompt sources differ from {TAG}; check out the tag first")
    commit = subprocess.run(
        ["git", "rev-parse", "--short", f"{TAG}^{{commit}}"],
        cwd=REPO, capture_output=True, text=True, check=True,
    ).stdout.strip()

    sys.path.insert(0, str(REPO))
    from shared import geocode

    # The home address only sets state.location, which the system prompt
    # never shows, so a fixed point avoids the network call.
    geocode.lookup = lambda _addr: (53.583, 9.933)

    from agentic.bus_driver import agent, prompts

    state = agent.bootstrap_state(REPO / "agentic/bus_driver/identity.yaml")
    system = prompts.render_system(state, None)

    i_contract = system.index("REASONING LOOP")
    i_playbook = system.index("THIS WAKE")
    parts = {
        "bus_driver_persona.txt": system[:i_contract],
        "bus_driver_contract.txt": system[i_contract:i_playbook],
        "bus_driver_playbook_message.txt": system[i_playbook:],
    }
    for name, text in parts.items():
        text = DEEP_INDENT.sub(" " * PAGE_INDENT, text)
        (OUT / name).write_text(text.strip("\n") + "\n", encoding="utf-8")

    print(f"rendered from {TAG} ({commit}): {', '.join(parts)}")


if __name__ == "__main__":
    main()
