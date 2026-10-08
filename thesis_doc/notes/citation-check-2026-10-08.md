# Citation check, 2026-10-08
Scope: whole report (`main.tex`, `inc/*.tex`, `alg/*`, `pics/*.tex`; citations occur only in `inc/*.tex`). Citation uses: 99. Distinct sources: 49.

Verdict labels follow the verifier table. The caller's labels map as: SUPPORTED = OK; PARTLY SUPPORTED = CLAIM-MISMATCH (partial); bib field differences = BIB-ERROR; UNVERIFIABLE = UNVERIFIABLE; no key is MISSING-KEY.

Reading constraints this session: no PDF renderer was available, so PDF-only sources were read through a text proxy (`r.jina.ai`) where it worked (FwDV 100, Rao 1995, Gelman 2014) and otherwise judged from the abstract. Crossref and Semantic Scholar rate-limited heavily; OpenAlex and Europe PMC filled the gaps.

## Summary
| Verdict | Count |
| --- | --- |
| SUPPORTED | 85 |
| PARTLY SUPPORTED | 12 |
| NOT SUPPORTED | 0 |
| CONTRADICTED | 0 |
| UNVERIFIABLE | 2 |

Bib entries with errors: 3 (ganesh2018, piaggio2012, gelman2014; plus two optional improvements: reichert2012 subtitle, wang2024 published version). Keys missing from the bib: 0.

## Fix first

1. `inc/intro.tex:25` yin2024, PARTLY SUPPORTED. The abstract says elderly people are "a large proportion of flood fatalities" and that plans "primarily focus on the evacuation of the general public"; it names shelter capacity, not elderly transport, as the binding constraint. Nothing reached says that moving elderly people "dominates the logistics". Reword: "Studies of coastal evacuation show that elderly people make up a large share of flood deaths and that moving them needs its own planning \parencite{yin2024}." If the author has the full paper and finds a "dominates" statement, keep the sentence and add the page.
2. `inc/intro.tex:26` and `inc/casestudy.tex:23` alqahtani2025a, PARTLY SUPPORTED. The source hedges ("designers might underestimate evacuation times") and its result is one 50-agent room-egress simulation (+50 %), not a nursing-home transport operation. Reword: "Evacuation models that ignore differences in mobility can underestimate how long an evacuation takes; one simulation found about 50 % longer with mobility-impaired people included \parencite{alqahtani2025a}."
3. `inc/evaluation.tex:289-293` ganesh2018 + nunn2016, PARTLY SUPPORTED. "Stroke trials keep the ordinal modified Rankin Scale" is contradicted by the co-cited Nunn review ("Trials published since 2007 still favoured dichotomous analyses over ordinal"). Ganesh argues for ordinal analysis; most trials do not do it. Reword: "Stroke researchers argue for keeping the ordinal modified Rankin Scale for the same reason \parencite{ganesh2018}, although most trials still cut it in two and disagree about where the cut should fall \parencite{nunn2016}."
4. `inc/methods_critique.tex:245` ganesh2018, PARTLY SUPPORTED. Ganesh shows the ordinal mRS fits outcomes better than a dichotomy; it is not a power argument. The power claim is in nunn2016 ("preserving the ordinal nature of these scales increased statistical power") and, more directly, in the OAST 2007 reanalysis already in the bib (`optimisinganalysisofstroketrialsoastcollaboration2007a`). Cite one of those here.
5. `inc/evaluation.tex:469` holguin-veras2013, PARTLY SUPPORTED. The paper keeps logistic cost inside its objective (social cost = logistic cost + deprivation cost); it argues that cost alone is the wrong objective, not that operational cost "is not the outcome that matters". Reword: "since humanitarian logistics argues that the cost of human suffering, and not only the operational cost, must enter the objective \parencite{holguin-veras2013}."
6. `inc/intro.tex:52` cemri2025, PARTLY SUPPORTED. Cemri et al. study why multi-agent LLM systems fail; they are not "the critical literature on LLM planning". Either cite kambhampati2024 here, or reword to "The critical literature on LLM agents gives reasons for doubt \parencite{kambhampati2024,cemri2025}."
7. `inc/workflow_baseline.tex:58` fwdv100 [23], PARTLY SUPPORTED. FwDV 100 §3.2.5: level C is "Führen mit einer Führungsgruppe", level D is "Führen mit einer Führungsgruppe beziehungsweise mit einem Führungsstab". A staff (Führungsstab) belongs to level D only; level C has a command group. Reword: "which calls for one commander supported by a command group or, at level D, a command staff \cite[23]{fwdv100}."
8. `inc/workflow_baseline.tex:55` buck2006, chang2017, PARTLY SUPPORTED. Neither source says ICS is "the best-studied command system". Chang's review shows a long literature; Buck is one evaluation. Reword: "a well-studied command system".
9. `inc/background.tex:22` chang2017, PARTLY SUPPORTED. The cited sentence is fine; the next sentence "ICS sits on the mechanistic side" states as settled what Chang presents as the open debate ("The majority of ICS debates can be related to the discussions of using a mechanistic system or an organic system"). Reword: "Whether ICS is mechanistic or organic is itself debated; its formal structure is mechanistic."
10. `inc/data_architecture.tex:428` yuan2025, PARTLY SUPPORTED. The source names batch size, continuous batching, GPU count and type, and floating-point non-associativity. It does not name "cache state" as a cause (KV cache appears only as a memory cost in §4). Drop "and cache state" or replace with "and GPU configuration".
11. `inc/intro.tex:41` and `inc/background.tex:33` reichert2012, UNVERIFIABLE. Only the book's metadata and chapter list were reachable (Ch. 6 "Exception Handling", pp. 127-151; Ch. 7 "Ad hoc Changes of Process Instances", pp. 153-217). The structure matches the anticipated/unanticipated split, but no sentence could be read. The author should add a chapter pinpoint (likely `\parencite[Ch.~6]{reichert2012}`) after checking a copy.
12. Bib fixes: ganesh2018 add `pages = {e1951--e1960}`; piaggio2012 `pages = {2594--2604}`; gelman2014 `pages = {460--465}`. Optional: reichert2012 title subtitle "Challenges, Methods, Technologies"; wang2024 has a peer-reviewed version (ACL 2024, pp. 6106-6131, DOI 10.18653/v1/2024.acl-long.331) that could replace the arXiv entry.
13. FwDV 100 pinpoints (`inc/workflow_baseline.tex:58,60,71,73,173`): the bib cites the Würzburg "Ausgabe 08/2004, Stand 1999"; only the 1999 Saxony print was readable. Its pages are 3.2.5 at p. 24, 3.3 at p. 25, 3.3.3.2 at p. 38, which sit one page after the thesis pinpoints 23, 24-25 and 37. The content matches; the author should confirm the page numbers against the 2004 copy.

