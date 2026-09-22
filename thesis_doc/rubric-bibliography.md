# Annotated Bibliography — Section 10: The Recovery-Outcome Rubric

> Supplement to `rescuesim-annotated-bibliography.md`. Organised by **rubric design decision**,
> so each subsection is the defence for one choice a reviewer will question.
>
> **Verification status (2026-08-04): every reference below was checked against the publisher
> record or an indexing database. All exist. Venues, volumes, pages and DOIs as given here are
> confirmed unless a line says otherwise.**

---

## A. Why an ordinal ladder — and why not to dichotomise it

The strongest transferable methodology here is from **stroke clinical trials**, where the modified
Rankin Scale (mRS) is a 7-level ordered categorical outcome (0 = fully independent → 6 = dead)
analysed across thousands of trials. The structural parallel to a 0–4 recovery ladder is close
enough that you can import both the design and its critiques.

**MUST-CITE**

**Savitz, S. I., Lew, R., Bluhmki, E., Hacke, W., & Fisher, M. (2007). *Shift Analysis Versus
Dichotomization of the Modified Rankin Scale Outcome Scores in the NINDS and ECASS-II Trials.*
Stroke, 38(12):3205–3212. DOI: 10.1161/STROKEAHA.107.489351.**
Uses the Cochran–Mantel–Haenszel shift test on the full 90-day mRS distribution and compares it
against dichotomised logistic regression. This is the direct precedent for analysing the *whole
level distribution* rather than collapsing to "success/failure," and CMH is a ready-made,
assumption-light test you can run on per-disruption level distributions.

**Cite it for the method, not for a verdict.** The paper's own conclusion is that the shift
analysis did *not* outperform the dichotomised mRS 0–2 outcome, and that the shift lost
significance in both datasets once the fringe severity strata were removed. Use Savitz for "here
is how you analyse an ordinal outcome distribution"; let Nunn and Ganesh carry the claim that
retaining the ordinal structure is preferable. Misreporting this is an easy own goal — a stroke-
literate reviewer will know the result.

**Nunn, A., Bath, P. M., & Gray, L. J. (2016). *Analysis of the Modified Rankin Scale in
Randomised Controlled Trials of Acute Ischaemic Stroke: A Systematic Review.* Stroke Research and
Treatment, 2016:9482876. DOI: 10.1155/2016/9482876.**
Systematic review of 42 RCTs finding most still dichotomise despite evidence that preserving the
ordinal structure increases statistical power. Cite to justify why the rubric is a five-level
ladder rather than a pass/fail gate — and note that the same review documents *disagreement about
where the dichotomy should fall*, which is exactly the objection your sensitivity check answers.

**The Optimising Analysis of Stroke Trials (OAST) Collaboration. (2007). *Can We Improve the
Statistical Analysis of Stroke Trials? Statistical Reanalysis of Functional Outcomes in Stroke
Trials.* Stroke, 38(6):1911–1915.**
The origin of the "retain the ordinal scale" recommendation: a reanalysis across many trials
showing ordinal methods are more statistically efficient than dichotomisation. This is the OAST
citation.

**Ganesh, A., Luengo-Fernandez, R., Wharton, R. M., & Rothwell, P. M. (2018). *Ordinal vs
dichotomous analyses of modified Rankin Scale, 5-year outcome, and cost of stroke.* Neurology,
91(21):1951–1960. DOI: 10.1212/WNL.0000000000006554.**
Note this is **not** an OAST paper — it comes out of the Oxford Vascular Study, and citing it as
OAST is the kind of slip a stroke-literate examiner spots immediately. It documents the pitfalls
of dichotomising ordinal scales and the superiority of
retaining the full range. Also raises the counter-consideration you should acknowledge: ordinal
analysis treats all state transitions as equal, which for your ladder means a 0→1 step counts the
same as 3→4. Decide explicitly whether that is acceptable or whether a weighted variant is
warranted, and say which.

**SUPPORTING**

**Xie, J., Zhang, K., Chen, J., Zhu, T., Lou, R., Tian, Y., Xiao, Y., & Su, Y. (2024).
*TravelPlanner: A Benchmark for Real-World Planning with Language Agents.* ICML 2024.
arXiv:2402.01622** [already §7 of the main bibliography].
Programmatic, constraint-based scoring with commonsense and hard-constraint components — the
closest agentic-evaluation precedent for a deterministic scorer with frozen pass criteria.

