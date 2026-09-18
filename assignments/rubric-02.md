# Rubric — Assignment 2 (20 marks)

Applies to [Assignment 2](assignment-02.md).

## Task 1 — Trace and explain (5)

| Band | Descriptor |
| --- | --- |
| 5 | All four correct with mechanisms ("length fails first", "index out of range", etc.). |
| 3–4 | Three correct, or all four values right but two mechanisms hand-waved. |
| 1–2 | Two correct. |
| 0 | Guesses without mechanism. |

*(Reference: (a) "bad" — length 5; (b) "bad" — last character `c` is not a
digit; (c) "bad" — first character `1` is not a letter, though length is 8;
(d) "bad" — length 7.)*

## Task 2 — Test table from requirements (6)

| Band | Descriptor |
| --- | --- |
| 5–6 | ≥ 12 deliberate rows; every rule's pass and fail side covered; length boundaries (7, 8, 9) present; predictions marked with plausible mechanisms; rows visibly derived from the requirement. |
| 3–4 | 12 rows but mostly pass-side or happy-path; predictions generic. |
| 1–2 | Table written after running the code (rows mirror the code's behaviour); or fewer than 8 rows. |
| 0 | No table. |

## Task 3 — Better contract (4)

| Band | Descriptor |
| --- | --- |
| 4 | First-failure ordering correct; empty string handled explicitly (named verdict, not a crash); pseudocode translatable. |
| 2–3 | Ordering correct but empty string undefined, or verdicts not per-rule. |
| 0–1 | Ordering wrong or no contract stated. |

## Task 4 — Fix and prove (5)

| Band | Descriptor |
| --- | --- |
| 5 | `verdict` correct; both full runs pasted; the comparison identifies the discriminating rows and articulates why a passing-only suite is weak evidence. |
| 4 | All present but the comparison is shallow ("verdict is better"). |
| 2–3 | Implementation correct but runs incomplete or edited. |
| 0–1 | Implementation fails its own table. |

## Cross-cutting adjustments

- Runs that were visibly "cleaned up" (all PASS on the buggy checker)
  cap task 4 at 2.
- A student whose task-2 predictions all came true must still show the
  buggy-code run — the run is the evidence, not the prediction.
