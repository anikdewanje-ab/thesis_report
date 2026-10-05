# Thesis Defence Preparation

Living document. Update it while writing each chapter, not at the end. When a
chapter is drafted, come back here and add: the one key message, any figure
worth showing, the numbers worth quoting, and any question the chapter invites.

Talk length target: about 20 minutes of speaking, roughly 15 to 18 slides,
then questions.

---

## 1. The one-sentence pitch

> We built LLM agents that play the eight organizations evacuating a Hamburg
> nursing home and scored them, on one shared event log, against a scripted
> DV 100 baseline: the script saved every resident, the agents lost whole
> bus-loads because they kept rewriting plans they had already committed to.

Short form for slide 3: "Can the agents beat the script? No. Why not? They
understood the problem but did not carry their plans through."

The introduction (`inc/intro.tex`, drafted 2026-10-02) is the wording the
conclusion and abstract should mirror: three RQs, four contributions (artefact,
negative comparison, diagnosis, method), RQ1 boundary stated next to RQ1.

The abstract (`inc/abstract.tex`, drafted 2026-10-02) is the 60-second
spoken version of the talk. Its four paragraphs follow the opening slides in
order: problem, what we built, what we found (26 of 27 cells, 0.894, 93.8 %
of 1,932 handshakes closed, loss in whole bus-loads, rubric 5 / 5), and what a
designer should change. If asked for "the thesis in one minute", say the
abstract.

---

## 2. Slide outline

Each row becomes one slide. Keep the "key message" to a single spoken sentence.

| # | Slide | Key message (one sentence) | Visual to show | Status |
|---|-------|----------------------------|----------------|--------|
| 1 | Title | Who I am, title, supervisors | TU logo | draft |
| 2 | Motivation | Moving a nursing home before a surge needs eight organizations to agree, and a script only covers the disruptions its author foresaw | Hamburg flood map | draft |
| 3 | Problem and research questions | RQ1 can the agents beat the script, RQ2 why not, RQ3 what should change; RQ1 is answered for these scenarios only | RQ box with the RQ1 boundary under it | draft |
| 3b | Related work and gap | LLM agents have played evacuees and helped practitioners shape procedures, but nobody had set them, as the coordinating organizations, against a doctrine-grounded script on a scored outcome | Positioning table (RESPOND, Lee 2025, Li 2026, this thesis), if built | draft |
| 4 | Case study | 100 residents, 2 buses of 50, 2 shelters of 60: tight on purpose, so the allocation is a real decision | Storyline swimlane (Fig. `fig:cs:storyline`) | draft |
| 5 | The agents | Every agent is a person in a real agency; only agents that decide get a model | Roster table (`tab:cs:roster`) | draft |
| 6 | Architecture | Ten agents on one engine, and every message, state change and decision goes through one PostgreSQL database | Architecture diagram (Fig. `fig:ag:architecture`) | draft |
| 7 | Data architecture | One database is state store, message broker and scoring backbone; the novelty is the shared append-only log, not the shared database | Event-log backbone (Fig. `fig:data:backbone`); table overview (Fig. `fig:data:tables`) as backup | draft |
| 8 | Workflow baseline | One scripted commander walks the DV 100 command cycle; at the seam where an agent would call its model, three checks run in a fixed order: correct, hold, advance | Command cycle (Fig. `fig:wf:cycle`) | draft |
| 9 | Agentic system | The model proposes a step and a plan; the runtime owns time, validation and the audit row. Replanning is any rewrite of the step (echo, splice, supersede), not a separate module | Bus-Driver-1 walkthrough, or the replanning cases as a small table | draft |
| 10 | Observation interface | We can watch a live agentic run on the map and open the full prompt and answer behind any single decision (the baseline has no live view) | UI screenshot (Fig. `fig:ui:main`); tick drawer (Fig. `fig:ui:tick`) as backup | draft |
| 11 | Evaluation method | Three gates read in order: a system that loses residents has lost, however fast it was | Three-gates diagram (Fig. `fig:eval:gates`) | draft |
| 12 | Metrics | One ordinal ladder over valid completeness, every cut justified before the runs | Level-ladder diagram (`pics/method-ladder.tex`, slide only, no longer in the thesis) | draft |
| 12b | Validity (backup only) | Chapter dropped from the report on 2026-10-02. Keep the parity points below as backup answers; in the text they now live in Sec. `sec:wf:fleet`, `sec:wf:world` and `sec:crit:limitations` | none | dropped |
| 13 | Results: anticipated | H1 is rejected: non-inferiority holds in 1 of 8 anticipated cells | Anticipated-arm table | todo |
| 14 | Results: novel disruption | H2 is rejected outright: the baseline wins survival in every novel cell | Forest plot of the 15 risk differences | todo |
| 14b | Why it lost | A commitment failure, not a comprehension failure | Quantised delivery histogram | todo |
| 14c | The test could not be lost | Ignoring the disruption scored the ceiling, so the baseline's 1.000 is the null policy's score, and the agentic system lost to doing nothing | Gate 0 table (`tab:crit:gate0`) + regret bars (`pics/critique-regret.pdf`, slide only) | draft |
| 15 | Trade-offs | Baseline wins on speed and cost, and it also won the primary outcome | Coordination-surface table | todo |
| 15b | Design considerations (RQ3) | Commit before re-planning, confirm delivery, make the disruption change the world, and run Gate 0 before the campaign | Four-line list, each with its number (90 % to 32 %; 93.8 % closure; byte-identical control); reuse the plan-revision figure | draft |
| 16 | Contributions and limits | Two contributions, honest scope | Bullet list | todo |
| 17 | Conclusion | The agents read the situation correctly but did not keep a plan once it was moving; the next experiment is the commitment-constrained variant | Three RQ answers in one box, then the ranked future-work list (variant first) | draft |

---

## 3. Numbers worth quoting

From the results chapter (`inc/results.tex`), drafted 2026-09-22. Every figure
traces to `thesis-pack/00-start-here/RESULTS.md`, which is authoritative.

**The headline, in four numbers**

