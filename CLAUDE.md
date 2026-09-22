# Thesis Report — Working Instructions

This folder is the LaTeX writeup of Anik Dewanje's TU Ilmenau master thesis:
"Design and Evaluation of a Database-Centric Agentic Architecture for Nursing
Home Evacuation Coordination in Storm Surge Scenarios".

## Writing style (important)

- The author writes at a **B2 English level**. Match it. Use plain, common words.
- Keep the language **humanized and natural**, not dense or overly academic.
- Keep sentences short. Break long sentences into two.
- **Avoid the "—" dash.** Do not use it as a connector. Prefer commas, full
  stops, or separate sentences. Normal hyphens inside words (e.g. "database-centric")
  are fine.
- Write in a consistent voice across chapters. Prefer present tense for
  describing the system, past tense for describing what was done in evaluation.

## Ground truth

- `thesis-pack/` is the source of truth. It was built on 2026-09-22 from the
  RescueSim repo and is organised by thesis chapter. Read
  `thesis-pack/README.md` first, then `thesis-pack/00-start-here/`.
  - `00-start-here/RESULTS.md` — **authoritative on every number.** Where any
    other document disagrees, RESULTS wins.
  - `00-start-here/THESIS_SOURCES.md` — which doc feeds which chapter, which doc
    wins a conflict, and the open methodology items.
  - `thesis-pack/README.md` has the chapter map and the conflict table. Follow them.
- The pack is a set of **copies**. Editing a file there does not reach the repo,
  and the pack goes stale if the repo moves. Never edit in place; rebuild.
- `thesis_doc/` now holds only what the pack does not carry:
  - `rubric-bibliography.md` — the defence for each Recovery-Outcome Rubric
    design decision
  - `defence-prep.md` — living slide outline and defence notes
  - `notes/` — scratch notes, Zotero import lists, per-chapter TODOs
  - (`PROJECT_BRIEFING.md`, `CONTEXT.md` and
    `rescuesim-annotated-bibliography.md` were deleted on 2026-09-22; the pack
    carries newer copies in `01-introduction/`, `03-case-and-domain/` and
    `02-related-work/`.)
- Never invent citations or empirical results. If a fact or reference is not in
  `thesis-pack/`, ask before writing it as fact.
- Sources marked *(verify)* in the annotated bibliographies are cited from recall
  and are **not** confirmed. Do not cite them until the author has checked venue,
  volume, and pages.
- Note that most sources in `rubric-bibliography.md` are not yet in
  `bibs/litDB.bib`. Check the bib before writing a `\cite` for them.

## Framing (settled with the supervisor, 2026-09-22)

This is a **design-and-evaluation study**, not a hypothesis-confirmation study.
The motivation was to design an agentic simulation architecture, evaluate it
against an old-style scripted baseline, and report what was learned either way.
A negative answer is a result, not a failure. Never apologise for the outcome.

| | Question | Answer |
| --- | --- | --- |
| RQ1 | Can the agentic architecture beat the scripted baseline? | **No.** It also loses to a null policy. |
| RQ2 | If not, why? | A **commitment** failure, not a comprehension failure. |
| RQ3 | What must change? | Constrain commitment; test on scenarios that discriminate. |
| RQ4 | What should a designer consider? | `inc/design_considerations.tex`. |

Two claims the old skeleton made are **deleted and must not return**:
"LLM-agent coordination degrades more gracefully than pre-scripted workflows",
and the same sentence as empirical contribution 1. Both were the proposal's
expectation, written before the data existed, and both are the opposite of the
result.

State this boundary whenever RQ1 is answered: no scenario in this thesis ever
*required* adaptation, so RQ1 is answered as "did it win here", not "can it ever
win".

## The headline, so no chapter drifts from it

Both pre-registered hypotheses fail. The workflow baseline beats the
database-centric agentic system on resident survival in every disruption tested.
Gate 1 fails 26 of 27 cells. Decision quality is **split**, not at parity: over
the 16 held-out rubric criteria the agentic models match the baseline on 5 and
fall short on 5.

Two corrections from Protocol v2 that apply in every chapter:

1. Never write that the baseline "adapted", "recovered" or "replanned better".
   A controller that ignores every disruption scores the identical level, so the
   baseline's `S` = 1.000 is the null policy's score. H2's verdict is withdrawn
   **as a statement about adaptability**, and is not replaced by an agentic win.
2. The agentic deficit is a **commitment** failure, not a handshake failure.
   Handshake closure is 0.938 over 1,932 requests. The loss is dominated by
   residents never dispatched.

## Facts that were wrong in earlier drafts

- The case has **100 residents**, not 300. The "300" came from a stale code
  comment and reached earlier drafts and an earlier RESULTS. The feasibility
  ceiling is 100.
- The stack is **Ollama + a custom asyncio `AgenticEngine` + PostgreSQL**. There
  is no LangGraph and no PostgresSaver. The file-backed JSON persistence was
  retired by ADR-0005; Postgres is the single source of truth.


