# Writing plan

Written 2026-09-22, after `thesis-pack/` landed and the three superseded docs
were deleted. This is the order to write the report in, and the decisions that
have to be made before drafting starts.

## 1. Framing — SETTLED with the supervisor, 2026-09-22

The thesis is a **design-and-evaluation study**, not a hypothesis-confirmation
study. The motivation was to design an agentic simulation architecture, evaluate
it honestly against an old-style scripted baseline, and report what was learned
either way. A negative answer is a result here, not a failure. Write every
chapter in that voice and never apologise for the outcome.

Four research questions, each with an answer the evidence supports:

| | Question | Answer | Where |
| --- | --- | --- | --- |
| RQ1 | Can the agentic architecture beat the scripted baseline? | **No.** Gate 1 fails 26 of 27 cells. It also loses to a null policy: 68 of 150 runs came out worse than doing nothing. | Results, Methods critique |
| RQ2 | If not, why? | A **commitment** failure, not a comprehension failure. The agents understood the disruption; they could not carry one committed plan to delivery. | Results, Discussion |
| RQ3 | What must change? | Constrain commitment, and test on scenarios that discriminate. The named experiment is a commitment-constrained variant. | Conclusion, future work |
| RQ4 | What should a designer consider? | The generalisable deliverable. | Design Considerations chapter |

**Why this framing is stronger than it first looks.** Gate 0 showed the baseline
wins these scenarios without replanning at all. That does not rescue the agentic
side, it indicts it harder: the agentic system failed at a task solvable by doing
nothing. And the architecture's advertised capability is re-planning on
disruption, while on these scenarios the correct number of re-plans was **zero**.
Runs that re-planned the minimum delivered everyone 90 % of the time; runs that
re-planned six or more times, 32 %. That is the sharpest finding in the thesis.

**The boundary to state in the same breath.** No scenario in this thesis ever
*required* adaptation. So RQ1 is answered as "did it win here", not "can it ever
win". Say so explicitly, in the introduction and again in the conclusion.

**Two claims the old skeleton made that are now deleted.** `discussion.tex`
asserted "LLM-agent coordination degrades more gracefully than pre-scripted
workflows", and `conclusion.tex` listed that as empirical contribution 1. Both
were the proposal's expectation written in before the data existed. Both are the
opposite of the result. If either phrasing reappears in a draft, delete it.

## 2. Structural changes to `main.tex` — DONE 2026-09-22

Two chapters in `thesis-pack/` have no home in `main.tex`:

- **Validity** (`08-validity/PARITY.md`) — are the two systems comparable? Seven
  declared deviations, each with its direction. This chapter is what makes the
  comparison admissible, and it currently does not exist.
- **Methods critique** — the pack says it is a chapter in its own right, and
  under the frame above it is the centre of the thesis, not an appendix to the
  method chapter.

Also reorder to match the pack: architecture (agentic, then baseline), then the
data layer. Right now `data_architecture` sits before both.

Proposed chapter order:

1. Introduction
2. Background and Related Work
3. Case Study and Domain
4. Architecture: the Agentic System
5. Architecture: the Workflow Baseline
6. Data Layer
7. Observation UI (short, supporting material)
8. **Validity: are the two systems comparable?** (new)
9. Method and Evaluation Protocol
10. Instrument Implementation (may fold into 9)
11. Results
12. **Methods Critique** (new)
13. Discussion
14. Conclusion

## 3. Fix these before writing a word

The 300 -> 100 fix is **done**. The rest still stand.

- ~~`inc/casestudy.tex` says **300 residents**.~~ **Fixed 2026-09-22**, along
  with two other stale facts in the same chapter: the fleet is **2 buses at 50
  seats**, not three, and the shelters are **SC1 and SC2 at 60 beds each**, not
  two out of five candidates. The disruption list in that chapter named the
  three retired prototyping fixtures; it now names the real seven scenarios.
- **No chapter cites anything yet.** `bibs/litDB.bib` holds 46 entries and
  `inc/` uses zero `\cite`. `casestudy.tex` is the only chapter with prose and
  it does cite, so the habit exists; the rest are skeletons.
- Most sources in `rubric-bibliography.md` are **not** in `litDB.bib`. Import
  them before writing the rubric justification.
- `bibs/litDB.bib` has 9 em-dashes in titles that the Times font cannot render.
  They print as missing characters in the bibliography. Replace with `---`.
- `pics/` holds only a logo and `data/` holds only a README. Every results
  figure still has to be produced from `thesis-pack/11-results/data/`.

## 4. Writing order

Do not start at chapter 1. Start where the facts are frozen, because those
chapters constrain the ones that interpret them.

| Order | Chapter | Source | Why here |
| --- | --- | --- | --- |
| 1 | Results | `00-start-here/RESULTS.md` | Every number is fixed and generated. Nothing downstream can be written honestly until the numbers are on the page. |
| 2 | Method | `09-method/EVALUATION_PROTOCOL.md`, `PREREGISTRATION.md` | Defines the gates and hypotheses the results chapter refers to. |
| 3 | Methods critique | `09-method/EVALUATION_PROTOCOL_V2.md`, `RESULTS.md` §6.7–6.8 | The Gate 0 evidence and the six declared limitations. Write while the protocol is fresh. |
| 4 | Validity | `08-validity/PARITY.md` | Seven deviations with directions. Deviation 7 is closed by re-argument. |
| 5 | Case study | `03-case-and-domain/CONTEXT.md`, `01-introduction/PROJECT_BRIEFING.md` | Already part-drafted. Fix 300 → 100 and finish. |
| 6 | Architecture: agentic | `04-architecture-agentic/`, ADRs 0003, 0005, 0006–0013, 0016 | Mechanical from the READMEs. `bus_driver` is the reference agent. |
| 7 | Architecture: baseline | `05-architecture-baseline/`, ADRs 0002, 0015 | Note that ADR-0015 rule 7 is **not implemented** and must not be cited as built. |
| 8 | Data layer | `06-data-layer/DATABASE_IMPLEMENTATION.md`, ADR 0005 | This is what earns the word "database-centric" in the title. |
| 9 | Observation UI | `07-observation-ui/ui-README.md` | Short. Supporting material only. |
| 10 | Background and related work | `02-related-work/` | Aim it at the frame chosen in §1, so write it after the frame is settled. |
| 11 | Discussion | `RESULTS.md` §4–5 | The split rubric, the capability ordering, the commitment mechanism. |
| 12 | Introduction | — | Written last, because it promises what the thesis delivers. |
| 13 | Conclusion, then abstract | — | Abstract absolutely last. |

Compile after each chapter, as `CLAUDE.md` says, so LaTeX errors stay local.

## 5. Claims to never make

- That the baseline "adapted", "recovered" or "replanned better".
- That the agentic models match or beat the baseline on every discriminating
  rubric criterion but one. They fall short on **five** of sixteen.
- Any crossover, trend or scale-dependence claim. Only one `SIM_TIME_SCALE`
  (8.4) ran, so **H4 was not tested**.
- That the deficit is a handshake failure. That diagnosis is superseded.

## 6. Limitations chapter, already decided

`thesis-pack/README.md` lists six, each with the position to take. They are
positions, not open questions, and none blocks submission. Copy the table and
argue each one.
