# Lab 6 — Checkpoint Notes (instructor only)

Not for publication; discuss after the lab.

- **A1 — S1.** total = 1 + 9 + 25 = 35 (i takes 1, 3, 5; squares of odd
  numbers up to 5). Typical divergence: students square *after* the
  increment, or stop at i = 4.
- **A1 — S2.** best = 5, but the latent defect is initialising `best = 0`:
  any all-negative list returns 0 instead of the true maximum. This is the
  same accumulator trap as cs-036's wrong turn; expect pairs to "prove" S2
  correct because their trace table on the given data is perfect — that is
  the lesson: a trace on one input verifies nothing about the input class.
- **A1 — S3.** n = 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1, count = 8.
  The termination prediction for small n is always "yes"; the honest answer
  to *why* is "no idea" — which is the correct segue to D1. (Collatz
  termination is famously unproven in general; do not let the lab imply
  otherwise, and do not let students claim their run proves anything about
  all n.)
- **A2.** Expected sites: S1 the `i = i + 2` (skips values / wrong bound);
  S2 the `best = 0` initialisation; S3 the swap of `//` and `%` or the
  count incremented outside the loop. Marking: any *argued* site with a
  one-sentence mechanism counts; this is prediction, not answer-matching.
- **B2.** Defect class: initial value outside the data's range. Input:
  `[-4, -1, -9]` → returns 0, expected −1. Minimal fix: `best = xs[0]`
  (with an empty-guard) — the same fix as Lab 1's largest-of-session.
  Note the recurrence: this is the third time the course has met this
  defect class (Lab 1 B1, cs-036, now here); say so out loud.
- **C1/C2.** Encourage defects that are *mechanism-level* (wrong branch,
  wrong initial value) rather than syntax noise — reject snippets whose
  "defect" is a typo. Scoring: 1 point per correct element (symptom,
  mechanism line, fix), 3 max per snippet. The game works because writing
  a subtle defect forces the author to articulate the mechanism too.
- **C3.** Good invariant for S1: "after k iterations, total = sum of
  squares of the odd numbers below i and i is the (k+1)-th odd number."
  S2: "best is the maximum of the prefix seen so far *of the values
  compared*" — the defective version violates it for negative prefixes
  because 0 was never compared. Accept any *checkable* sentence; reject
  restatements of the loop body.
- **D1.** To prove termination you need a quantity that (a) stays in a
  well-founded set (e.g. positive integers) and (b) strictly decreases
  every iteration. "It ran and stopped" is evidence for one input only.
  Full connection: this is lecture 19's invariant discipline and lecture
  06's termination question meeting each other.
- **D2.** Answers vary; the mark is for noticing that a *reasoned*
  termination claim (a decreasing bound) was present even if never named.
- Completion bar as in Lab 1. Fast finishers: hand them cs-024's
  loop_c_fixed and ask for its termination argument (i decreases every
  iteration because i//4 + 1 ≥ 1 — loop_c_fixed(100) = 13 steps, verified
  by execution on 2026-09-18; the subtle part students must find is that
  the decrease is fast but the *invariant* i > 0 holds until exactly one
  final step — see the case solution for the full discussion).
