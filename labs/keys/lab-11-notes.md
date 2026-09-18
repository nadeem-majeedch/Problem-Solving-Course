# Lab 11 — Checkpoint Notes (instructor only)

Not for publication; discuss after the lab.

- **A1.** Canonical loop (accept any equivalent):
  `lo, hi = 0, len(items)`; while `lo < hi`: `mid = (lo+hi)//2`;
  `if items[mid] >= target: hi = mid else: lo = mid + 1`; return `lo`.
  The invariant sentence must claim *two* things (first-possible-answer
  property of lo; hi's known relation); a one-sided invariant is the
  most common half-answer.
- **A2.** Duplicates: this loop returns the *first* index of a run of
  equal targets — because `hi = mid` never jumps past an equal value.
  Pairs whose loop returns the *last* equal index have written the
  "last ≤" variant: accept it only if their invariant sentence and
  boundary table agree with what the code does (the lesson: the code's
  guarantee and the spec's word "first" must be reconciled explicitly).
- **A3.** ⌈log₂ 1001⌉ = 10: the interval halves each probe and 2¹⁰ = 1024
  ≥ 1001. "Without mentioning code" forces the halving argument — the
  same one as cs-081's guessing game.
- **B1/B2.** Latest feasible t: search over candidate minutes; predicate
  is monotone decreasing in t. The clean formulation reuses `first_ge`
  on the *flipped* predicate (find first infeasible, subtract one) —
  pairs that re-derive a "last true" loop from scratch should compare
  both and notice the flip. Call budget: ≤ 10 calls for any minute range
  up to 2¹⁰ = 1024 minutes; give `bridge.py` a 1440-minute (24 h) domain
  so 11 calls are needed if they start with the full day — a useful
  wobble that forces a shrinking start or a tighter domain claim.
- **B3.** The glitch breaks "if t works, earlier works" — with the claim
  void, `hi = mid` may discard the true latest time. Debrief line: the
  loop never read the glitch as *data error*; it read it as *contract
  violation*, and correctly (its correctness proof died). Connect to
  cs-084 (rotten timeline) where the same predicate-monotonicity issue
  decides which data can be binary-searched at all.
- **C1.** Expected counts: A = 10 on 1000 items (some pairs get 9 — the
  last probe can land exactly); B ≤ 10 by construction. Any pair
  reporting an unbounded count has a non-shrinking interval — send them
  to C2 early.
- **C2.** Two defect classes, both verified by execution on 2026-09-18:
  (a) `hi = mid - 1` skips the answer — on items [5, 10], target 7 the
  canonical loop returns index 1; the broken variant returns 0 (and 0 for
  target 10 too). (b) `lo = mid` (missing the +1) spins forever — on the
  same data the loop never exits with lo stuck at 0, hi at 1. The
  pedagogical point: one wrong line produces two different failure
  *classes* depending on which update is damaged.
- **C3.** Reconstruction from behaviour usually recovers the shrinking
  rule but not the first/last-position *intent*; note the gap — the
  intent lives in the invariant sentence, which is why A1 made them
  write it first.
- **D1.** Good answers: "first day the canteen sells out" (cumulative
  demand is monotone); "smallest study-group size that still reaches the
  deadline" (progress is monotone in size); "first week the menu price
  crossed the budget" (price series — monotone only if the series is;
  the good answers *argue* the source of monotonicity, which is the mark).
- **D2.** Load is feasible for cap C iff a greedy sweep never exceeds C;
  feasibility is monotone in C (more capacity never hurts), so the
  greedy check is a valid predicate — the greedy's exchange argument
  lives in cs-083's solution.
- Completion bar as in Lab 1. Fast finishers: prove the loop terminates
  (interval strictly shrinks because lo ≤ mid < hi) — their second
  correctness argument after Lab 6's D1.
