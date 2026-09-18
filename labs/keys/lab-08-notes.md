# Lab 8 — Checkpoint Notes (instructor only)

Not for publication; discuss after the lab.

- **Correct values for fee.py as printed (it is clean):** day 0 or
  negative → 2.00; day 1 → 2.30; day 14 → 2.00 + 14×0.30 = 6.20;
  day 15 → 6.20 + 0.10 = 6.30; day 30 → 2.00 + 4.20 + 1.60 = 7.80;
  day 60 → 2.00 + 4.20 + 4.60 = 10.80 → capped at 8.00. The cap binds
  first at day 32 (2.00 + 4.20 + 1.80 = 8.00). Boundary interest: at
  day 32 the cap is reached exactly — a cap-edge row for C1.
- **A1 marking.** The requirement column is the point: a row without a
  named requirement is noise. Common gaps: forgetting the negative side
  of day 0 (early return), and treating 14/15 as one row instead of two.
- **A2.** Expected suspects: the 14/15 boundary (two rules meet) and the
  cap region (a min() that can hide an addition bug). Either answer with
  mechanism-level reasoning earns the marks.
- **B1.** The adjudication discipline matters more than the verdict:
  pairs that immediately blame the program when a row mismatches are
  missing the lab. Typical own-table bug: computing day 15 as
  2.00 + 15×0.30 (forgetting the rate switch *replaces*, not adds).
- **B2.** As printed, `fee.py` is clean; the honest verdict is "no defect
  found" with the closest row named (usually 32 or 60). The instructor
  variant: swap in `fee_buggy.py` (below) for half the room so both
  verdicts occur; pairs must not know which variant they hold.
  `fee_buggy.py` defect: `min(days_late, 14) * 0.30` →
  `min(days_late, 15) * 0.30` (day 15 → 6.60 instead of 6.30; exposing
  input 15, symptom one extra 0.30 step). Verified by execution on
  2026-09-18: 14→15 costs 0.40 instead of 0.10 under the buggy variant.
  Note the buggy fee is still monotonically non-decreasing — monotonicity
  alone does NOT expose this defect; only the boundary row at 15 does.
- **C1.** The cap-boundary row (day 32) and the interaction row
  ("cap reached while still in the expensive band"? — it is not, at 32;
  asking the question is the exercise). Reject "hostile" rows that are
  just big numbers; hostility lives at boundaries.
- **C2.** Adjudication of a mismatch: recompute by hand, then check which
  side's arithmetic drifted. Score as stated; a clean "no defect" verdict
  with a well-argued closest-row earns full marks — the lab does not
  require finding a defect, and pairs holding the buggy variant who
  conclude "clean" should be asked to recheck day 15 specifically, not
  told the answer.
- **D1.** Valid properties: monotone non-decreasing in days late; bounds
  [2.00, 8.00]; integer-day inputs never produce a third decimal place.
  Each is checkable on sampled rows and *strengthened* by every row.
- **D2.** No finite table proves a universal property — the rows are
  evidence, not proof; the argument that proves it is reasoning over the
  rule structure (case analysis), which is lecture 06/19's invariant
  discipline in data-clothing. Connect to cs-029–cs-032 (test design
  from requirements) and to the course's "testing and proving" contrast.
- Completion bar as in Lab 1. Fast finishers: write `property_check.py`
  that runs the monotonicity property over days −5..100 and reports the
  first violating pair. There is none for either variant — both are
  monotone — and that is the lesson: a passing property check is evidence,
  not proof of correctness; the buggy variant survives it and is caught
  only by the boundary row (day 15).