## Per source

### adams2007: Adams et al. 2007, Dynamic, Extensible and Context-Aware Exception Handling for Workflows
Source reached: abstract only (companion BPM Center report abstract via search; Crossref metadata) - https://doi.org/10.1007/978-3-540-76848-7_8
Bib entry: OK (Crossref: authors, title, pages 95-112, Springer, 2007 match).

- `inc/background.tex:39` - **SUPPORTED**
  Claim: "Worklets, for example, select a prepared sub-process that fits the current context."
  Source: the system "selects among them at runtime, based on the context of the exception and the specific work instance" (abstract of the companion report; the OTM chapter abstract in the bib says the same).
  Note: abstract-level support for the paper's main contribution.

### alqahtani2025a: Alqahtani et al. 2025, Inclusive crowd evacuation modeling under heterogeneous mobility constraints
Source reached: full text (Europe PMC PMC12511302) - https://europepmc.org/articles/PMC12511302
Bib entry: OK (Sci Rep 15(1), art. 35337, 2025, DOI matches).

- `inc/intro.tex:26` - **PARTLY SUPPORTED**
  Claim: "Models that ignore differences in mobility underestimate how long the operation takes."
  Source: "Traditional evacuation models often assume a homogeneous crowd with average mobility" and "Without inclusive modeling, designers might underestimate evacuation times and conditions" (Introduction); "the presence of disabled individuals increased total evacuation time by approximately 50%" (Abstract).
  Note: the source hedges ("might") and its evidence is one room-egress simulation with 50 agents, not a transport operation. See Fix first 2.
- `inc/casestudy.tex:23` - **PARTLY SUPPORTED**
  Claim: "Evacuation models that ignore differences in mobility underestimate how long such an operation takes."
  Source: as above.
  Note: same rewording as Fix first 2.
- `inc/conclusion.tex:110` - **SUPPORTED**
  Claim: "Modelling them individually, for example with different mobility needs, would make it possible to ask about equity."
  Source: the paper's model "includes wheelchair users and visually impaired individuals, adjusting parameters such as speed, body size, and barrier navigation" (Abstract, paraphrased).

### bigley2001a: Bigley and Roberts 2001, The Incident Command System
Source reached: abstract only (secondary indexing sites; Crossref and OpenAlex metadata) - https://doi.org/10.5465/3069401
Bib entry: OK (AMJ 44(6), 1281-1299, 2001).

- `inc/background.tex:23` - **SUPPORTED**
  Claim: "Bigley and Roberts show that such a bureaucratic system can respond in a flexible and reliable way when the situation keeps changing."
  Source: "three main factors enabling this distinctively bureaucratic system to produce remarkably flexible and reliable organizations for complex, volatile task environments" (Abstract).

### buck2006: Buck, Trainor and Aguirre 2006, A Critical Evaluation of the ICS and NIMS
Source reached: abstract only (OpenAlex, Crossref) - https://doi.org/10.2202/1547-7355.1252
Bib entry: OK. RePEc lists this as article 4 of 3(3) with 29 pages; the bib has no pages or article number, which is acceptable for this online-only journal.

- `inc/background.tex:26` - **SUPPORTED**
  Claim: "Buck et al. find that ICS works less well when many independent organizations must cooperate, and that it has trouble absorbing help that was not part of the plan."
  Source: "It works best when those utilizing it are part of a community, when the demands being responded to are routine to them, and when social and cultural emergence is at a minimum" (Abstract).
  Note: fair paraphrase of the abstract's main finding.
- `inc/workflow_baseline.tex:55` - **PARTLY SUPPORTED**
  Claim: "it is the best-studied command system in the research literature."
  Source: nothing in the abstract makes a "best-studied" claim.
  Note: see Fix first 8.

### cemri2025: Cemri et al. 2025, Why Do Multi-Agent LLM Systems Fail?
Source reached: abstract (arXiv 2503.13657 v3) and NeurIPS 2025 poster page - https://arxiv.org/abs/2503.13657
Bib entry: OK for authors and title. The neurips.cc page lists the paper as a "Spotlight Poster" and does not show the track; the bib's "Datasets and Benchmarks Track" could not be confirmed or refuted.

- `inc/intro.tex:52` - **PARTLY SUPPORTED**
  Claim: "The critical literature on LLM planning gives reasons for doubt."
  Source: the paper is about multi-agent failure modes (MAST taxonomy: "system design issues", "inter-agent misalignment", "task verification"), not about LLM planning.
  Note: see Fix first 6.
- `inc/background.tex:123` - **SUPPORTED**
  Claim: "study execution traces from several popular frameworks and build a taxonomy ... three groups: poor system design, poor alignment between agents, and poor checking of whether the task is done."
  Source: "1600+ annotated traces collected across 7 popular MAS frameworks"; "14 unique modes, clustered into 3 categories: (i) system design issues, (ii) inter-agent misalignment, and (iii) task verification" (Abstract).
- `inc/discussion.tex:150` - **SUPPORTED**
  Claim: "name poor checking of task completion as one of three main failure groups."
  Source: "(iii) task verification" (Abstract).

### chang2017: Chang 2017, A literature review and analysis of the incident command system
Source reached: abstract only (Inderscience page, OpenAlex) - https://doi.org/10.1504/IJEM.2017.081193
Bib entry: OK (IJEM 13(1), 50-67, 2017).

- `inc/background.tex:22` - **PARTLY SUPPORTED**
  Claim: "Research on ICS describes a tension between two kinds of organization. A mechanistic organization works by rules and a clear hierarchy. An organic one adapts its structure to the situation. ICS sits on the mechanistic side."
  Source: "The majority of ICS debates can be related to the discussions of using a mechanistic system or an organic system" (Abstract).
  Note: the cited sentence is supported; the follow-on "ICS sits on the mechanistic side" is what Chang presents as debated. See Fix first 9.
