# Lab 5 — Checkpoint Notes (instructor only)

Not for publication; discuss after the lab.

- **A1/A2.** Day n means "(n − 1) mod 5 + 1" in 1-based language; day 0
  would map to person 5 under the formula but no real schedule starts at
  zero, which is exactly why 1-based vs 0-based must be a stated choice.
  Correct predictions: day 47 → 47 mod 5 = 2 → person 2; day 100 → 100
  mod 5 = 0 → person 5. The day-100 case is the pedagogical payload:
  remainder 0 *is* the last person, and students who translate "mod = 0"
  as "person 0" discover the off-by-one themselves.
- **B1/B2.** Accept `(day - 1) % people + 1` or the 0-based rewrite with an
  explicit +1 at return. Common defect: `day % people` alone (fails day 5
  and every multiple). If prediction and program disagree, the interesting
  case is a *correct program with a wrong prediction* — make the student
  recompute by hand rather than "fixing" the program.
- **B3.** Waters on day d ⇔ d ≥ 4 and (d − 4) mod 3 = 0. The trap is
  `d mod 3 = 1` (which matches day 4 but also day 1 — before the duty
  started). Watch for students "fixing" it by testing `d > 3` with the
  wrong offset; the fix is shifting the origin, not patching the modulus.
  This mirrors cs-017/cs-018's cycle reasoning and lecture 05's second
  example.
- **C1.** Any *documented* choice is acceptable: reject day < 1 with an
  error, or define day 0 = person 5 as the mathematical continuation.
  The teaching point is that silent wrap-around (day 0 → person 5
  "because the formula says so") hides a modelling decision. Day −7:
  Python's `%` returns non-negative results for positive divisors, so
  `(day - 1) % 5 + 1` happens to produce a defined answer (day −7 → 3:
  (−8) mod 5 = 2, +1 = 3) — a rare case where the language's convention
  silently "helps"; surface it.
- **C2.** Minimal wrapper: for day < 30 use the 5-person rule; else use
  the 7-person rule with the *phase preserved at the switch day* — the
  hard question is who is on call on day 30 itself. Accept either
  convention if stated. The general lesson: schedule changes need the
  overlap resolved explicitly, exactly like cs-016's meeting-room model.
- **C3.** Good hostile inputs: day 1 (first), day 5 (boundary of first
  cycle), day 6 (first wrap), day 30 (team switch), day 10**9** (works —
  remainders don't care about magnitude; contrast with simulating day by
  day, which does not terminate in lab time).
- **D1.** Days 1,2,3 → remainders (after +1 shift) 1,2,3; the wrap is
  visible only at day 6, so let pairs extend the table to day 6 on their
  own initiative.
- **D2.** Cycle length 5. With skipped weekends the cycle is no longer
  pure remainder arithmetic — the honest answer is "you need a different
  model (walk the working days, or precompute)", which is the bridge to
  lecture 06's loop reasoning.
- Completion bar as in Lab 1. Fast finishers: prove that
  `(day - 1) % people + 1` is always in 1..people (a two-line argument —
  their first correctness proof).
