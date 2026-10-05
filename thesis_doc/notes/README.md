# Notes

Scratch space for writing the thesis. Not part of the final PDF.

Use this folder for:

- Per-chapter notes and outlines before drafting.
- A running list of open questions to resolve with the supervisor.
- Small TODO lists so nothing gets lost between sessions.

Start with [`writing-plan.md`](writing-plan.md): the chapter order, the framing
decision, and what to fix before drafting.

## Open questions

- [x] ~~**Framing.**~~ **Settled with the supervisor 2026-09-22.** The thesis is
      a design-and-evaluation study answering three RQs: can it beat the
      scripted baseline (no), why not (commitment failure), and what must
      change and what a designer should consider (the former RQ3 and RQ4,
      merged 2026-10-02). See `writing-plan.md` §1.
- [x] ~~Add the two missing chapters (Validity, Methods critique) to `main.tex`
      and reorder the architecture chapters.~~ **Done 2026-09-22.** 13 chapters,
      builds clean, no undefined references.
- [x] ~~Fill the real inventory number in `inc/profile.tex` (`\invnr`).~~
      **Removed 2026-10-05.** Not needed; the footer now shows the page number
      only.
- [x] ~~Import the `rubric-bibliography.md` sources into `bibs/litDB.bib`.~~
      **Done** (commit 0ab5099). All seven rubric DOIs are in the bib.
- [x] ~~Verify the *(verify)*-flagged sources before citing any of them.~~
      **Done.** The five that are cited (clopper1934, holm1979, efron1979,
      lipsitch2010, nosek2018) came in through Zotero by DOI or JSTOR id, and
      volume, issue and pages match the publisher records.

## Closed

- ~~Reconcile framework story: LangGraph + PostgresSaver vs. the built system.~~
  **Closed 2026-09-22.** There is no LangGraph and no PostgresSaver anywhere in
  the project. The stack is Ollama + a custom asyncio `AgenticEngine` +
  PostgreSQL. The file-backed JSON persistence was retired by ADR-0005, so
  Postgres is the single source of truth. Describe that.
- ~~Decide the bibliography style (currently `alpha`).~~ **Closed.** `main.tex`
  uses biblatex `style=numeric-comp`, `sorting=nyt`, `backend=bibtex`.