**Xu, F. F., et al. (2025). *TheAgentCompany: Benchmarking LLM Agents on Consequential Real World
Tasks.* NeurIPS 2025 Datasets & Benchmarks Track. arXiv:2412.14161.**
Defines a partial-completion score from checkpoint credit alongside a strict full-completion
binary, explicitly because binary success discards meaningful progress. Supports graded levels
over pass/fail in an agentic setting. Note it uses LLM judges for some rubric items — cite the
contrast, since your scorer is fully deterministic.

---

## B. How to compare the level distributions (dominance, not means)

**MUST-CITE**

**Yalonetzky, G. (2013). *Stochastic Dominance with Ordinal Variables: Conditions and a Test.*
Econometric Reviews, 32(1):126–163. DOI: 10.1080/07474938.2012.690653.**
The single most on-point statistical citation: dominance conditions and a test built specifically
for *ordinal* variables where cardinal distances between levels are undefined. This is precisely
your situation and it justifies dominance over any mean-level comparison.
State the fit accurately: the paper derives *multivariate* dominance conditions and extends
Anderson's nonparametric test to ordinal variables, demonstrated on multidimensional wellbeing in
Peru. Your single-ladder comparison is the univariate special case — legitimate, but say so rather
than implying the paper was written for your setting.

**Davidson, R., & Duclos, J.-Y. (2000). *Statistical Inference for Stochastic Dominance and for
the Measurement of Poverty and Inequality.* Econometrica, 68(6):1435–1464.** — and **Davidson, R.,
& Duclos, J.-Y. (2013). *Testing for Restricted Stochastic Dominance.* Econometric Reviews,
32(1):84–125** (same issue as Yalonetzky). The 2013 paper is the empirical-likelihood test, with a
null of *non*-dominance, and unlike most tests in this literature it applies to discrete as well as
continuous variables — which is why it is the one that survives contact with a five-level ladder.
The standard inference machinery for dominance testing. Cite for the formal definition and for
the point that dominance can be assessed on discrete supports.

**SUPPORTING**

**Barrett, G. F., & Donald, S. G. (2003). *Consistent Tests for Stochastic Dominance.*
Econometrica, 71(1):71–104**; **McFadden, D. (1989). *Testing for Stochastic Dominance.* In
T. B. Fomby & T. K. Seo (Eds.), Studies in the Economics of Uncertainty (pp. 113–134). Springer-
Verlag** — a book chapter, not a journal article; cite it accordingly.
The foundational lineage; cite one for provenance. Barrett & Donald's bootstrap approach is the
practical option if you want a significance claim rather than a descriptive dominance check.

**Practical caution from the dominance literature:** tests lose power in sparse tails. With
k ≈ 30 runs and five levels, some cells will be near-empty — report the raw level counts
alongside any test, and prefer descriptive dominance plus bootstrap CIs over a single p-value.

---

## C. Cut-point sensitivity — the "you picked numbers that make agentic win" defence

**MUST-CITE**

**Simonsohn, U., Simmons, J. P., & Nelson, L. D. (2020). *Specification Curve Analysis.* Nature
Human Behaviour, 4:1208–1214.**
Three-step procedure: enumerate all theoretically justified and non-redundant specifications,
display results graphically, then conduct joint inference across them. Your 40/50/60 % sensitivity
check is a small specification curve — cite this to name the method properly and consider
extending it to jointly vary the level-1/2 cut, the efficiency band, and the level-0 threshold
rather than one at a time.

**Steegen, S., Tuerlinckx, F., Gelman, A., & Vanpaemel, W. (2016). *Increasing Transparency
Through a Multiverse Analysis.* Perspectives on Psychological Science, 11(5):702–712.**
The original multiverse framing: report the full space of results consistent with defensible
processing choices rather than a single path. Directly applicable to the log-interpretation rules
as well as the thresholds.

**SUPPORTING**

**Del Giudice, M., & Gangestad, S. W. (2021). *A Traveler's Guide to the Multiverse: Promises,
Pitfalls, and a Framework for the Evaluation of Analytic Decisions.* Advances in Methods and
Practices in Psychological Science, 4(1). DOI: 10.1177/2515245920954925.**
Important caveat: only *genuinely arbitrary* specifications belong in the multiverse; treating
principled choices as arbitrary inflates the space and drowns the signal. Useful for arguing that
the 50 % cut is domain-justified ("half the home") while the efficiency band is more arbitrary and
therefore deserves the wider sweep.

---

## D. Freezing thresholds before eval day = preregistration

**MUST-CITE**