- Gate 1 fails **26 of 27** cells. The one pass is glm-5.2 on the undisrupted
  `closed_loop`, and it is a non-inferiority pass, not a superiority one.
- Novel-arm mean survival `S`: baseline **1.000**, qwen3.5 **0.894** (capped),
  glm-5.2 0.840, deepseek-v4-pro 0.727.
- The baseline scored a perfect 1.000 on **all 50** novel runs.
- Against the null policy the agentic regret is negative in **all 15** novel
  cells, and **68 of 150** runs came out worse than doing nothing.

**Scale of the study**

- 310 scored runs, 0 censored, 0 unscored, 0 invalid model bindings.
- 7 scenarios (2 anticipated, 5 novel), `k = 10` per cell, 3 models on the full
  novel arm, 7 models in total.
- One `SIM_TIME_SCALE` (8.4), so **H4 was not tested**.

**Decision quality (16 held-out rubric criteria)**

- Parity on 5, baseline wins 5, 3 indict the scenario (baseline scores 0 too).
- The sharpest single cell: `facility_answered_in_time`, baseline 10, all three
  agentic models **0**.
- Say "split", never "decision-quality parity".

**Why it lost (exploratory, Protocol v2)**

- Handshake closure **0.938** over 1,932 requests. The message layer worked.
- `r(never_dispatched, S)` = **−0.745**, the dominant mechanism.
- Loss is quantised: of 150 runs, 102 delivered everyone, 19 delivered exactly
  50, 18 delivered exactly 90, 2 delivered none.
- Full delivery falls from **90%** at 2 plan revisions to **32%** at 6 or more.
  `r(plan revisions, S)` = −0.408.

**Cost**

- Messages per resident delivered: baseline **0.13**, agentic 1.18 to 1.33.
- ~800,000 tokens per model arm; 1.8 to 2.7x the wall-clock budget; **140 of
  150** runs finished over budget. Baseline latency is 0.0 s by construction.

**Case study (from `inc/casestudy.tex`, drafted 2026-09-23, cut to ~5 pages 2026-10-04)**

- Key message: one small, tight case. Every disruption arrives as a message
  and none changes the world, so ignoring it still saves everyone. Say this on
  the case slide, because the whole Gate 0 argument rests on it.
- **100** residents, **2 x 50** seats (bus-2 is the reserve), **2 x 60** beds.
  That leaves only 20 spare beds, and neither shelter can take everyone alone.
- **10** agents in **8** organisations. **6** are LLM-driven (BIS, Hochbahn,
  2 bus drivers, Polizei, DRK) and **4** are scripted (ZKD, Augustinum, SC1,
  SC2). The baseline IC replaces BIS and Hochbahn only.
- Flood at **12:00**. 7 scenarios: 2 anticipated, 5 novel, revealed
  2026-09-10 after the freeze. S03 is retired.

**Method (from `inc/evaluation.tex`, drafted 2026-09-23, cut to ~3,500 words of prose 2026-10-04)**

- The chapter now carries the parity points itself (validity chapter dropped).
  The headless world client is a paragraph of its own under Study Design.
- 2026-10-04: 14 sections became 8. Model sweep and harness folded into Study
  Design; scenarios and firewall merged; construct validity dropped; the
  "not measured" table was deleted on 2026-10-05.
- 2026-10-05: the Reproducibility appendix was deleted. These are no longer in
  the thesis, so keep them ready from the repo for questions: prereg tags
  `prereg-v1` / `prereg-amendment-1` on commit `7a4d7cc` (2026-09-12);
  novel scenarios saved 15:27 to 16:04 on 2026-09-10; replicate blocks
  100-105 pilot, 1000-1009 confirmatory, 2000+ screenings; two-pass scoring
  (clean-run reference first, then levels); Wilcoxon exact up to 20 non-zero
  untied differences, else normal approximation with tie correction.

- Key message: the method fixed every threshold and margin before the runs,
  and it says openly where the execution departed from the plan.
- `delta_NI` = **0.05** on `S` (five residents of 100), registered 2026-09-04
  against zero runs. `delta_m` = **1 whole level**, and dominance is required.
- Level cuts **0.10 / 0.50 / 1.00**, efficiency band **+25 %** over `K*`,
  sensitivity cuts **0.40 / 0.50 / 0.60**.
- `k` = **10**: the pilot showed no `k` up to 200 buys H1, so `k` was set on
  budget and precision (Amendment 1).
- Freeze **11:41**, novel reveal **15:27 to 16:04**, both on 2026-09-10.
- **16** amendments. The novel-arm model set is exploratory (third slot moved
  three times after runs were seen).

**Methods critique (from `inc/methods_critique.tex`, drafted 2026-09-23)**

- Key message: the protocol found with its own negative control that its
  primary arm could not resolve H2, and Gate 0 is the rule that would have
  caught it. A finding, not an apology.
- Gate 0 fails on **7 of 7** scored scenarios; **0 of 6** disruption scenarios
  admitted. Only the shelter-closure fixture discriminates (level 3 vs 0).
- Baseline bus-km: **60.63** disrupted and undisrupted. Orders byte-identical
  to the no-replan control.
- Regret, with `S` capped at 1.0: baseline **0 / 50 / 0** (helped / neutral /
  harmed). Agentic **0 / 82 / 68** over 150. No agentic run beat doing
  nothing. Mean regret qwen3.5 −0.106, glm-5.2 −0.160, deepseek −0.273. The
  three qwen3.5 "helped" runs in the pack are the S = 1.1 over-ceiling runs;
  capping makes them neutral. If asked, that is the answer.
- Chapter cut to about half on 2026-10-05: the "Measuring Handshakes"
  subsection, the regret figure and three rows of the limitations table were
  removed. Handshake detail now lives only in Results.
- Aborts: 108 total, **52.8 %** post-failure stand-downs, **13.0 %** churn-
  initiated, 34.3 % other. Why the causal direction stays open.
- Sign-test floor: **0.0625** at five scenarios, **0.250** with two ties.
  qwen3.5 and glm-5.2 sit exactly on it.

**From the validity chapter** (`inc/validity.tex`, drafted 2026-09-23, dropped
from the report 2026-10-02; kept as backup material for parity questions; source
`thesis-pack/08-validity/PARITY.md`)

