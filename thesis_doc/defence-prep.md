# Thesis Defence Preparation

Living document. Update it while writing each chapter, not at the end. When a
chapter is drafted, come back here and add: the one key message, any figure
worth showing, the numbers worth quoting, and any question the chapter invites.

Talk length target: about 20 minutes of speaking, roughly 15 to 18 slides,
then questions.

---

## 1. The one-sentence pitch

> (Fill this in once the introduction is written. One plain sentence a
> non-expert examiner understands: what problem, what you built, what you found.)

Draft: We compare a plain workflow script against LLM-driven agents for
coordinating a nursing-home evacuation, using a shared event log so the two can
be scored the same way, and we test which one holds up better when a new,
unexpected disruption hits.

---

## 2. Slide outline

Each row becomes one slide. Keep the "key message" to a single spoken sentence.

| # | Slide | Key message (one sentence) | Visual to show | Status |
|---|-------|----------------------------|----------------|--------|
| 1 | Title | Who I am, title, supervisors | TU logo | draft |
| 2 | Motivation | Evacuation coordination is hard and current tooling is rigid | Hamburg flood map | todo |
| 3 | Problem and research question | Can the agentic architecture beat the scripted baseline, and if not, why? | RQ box | todo |
| 4 | Case study | 100 residents, 2 buses of 50, 2 shelters of 60: tight on purpose, so the allocation is a real decision | Storyline swimlane (Fig. `fig:cs:storyline`) | draft |
| 5 | The agents | Every agent is a person in a real agency; only agents that decide get a model | Roster table (`tab:cs:roster`) | draft |
| 6 | Architecture | Ten agents on one engine, and every message, state change and decision goes through one PostgreSQL database | Architecture diagram (Fig. `fig:ag:architecture`) | draft |
| 7 | Data architecture | Append-only event log makes fair scoring possible | Schema / event-log figure | todo |
| 8 | Workflow baseline | One scripted commander walks the DV 100 command cycle; at the seam where an agent would call its model, three checks run in a fixed order: correct, hold, advance | Command cycle (Fig. `fig:wf:cycle`) | draft |
| 9 | Agentic system | The model proposes a step and a plan; the runtime owns time, validation and the audit row. Replanning is any rewrite of the step (echo, splice, supersede), not a separate module | Bus-Driver-1 walkthrough, or the replanning cases as a small table | draft |
| 10 | Live UI | We can watch both systems run on the map | UI screenshot | todo |
| 11 | Evaluation method | Three gates read in order: a system that loses residents has lost, however fast it was | Three-gates diagram (Fig. `fig:eval:gates`) | draft |
| 12 | Metrics | One ordinal ladder over valid completeness, every cut justified before the runs | Level-ladder diagram (Fig. `fig:eval:ladder`) | draft |
| 12b | Validity | Parity is shown by shared code, not claimed; every non-inert difference favours the baseline, so none explains the loss away | Deviations table (`tab:val:deviations`) | draft |
| 13 | Results: anticipated | H1 is rejected: non-inferiority holds in 1 of 8 anticipated cells | Anticipated-arm table | todo |
| 14 | Results: novel disruption | H2 is rejected outright: the baseline wins survival in every novel cell | Forest plot of the 15 risk differences | todo |
| 14b | Why it lost | A commitment failure, not a comprehension failure | Quantised delivery histogram | todo |
| 14c | The test could not be lost | Ignoring the disruption scored the ceiling, so the baseline's 1.000 is the null policy's score, and the agentic system lost to doing nothing | Gate 0 table (`tab:crit:gate0`) + regret bars (`fig:crit:regret`) | draft |
| 15 | Trade-offs | Baseline wins on speed and cost, and it also won the primary outcome | Coordination-surface table | todo |
| 16 | Contributions and limits | Two contributions, honest scope | Bullet list | todo |
| 17 | Conclusion | What it means and what comes next | Summary | todo |

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

**Case study (from `inc/casestudy.tex`, drafted 2026-09-23)**

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

**Method (from `inc/evaluation.tex`, drafted 2026-09-23)**

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
- Regret: baseline **0 / 50 / 0** (helped / neutral / harmed). Agentic
  **3 / 79 / 68** over 150. Mean regret qwen3.5 −0.100, glm-5.2 −0.160,
  deepseek −0.273.
- Aborts: 108 total, **52.8 %** post-failure stand-downs, **13.0 %** churn-
  initiated, 34.3 % other. Why the causal direction stays open.