- `inc/workflow_baseline.tex:55` - **PARTLY SUPPORTED**
  Claim: "best-studied command system in the research literature."
  Note: see Fix first 8.

### clopper1934: Clopper and Pearson 1934, The use of confidence or fiducial limits
Source reached: metadata (Crossref) - https://doi.org/10.1093/biomet/26.4.404
Bib entry: OK.

- `inc/evaluation.tex:553` - **SUPPORTED**
  Claim: "an exact Clopper-Pearson interval."
  Note: standard method citation; metadata match is sufficient.

### cohen1988: Cohen 1988, Statistical Power Analysis for the Behavioral Sciences
Source reached: none (book, no open copy; standard reference) 
Bib entry: OK (2nd ed., Erlbaum, 1988).

- `inc/methods_critique.tex:247` - **SUPPORTED**
  Claim: "The minimum detectable effect is stated before any run."
- `inc/design_considerations.tex:91` - **SUPPORTED**
  Claim: "state the smallest effect the design can detect."
  Note: both are method citations for power analysis, which is the book's subject.

### cohen1990: Cohen and Levesque 1990, Intention is choice with commitment
Source reached: abstract only (jmvidal library; Crossref metadata) - https://doi.org/10.1016/0004-3702(90)90055-5
Bib entry: OK (AIJ 42(2-3), 213-261).

- `inc/background.tex:93` - **SUPPORTED**
  Claim: "describe an intention as a choice with commitment. The agent keeps it until it believes the goal is reached, believes the goal can no longer be reached, or the reason for the goal is gone."
  Source: "By making explicit the conditions under which an agent can drop his goals" (Abstract); the abstract also says intentions are adopted "relative to a background of relevant beliefs and other intentions or goals".
  Note: the exact three-part drop condition is the paper's persistent-goal definition, but it was not read in the body; the title and abstract carry the claim.
- `inc/design_considerations.tex:32` - **SUPPORTED**
  Claim: "an agent should keep an intention until it has a reason to drop it."
  Source: as above.

### efron1979: Efron 1979, Bootstrap Methods: Another Look at the Jackknife
Source reached: abstract (Project Euclid) - https://doi.org/10.1214/aos/1176344552
Bib entry: OK (Ann. Statist. 7(1), 1-26).

- `inc/evaluation.tex:536` - **SUPPORTED**
  Claim: "95 % percentile bootstrap interval."
  Source: "A general method, called the 'bootstrap', is introduced" (Abstract).
- `inc/results.tex:189` - **SUPPORTED**
  Claim: "bootstrap confidence intervals."

### fema2017: DHS/FEMA 2017, National Incident Management System, 3rd Edition
Source reached: official document listing (training.fema.gov PDF title; fema.gov NIMS pages) - https://www.fema.gov/sites/default/files/2020-07/fema_nims_doctrine-2017.pdf
Bib entry: OK (document is titled "National Incident Management System, Third Edition, October 2017").

- `inc/workflow_baseline.tex:53` - **SUPPORTED**
  Claim: "Its doctrine is written down in the National Incident Management System (NIMS) guidance."
  Source: FEMA's NIMS components page describes ICS as "a management system designed to enable effective and efficient domestic incident management".

### fwdv100: FwDV 100 (2004 Würzburg edition, text of 1999)
Source reached: full text of the 1999 Saxony print (via text proxy) - https://www.lfs.sachsen.de/download/fwdv100.pdf ; Bavarian introduction notice of 10 Aug 2004 - https://www.gesetze-bayern.de/Content/Document/BayVwV96946
Bib entry: OK. The Bavarian notice (AllMBl. 2004 S. 376) confirms the August 2004 Bavarian edition distributed via the Staatliche Feuerwehrschule Würzburg. Page pinpoints below are checked against the 1999 Saxony print, whose pages run one higher than the thesis pinpoints (Fix first 13).

- `inc/intro.tex:37` - **SUPPORTED**
  Claim: "In Germany such operations follow a written doctrine, DV 100."
  Source: the regulation "regelt Grundsätzliches für die Führungsarbeit der Feuerwehren" (Bavarian notice).
- `inc/background.tex:29` - **SUPPORTED**
  Claim: "German fire services and civil protection follow a comparable doctrine, DV 100."
  Source: Brandenburg decree of 27 Oct 1999 applies it as "Feuerwehr- und Katastrophenschutz-Dienstvorschrift 100".
- `inc/workflow_baseline.tex:48` - **SUPPORTED**
  Claim: "the German service regulation DV 100, Command and Control in Operations, under which the Hamburg fire service works."
  Note: title confirmed; the Hamburg-specific adoption was not checked (FwDV 100 is a nationwide recommendation).
- `inc/workflow_baseline.tex:58` [23] - **PARTLY SUPPORTED**
  Claim: "a level C or D incident, which calls for one commander with a staff."
  Source: §3.2.5 (p. 24, 1999 print): level C "Führen mit einer Führungsgruppe"; level D "Führen mit einer Führungsgruppe beziehungsweise mit einem Führungsstab".
  Note: see Fix first 7.
- `inc/workflow_baseline.tex:60` [13-14] - **SUPPORTED**
  Claim: "The IC implements three of the staff functions. The situation function (S2) keeps the situation picture. The operations function (S3) plans the mission... The logistics function (S4) turns a decision into transport, escort and medical orders."
  Source: Anlage 2 (pp. 52-56, 1999 print): S2 Lage "Beschaffen von Informationen", "Führen einer Lagekarte"; S3 Einsatz "Beurteilen der Lage", "Erteilen der Befehle"; S4 Versorgung "Bereitstellen von Verbrauchsgütern und Einsatzmitteln".
  Note: the Sachgebiete are listed under §3.2.2 Einsatzleitung (from p. 11) and detailed in Anlage 2; pp. 13-14 in the 2004 copy is plausible but unchecked.
- `inc/workflow_baseline.tex:71` [24-25] - **SUPPORTED**
  Claim: "DV 100 describes command as a repeating cycle, the command process, with three stages: situation assessment, planning and issuing orders."
  Source: §3.3 (p. 25): "Lagefeststellung (Erkundung der Lage / Kontrolle)", "Planung", "Befehlsgebung".