## How the project is organized

- `thesis-pack/` — the chapter-organised source material (read-only copies).
- `main.tex` — root document, includes each chapter from `inc/`.
- `inc/` — one `.tex` file per chapter.
- `bibs/litDB.bib` — bibliography (BibTeX).
- `pics/` — figures, diagrams, plots.
- `alg/` — algorithm listings.
- `data/` — evaluation data and the scripts that turn it into figures.
- `thesis_doc/notes/` — scratch notes, open questions, per-chapter TODOs.

## Build

The build engine is **Tectonic** (installed at
`%LOCALAPPDATA%\Programs\tectonic\tectonic.exe`), driven by the VS Code
LaTeX Workshop extension on save. To build from a terminal:

```sh
tectonic -X compile --keep-intermediates --keep-logs main.tex
```

Bibliography uses **biblatex with `backend=bibtex`** (see `main.tex` preamble),
because biber is not installed and Tectonic does not bundle it. The bibtex
backend is run by Tectonic natively. Cite with `\cite{key}`, `\parencite{key}`,
or `\textcite{key}`. The list prints via `\printbibliography`.

If a build fails with "File 'main.bbl' not created by biblatex", delete the
stale intermediates first (`main.aux main.bbl main.bcf main.run.xml`) and
rebuild. Compile after each chapter so LaTeX errors stay small and local.

## Figures and diagrams

**Standing instruction: proactively suggest a figure or diagram whenever a
section would be clearer with one.** Do not wait to be asked. Raise it while
drafting that section, not at the end, and keep it to one or two lines.

When suggesting one, say four things and no more:

1. **What it shows** in one sentence.
2. **Where the data or structure comes from** (a `thesis-pack/` file, a
   `data/` table, or an architecture fact). Never propose a figure whose
   content the project cannot supply.
3. **What kind** it is: TikZ diagram, plotted chart from `data/`, screenshot,
   or a table that is better drawn than tabulated.
4. **Whether it earns its place.** A figure that restates a sentence does not.
   Say so and drop it rather than padding.

Then wait for the author's yes before building it. Figures go in `pics/`, plot
scripts and their inputs in `data/`, and every figure needs a caption plus a
`\label{fig:...}` and at least one `\ref` from the prose.

### Current state

`pics/` holds only `logo-thi.jpg` and `data/` holds only a `README.md`, so
**every figure in the thesis still has to be made.** The raw material is in
`thesis-pack/11-results/data/`.

### Candidates already identified

Suggest these when the relevant section comes up. This list is a starting point,
not a limit.

| Chapter | Figure | Source |
| --- | --- | --- |
| Case study | Map of the Augustinum and the two shelters, with routes | already a `TODO(figure)` in `inc/casestudy.tex` |
| Case study | Resource-fit diagram: 100 residents, 2 buses x 50 seats, 2 shelters x 60 beds | shows why the allocation binds |
| Agentic system | Architecture diagram: 10 agents, 8 organisations, Postgres as broker | `04-architecture-agentic/agentic-core-README.md` |
| Agentic system | The sense / check-messages / reason / execute / reflect loop | `agentic_engine.py` description |
| Agentic system | Bus-Driver-1 sequence diagram — **must be redrawn**, the existing one is pre-ADR-0011 and shows 100 seats and one run | flagged in `PROJECT_BRIEFING.md` |
| Data layer | `event_log` as the shared backbone both systems write to | ADR-0003, ADR-0005 |
| Validity | The capability table, drawn as a two-column parity diagram | `08-validity/PARITY.md` |
| Method | The three gates and where each hypothesis is tested | `EVALUATION_PROTOCOL.md` |
| Results | Mean `S` per disruption, baseline vs the three full models | `RESULTS.md` §2 |
| Results | Risk differences with CIs, all 15 novel cells | `RESULTS.md` §2 — a forest plot suits this well |
| Results | The 16-criteria rubric split: parity on 5, baseline wins 5, scenario-indicting 3 | `RESULTS.md` §4 |
| Results | Delivery histogram showing the loss is **quantised**: 102 runs delivered everyone, 19 exactly 50, 18 exactly 90 | V2 §11.4 — this one is worth a full figure, it is the visual proof of RQ2 |
| Methods critique | Gate 0 evidence: every row reads `discriminates: no` | `data/discrimination-20260922T122707.md` |
| Methods critique | Null-policy regret per model: helped / neutral / harmed | V2 §11.1 |
| Design considerations | Plan revisions against full-delivery rate (90 % → 32 %) | V2 §11.4 |

## Working style

- Draft one chapter or one section per session to keep focus.
- The author verifies every empirical claim and citation. Flag anything uncertain.
- Suggest figures as you draft, per the section above. Do not wait to be asked.
- After drafting a chapter, update `thesis_doc/defence-prep.md`: add the
  chapter's one key message, any figure worth showing on a slide, numbers worth
  quoting, and any examiner question the chapter invites. Keep it current as we
  go, not at the end.