- Key message: parity is held by *shared code*, not by a look-alike copy. Every
  non-inert difference favours the baseline, so none explains the loss away.
- Reuse by identity: **49** IC attributes; **27** are the absorbed agents' own
  functions (23 BIS, 4 Hochbahn); **22** declared new with a reason.
- Vocabulary: 11 + 7 verbs, union **17**, minus 4 collapsed-link verbs = **13**.
  The baseline issues **9 of 13**.
- Deviations: **7**. 1 to 4 inert, 5 and 6 favour the baseline, 7 runs against it.
- Replacement-leg anchor: at most **6 km** (83.1 vs 89.1 km on the road
  closure); no level moves.
- Parity suite: **17** test functions (**31** items); **160** items in the
  baseline package. Mutation pass **not run** before the 2026-09-10 freeze.

**From the agentic architecture chapter** (`inc/agentic_system.tex`, drafted
2026-09-23; source `04-architecture-agentic/`):

- **10** agents, **8** organisations; **6** reason with a model, **4** scripted.
- **3** kinds of wake call the model (message, step finished, timing conflict).
  Dispatching due actions makes **no** model call.
- Temperature **0.2**; **no retry** of malformed output.
- Timing-conflict slack **60 s**; back-pressure stops after **3** attempts, or
  as soon as the gap stops shrinking.
- Time scale **8.4** in every scored run; client timeout **120 s** bounds how
  much simulated time one model call can cost.
- The back-pressure origin run: **8** timing-conflict wakes, gap 8, 3, 6, 12,
  7, 23, 16, 23 min, **869k** prompt tokens, **3.4x** its decision budget.

**From the data architecture chapter** (`inc/data_architecture.tex`, drafted
2026-09-29; source `06-data-layer/DATABASE_IMPLEMENTATION.md`, ADR-0003, 0005):

- **12** tables: **5** runtime (cleared before each run), **1** audit
  (`event_log`, never cleared), **6** sensing.
- Every `event_log` row: **7** fields (id, wall time, sim time, kind, subkind,
  summary, details) plus run, agent, model.
- **5** kinds of entry: `event_received`, `llm_response` (incl. `cron_fire`),
  `world_ack`, `decision` (baseline), `run_manifest` / `run_outcome`.
- **3** guarantees, all enforced by the database: trigger rejects UPDATE and
  DELETE; unique key (run, agent, id) makes a re-save harmless; read in
  insertion order.
- **3** notification channels per agent (state, inbox, world); fallback poll
  **5 s**, so a lost notification slows an agent and never stalls it.

**From the baseline chapter** (`inc/workflow_baseline.tex`, drafted
2026-09-24; source `05-architecture-baseline/`, ADR-0002, 0015, 0016):

- The IC replaces **2** agents (BIS, Hochbahn); the other **8** are shared.
- The Führungsvorgang has **3** stages in FwDV 100 (p. 24): Lagefeststellung,
  Planung, Befehlsgebung. Kontrolle is part of the *repeated* Lagefeststellung,
  not a fourth stage. Say it this way if asked.
- **4** phases, time budgets **20 / 15 / 90 / 10** min. **3** anticipated
  branches (road closure, capacity lost, bus breakdown). **1** generic hold.
- Citation matrix: **87** rows, **42** still `SOURCE_PENDING` (page cited on 45).
- Splitting transport and escort into two phases cost **26** sim-minutes.
- Closed loop walk: **13** turns, **13** orders; only the alarm is scripted.
- Frozen at `67a14f8`, **2026-09-10**; one post-reveal change (`e9e20cd`, the
  replan switch, Amendment 6).
- Baseline `S` = **1.000** on all 50 novel runs and **60.63** bus-km disrupted
  and undisrupted alike: the null policy's score, not adaptation.

---

## 4. Figures I can reuse from the thesis

Track figures here so the slides reuse the exact same images as the report.

- [x] **Architecture diagram**, built in TikZ (`pics/ag-architecture.tex`,
      `fig:ag:architecture`, Chapter 4). Slide 6. Every arrow passes through
      PostgreSQL, which is the visual meaning of "database-centric".
- [ ] Event-log / schema figure (data layer chapter)
- [x] **Engine wake cycle**, built in TikZ (`pics/ag-engine.tex`,
      `fig:ag:engine`, Chapter 4). Slide 9. Eight steps, only one calls the
      model; the model-free dispatch path beside them; the two loops back into
      the queue (step finished, timing conflict).
- [ ] Bus-Driver-1 sequence diagram, redrawn for 2 runs x 50 seats (ADR-0011).
      Not built.
- [x] **Coordination storyline swimlane**, built in TikZ (`pics/cs-storyline.tex`,
      `fig:cs:storyline`). Slide 4. The map was declined.
- [x] **Baseline command cycle**, built in TikZ (`pics/wf-cycle.tex`,
      `fig:wf:cycle`, Chapter 5). Slide 8. The three checks at the seam in
      their fixed order, and the execution model closing the loop.
- [ ] Main results chart (Chapter 8)
- [x] **Observation interface screenshot** (`pics/ui-main.png`,
      `fig:ui:main`, Chapter 7). Slide 10. Map with the two buses, escort car
      and ambulance; agent tabs; Bus-Driver-2's plan and tick list.
- [x] **Tick drawer screenshot** (`pics/ui-tick-drawer.png`, `fig:ui:tick`).
      Backup for slide 10. BIS woken by the ZKD storm surge alarm: prompt on
      the left, raw model output and parsed plan on the right. Good answer to
      "how do you know what the model was thinking?".
- [x] **UI data flow**, built in TikZ (`pics/ui-dataflow.tex`,
      `fig:ui:dataflow`). Probably not a slide; four columns, each one path
      through Postgres (state out, scenario in, ACK back, prompt records).

The results chapter has three figures. All three, and the cut forest plot, are
slide-worthy:

