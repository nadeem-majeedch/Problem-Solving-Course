# Rubric — Assignment 6 (20 marks)

Applies to [Assignment 6](assignment-06.md). Band descriptors per
criterion; award half-bands where genuinely between.

## Part 1 — Portfolio pages (8; ~2.7 per page, mark holistically)

| Band | Descriptor |
| --- | --- |
| 8 | Three pages from three distinct blocks; each names three *ordered* moves with reasons for the order; each generalisation carries a genuine counter-example (a problem where the move misfires); the trace solves the worked instance correctly by method. |
| 6–7 | Pages complete but one order-justification is circular ("first I read the problem, then I solve it"), or one counter-example is a token denial rather than a real misfire case. |
| 3–5 | Moves listed without ordering reasons, or counter-examples missing on two pages, or traces copied from the case's published solution wording. |
| 0–2 | Summaries of the cases rather than a personal method; no distinct-block coverage. |

## Part 2 — Adversarial review (4)

| Band | Descriptor |
| --- | --- |
| 4 | Three concrete challenges (each names a move or an input); each accept/rebut sentence engages the specific challenge — a rebuttal argues why the misfire does not apply, an acceptance names the corrected move. |
| 2–3 | Challenges present but generic ("your move might not always work"), or one accept/rebut missing. |
| 0–1 | Praise instead of challenge; partner unnamed. |

## Part 3 — Unifying program (8)

| Criterion | Band | Descriptor |
| --- | --- | --- |
| (i) Invariant loop | 2 | Invariant stated in the paragraph *and* true of the code; 1 if stated but false, or true but unstated. |
| (ii) Decomposition | 2 | ≥ 3 functions, each with a one-line contract (parameters, return, no prints-as-returns); 1 for ≥ 3 functions with vague contracts. |
| (iii) Test table | 2 | ≥ 6 rows including one deliberate-failure row with the failure demonstrated (before the fix) or explained; 1 for a happy-path-only table. |
| (iv) Mapping paragraph | 2 | Each program part explicitly tied to a portfolio page's method; 1 for a vague "this shows my method" sentence. |
| Program quality | — | Not separately marked, but a program that does not run caps Part 3 at 4. |

## Cross-cutting modifiers

- **+1 (max 20):** a portfolio page that connects two blocks' methods
  (e.g. how Block I's assumption-stating changes Block III's invariant
  work) with a concrete example.
- **−1:** any portfolio page whose trace matches the published case
  solution's numbers *and* phrasing — the closed-book trace is the
  honesty check.
- **−1:** the Part 3 problem is a restated course case (cs-013's
  sentinel echo, cs-049's word tally, etc.) rather than the student's own.