- Sign-test floor: **0.0625** at five scenarios, **0.250** with two ties.
  qwen3.5 and glm-5.2 sit exactly on it.

**From the validity chapter** (`inc/validity.tex`, drafted 2026-09-23; source
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

**From the baseline chapter** (`inc/workflow_baseline.tex`, drafted
2026-09-24; source `05-architecture-baseline/`, ADR-0002, 0015, 0016):

- The IC replaces **2** agents (BIS, Hochbahn); the other **8** are shared.
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

From the results chapter, three figures are flagged as `TODO(figure)` in
`inc/results.tex` and all three are slide-worthy:

- [x] **Forest plot of the 15 novel risk differences with CIs** — built,
      `pics/results-forest-rd.pdf`, Figure 10.1. The single clearest picture of
      the result. All 15 intervals left of zero; eight strictly below, six
      touching, one reaching past to +0.02.
- [x] **Residents delivered per run** — built,
      `pics/results-delivery-histogram.pdf`, Figure 10.2. The visual proof of
      RQ2: the loss is quantised, not gradual.
- [ ] Mean `S` per disruption, baseline against the three full models

From the method chapter, both built as TikZ:

- [x] **The three gates** (`pics/method-gates.tex`, `fig:eval:gates`). Slide 11.
- [x] **The level ladder** (`pics/method-ladder.tex`, `fig:eval:ladder`). Slide 12
      or a backup slide.
- [ ] The 16-criteria rubric split, drawn as three bands
- [x] **Null-policy regret, helped / neutral / harmed** — built,
      `pics/critique-regret.pdf`, `fig:crit:regret`, via
      `python data/scripts/plot_regret.py`. Slide 14c. Pair it with the Gate 0
      table (`tab:crit:gate0`), which is a table on purpose.
- [ ] Plan revisions against full-delivery rate (90% down to 32%)

Both built figures are regenerated with `python data/scripts/plot_*.py` and use
one shared style, so anything added later will match them on the slides.

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

**Q: Maybe the multi-agent design is not why it wins (Tran & Kiela).**
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

**Q: How do you know it's commitment and not something else?**
A: Six alternatives were tested and ruled out (`tab:crit:ruledout`): wrong
population, message layer, too few dispatches, scorer dedup, driver
over-claiming, running out of clock. Then the positive evidence: whole
bus-loads lost, and full delivery 90 % to 32 % as plan revisions rise. The
causal direction is still open.

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

### Questions the baseline chapter invites

**Q: Isn't the baseline a strawman you built to lose?**
A: No. It implements DV 100, the doctrine Hamburg actually works under, element
by element. A test fails if any public function lacks a row in the citation
matrix. It passed every anticipated disruption and was frozen before the novel
ones were revealed. And it won.

**Q: How "doctrine-grounded" is it really?**
A: The element mapping is complete. The page mapping is not: 42 of 87 rows still
wait for a page reference. That limits the "doctrine-grounded in every detail"
claim, and changes no number.

**Q: Why does the baseline send the reserve bus out at once?**
A: Its scheduler gives each run to the first free bus and never reads the
reserve mark. The sequential-reserve rule in ADR-0015 was never built. Both
sides may use bus 2, so this is a decision difference, not a parity defect, and
it explains part of the gap.

**Q: Did the fallback ever decide a novel scenario?**
A: No. Every disruption was a message that did not change the world, so
ignoring it still delivered everyone. The baseline's 1.000 is the null policy's
score. The fallback's quality was never tested, in either direction.

**Q: Why an execution model? Wasn't the scenario enough?**
A: The old scenario files carried the outcome, so a commander that sent
everyone to a closed shelter still scored full marks. The execution model makes
the score a consequence of the orders. A test shows noticing a closure scores
1.0 and missing it scores 0.

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

**Q: Why not use an LLM judge for decision quality?**
A: A model judging models brings back the nondeterminism being measured. The
rubric reads structure only (who, when, what was ordered, what landed) and
anything that depends on prose is listed as not judged.

**Q: Why not just use LangGraph / why Ollama?** (Resolve once the framework
story in Chapter 6 is settled.)
A: (TODO)

---

## 6. Backup slides (only if asked)

- Full agent roster with the nine-facet template
- Database schema in detail
- Scoring rubric (0 to 4 recovery-outcome levels)
- Per-scenario result tables

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