- [x] **Forest plot of the 15 novel risk differences with CIs** — built,
      `pics/results-forest-rd.pdf`. Cut from the thesis on 2026-10-05 (Table
      9.4 carries the same values); keep it for the slides. The single clearest picture of
      the result. All 15 intervals left of zero; eight strictly below, six
      touching, one reaching past to +0.02.
- [x] **Residents delivered per run** — built,
      `pics/results-delivery-histogram.pdf`, Figure 9.1. The visual proof of
      RQ2: the loss is quantised, not gradual.
- [x] **The sixteen rubric criteria** — built,
      `pics/results-rubric-split.pdf`, Figure 9.3. The split in reading order:
      parity 5, baseline ahead 5, baseline also at zero 4, unplaced 2. Use it
      whenever someone rounds the result to "decision-quality parity".
- [x] **Plan revisions against delivery** — built,
      `pics/results-commitment-scatter.pdf`, Figure 9.2. All 150 runs, not the
      five band means. Shows that the revision floor sits on full delivery
      while the six-or-more band spreads over the whole range.
- [x] ~~Mean `S` per disruption~~ — **considered and dropped.** It
      duplicates the forest plot. If an examiner wants the headline as bars,
      show the forest plot slide instead. The per-disruption `S` table was also cut on
      2026-10-05: the baseline is 1.000 in every cell, so each agentic value is
      1 + RD and Table 9.4 (risk differences) already carries it.

Results chapter shortened on 2026-10-05 (prose 3,931 to 2,976 words, 14 tables
to 7, about 8 pages saved). The median level shift, Clopper-Pearson and
sign-test tables and the six over-ceiling runs went first to an Appendix D,
which was then deleted the same day. The thesis now states only their
verdicts. If an examiner asks for the per-cell numbers or the six run IDs,
they are in `thesis-pack/00-start-here/RESULTS.md` (over-ceiling runs in
sec. 6.2). Deleted as redundant: the Gate 1 count table, the
per-disruption `S` table, the loss-mechanism scope table (the novel-arm,
three-model figures 985 late / 26 runs / 215 overload stay in the prose).
Process diagnostics now sit inside "What the Losses Were Made Of", and
sensitivity inside "Novel Disruptions".

From the data architecture chapter:

- [x] **Event log as backbone** (`pics/data-backbone.tex`, `fig:data:backbone`).
      Slide 7. Both systems write, one scorer reads; the harness manifest is
      nested so it cannot change a score.
- [x] **Table overview** (`pics/data-tables.tex`, `fig:data:tables`). Backup
      slide, if asked what is in the database.

From the method and critique chapters:

- [x] **The three gates** (`pics/method-gates.tex`, `fig:eval:gates`). Slide 11.
- [x] **The level ladder** (`pics/method-ladder.tex`). Cut from the thesis on
      2026-10-02 (it restated the equation), still good for slide 12.
- [x] **Null-policy regret, helped / neutral / harmed** — built,
      `pics/critique-regret.pdf`, via `python data/scripts/plot_regret.py`,
      with `S` capped at 1.0. No longer in the thesis (the table carries it),
      still good for slide 14c. Pair it with the Gate 0
      table (`tab:crit:gate0`), which is a table on purpose.

Every plotted figure regenerates with `python data/scripts/plot_*.py` and shares
one style, so the slides can reuse the exact files in the report. All of them
are byte-reproducible, so re-running a script is a no-op in git.

**One caveat for the commitment scatter.** It is the only figure that needs the
Postgres container, because per-run plan revisions are not in `thesis-pack/`.
It falls back to `data/commitment_per_run.csv` when the container is down, so
it still rebuilds on a machine without Docker.

---

## 5. Anticipated questions (and my answer)

The hardest questions are already known from the literature. Prepare these first.

**Q: LLMs cannot really plan (Kambhampati et al.). Why should I trust yours?**
A: I do not assume they plan well. I measure how they degrade. The deterministic
scorer over the event log is an external verifier, which is exactly what that
line of work recommends. (Refine after Chapter 2.)

**Q: A shared database for coordination is not new (Linda, blackboards, event
sourcing). What is novel here?**
A: I concede the substrate is old. The novelty is using the same event log at
once as the coordination medium for both systems and as the scoring oracle, so
the comparison is fair and replayable. (Refine after Chapter 4.)

**Q: Maybe the multi-agent design is not what decides the outcome (a strong single agent can match a multi-agent discussion, Wang et al. 2024).**
A: The parity spec holds everything equal except the coordination strategy:
same information, same actions, same world model. That is the control. (Refine
after Chapter 8.)

**Q: Is the workflow baseline a strawman?**
A: No. It implements an established doctrine (DV 100 / ICS) and passes 100
percent of the anticipated disruptions. (Refine after Chapter 5.)

**Q: How do you know the disruptions are truly "novel" and not tuned to favor
the agents?**
A: They were supplied by an independent domain expert who was blind to the
frozen baseline, from a characteristics-only brief. The freeze commit
(`67a14f8`, 11:41) predates the reveal (15:27 to 16:04) on 2026-09-10, and git
records both. One later baseline change (the no-replan switch) is disclosed in
Amendment 6 with equivalence evidence.

**Q: LLM output is random. How is this reproducible?**
A: I repeat each scenario ten times per cell under common random numbers and
report distributions, not single points. I do **not** claim digest pinning: the
`:cloud` tags are not version-frozen, and that is declared as a limitation.

### Questions the results chapter invites

**Q: Your baseline scored 1.000 everywhere. Is the comparison rigged?**
A: The opposite problem, and I found it myself. A controller that ignores every
disruption scores the identical level, so the baseline's 1.000 is the null
policy's score. That is Gate 0 in Chapter `ch:critique`. I never claim the
baseline adapted.

**Q: Then does the agentic system come out even?**
A: No. The withdrawal cuts one way only. Against the same null policy the
agentic regret is negative in all 15 novel cells, and 68 of 150 runs came out
worse than doing nothing.

**Q: Three qwen3.5 runs score `S` = 1.1. Is your scorer broken?**
A: Six runs shelter more residents than the feasibility ceiling admits, and I
diagnose why in Section `sec:res:integrity`. It is genuine over-delivery
credited against a ceiling that does not admit it. I cap at the reporting
layer, not in the scorer, because capping in the scorer would rewrite a
confirmatory result after the fact.