- `inc/workflow_baseline.tex:73` [24] - **SUPPORTED**
  Claim: "Control comes from repeating the situation assessment, which checks whether the orders are still right."
  Source: §3.3 (p. 25): "Nur durch die wiederholte Lagefeststellung wird die unbedingt notwendige Kontrolle über die Durchführung und Richtigkeit der gegebenen Befehle sichergestellt".
- `inc/workflow_baseline.tex:173` [37] - **SUPPORTED**
  Claim: "DV 100 requires a report back when the situation no longer matches the order. It does not describe a holding order."
  Source: §3.3.3.2 (p. 38): "Wer vom gegebenen Befehl abweichen muss, muss umgehend eine Rückmeldung machen."; §3.3.1.3 (p. 29) lists reporting "bei Undurchführbarkeit erhaltener Einsatzaufträge".
- `inc/methods_critique.tex:298` - **SUPPORTED**
  Claim: "45 of the 87 entries are cited to a page of the doctrine."
  Note: the citation only names the doctrine; no claim about its content.
- `inc/conclusion.tex:6` - **SUPPORTED**
  Claim: "a workflow baseline that follows the DV 100 doctrine."

### ganesh2018: Ganesh et al. 2018, Ordinal vs dichotomous analyses of modified Rankin Scale
Source reached: abstract (OpenAlex) - https://doi.org/10.1212/WNL.0000000000006554
Bib entry: pages missing; source says e1951-e1960 (Neurology 91(21)).

- `inc/evaluation.tex:291` - **PARTLY SUPPORTED**
  Claim: "Stroke trials keep the ordinal modified Rankin Scale for the same reason."
  Source: the ordinal mRS "was more strongly associated with 5-year mortality than either dichotomy" and the authors argue this "favors ordinal analysis in trials" (Abstract, paraphrased).
  Note: Ganesh argues for ordinal analysis; the co-cited Nunn review shows most trials still dichotomise. See Fix first 3.
- `inc/methods_critique.tex:245` - **PARTLY SUPPORTED**
  Claim: "reducing an outcome to a direction throws power away."
  Note: Ganesh is a goodness-of-fit comparison, not a power analysis. See Fix first 4.

### gelernter1985: Gelernter 1985, Generative communication in Linda
Source reached: abstract (OpenAlex; Crossref metadata) - https://doi.org/10.1145/2363.2433
Bib entry: OK (TOPLAS 7(1), 80-112).

- `inc/background.tex:149` - **SUPPORTED**
  Claim: "processes communicate by placing tuples in a shared space and taking them out again, without knowing each other."
  Source: messages are added "in tuple-structured form to the computation environment, where they exist as named, independent entities until some process chooses to receive them"; Linda is "fully distributed in space and distributed in time" (Abstract).
- `inc/data_architecture.tex:42` - **SUPPORTED**
  Claim: "tuple spaces did so decades before this work."

### gelman2014: Gelman and Loken 2014, The Statistical Crisis in Science
Source reached: full text (author copy via text proxy) - http://www.stat.columbia.edu/~gelman/research/published/ForkingPaths.pdf
Bib entry: pages: bib says 460, source says 460-465 (American Scientist 102(6)).

- `inc/evaluation.tex:608` - **SUPPORTED**
  Claim: "Choices made after seeing data bias a result even without intent, and hypotheses written after the results misrepresent what was tested."
  Source: "the researchers are not trying multiple tests to see which has the best p-value"; "they refine that idea in light of the data"; "defining the entire data-collection and analysis protocol ahead of time" (text, no page numbers in the proxy output).
- `inc/methods_critique.tex:21` - **SUPPORTED**
  Claim: "choices made after seeing the data can bias a result even without intent."
- `inc/design_considerations.tex:95` - **SUPPORTED**
  Claim: "each such choice opens a path the analysis could have taken differently."
  Source: the article's "garden of forking paths" framing.

### hevner2004: Hevner et al. 2004, Design Science in Information Systems Research
Source reached: abstract (OpenAlex) - https://doi.org/10.2307/25148625
Bib entry: OK (MISQ 28(1), 75-106).

- `inc/intro.tex:71` - **SUPPORTED**
  Claim: "design science research, which builds an artifact and then evaluates it."
  Source: in design science, knowledge of a problem and its solution "are achieved in the building and application of the designed artifact" (Abstract).

### holguin-veras2013: Holguín-Veras et al. 2013, On the appropriate objective function for post-disaster humanitarian logistics models
Source reached: abstract (OpenAlex; Crossref metadata) - https://doi.org/10.1016/j.jom.2013.06.002
Bib entry: OK (JOM 31(5), 262-280).

- `inc/background.tex:194` - **SUPPORTED**
  Claim: "argue that such models should minimize social cost. This adds the cost of human suffering from late or missing supplies to the cost of the logistics itself."
  Source: recommends "social costs, meaning logistics costs plus deprivation costs, as the preferred objective function"; deprivation cost is "the economic value of the suffering caused by lacking access to a good or service" (Abstract, paraphrased).
- `inc/evaluation.tex:469` - **PARTLY SUPPORTED**
  Claim: "operational cost is not the outcome that matters in a disaster."
  Note: the source keeps logistic cost inside the objective. See Fix first 5.

### holm1979: Holm 1979, A Simple Sequentially Rejective Multiple Test Procedure
Source reached: metadata (OpenAlex) - Scand. J. Statist. 6, 65-70
Bib entry: OK.

- `inc/evaluation.tex:556` - **SUPPORTED**
  Claim: "Holm-Bonferroni correction."

### hong2024: Hong et al. 2024, MetaGPT
Source reached: abstract (arXiv 2308.00352) and ICLR 2024 proceedings listing - https://proceedings.iclr.cc/paper_files/paper/2024/hash/6507b115562bb0a305f1958ccc87355a-Abstract-Conference.html
Bib entry: OK. The ICLR proceedings list the third author as "Jonathan Chen" (arXiv has "Jiaqi Chen"); the bib follows ICLR. The page range 23247-23275 and the editor list could not be checked.

- `inc/background.tex:75` - **SUPPORTED**
  Claim: "writes human standard operating procedures into the prompts of role-specialized agents and passes work along an assembly line."
  Source: encodes "Standardized Operating Procedures (SOPs) into prompt sequences" and uses "an assembly-line paradigm to assign roles" (Abstract).

