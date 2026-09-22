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
| 4 | Case study | Storm surge, Augustinum, 100 residents, Hamburg | Map + storyline | todo |
| 5 | The agents | Every agent is a person in a real agency | Agent roster diagram | todo |
| 6 | Architecture | The database is the shared source of truth | Architecture diagram from briefing | todo |
| 7 | Data architecture | Append-only event log makes fair scoring possible | Schema / event-log figure | todo |
| 8 | Workflow baseline | A competent scripted baseline, not a strawman | 10-step flow | todo |
| 9 | Agentic system | Sense, reason, act, reflect loop with replanning | Agent loop diagram | todo |
| 10 | Live UI | We can watch both systems run on the map | UI screenshot | todo |
| 11 | Evaluation method | Same scenarios, same scorer, one thing changed | Method diagram | todo |
| 12 | Metrics | Recovery-outcome level is the primary result | Metric table | todo |
| 13 | Results: anticipated | H1 is rejected: non-inferiority holds in 1 of 8 anticipated cells | Anticipated-arm table | todo |
| 14 | Results: novel disruption | H2 is rejected outright: the baseline wins survival in every novel cell | Forest plot of the 15 risk differences | todo |
| 14b | Why it lost | A commitment failure, not a comprehension failure | Quantised delivery histogram | todo |
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

---

## 4. Figures I can reuse from the thesis

Track figures here so the slides reuse the exact same images as the report.

- [ ] Architecture diagram (Chapter 6)
- [ ] Event-log / schema figure (Chapter 4)
- [ ] Agent sense-reason-act loop (Chapter 6)
- [ ] Case-study map (Chapter 3)
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
- [ ] The 16-criteria rubric split, drawn as three bands
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
frozen baseline. (Refine after Chapter 8.)

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