**Q: You said the deficit was a handshake problem. Now you say commitment.
Which is it?**
A: Commitment. The handshake reading was my first write-up and measurement
superseded it: closure is 0.938 over 1,932 requests. The deficit is residents
never dispatched, `r` = −0.745.

**Q: Does plan churn cause the losses?**
A: Not established, and I say so. 53% of aborts are post-failure stand-downs,
so a failing run plausibly re-plans because it is failing. The experiment that
would settle it is a commitment-constrained variant on the same scenarios.

**Q: Your registered primary test was coded after you saw the data.**
A: Yes, and it is declared as a timing deviation and labelled exploratory. The
more interesting point is that at `k` = 10 the registered aggregation cannot
reach conventional significance however the data fall. The floor on `p` is
0.0625, and with ties it is 0.250, which is exactly where two models sit.

**Q: You registered four hypotheses. Where are H3 and H4?**
A: Both are reported, and neither is part of the claim. The pre-registration
puts H1 and H2 together as claim C and treats H3 and H4 as estimation, not
testing, with no significance test pre-specified for either.
**H3 cannot be resolved because it presupposes H2**: it asks whether the
agentic advantage is model-robust and where the capability threshold sits, and
there is no advantage here to be robust or fragile, so the threshold is
undefined rather than unobserved. **H4 was not tested**: only one
`SIM_TIME_SCALE` (8.4) ran, so Gate 3 has one point per cell and no crossover
can be located. I claim no crossover, trend or scale-dependence of any kind.

Do **not** offer to remove either from the thesis. They are pre-registered, the
frozen-artifact appendix makes the register checkable, and dropping an unfilled
hypothesis is the exact practice pre-registration exists to prevent.

**Q: Did you cherry-pick the level thresholds?**
A: The cut-point sensitivity is reported at 0.40, 0.50 and 0.60. Every cell in
the three full novel arms is stable except one, and no agentic-versus-baseline
ordering moves anywhere in the range.

### Questions the methods critique invites

**Q: Isn't Gate 0 just a post-hoc excuse?**
A: It is post hoc, and it is labelled exploratory for that reason. But it
excuses nothing. It changes no number and it withdraws a claim in the
baseline's favour, not the agentic system's. It also makes the agentic result
worse: regret against doing nothing is negative in every cell.

**Q: Doesn't this invalidate the thesis?**
A: It invalidates one reading, H2 as a statement about adaptability. RQ1 is
still answered: on these scenarios the agentic system did not win, and it lost
to doing nothing. RQ2 and the rubric stand. What the thesis cannot say is
whether an agentic system would win when adaptation is required, and I say
that boundary every time.

**Q: Why not re-run on scenarios that pass Gate 0?**
A: That is the next campaign, and Protocol v2 specifies how to author them.
The evaluation here is finished and frozen. Running a new arm after seeing
these results would be exploratory again.

**Q: If the baseline's score is uninformative, why is the agentic score
informative?**
A: Because the scenario design explains why the baseline could not lose, not
why the agents did. A system that damages a working plan on news it should
have absorbed has a defect. 68 of 150 runs did exactly that.

**Q: So does the baseline win because it ignores the disruption?**
A: No, on two counts. It does not ignore it: it issues the holding order, three
status updates and a `wait_for_reply`. And ignoring is not what produced the
score. The disruptions never changed the world, so responding and not
responding scored the same, which is why the baseline's regret is exactly zero
in all 50 runs. If ignoring were doing the work, the null policy would beat the
baseline; it ties it.

> **Do not say "the baseline wins by ignoring the disruption."** It invites
> either "then your baseline is a strawman" or "then you have shown ignoring is
> optimal", and it contradicts Gate 0, which puts the failure in the scenario
> rather than in either controller. Say the baseline wins on survival in every
> disruption tested, and that the win is invariance rather than recovery.

**Q: How do you know it's commitment and not something else?**
A: Six alternatives were tested and ruled out (`tab:crit:ruledout`): wrong
population, message layer, too few dispatches, scorer dedup, driver
over-claiming, running out of clock. Then the positive evidence: whole
bus-loads lost, and full delivery 90 % to 32 % as plan revisions rise. The
causal direction is still open.

### Questions the discussion chapter invites

Key message: the agents understood the disruption and then did not carry their
plan through. The architecture's main feature, re-planning, is where it lost,
on scenarios where the right number of re-plans was zero. No new figure; reuse
the delivery histogram and the plan-revision scatter on one slide.

Numbers to quote: 68 of 150 runs worse than doing nothing; full delivery 90 %
to 32 % as plan revisions rise; 16 of 20 medical-emergency runs named the right
action and issued no medical order; 9 to 10x messages per resident delivered.

**Q: Could a stronger model close the gap?**
A: The deficit narrows with capability (-0.27, -0.16, -0.10). deepseek is last
on all five disruptions; qwen3.5 leads glm-5.2 on four (on sc1 glm -0.19 vs
qwen -0.22). But no model reaches zero, and the design does not
support extrapolating past qwen3.5. A stronger model is a guess; a commitment
boundary is a testable design change.

**Q: Does your finding contradict the agent literature or confirm it?**
A: It is consistent with the critical side: Kambhampati (no self-verification),
Huang and Stechly (self-correction without external feedback gets worse),
Cemri et al. (failure to check task completion). I say "consistent with", not
"confirms", because my data cannot show the mechanism is the same.

**Q: Why would anyone build this, given the cost?**
A: On these scenarios they should not: 9 to 10x the messages and about 800k
tokens bought nothing. Whether it pays off when adaptation is really needed is
untested. What transfers today is the method (shared event log, Gate 0, regret
against a null policy) and the diagnosis, not a performance claim.

### Questions the design considerations chapter invites

Key message: four groups of advice, each earned by one measurement here. Agent
architecture: a commitment boundary on legs in flight and an explicit delivery
confirmation per leg. Scenario design: binding resources, disruptions that
change the declared world, declared meanings (the reserve role) fixed for both
sides. Evaluation design: Gate 0 first, size the design, fix and pin models,
treat retries as a factor. Cost: plan it from the start. Chapter is short on
purpose (about 1,150 words) and points back to the evidence. No new figure.