### huang2012: Huang, Smilowitz and Balcik 2012, Models for relief routing
Source reached: abstract (institutional repository summary; Crossref metadata) - https://doi.org/10.1016/j.tre.2011.05.004
Bib entry: OK (TR-E 48(1), 2-18).

- `inc/background.tex:192` - **SUPPORTED**
  Claim: "define performance measures for relief routing and show that efficiency, efficacy and equity can pull in different directions."
  Source: the paper formalises metrics for "efficacy" and "equity" and studies "how efficiency, efficacy, and equity shape vehicle route structure" (Abstract, paraphrased); "Humanitarian relief is complicated by the presence of multiple objectives beyond minimizing cost".
- `inc/methods_critique.tex:320` - **SUPPORTED**
  Claim: "Relief logistics treats equity as an objective of its own."

### huang2024: Huang et al. 2024, Large Language Models Cannot Self-Correct Reasoning Yet
Source reached: abstract (arXiv 2310.01798, comment "ICLR 2024") - https://arxiv.org/abs/2310.01798
Bib entry: OK for authors, title, venue; pages 32808-32824 unchecked.

- `inc/background.tex:117` - **SUPPORTED**
  Claim: "when a model corrects its own reasoning without outside feedback, the result often gets worse."
  Source: "LLMs struggle to self-correct their responses without external feedback", and performance "sometimes gets worse after self-correction" (Abstract).
- `inc/discussion.tex:146` - **SUPPORTED**
  Claim: "self-correction without outside feedback often makes results worse."
  Note: "often" is slightly stronger than the abstract's "sometimes"; acceptable paraphrase, but "can make results worse" would be exact.

### kambhampati2024: Kambhampati et al. 2024, LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks
Source reached: abstract (PMLR v235 page) - https://proceedings.mlr.press/v235/kambhampati24a.html
Bib entry: OK (PMLR 235, 22895-22907).

- `inc/background.tex:112` - **SUPPORTED**
  Claim: "an LLM on its own can neither plan reliably nor check its own plans ... leave the checking to a sound external verifier."
  Source: "auto-regressive LLMs cannot, by themselves, do planning or self-verification"; "LLM-Modulo Frameworks that combine the strengths of LLMs with external model-based verifiers" (Abstract).
- `inc/agentic_system.tex:257` - **SUPPORTED**
  Claim: "the advice to pair a language model with an external checker instead of trusting its plans directly."
- `inc/discussion.tex:145` - **SUPPORTED**
  Claim: "an LLM cannot reliably check its own plans and needs an external verifier."

### lee2025: Lee et al. 2025, Evaluating the Predictability of Disaster Evacuation Behavior using LLM Agent Simulations
Source reached: abstract (OpenAlex) - https://doi.org/10.1145/3764925.3770907
Bib entry: OK (UMFM workshop, pp. 19-21, 2025).

- `inc/background.tex:170` - **SUPPORTED**
  Claim: "give LLM agents synthetic personas built from mobility and demographic data, and ask how well they predict real evacuation decisions."
  Source: examines "whether synthetic personas grounded in pre-disaster demographic information make realistic decisions" and compares simulations "with real-world mobility data" (Abstract, paraphrased).

### li2026: Li, Das and Shirado 2026, What Makes LLM Agent Simulations Useful for Policy Practice?
Source reached: abstract (arXiv 2509.21868 v2) - https://arxiv.org/abs/2509.21868
Bib entry: OK.

- `inc/background.tex:176` - **SUPPORTED**
  Claim: "ran a long design study with emergency-preparedness practitioners. They conclude that LLM agent simulations are more useful for shaping procedures and training than for predicting outcomes."
  Source: "year-long, stakeholder-engaged design process with a university emergency preparedness team"; "Rather than producing predictive forecasts, these simulations supported policy practice" by "shaping volunteer training, evacuation procedures, and infrastructure planning" (Abstract).

### lipsitch2010: Lipsitch, Tchetgen Tchetgen and Cohen 2010, Negative Controls
Source reached: abstract (PubMed Central) - https://pmc.ncbi.nlm.nih.gov/articles/PMC3053408/
Bib entry: OK (Epidemiology 21(3), 383-388).

- `inc/evaluation.tex:379` - **SUPPORTED**
  Claim: "It is also the instrument's negative control."
  Source: negative controls are "designed to detect both suspected and unsuspected sources of spurious causal inference" (Abstract).
  Note: the thesis borrows an epidemiological concept by analogy; the sentence makes this clear.
- `inc/methods_critique.tex:47` - **SUPPORTED**
  Claim: "The protocol's own negative control confirms this."
- `inc/design_considerations.tex:83` - **SUPPORTED**
  Claim: "A no-replan control checks this."

### nii1986: Nii 1986, Blackboard Application Systems
Source reached: abstract (AAAI OJS page) - https://doi.org/10.1609/aimag.v7i3.550
Bib entry: OK (AI Magazine 7(3), 82-106). The DOI returned 404 from the Crossref API but resolves on the publisher's site.

- `inc/background.tex:147` - **SUPPORTED**
  Claim: "The classic example is the Hearsay-II speech recognizer."
  Source: "The first blackboard system was the Hearsay-II speech-understanding system" (Abstract).
- `inc/data_architecture.tex:41` - **SUPPORTED**
  Claim: "Blackboard systems ... did so decades before this work."

### nosek2018: Nosek et al. 2018, The preregistration revolution
Source reached: abstract (OpenAlex) - https://doi.org/10.1073/pnas.1708274114
Bib entry: OK (PNAS 115(11), 2600-2606).

- `inc/evaluation.tex:609` - **SUPPORTED**
  Claim: "Pre-registration guards against both."
  Source: "An effective solution is to define the research questions and analysis plan before observing the outcomes"; "Mistaking generation of postdictions with testing of predictions reduces the credibility of research findings" (Abstract).

### nunn2016: Nunn, Bath and Gray 2016, Analysis of the Modified Rankin Scale in RCTs of Acute Ischaemic Stroke
Source reached: full text (Europe PMC PMC4818820) - https://europepmc.org/articles/PMC4818820
Bib entry: OK (Stroke Res Treat 2016, 1-7).

