# Rubric — Assignment 5 (20 marks)

Applies to [Assignment 5](assignment-05.md). Band descriptors per
criterion; award half-bands where genuinely between.

## Problem 1 — The overdue sweep (10)

| Criterion | Band | Descriptor |
| --- | --- | --- |
| (a) Two approaches + costs | 4 | Two genuinely different structures (map-pass vs sort-group, or streaming vs batching); costs stated with input-size arithmetic (not just "O(n)" — say what n is here and what the constant work is). |
| | 2–3 | Two approaches named but one is a re-skin of the other, or costs without the size arithmetic. |
| | 0–1 | One approach, or costs asserted from memory. |
| (b) Choice justified | 3 | The justification cites the student's own (a) numbers and a workload fact (10,000 entries, nightly run) — including a defensible "either is fine at this size" verdict with a reason. |
| | 1–2 | Choice made on vibes ("hashmaps are fast") without the arithmetic. |
| (c) Invariant + end argument | 2 | Invariant is checkable (e.g. "after processing entry i, the map holds the exact totals for the entries seen so far") and the end-argument uses loop exit. |
| | 0–1 | Restates the code, or an invariant that is false mid-loop. |
| (d) Tie test | 1 | A concrete input with two equal maxima and the expected two-member output. |

## Problem 2 — The seating swap (10)

| Criterion | Band | Descriptor |
| --- | --- | --- |
| (a) Formulation + space size | 3 | Candidate = an assignment of desks (occupied/empty); worst-case space given exactly (e.g. 2^(n²) assignments or C(n², k) for exactly-k) with the arithmetic. |
| | 1–2 | "Try all seatings" without a size, or a size that miscounts. |
| (b) Backtracking + pruning | 4 | Correct recursion with base case; pruning rule stated and *safety-argued* (pruned branches provably contain no solution). Correct code with a false safety argument earns 2 — the argument is the mark. |
| | 2 | Works but prunes nothing, or prunes by a rule that can discard solutions. |
| | 0–1 | Not recursive, or not runnable. |
| (c) Node counts | 2 | Real instrumented numbers for all six runs (3 sizes × on/off); growth sentence matches the numbers. |
| | 1 | Numbers for some runs, or a growth sentence contradicted by the table. |
| (d) C(n²,k) comparison | 1 | Credit for the honest answer: when k is small *and* the rule-check is expensive per candidate, enumerate-and-test beats deep search with cheap checks. |

## Cross-cutting modifiers

- **+1 (max 20):** an extra pruning rule (symmetry, ordering) with its safety argued.
- **−1:** node counts that the submitted instrumentation cannot have produced (e.g. pruned search reporting more nodes than exhaustive).
- **−1:** invariant or pruning argument lifted verbatim from course pages without adaptation (the independent-reasoning component).