Numbers to quote: full delivery 90 % at 2 revisions vs 32 % at 6+;
r(revisions, S) = -0.408 vs r(missions, S) = -0.070; 93.8 % closure over 1,932
requests; 53 % of 108 aborts are post-failure stand-downs, 13 % churn-initiated;
sign test floor p = 0.0625 at k = 10; 140 of 150 novel runs over budget.

**Q: These come from one case. Why should anyone take them as general?**
A: I do not claim they are general. They are the considerations this one
evaluation earned, each with its number and its limit. The chapter ends by
saying they should be tested on the next design before being generalised. The
evaluation-design points (Gate 0, sizing the design) depend least on the case.

**Q: Isn't the commitment boundary just your guess at the cause?**
A: It rests on a strong correlation, and I say the causal direction is open.
The commitment-constrained variant is one campaign on the same scenarios and
would settle it. That is why it leads the future work.

### Questions the background chapter invites

Key message: the critical planning literature (Kambhampati, Huang, Stechly,
Cemri) predicted what we found. Agents can understand a situation and still
fail to act on it. That is why the scorer is deterministic code over the event
log and never a model.

**Q: RESPOND looks close to this. What is different?**
A: RESPOND models the population that evacuates, and it is a short demo with no
controlled comparison. In our system the residents decide nothing. The agents are the organizations, and
we compare them with a scripted baseline under parity.

**Q: The literature already says LLMs cannot plan. Why build this at all?**
A: The literature tests planning puzzles and reasoning benchmarks. Nobody had
measured it on a multi-organization evacuation against a competent scripted
opponent. Our result agrees with the critics, and we say where the failure sits:
commitment, not comprehension.

**Q: Is a shared database as coordination medium new?**
A: No. Blackboards and Linda tuple spaces did it decades ago, and we say so in
Chapter 2 and in the data chapter. Our claim is the shared log as the backbone
of both systems and of the scorer.

**Q: Where does your word "commitment" come from? Did you invent it after the
results?**
A: No, it is classic agent theory and Section 2.3 introduces it before any
result. Cohen & Levesque (1990) define an intention as a choice with
commitment, kept until the goal is reached, impossible, or no longer needed.
Rao & Georgeff (1995) explain why a BDI agent needs that persistence in a
changing world. An LLM agent can rewrite its plan at every call, so how often
it should is a design question. Our data show what happens when it rewrites
too often.

**Q: Why not just solve the evacuation as an optimization problem?**
A: Relief-logistics models (Huang 2012, Holguín-Veras 2013, Yin 2024) assume
one planner who sees everything. Our question is coordination between
organizations that each own part of the resources and part of the
information. We measure how well that coordination works, not how close it
gets to an optimum.

### Questions the case study invites

**Q: Why only two buses and two shelters?**
A: Two of each is the smallest roster where the allocation is a real
decision. One bus cannot carry everyone and one shelter cannot take everyone.
Every extra clone adds run cost and model variance but no new coordination
pattern. The price is a single case, which I declare.

**Q: Why are four of the agents scripted?**
A: One rule decides it: an agent that makes no decision gets no model. ZKD
relays and countersigns. The schools and the home report numbers. Giving them a
model would add noise and cost but no decision to measure.

**Q: Why did none of the disruptions change the world?**
A: They were written as reports. The shelter keeps its beds and the bus keeps
its seats. That is how they were supplied, and for S07 and S08 the files say
so in advance. The consequence is that ignoring a report cannot cost a resident,
which is exactly what Gate 0 found. It is a limit of the scenarios, not of the
scorer.

**Q: Are these real people?**
A: No. The names are placeholder identities. The organisations are real
Hamburg agencies. The roles follow how civil protection there is organised.

### Questions the validity chapter invites

**Q: Deviation 7 was "closed" after the results were known. Isn't that
convenient?**
A: Yes, the argument works only because of the direction of the result, and I
say so in the chapter. The deviation removes an advantage the baseline used to
have, so it can only have made the baseline's margin look smaller. Had the
agentic side won, I would have had to close the gate properly first.

**Q: The IC sees both the command and the fleet picture. Isn't the baseline
now the unfair one?**
A: It is a real advantage, declared as deviation 5, and it follows from
doctrine: a central commander who cannot see what they command would be a
strawman. It weakens the agentic loss in part, and I say so both ways: an
agentic win despite it would have been stronger.

**Q: Your parity tests were never mutation-tested. How do you know they can
fail?**
A: I don't know it for the rewritten ones, and the chapter says so. They carry
anti-vacuity guards, and the old suite was mutation-checked. The nine-mutation
minimum set is written down but was not run before the freeze.

**Q: Isn't the reserve bus a confound?**
A: No. Both sides hold the same fleet and may use bus 2. Sending it and parking
it are two decisions over one capability, which is what the study measures. I
report parking it while residents are at risk as a decision-quality failure.

### Questions the agentic chapter invites

**Q: Why a custom engine and not LangGraph or another agent framework?**
A: The runtime has to own three things: simulated time, validation of every
action and message, and the audit rows the evaluation scores from. The baseline
must write the very same rows. A framework that hides these behind its own
abstractions would make the comparison harder to defend.

**Q: Why no retry when the model returns broken JSON?**
A: A retry gives a weak model a second chance a strong model never needed, and
hides a real difference between models. The cost, one lost decision, is
declared in the protocol.

**Q: Doesn't the runtime do the agents' thinking for them?**
A: No. It never picks a destination, a split of residents or a message. It sets
clock times from the model's "now" or "by the deadline", refuses what the role
does not allow, and keeps the real position. Several of these rules exist
because an earlier version failed without them.

**Q: Where is the replanning module?**
A: There is none, on purpose. The model may rewrite its step or plan on any
wake, and the engine handles the difference as an echo, a splice or a
supersede. Replanning was the capability the design offered. On these scenarios
the right number of re-plans was zero, and runs that re-planned more delivered
everyone less often. The causal direction is open.