**Bertinetto, L., Henriques, J. F., Albanie, S., Paganini, M., & Varol, G. (Eds.) (2021).
*NeurIPS 2020 Workshop on Pre-registration in Machine Learning.* Proceedings of Machine Learning
Research, Vol. 148. PMLR.** — and **Albanie, S., Henriques, J. F., Bertinetto, L.,
Hernández-García, A., Doughty, H., & Varol, G. (Eds.) (2022). *NeurIPS 2021 Workshop on
Pre-registration in Machine Learning.* PMLR, Vol. 181.**
The two-stage protocol (preregistered proposal → confirmatory review that the protocol was
followed) is the CS-native precedent for your git-freeze + tag. Cite to establish that
preregistration is an accepted practice in ML, not an import you invented.

**Citation warning — this is the one place in this bibliography where the obvious citation is
wrong.** A "Bengio, Y., Pineau, J., Bach, F., Zosa Forde, J., & Whitaker, K. (2020). *The
Pre-Registration Workshop: An Alternative Publication Model for Machine Learning Research*" entry
circulates in the literature (e.g. in Hofman et al., *Pre-registration for Predictive Modeling*,
arXiv:2311.18807), but it is an informal, non-archival reference to the **workshop announcement**
at preregister.science. It has no PMLR entry, no pages and no DOI, and PMLR 148 is **not** edited
by those authors. The same trap applies to "Albanie et al. (2021), PMLR 181": the only Albanie
et al. item inside that volume is the one-page Preface (181:i–i). Cite the volumes as venues (as
above), or cite the Preface explicitly as a preface — do not present either as a paper making an
argument. For a citation that actually carries argumentative weight, use van Miltenburg et al.
below: it is peer-reviewed and it makes the case in prose.

**SUPPORTING**

**Gelman, A., & Loken, E. (2013/2014). *The Garden of Forking Paths.***
Explains why decisions made after seeing data bias results even without deliberate p-hacking —
the cleanest statement of *why* thresholds must be frozen before eval day, and stronger for your
purpose than a fraud-prevention framing.

**Kerr, N. L. (1998). *HARKing: Hypothesizing After the Results are Known.* Personality and Social
Psychology Review, 2(3):196–217.**
Names the specific failure your freeze prevents. Useful one-line citation in the methodology
chapter.

**van Miltenburg, E., van der Lee, C., & Krahmer, E. (2021). *Preregistering NLP Research.*
Proceedings of NAACL-HLT 2021, pp. 613–623. ACL. DOI: 10.18653/v1/2021.naacl-main.51.
arXiv:2103.06944.**
Practical guidance on what a preregistration document should contain in an NLP/ML setting, and on
labelling parts of a study exploratory vs. confirmatory. Directly useful as a template for what
goes in the frozen artifact alongside the thresholds.

---

## E. Construct validity — does the ladder measure *replanning capability*?

**MUST-CITE**

**Jacobs, A. Z., & Wallach, H. (2021). *Measurement and Fairness.* FAccT '21, pp. 375–385.
DOI: 10.1145/3442188.3445901. arXiv:1912.05511.**
The essential citation for this chapter. Argues that computational systems routinely operationalise
unobservable theoretical constructs via measurement models, and that harms follow from mismatches
between the construct and its operationalisation. Your construct is "replanning capability"; your
measurement model is the recovery ladder over the event_log. The paper's seven components of
construct validity (face, content, convergent, discriminant, predictive, hypothesis, consequential)
give you a ready-made section structure for defending the rubric — and a principled place to admit
what the ladder does *not* capture.

Practical use: write one short paragraph per component. Face and content validity are cheap.
Convergent validity is where your diagnostic metrics earn their keep (supersede count should
correlate sensibly with level). Consequential validity is where you discuss gaming — e.g. the
feasibility-ceiling denominator.

---

## F. Resilience quantification — the ladder as a discretised resilience curve

**MUST-CITE**

**Bruneau, M., Chang, S. E., Eguchi, R. T., Lee, G. C., O'Rourke, T. D., Reinhorn, A. M.,
Shinozuka, M., Tierney, K., Wallace, W. A., & von Winterfeldt, D. (2003). *A Framework to
Quantitatively Assess and Enhance the Seismic Resilience of Communities.* Earthquake Spectra,
19(4):733–752. DOI: 10.1193/1.1623497.**
The origin of the resilience triangle: a functionality curve Q(t), with resilience loss as the
area between full functionality and actual performance, decomposed into robustness and rapidity
(ends) and resourcefulness and redundancy (means). This is the canonical quantitative
operationalisation of "degrades more gracefully," and it pairs with Woods (2015, 2018) — Woods
gives the theory, Bruneau gives the measurement tradition.

