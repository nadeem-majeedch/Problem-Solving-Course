# Rubric — Assignment 4 (20 marks)

Applies to [Assignment 4](assignment-04.md). Band descriptors per
criterion; award half-bands where genuinely between.

## Task 1 — The claim audit (6)

| Band | Descriptor |
| --- | --- |
| 5–6 | Three means computed from *their* log with visible arithmetic; the defensibility verdict follows from the numbers; the notice sentence names the summary's base and population. |
| 3–4 | Means present but one cleaning variant is undefined or arithmetic slips; verdict asserted more than derived. |
| 0–2 | One mean, no variants, or numbers that do not follow from the constructed log. |

## Task 2 — Cleaning ledger (5)

| Band | Descriptor |
| --- | --- |
| 5 | Every rule counted, argued (not defaulted), and the before/after totals reconcile exactly. |
| 3–4 | Ledger complete but one decision unjustified, or the reconciliation is off by rows the student cannot account for. |
| 1–2 | Rules listed without counts, or counts that contradict the code's actual effect. |
| 0 | No ledger; cleaning visible only inside uncommented code. |

## Task 3 — Simulation (5)

| Band | Descriptor |
| --- | --- |
| 5 | Trial definition is precise (random vs fixed vs derived); 10,000 seeded trials; buckets sum to the trial count; the unjustifyable assumption is genuinely structural (e.g. arrival process shape). |
| 3–4 | Working simulation with one vague trial-definition edge (what happens to the 240-minute visits at closing?), or buckets that do not sum. |
| 1–2 | Simulation confounds log-derived and assumed quantities; seed missing. |
| 0 | Not submitted or not runnable. |

## Task 4 — Honesty paragraph (4)

| Band | Descriptor |
| --- | --- |
| 4 | Calibrated: one refusal with a data-shaped reason; no over-claim; consistent with their own numbers. |
| 2–3 | Honest in tone but vague about which number is refused, or why. |
| 0–1 | Marketing copy: repeats the claim with confidence the data does not support. |

## Cross-cutting modifiers

- **+1 (max 20):** the ledger or code catches a genuine edge the brief did not name (e.g. a 240-minute pass with −1 duration — which rule wins?) and resolves it with a stated rule.
- **−1:** pasted outputs that could not have been produced by the submitted code (wrong seed, impossible bucket counts).
