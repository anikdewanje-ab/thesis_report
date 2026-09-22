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
      a design-and-evaluation study answering four RQs: can it beat the scripted
      baseline (no), why not (commitment failure), what must change, and what a
      designer should consider. See `writing-plan.md` §1.
- [x] ~~Add the two missing chapters (Validity, Methods critique) to `main.tex`
      and reorder the architecture chapters.~~ **Done 2026-09-22.** 13 chapters,
      builds clean, no undefined references.
- [ ] Fill the real inventory number in `inc/profile.tex` (`\invnr`).
- [ ] Import the `rubric-bibliography.md` sources into `bibs/litDB.bib`.
- [ ] Verify the *(verify)*-flagged sources before citing any of them.

## Closed

- ~~Reconcile framework story: LangGraph + PostgresSaver vs. the built system.~~
  **Closed 2026-09-22.** There is no LangGraph and no PostgresSaver anywhere in
  the project. The stack is Ollama + a custom asyncio `AgenticEngine` +
  PostgreSQL. The file-backed JSON persistence was retired by ADR-0005, so
  Postgres is the single source of truth. Describe that.
- ~~Decide the bibliography style (currently `alpha`).~~ **Closed.** `main.tex`
  uses biblatex `style=numeric-comp`, `sorting=nyt`, `backend=bibtex`.
