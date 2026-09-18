# Rubric — Assignment 3 (20 marks)

Applies to [Assignment 3](assignment-03.md).

## Part A (10)

### (a) Visit counts (3)

| Band | Descriptor |
| --- | --- |
| 3 | V1: n (average) + n (scan) = 2n; V2: n × (n + n) = 2n² or equivalent per-element accounting; V3: n log n sort + log n search. Expressions tied to the n-values. |
| 2 | Right shapes but one version's bookkeeping off (e.g. V2 counted as n² without the inner pair). |
| 0–1 | Constant-time claims for re-computation, or no expressions. |

### (b) Empirical timings (4)

| Band | Descriptor |
| --- | --- |
| 4 | Both n values × both versions with raw times and the ratio; the ratio's agreement with 2n vs 2n² (≈ ×10 time growth for ×10 data on V1, ≈ ×100 on V2) checked explicitly. |
| 2–3 | Timings present but no ratio/agreement analysis, or one version missing. |
| 0–1 | Single numbers, no measurement conditions. |

### (c) Binary search correctness (2)

| Band | Descriptor |
| --- | --- |
| 2 | A concrete unsorted list where the average is present but binary search misses it (e.g. `[4, 2, 8, 6]`, average 5 is absent — pick one where it is present, like `[2, 4, 8, 2]`, average 4, present but unsorted), plus the statement that V3 sorts the copy first, which is the fix. |
| 1 | Vague "needs sorted data" without the concrete list. |
| 0 | Wrong or missing. |

### (d) Shipment verdict (1) — any defensible choice with a stated reason.

## Part B (10)

### (a) Model precision (3)

| Band | Descriptor |
| --- | --- |
| 3 | State = remaining minutes (start 120); decision = "does the next arrival's need fit in remaining?"; stopping rule = first non-fit ends the slot (arrival order only); ties and zero remaining handled. |
| 2 | Model right but one rule implicit. |
| 0–1 | Ambiguous state or no stopping rule. |

### (b) Trace (3)

| Band | Descriptor |
| --- | --- |
| 3 | Table: 15→105, 20→85, 30→55, 20→35, 15→20, 30→refused (30 > 20 remaining). One patient referred (the last). |
| 2 | Correct flow, one arithmetic slip. |
| 0–1 | Wrong rule (e.g. serving the refused patient partially). |

### (c) Shortest-first (3)

| Band | Descriptor |
| --- | --- |
| 3 | Sorted needs `[15, 15, 20, 20, 30, 30]`: 15→105, 15→90, 20→70, 20→50, 30→20, 30 refused → **5 served** vs 5 in (b) — same count here (say so honestly); fairness discussed (later arrivals with small needs leapfrog — longer waits for earlier, longer cases). |
| 2 | Trace right but fairness unargued, or count wrong. |
| 0–1 | Reordering not traced. |

### (d) No-better-ordering claim (1)

Award for either a concrete instance where arrival order is already
optimal (any set that fills 120 exactly in arrival order) *or* a coherent
argument that with these sizes an optimal order always exists offline —
the rubric rewards the reasoning, not a specific answer.

## Cross-cutting adjustments

- Arithmetic errors that propagate (wrong trace feeding (c)) lose marks
  once in (b), not again in (c), if (c)'s method is right on its own
  numbers.
- Code must run; a submitted timing script that errors caps Part A at 5.