**Why your rubric departs from it — and why that is defensible.** A documented limitation of the
triangle is that it can produce identical resilience values for very different functionality
trajectories, because every time instant is weighted equally — see **Cremen, G. (2025). *A New
End-User-Oriented and Dynamic Approach to Post-Disaster Resilience Quantification for Individual
Facilities.* Risk Analysis, 45(3):701–709. DOI: 10.1111/risa.17637** (single author; cite it
properly rather than by PMC ID). A hospital that is barely functional during the critical emergency
phase but recovers fast can score the same as one that stays capable throughout. Your ladder
sidesteps this by scoring the *outcome* (were residents validly sheltered before the deadline)
rather than the area under a curve — cite this critique explicitly to justify the choice rather
than leaving it as an unexplained departure from the standard metric.

**SUPPORTING**

**Cimellaro, G. P., Reinhorn, A. M., & Bruneau, M. (2010). *Framework for Analytical Quantification
of Disaster Resilience.* Engineering Structures, 32(11):3639–3649.**
Functional-temporal formulations extending Bruneau; cite if you want a more formal resilience
function than the triangle.

**Zobel, C. W. (2011). *Representing Perceived Tradeoffs in Defining Disaster Resilience.* Decision
Support Systems, 50(2):394–403. DOI: 10.1016/j.dss.2010.10.001.**
Year note: available online October 2010, published in the January **2011** issue. Both years
appear in the wild — use 2011 and be consistent across the thesis.
Makes the trade-off between initial performance loss and recovery-period length explicit — the
closest existing framing of the "how much worse, for how long" question your levels 1–3 encode.

---

## G. The completeness and efficiency dimensions — humanitarian logistics

**SUPPORTING (grounds the choice of dimensions; none is a must-cite)**

**Huang, M., Smilowitz, K., & Balcik, B. (2012). *Models for Relief Routing: Equity, Efficiency and
Efficacy.* Transportation Research Part E: Logistics and Transportation Review, 48(1):2–18.**
This — not Beamon & Balcik — is the canonical source for the three-objective framing in
humanitarian relief. It defines and formulates efficiency, efficacy and equity metrics for
last-mile distribution. Maps onto your rubric: completeness ≈ efficacy, bus-km ≈ efficiency, and
the third axis is the one you don't have.

**Beamon, B. M., & Balcik, B. (2008). *Performance Measurement in Humanitarian Relief Chains.*
International Journal of Public Sector Management, 21(1):4–25. DOI: 10.1108/09513550810846087.**
Volume and pages confirmed. **But check the text before you attribute the 3E triad to it** — its
framework extends a commercial supply-chain model along resource / output / flexibility metrics,
which is not the same thing. Cite it for "performance measurement in relief chains needs its own
metrics, not commercial ones"; cite Huang et al. for the triad itself.

**Wang, S. L., & Sun, B. Q. (2023). *Model of multi-period emergency material allocation for
large-scale sudden natural disasters in humanitarian logistics: Efficiency, effectiveness and
equity.* International Journal of Disaster Risk Reduction, 85:103530.
DOI: 10.1016/j.ijdrr.2023.103530.**
Two authors, not "et al."; the venue is IJDRR. Operationalises the triad quantitatively and
combines the three objectives by weighted sum. Useful as a concrete example
of how the third dimension is normally measured.

**Holguín-Veras, J., Pérez, N., Jaller, M., Van Wassenhove, L. N., & Aros-Vera, F. (2013). *On the
Appropriate Objective Function for Post-Disaster Humanitarian Logistics Models.* Journal of
Operations Management, 31(5):262–280. DOI: 10.1016/j.jom.2013.06.002.**
Argues that logistics cost is the wrong objective in humanitarian settings and introduces
deprivation cost as the human-suffering term. Cite in defence of excluding raw latency and cost
from the primary DV: the field has an established argument that operational cost is not the
outcome that matters.

> **Gap the literature exposes in your rubric: there is no equity dimension.** Huang et al. treat
> equity as co-equal with efficiency and efficacy, and the assisted-evacuation
> literature (§4 of the main bibliography, esp. the high-rise hospital assistance-behaviour study)
> analyses evacuation *equity* for vulnerable groups explicitly. Your ladder is indifferent between
> a run that shelters the 60 most mobile residents and one that shelters the 60 least mobile —
> both score 2. In a nursing-home evacuation that is a real distinction. Either add a diagnostic
> equity KPI alongside Constraint Violations, or declare the omission in limitations with these
> citations. Declaring it is cheap; being caught not having noticed is not.