**Q: Is "database-centric" more than "it uses a database"?**
A: Yes. The database is the only channel between agents and the only source of
truth. Every message, state, world report and decision passes through it, and
the notifications in it are what wake the agents. Figure `fig:ag:architecture`
shows no agent-to-agent arrow.

**Q: Did the prompt tell the agents to wait, and so cause the commitment
failure?**
A: The prompt says the opposite. The infeasibility playbook states that
holding is not free, because the clock runs while the agent waits, and that a
driver who will drive the leg anyway should commit, start driving and ask in
the same answer. Appendix A prints the persona, contract and message playbook
verbatim from the campaign commit `7a4d7cc`, and Table `tab:app:playbooks`
summarises the other two. The examiner can read exactly what the model was told.

### Questions the baseline chapter invites

**Q: Isn't the baseline a strawman you built to lose?**
A: No. It implements DV 100, the doctrine Hamburg actually works under, element
by element. A test fails if any public function lacks a row in the citation
matrix. It passed every anticipated disruption and was frozen before the novel
ones were revealed. And it won.

**Q: How "doctrine-grounded" is it really?**
A: The core is cited to FwDV 100 pages: the command system (p. 3), staff
areas S1 to S6 (pp. 13-14), command levels (p. 23), the command cycle (pp. 24-25),
report back on deviation (p. 37), joint order (p. 38). Three things are my
declared design choices, not doctrine: the mission phases and time budgets,
writing the disruption branches in advance, and the holding order. 42 of 87
matrix rows still lack a page. None of this changes a number.

**Q: Why does the baseline send the reserve bus out at once?**
A: Its scheduler gives each run to the first free bus and never reads the
reserve mark. The sequential-reserve rule in ADR-0015 was never built. Both
sides may use bus 2, so this is a decision difference, not a parity defect, and
it explains part of the gap.

**Q: Did the fallback ever decide a novel scenario?**
A: No. Every disruption was a message that did not change the world, so
ignoring it still delivered everyone. The baseline's 1.000 is the null policy's
score. The fallback's quality was never tested, in either direction.

**Q: Does the holding order stop the buses?**
A: No. The IC has no command that stops a bus. The hold-departure advisory goes
to the Hochbahn mailbox, which in the baseline is the IC's own, so it reaches
no driver. The hold stops the IC from issuing new orders; buses already on the
road keep going. On these scenarios it never mattered, because no novel
disruption changed the world.

**Q: Why an execution model? Wasn't the scenario enough?**
A: The old scenario files carried the outcome, so a commander that sent
everyone to a closed shelter still scored full marks. The execution model makes
the score a consequence of the orders. A test shows noticing a closure scores
1.0 and missing it scores 0.

### Questions the data architecture chapter invites

**Q: Isn't a shared database for agents just a blackboard or a tuple space?**
A: Yes, and I say so in the chapter. I do not claim the shared database as a
new coordination medium. The claim is methodological: one append-only log that
both systems write and the scorer reads, so scoring is deterministic, parity is
testable and every run can be re-scored.

**Q: What stops you from deleting a bad run?**
A: The database. A trigger rejects every UPDATE and DELETE on `event_log`, and
reset between runs clears only the runtime tables. A dropped run still leaves
its rows behind.

**Q: Is a run reproducible?**
A: Re-scorable, yes, from its rows. Re-runnable only approximately. Every model
call is seeded and the seed is logged, but inference is only near-deterministic
(batching, cache state). That is why every cell has k = 10 repetitions.

**Q: Why store the agent state as one JSON document and not normalise it?**
A: The runtime always loads and saves it whole, and no measurement reads it.
Everything the evaluation needs is in the event log, written as it happens.

**Q: Why no file fallback if the database goes down?**
A: A fallback nobody runs drifts silently into a second implementation. With
one backend, an outage stops the simulation, and start-up checks the database
first.

**Q: Can two runs leak into each other?**
A: The event log cannot, since every row carries the run. `messages` and
`world_events` have no run column, so separation relies on the reset the
harness performs before every cell. That is a stated limitation of the schema.

### Questions the observation interface chapter invites

**Q: Could the UI have influenced the results?**
A: Only through one channel: the browser's animation sends the `task_complete`
acknowledgement that closes a drive. In the evaluation no browser is open; a
headless client sends the same acknowledgements. A cell refuses to start if
any browser tab is connected, because two sources would count every drive
twice. Otherwise the UI only reads, and it never writes an agent's state.

**Q: Why not let the engine acknowledge its own drives?**
A: That would remove the handshake with the world that the agent must
complete, so the architecture would be scored on a property it does not have.

**Q: Can I see the UI for the baseline too?**
A: No. The baseline runs from its command-line tool and its execution model
moves the vehicles, so it needs no map. Its runs are read from the same event
log as the agentic ones.

### Questions the method chapter invites

**Q: Your H1 rule is a point estimate with no significance level. Why?**
A: The code always decided on the point estimate. With pilot data seen, I
registered the implemented rule rather than change the code, and I state the
cost: a system exactly at the margin passes about half the time. So a pass is
reported as "the point estimate lies inside the margin", never as
"non-inferiority demonstrated". In the event only one cell passed.

**Q: Why was the negative control read on a fixture and not on the scored
scenarios?**
A: The protocol wrote down that on the scored files the control could not
differ from the doctrine in outcome. That was the reason to move the gate. Its
consequence for the scored arms was not drawn at the time, and Chapter
`ch:critique` draws it. That is Gate 0.

**Q: You changed models four times. Isn't that fishing?**
A: Every change is an amendment with a "data seen" column. Because the third
slot moved after runs were seen, the novel-arm model set is labelled
exploratory. glm-5.2 and deepseek-v4-pro were fixed before the arm ran, and
they show the same result.

**Q: Why no equity measure in a nursing-home evacuation?**
A: Registered as undefined, with the reason: residents are counts with no
attribute to split on, so a subgroup difference is always zero. Mobility tiers
would be better; they were declined as late scope chosen with the campaign in
view. The ladder cannot tell the 60 most mobile from the 60 least mobile, and I
say so.