- `inc/evaluation.tex:293` - **SUPPORTED**
  Claim: "they disagree about where a single cut should fall."
  Source: "Outcome was deemed favourable for mRS scores of 0-1 and 0-2 in equal numbers of studies, 10 (23.8%) for each"; "Only one (2.4%) study defined a favourable outcome to be an mRS score of 0-3" (Sec. 3.3).
  Note: the same source says "Trials published since 2007 still favoured dichotomous analyses over ordinal" (Abstract), which bears on the first half of the sentence (Fix first 3).

### omicini1999: Omicini and Zambonelli 1999, Coordination for Internet Application Development
Source reached: abstract (Semantic Scholar; Crossref metadata) - https://doi.org/10.1023/A:1010060322135
Bib entry: OK (AAMAS 2(3), 251-269).

- `inc/background.tex:151` - **SUPPORTED**
  Claim: "Later tuple spaces became reactive. They can run code when a tuple arrives, so a process reacts to new data without asking for it again and again."
  Source: "tuple centres, whose behaviour can be defined so as to embody the laws of coordination" (Abstract).
  Note: abstract-level support for programmable (reactive) tuple centres; the "without polling" phrasing is the thesis's own gloss.
- `inc/data_architecture.tex:324` - **SUPPORTED**
  Claim: "Reactive tuple spaces solve the same problem by running code when new data arrives."

### oumeraci2015a: Oumeraci et al. 2015, XtremRisK
Source reached: abstract (OpenAlex) - https://doi.org/10.1142/S057856341540001X
Bib entry: OK (CEJ 57(1), 1540001).

- `inc/casestudy.tex:12` - **SUPPORTED**
  Claim: "Risk studies for the German Bight and the Elbe estuary model how such surges develop and which areas they reach."
  Source: the project developed "physically possible extreme storm surge" scenarios and a "source-pathway-receptor" flood risk analysis for "two selected pilot sites (representative for an open coast and an urban estuarine area in Germany)" (Abstract).
  Note: the abstract does not name the Elbe; the estuarine pilot site is Hamburg in the project literature, which the author may wish to pinpoint.

### overeem2021: Overeem et al. 2021, An Empirical Characterization of Event Sourced Systems and Their Schema Evolution
Source reached: full text (ar5iv of arXiv 2104.01146) - https://ar5iv.labs.arxiv.org/html/2104.01146
Bib entry: OK (JSS 178, 110970).

- `inc/background.tex:157` - **SUPPORTED**
  Claim: "An industry study finds this useful for audits and replay but notes that it makes schema changes harder."
  Source: "they provide audit functionality" (Sec. 1); "a projection can be rebuilt from its source events at any point" (Sec. 5.2); "the most prominent challenge encountered in ESSs: schema evolution" (Sec. 1); "event schema evolution in ESSs is difficult" (Sec. 7).
- `inc/data_architecture.tex:50` - **SUPPORTED**
  Claim: "event sourcing, where the history of events is stored and every later view is derived from it."
  Source: Sec. 5.2 as above.

### park2023: Park et al. 2023, Generative Agents
Source reached: abstract (arXiv 2304.03442; OpenAlex metadata) - https://doi.org/10.1145/3586183.3606763
Bib entry: OK (UIST 2023, 1-22).

- `inc/background.tex:68` - **SUPPORTED**
  Claim: "places 25 agents with memory, reflection and planning in a small simulated town, and human raters find their social behaviour believable."
  Source: a sandbox town "of 25 agents"; the architecture records experiences, synthesises "higher-level reflections" and retrieves them "to plan behavior"; ablations showed "observation, planning, and reflection each contribute to believability" (Abstract, paraphrased).
  Note: the human-rater detail is in the paper's evaluation section, not read here.

### piaggio2012: Piaggio et al. 2012, Reporting of Noninferiority and Equivalence Randomized Trials
Source reached: abstract (Europe PMC) - https://doi.org/10.1001/jama.2012.87802
Bib entry: pages: bib says 2594, source says 2594-2604 (JAMA 308(24)).

- `inc/evaluation.tex:336` - **SUPPORTED**
  Claim: "We take the non-inferiority margin from clinical trials."
  Source: "updated extension of the CONSORT checklist for reporting noninferiority and equivalence trials" (Abstract).
  Note: the margin itself is a checklist item in the body; the sentence only borrows the concept.

### rao1995: Rao and Georgeff 1995, BDI Agents: From Theory to Practice
Source reached: full text (AAAI scan via text proxy, OCR) - https://cdn.aaai.org/ICMAS/1995/ICMAS95-042.pdf
Bib entry: OK (ICMAS-95, pp. 312-319).

- `inc/background.tex:90` - **SUPPORTED**
  Claim: "an agent holds beliefs about the world, desires it would like to reach, and intentions it has chosen to act on. Rao and Georgeff explain why a practical agent needs intentions at all. The world changes while the agent acts, and the agent cannot afford to plan again from the start at every change."
  Source: "beliefs can be viewed as the informative component of system state" (p. 313); desires represent "the motivational state of the system" (p. 314); "the intentions of the system capture the deliberative component of the system" (p. 314); "re-considering the choice of action at each step is potentially too expensive" (p. 314).
- `inc/discussion.tex:101` - **SUPPORTED**
  Claim: "In agent theory, an intention is a plan the agent keeps until it has a reason to drop it."
  Source: "In a continuously changing environment, commitment lends a certain sense of stability to the reasoning process of an agent" (p. 315); "unconditional commitment to the chosen course of action can result in the system failing to achieve its objectives" (p. 314).
  Note: cohen1990 is the sharper source for drop conditions; citing both would be stronger.

### reichert2012: Reichert and Weber 2012, Enabling Flexibility in Process-Aware Information Systems
Source reached: metadata only (Springer book page; Crossref chapter records) - https://doi.org/10.1007/978-3-642-30409-5
Bib entry: title lacks the subtitle "Challenges, Methods, Technologies" (optional fix); otherwise OK.

- `inc/intro.tex:41` - **UNVERIFIABLE**
  Claim: "Research on business processes calls these anticipated exceptions. It separates them from unanticipated exceptions, which a fixed script cannot handle by itself."
  Reached: chapter list only (Ch. 6 "Exception Handling", pp. 127-151; Ch. 7 "Ad hoc Changes of Process Instances", pp. 153-217), consistent with the claim but no sentence readable. A copy is on SpringerLink (institutional access) or in the author's Zotero if present.