---

## H. The feasibility ceiling — thin literature, one good analogue

There is little direct methodological work on normalising an outcome scale by a
disruption-dependent achievable maximum. The closest established practice:

**Murray, G. D., Barer, D., Choi, S., Fernandes, H., Gregson, B., Lees, K. R., Maas, A. I. R.,
Marmarou, A., Mendelow, A. D., Steyerberg, E. W., Taylor, G. S., Teasdale, G. M., & Weir, C. J.
(2005). *Design and Analysis of Phase III Trials with Ordered Outcome Scales: The Concept of the
Sliding Dichotomy.* Journal of Neurotrauma, 22(5):511–517. DOI: 10.1089/neu.2005.22.511.**
This is the origin of the sliding dichotomy, in the traumatic-brain-injury literature. Its uptake
in stroke is documented in Nunn, Bath & Gray 2016: of their 42 trials, three defined favourable
outcome by baseline NIHSS stratum and two used sliding dichotomy as the analysis method (PAIS
2009, AbESTT-II 2008) — a small but real minority, which is exactly the honest way to describe it.
A minority of trials define favourable outcome *relative to baseline severity* rather than by a
fixed cut, precisely because a fixed threshold is unattainable for the most severely affected
patients. That is structurally identical to your feasibility ceiling: the achievable maximum
depends on the severity of the insult, so the scale is normalised by it. Cite this as the
precedent — it converts an apparent ad-hoc normalisation into an established design.

**Caveat to state:** the sliding-dichotomy literature also documents the cost — it complicates
interpretation and makes results harder to compare across studies. The same applies to you, plus
the endogeneity risk (the ceiling must be computed from the scenario and disruption spec alone,
never from the run log, or a system can lower its own denominator).

**Watch the wording of the formula here.** `min(100, Σ remaining_shelter_capacity)` reads as
log-dependent — "remaining" invites the question *remaining after what?* If capacity consumed by
the run's own placements feeds back into the denominator, a system that shelters badly shrinks its
own ceiling and scores higher. Define `remaining` explicitly as capacity surviving the scenario
and disruption spec, evaluated before any agent action, and say so in the same sentence as the
formula. This is a one-line fix in the rubric text and it closes the most obvious attack on the
feasibility ceiling.

---

## Priority summary

| Rubric decision | Single strongest citation |
|---|---|
| Ordinal ladder, not binary | OAST Collaboration 2007 (Stroke); Savitz et al. 2007 for the CMH method |
| Distribution/dominance, not means | Yalonetzky 2013 (Econometric Reviews) |
| Cut-point sensitivity sweep | Simonsohn, Simmons & Nelson 2020 (Nat Hum Behav) |
| Git-frozen thresholds | van Miltenburg et al. 2021 (NAACL-HLT); PMLR 148 / 181 as venue precedent |
| Rubric measures what it claims | Jacobs & Wallach 2021 (FAccT) |
| "Degrades gracefully" as a measurable | Bruneau et al. 2003 (Earthquake Spectra) |
| Outcome not area-under-curve | Cremen 2025 (Risk Analysis) critique of the resilience triangle |
| Feasibility ceiling | Murray et al. 2005 (J Neurotrauma), uptake via Nunn et al. 2016 |
| Missing equity dimension | Huang, Smilowitz & Balcik 2012 (Transp Res E) |

## Caveats

- Davidson & Duclos are two distinct papers: 2000 (Econometrica) for the formal definition and
  inference machinery, 2013 (Econometric Reviews, *Testing for Restricted Stochastic Dominance*)
  for the empirical-likelihood test on discrete supports. Cite the right one per claim.
- The mRS analogy is structural, not domain-based. State that explicitly when you use it, so no
  reviewer thinks you are claiming clinical equivalence.
- Two claims in this file are about what a source *argues*, not what it *is*, and are worth
  reading before you lean on them: whether Beamon & Balcik really carry the 3E triad (§G), and
  whether Savitz supports ordinal-over-binary (§A — it does not; see the note there).
- Everything else was verified against the publisher record on 2026-08-04. Corrections applied in
  this revision: OAST → Ganesh et al. attribution (§A); Bengio/Albanie → PMLR volume editors (§D);
  PMC ID → Cremen 2025 (§F); Wang, Q. → Wang & Sun, IJDRR (§G); 3E triad → Huang et al. (§G);
  Murray et al. 2005 resolved (§H); Zobel 2010 → 2011; McFadden venue added.