**Q: Why an ordinal ladder and not the resilience triangle?**
A: The triangle is an area under a functionality curve (Bruneau 2003), and very
different trajectories can give the same area (Cremen 2025). The ladder records
what matters here: were the residents in a shelter before the water arrived.
(The thesis text no longer makes this argument; both sources were cut to keep
the bibliography at 50. They are still in `litDB.bib`.)

**Q: Why not use an LLM judge for decision quality?**
A: A model judging models brings back the nondeterminism being measured. The
rubric reads structure only (who, when, what was ordered, what landed) and
anything that depends on prose is listed as not judged.

**Q: Why not just use LangGraph / why Ollama?**
A: The runtime has to own three things that a framework keeps for itself.
First, the simulated clock, which keeps running while the agents think.
Second, the check of every command and message against the agent's role.
Third, the audit trail, so that the agents and the baseline write the same
rows to the event log. If a framework hid these, the comparison would be much
harder to defend. So we wrote a small engine in plain asynchronous Python, and
PostgreSQL is the single source of truth (ADR-0005). Ollama serves cloud and
local models through one interface, so changing the model for the sweep is one
setting and no code change.

### Questions the conclusion invites

Key message: three answers and one next step. RQ1 no (and the boundary in
the same breath), RQ2 commitment rather than comprehension, RQ3 the four
groups from the design chapter. The four contributions mirror the intro. The
future work is ranked: commitment-constrained variant, Gate-0-passing
scenarios, a design sized to detect an effect, a broader case. No new numbers
and no figure; everything quoted already appears in Results or Critique.

Numbers to quote: 26 of 27 cells; 0.894 best capped mean vs 1.000; 68 of 150
worse than the null policy; 93.8 % closure over 1,932 requests; 102 / 19 / 18;
90 % to 32 %; p floor 0.0625 at k = 10.

**Q: If you could run one more experiment, which and why?**
A: The commitment-constrained variant: cap re-plans or forbid cancelling a leg
in flight, same scenarios, same models. One campaign, no new scenarios, and it
settles the causal direction. If constrained runs deliver more, churn causes
the loss; if not, churn is a symptom of runs already failing.

**Q: Why not lead the future work with better scenarios instead?**
A: Gate-0-passing scenarios answer RQ1's open half ("can it ever win"), but
they need new scenario authoring and a new campaign. The variant reuses
everything and tests the diagnosis this thesis actually made, so it comes first.

**Q: What carries over beyond this case?**
A: The method (one shared event log, regret against a null policy, Gate 0) and
the diagnosis (look at the step where a new message may cancel a leg in
flight). The design considerations themselves still need testing on another
case.

### Questions the introduction invites

**Q: If no scenario required adaptation, why run the comparison at all?**
A: We did not know that before the runs. The scenarios were supplied blind by
a domain expert and looked like disruptions. The no-replan control showed
afterwards that ignoring them scored the ceiling. That is why RQ1 is answered
as "did it win here", and why Gate 0 is a contribution: it would have caught
this before the campaign.

**Q: Your RQ1 answer is "no". Isn't the thesis then a failure?**
A: It is a design-and-evaluation study, so a negative answer is a result. And
the agents did not just lose to the script, they lost to doing nothing (68 of
150 runs), which is what made the diagnosis in RQ2 possible.

**Q: Why four contributions when one of them is a negative result?**
A: Each stands on its own evidence. The artefact runs, the comparison is
pre-registered and scored, the diagnosis is measured (0.938 closure, quantised
losses, 90 % to 32 %), and the event log plus Gate 0 is reusable whatever the
outcome.

### Questions the scenario appendix invites

Key message: every disruption is a message with the same text on both sides,
and none of them changes a bed, a road or a vehicle. Appendix B prints the
disruption messages word for word (S02 and the five novel ones). Slide
candidate: one of the printed messages, e.g. S06, to show what "a disruption"
looked like to the agents.

**Q: Did both systems receive the same disruption?**
A: The same text at the same time, yes. The type differs on purpose. The
agentic side gets `situation_update`, which BIS routes to re-planning. The
baseline gets a type outside its catalogue, so it reaches the fallback and
holds. Sent as `situation_update`, the commander would have read it as an
order from above.

**Q: Why does the baseline control start at 09:30 and the agentic control at
09:45?**
A: Priced on real road distance, the baseline's control plan takes about
2 h 07 min, because its allocation rule fills SC1 first and one bus makes a
second trip. From 10:00 it would land at 12:07 and lose 40 residents with no
disruption. In the novel arm both sides start at 09:45. (Prepare this one:
the 15-minute offset applies only to S01, and it is not in the validity
chapter's list of deviations.)

**Q: Why does S02 hold 60 residents on the baseline side and 100 on the
agentic side?**
A: The baseline cannot re-route, so a closure can only reach it as a shelter
going unreachable. Losing a 60-bed shelter leaves no complete allocation for
100. Completeness is scored against each file's own population.

---

## 6. Backup slides (only if asked)

- Full agent roster with the nine-facet template
- Database schema in detail
- Scoring rubric (0 to 4 recovery-outcome levels)
- Per-scenario result tables
- The seven scenarios in one line each (`tab:cs:scenarios`, Chapter 3), for
  "what exactly happens in S05?"

---

## 7. Terminology to say consistently

Keep the spoken words identical to the thesis so nothing sounds contradictory.

- "agentic system" (not "the AI", not "the bots")
- "workflow baseline" (not "the old way")
- "event log" as the single source of truth
- "recovery-outcome level" as the primary result
- "a commitment failure, not a comprehension failure" for why the agentic
  system lost
- "decision quality is split" and never "decision-quality parity"

Words that must **not** be spoken, because the data contradict them:

- "graceful degradation under novel disruption" as a headline claim. It was the
  proposal's expectation and it is the opposite of the result.
- the baseline "adapted", "recovered" or "replanned better". It was not
  disturbed. Its score is the null policy's score.
- the baseline "wins because it ignores the disruption". It does respond, and
  the response is what scores zero regret, not the ignoring. Say the win is
  invariance rather than recovery.
