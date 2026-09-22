# Zotero import helper — rubric bibliography

Identifiers extracted from `thesis_doc/rubric-bibliography.md` (Section 10, the
Recovery-Outcome Rubric). Same workflow as `zotero-import-identifiers.md`: use
Zotero's "Add Item by Identifier" (magic-wand button), paste a batch, one
identifier per line, then check each item landed in the **thesis** collection.

None of these sources are in `bibs/litDB.bib` yet. As of this note the bib holds
32 entries and none of them match this list.

After importing, verify author names and years against the rubric bibliography,
since automatic metadata is not always perfect.

## Batch A — DOIs printed in the rubric bibliography

These DOIs are written out in the source document, so they can be pasted
directly.

10.1161/STROKEAHA.107.489351
10.1155/2016/9482876
10.1212/WNL.0000000000006554
10.1080/07474938.2012.690653
10.1145/3442188.3445901
10.1193/1.1623497
10.1177/2515245920954925

Mapping, for the check after import:

| DOI | Item |
|---|---|
| 10.1161/STROKEAHA.107.489351 | Savitz et al. 2007, Shift Analysis vs Dichotomization (Stroke) |
| 10.1155/2016/9482876 | Nunn, Bath & Gray 2016, mRS systematic review |
| 10.1212/WNL.0000000000006554 | OAST line, ordinal vs dichotomous, 5-year outcome (Neurology 2018) |
| 10.1080/07474938.2012.690653 | Yalonetzky 2013, Stochastic Dominance with Ordinal Variables |
| 10.1145/3442188.3445901 | Jacobs & Wallach 2021, Measurement and Fairness (FAccT) |
| 10.1193/1.1623497 | Bruneau et al. 2003, Seismic Resilience of Communities |
| 10.1177/2515245920954925 | Del Giudice & Gangestad 2021, A Traveler's Guide to the Multiverse |

## Batch B — arXiv IDs printed in the rubric bibliography

arXiv:2103.06944
arXiv:1912.05511

`arXiv:2103.06944` is van Miltenburg, van der Lee & Krahmer 2021, Preregistering
NLP Research.

`arXiv:1912.05511` is the preprint of Jacobs & Wallach 2021. Import it **only if**
the DOI in Batch A fails to resolve. Do not keep both, or the entry will be
duplicated.

Note: Xie et al. 2024 (TravelPlanner, arXiv:2402.01622) is cited in the rubric
document but is **already in `litDB.bib`** as `xie2024`. Do not import it again.

## Batch C — no identifier given, add by title

The rubric bibliography lists these with venue and pages but no DOI. Search the
title in Google Scholar or the publisher page, then use the Zotero Connector
browser button, or paste the DOI once found. Do not guess a DOI.

**Section B, dominance testing**

- Davidson, R., & Duclos, J.-Y. (2000). Statistical Inference for Stochastic
  Dominance and for the Measurement of Poverty and Inequality. *Econometrica*,
  68(6):1435–1464.
- Davidson, R., & Duclos (2013). Empirical-likelihood first-order dominance test.
  **Open question:** the rubric doc flags that Davidson & Duclos appears as both
  2000 and 2013. Confirm which paper backs which claim before importing, and
  import both only if both are actually cited.
- Barrett, G. F., & Donald, S. G. (2003). Consistent Tests for Stochastic
  Dominance. *Econometrica*, 71(1):71–104.
- McFadden, D. (1989). Testing for Stochastic Dominance.

**Section C, cut-point sensitivity**

- Simonsohn, U., Simmons, J. P., & Nelson, L. D. (2020). Specification Curve
  Analysis. *Nature Human Behaviour*, 4:1208–1214.
- Steegen, S., Tuerlinckx, F., Gelman, A., & Vanpaemel, W. (2016). Increasing
  Transparency Through a Multiverse Analysis. *Perspectives on Psychological
  Science*, 11(5):702–712.

**Section D, preregistration**

- Bengio, Y., Pineau, J., Bach, F., Forde, J. Z., & Whitaker, K. (2020). The
  Pre-Registration Workshop. NeurIPS 2020, PMLR 148.
- Albanie, S., et al. (2021/2022). NeurIPS 2021 Preregistration Workshop,
  PMLR 181. Confirm the year, the doc gives two.
- Gelman, A., & Loken, E. (2013/2014). The Garden of Forking Paths. Confirm which
  version is being cited, the working paper and the published version differ.
- Kerr, N. L. (1998). HARKing: Hypothesizing After the Results are Known.
  *Personality and Social Psychology Review*, 2(3):196–217.

**Section A, agentic evaluation**

- Xu, F. F., et al. (2025). TheAgentCompany: Benchmarking LLM Agents on
  Consequential Real World Tasks. NeurIPS 2025 Datasets & Benchmarks Track. It
  has an arXiv preprint, but the rubric doc does not give the ID, so look it up
  rather than guessing.

**Section F, resilience quantification**

- Cimellaro, G. P., Reinhorn, A. M., & Bruneau, M. (2010). Framework for
  Analytical Quantification of Disaster Resilience. *Engineering Structures*,
  32(11):3639–3649.
- Zobel, C. W. (2010). Representing Perceived Tradeoffs in Defining Disaster
  Resilience. *Decision Support Systems*, 50(2):394–403.
- The critique of the resilience triangle, referenced only as **PMC11954729** ("A
  new end-user-oriented and dynamic approach to post-disaster resilience
  quantification for individual facilities"). Open the PMC ID, get the real title
  and DOI, then import. This one carries weight in the argument, since it is the
  justification for scoring the outcome instead of the area under a curve, so it
  should not stay a bare PMC number.

## Batch D — VERIFY BEFORE IMPORT

The rubric bibliography's own Caveats section marks these as cited from recall or
from search summaries. Venue, volume, and pages are **not** confirmed. Check each
one against the publisher page before adding it to Zotero, and do not cite any of
them in the thesis until it has been checked.

- Beamon, B. M., & Balcik, B. (2008). Performance Measurement in Humanitarian
  Relief Chains. *International Journal of Public Sector Management*, 21(1):4–25.
  Volume and pages flagged for verification.
- Wang, Q., et al. (2023). Multi-period emergency material allocation, the 3E
  paper. Venue is uncertain, the doc gives two candidate journals.
- Holguín-Veras, J., et al. (2013). On the Appropriate Objective Function for
  Post-Disaster Humanitarian Logistics Models. *Journal of Operations
  Management*, 31(5):262–280.
- Murray, G. D., et al. Prognosis-adjusted outcome analysis in TBI trials, the
  origin of the sliding dichotomy. The doc gives no specific paper, only the
  author and the topic, so this needs a real search first.

## Priority

If time is short, Batch A alone covers six of the eight rows in the rubric
document's own priority summary table. The two rows it does not cover are the
Simonsohn specification-curve citation (Batch C) and the PMC11954729 resilience
critique (Batch C).