- `inc/background.tex:33` - **UNVERIFIABLE**
  Claim: "separate two kinds of exceptions. An anticipated exception is one the designer foresaw ... An unanticipated exception is one nobody foresaw. It needs a change to the running process."
  Note: add a chapter pinpoint once checked (Fix first 11).

### shinn2023: Shinn et al. 2023, Reflexion
Source reached: full text (ar5iv of arXiv 2303.11366) and NeurIPS proceedings page - https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html
Bib entry: OK (five authors as in the NeurIPS version; DOI 10.52202/075280-0377 confirmed on the proceedings page; pages unchecked).

- `inc/background.tex:61` - **SUPPORTED**
  Claim: "the agent writes a short reflection on its own performance and keeps it in memory for the next attempt. The authors also note that this works best when the agent receives a clear signal about what went wrong."
  Source: "Reflexion converts binary or scalar feedback from the environment into verbal feedback in the form of a textual summary" (Sec. 1); "This feedback ... is then stored in the agent's memory" (Sec. 3); "Generating useful reflective feedback is challenging since it requires a good understanding of where the model made mistakes" (Sec. 1); "the agent does not generate helpful, intuitive self-reflections after failed attempts" (App. B.1, WebShop limitation).
  Note: fair paraphrase; the source frames it as a limitation rather than "works best when".
- `inc/agentic_system.tex:421` - **SUPPORTED**
  Claim: "no reflection step after a failure as in Reflexion."

### simonsohn2020: Simonsohn, Simmons and Nelson 2020, Specification curve analysis
Source reached: abstract (Europe PMC) - https://doi.org/10.1038/s41562-020-0912-z
Bib entry: OK (Nat Hum Behav 4(11), 1208-1214).

- `inc/evaluation.tex:599` - **SUPPORTED**
  Claim: "It is a small specification curve."
  Source: "(1) identifying the set of theoretically justified, statistically valid and non-redundant specifications; (2) displaying the results graphically ... (3) conducting joint inference across all specifications" (Abstract).
- `inc/results.tex:248` - **SUPPORTED**
  Claim: "a cut-point sensitivity analysis."
- `inc/methods_critique.tex:232` - **SUPPORTED**
  Claim: "The cut-point sensitivity analysis was added under the same amendment."

### stechly2024: Stechly, Valmeekam and Kambhampati 2024, On the Self-Verification Limitations of LLMs
Source reached: abstract (arXiv 2402.08115 v2) - https://arxiv.org/abs/2402.08115
Bib entry: OK.

- `inc/background.tex:119` - **SUPPORTED**
  Claim: "Performance drops when the model criticizes its own answers and rises when a correct external checker gives the feedback."
  Source: "We observe significant performance collapse with self-critique and significant performance gains with sound external verification" (Abstract).
- `inc/discussion.tex:147` - **SUPPORTED**
  Claim: "self-correction without outside feedback often makes results worse."

### sultimov2026: Sultimov et al. 2026, RESPOND
Source reached: abstract (AAAI OJS page) - https://doi.org/10.1609/aaai.v40i48.42384
Bib entry: OK (AAAI 40(48), 41694-41696, Demonstration Track).

- `inc/background.tex:169` - **SUPPORTED**
  Claim: "couples a flood forecast with an agent-based model of the population. LLM-driven agents decide how residents evacuate, look for resources and communicate. It is a short demonstration paper and does not report a controlled comparison."
  Source: "This demo presents RESPOND, a multi-agent LLM-enhanced platform"; "LLM modules improve each agent decision-making"; "simulates evacuation flows, resource seeking, and communication patterns" (Abstract). The abstract reports no baseline or controlled comparison; the paper is three pages.

### wang2024: Wang et al. 2024, Rethinking the Bounds of LLM Reasoning
Source reached: abstract (arXiv 2402.18272) and ACL Anthology page - https://aclanthology.org/2024.acl-long.331/
Bib entry: the arXiv preprint is cited; a peer-reviewed version exists (ACL 2024 Long Papers, pp. 6106-6131, DOI 10.18653/v1/2024.acl-long.331). Optional update.

- `inc/background.tex:128` - **SUPPORTED**
  Claim: "A strong single agent with good prompts can match a multi-agent discussion."
  Source: "a single-agent LLM with strong prompts can achieve almost the same performance as the best existing discussion approach" (Abstract).
- `inc/design_considerations.tex:115` - **SUPPORTED**
  Claim: "one strong agent with good prompts can match a multi-agent discussion."

### wilcoxon1945: Wilcoxon 1945, Individual Comparisons by Ranking Methods
Source reached: metadata (OpenAlex) - https://doi.org/10.2307/3001968
Bib entry: OK (Biometrics Bulletin 1(6), 80-83).

- `inc/evaluation.tex:538` - **SUPPORTED**
  Claim: "A Wilcoxon signed-rank test."

### woods2015a: Woods 2015, Four concepts for resilience
Source reached: abstract (via RePEc listing and secondary summaries; Crossref metadata) - https://doi.org/10.1016/j.ress.2015.03.018
Bib entry: OK (RESS 141, 5-9).

- `inc/intro.tex:41` - **SUPPORTED**
  Claim: "draws a similar line between robustness against disruptions that were modelled in advance and graceful extensibility beyond them."
  Source: the four concepts include "(2) resilience as a synonym for robustness; (3) resilience as the opposite of brittleness, i.e., as graceful extensibility when surprise challenges boundaries" (Abstract).
- `inc/background.tex:42` - **SUPPORTED**
  Claim: "separates robustness from graceful extensibility. Robustness means handling disruptions that were modelled in advance. Graceful extensibility means stretching to meet a surprise that falls outside the model."
  Source: as above.

### xie2024a: Xie et al. 2024, TravelPlanner
Source reached: full text (arXiv HTML v4) - https://arxiv.org/html/2402.01622v4
Bib entry: OK (PMLR 235, 54590-54613, confirmed on proceedings.mlr.press/v235/xie24j.html).

- `inc/background.tex:185` - **SUPPORTED**
  Claim: "asks agents to build travel plans with tools and checks each plan against hard constraints and common-sense rules."
  Source: "Commonsense Constraint Pass Rate" and "Hard Constraint Pass Rate" (Sec. 3.4).
- `inc/agentic_system.tex:466` - **SUPPORTED**
  Claim: "Language agents are also known to struggle to carry a long plan through under many constraints."
  Source: "They often fail to convert their reasoning into the right actions correctly and keep track of global or multiple constraints" (Sec. 1); "current agents struggle with multi-constraint tasks" (Sec. 5.2).

### xu2025: Xu et al. 2025, TheAgentCompany
Source reached: full text (arXiv HTML v3) - https://arxiv.org/html/2412.14161v3
Bib entry: OK.

- `inc/background.tex:186` - **SUPPORTED**
  Claim: "scores agents on professional tasks in a simulated software company."
  Source: "a self-contained environment with internal web sites and data that mimics a small software company environment" (Abstract).
- `inc/evaluation.tex:302` - **SUPPORTED**
  Claim: "as some agent benchmarks do [use a language model as a judge]."
  Source: "In such cases, we employ LLM-based evaluation" (Sec. 4); "there are 51 tasks (29%) involving LLM evaluation" (App. E).
- `inc/results.tex:524` - **SUPPORTED**
  Claim: "The gap differs strongly between models, as agent benchmarks also find."
  Source: Table 1: Gemini-2.5-Pro 30.3 % success vs GPT-4o 8.6 % and Qwen-2-72b 1.1 % (Sec. 7.1).

### yalonetzky2013: Yalonetzky 2013, Stochastic Dominance with Ordinal Variables
Source reached: abstract (OpenAlex) - https://doi.org/10.1080/07474938.2012.690653
Bib entry: OK (Econometric Reviews 32(1), 126-163).

- `inc/evaluation.tex:521` - **SUPPORTED**
  Claim: "first-order stochastic dominance, which needs no arithmetic on an ordinal scale."
  Source: the paper "derives multivariate stochastic dominance conditions for ordinal variables" (Abstract, paraphrased).
- `inc/results.tex:227` - **SUPPORTED**
  Claim: "first-order stochastic dominance of the agentic system over the baseline."

### yao2023: Yao et al. 2023, ReAct
Source reached: abstract (arXiv 2210.03629, ICLR camera-ready) - https://arxiv.org/abs/2210.03629
Bib entry: OK.

- `inc/intro.tex:48` - **SUPPORTED**
  Claim: "An LLM agent observes, reasons and acts in a loop, and it can revise its plan when something unexpected happens."
  Source: reasoning traces help the model "track, and update action plans and handle exceptions" (Abstract, as summarised).
- `inc/background.tex:59` - **SUPPORTED**
  Claim: "ReAct interleaves written reasoning steps with actions. The authors argue that the reasoning helps the model track and update its plan and deal with exceptions."
- `inc/agentic_system.tex:236` - **SUPPORTED**
  Claim: "Reasoning written before the action follows ReAct."

### yin2024: Yin et al. 2024, Strategic storm flood evacuation planning for large coastal cities
Source reached: abstract and landing page (Nature via text proxy; Birmingham repository record) - https://doi.org/10.1038/s44221-024-00210-z ; accepted manuscript at https://research.birmingham.ac.uk/files/220418531/Yin_Yang_Yu_Lin_Wilby_Lane_Sun_Bricker_Wright_Yang_Guan_2024_accepted_manuscript.pdf
Bib entry: OK (Nature Water 2(3), 274-284).

- `inc/intro.tex:25` - **PARTLY SUPPORTED**
  Claim: "Studies of coastal evacuation show that moving elderly people is the part that dominates the logistics."
  Source: "existing contingency plans primarily focus on the evacuation of the general public"; elderly people "constitute a large proportion of flood fatalities"; "Storm flood evacuation is more challenging in Shanghai due to insufficient provision of shelter capacity" (Abstract).
  Note: the source makes elderly transfer a priority and shelter capacity the constraint; it does not say elderly transfer dominates the logistics. See Fix first 1.
- `inc/background.tex:196` - **SUPPORTED**
  Claim: "For coastal cities, Yin et al. plan storm-flood evacuations with a focus on moving elderly people."
  Source: title and abstract.

### yuan2025: Yuan et al. 2025, Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference
Source reached: full text (arXiv HTML v2) - https://arxiv.org/html/2506.09501v2
Bib entry: OK.

- `inc/evaluation.tex:101` - **SUPPORTED**
  Claim: "inference is not bit-exact even with a fixed seed."
  Source: "even with the same prompt and random seed, the generated output can still differ significantly" (Sec. 1); "greedy decoding does not guarantee deterministic outputs across different hardware and system configurations" (Sec. 3.2).
- `inc/data_architecture.tex:428` - **PARTLY SUPPORTED**
  Claim: "because batching and cache state inside the inference server change the sampling."
  Source: continuous batching "dynamically modifies the set of requests within a batch" (Sec. 2.2); batch size, GPU count and type are the named causes.
  Note: "cache state" is not named as a cause. See Fix first 10.
- `inc/design_considerations.tex:103` - **SUPPORTED**
  Claim: "the agentic side is not deterministic."

### zheng2023: Zheng et al. 2023, Judging LLM-as-a-Judge
Source reached: abstract (arXiv 2306.05685) and NeurIPS proceedings page - https://proceedings.neurips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract-Datasets_and_Benchmarks.html
Bib entry: OK (DOI 10.52202/075280-2020 confirmed; Datasets and Benchmarks Track).

- `inc/background.tex:187` - **SUPPORTED**
  Claim: "avoids the known biases of using an LLM as the judge."
  Source: "position, verbosity, and self-enhancement biases" (Abstract).
- `inc/evaluation.tex:301` - **SUPPORTED**
  Claim: "We do not use a language model as a judge, as is common."

## Not checked
- `alg/` and `pics/*.tex` contain no citation commands.
- Bib entries not cited anywhere (bertinetto2021, bjarnason2026, bruneau2003, cabri1998, cremen2025, davidson2000, davidson2013, delgiudice2021, efron1992, erman1980, fema2015, fowler2005, ICLR2024_e9df36b2, jacobs2021, kerr1998, lamers2022, law2015, li2023, marrella2017, miltenburg2021, moynihan2009, murray2005, optimisinganalysisofstroketrialsoastcollaboration2007a, plattner2006, qian2024, savitz2007, steegen2016, tran2025, tran2026, valmeekam2024, vanderaalst2009, vonstorch2008, wahl2015a, wang2026, woods2018, wu2023, zhuLLMBasedMultiAgentOrchestration2026a) were not verified.
