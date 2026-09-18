# Lab 10 — Checkpoint Notes (instructor only)

Not for publication; discuss after the lab.

- **A1.** 9 choices for chair × C(8,2) = 28 pairs of ordinary members
  = 252. (Ordered-triple reasoning 9×8×7 = 504 divided by the 2! orderings
  of the ordinary pair is the same 252 — accept either route, but the
  division must be *explained*, not magic.)
- **A2.** Fast pair: C(9,2) = 36. The chair question is a trap: the fast
  pair's *definition* does not involve the chair at all, so nothing
  doubles or halves — pairs who multiply by 2 ("chair may or may not be
  in it") are counting two overlapping cases as disjoint. If the intent
  were "one of the pair must be the chair", the count is 8; say the
  distinction out loud in plenary.
- **A3.** Ordered triples of distinct members: 9×8×7 = 504; of these 252
  are valid, so exactly half are wasted (the 2! orderings of the ordinary
  pair). This fraction — 2 wasted per hit — is the cost of thinking-less:
  the point of A3.
- **B1.** Agreements: 252 and 36. Typical failure: using combinations
  for the full A1 structure (gives 36 — the ordinary-pair count only).
  The reasoning is guilty more often than the code; make them recompute
  9×8×7/2 by hand before debugging `itertools`.
- **B2.** Combinations-for-chair demo: C(9,1)·C(8,2) with combinations
  everywhere = 9 × 28 = 252 is *right*; the instructive breakage is
  using permutations for the ordinary pair: 9×8×7 = 504 — it counts
  {ann,bo} and {bo,ann} as different panels. The sentence must name
  "order that doesn't exist as a distinction".
- **B3.** Doubling n multiplies brute-force time by roughly ×8 (three
  nested choices): n = 18 enumerates 18×17×16 = 4896 candidates against
  9×8×7 = 504 — a measured ratio of about 9.7× on the naive count (the
  idealised 2³ = 8× assumes the same pruning at every scale). Trustworthy
  as an order-of-magnitude claim *if* the program's work is pure
  enumeration (no early exit); not trustworthy if filtering
  short-circuits. Measure it with the counter rather than asserting 8×.
  The two-sentence defence is the deliverable, not the number.
- **C1.** 10×9×8 = 720 both ways. Reconciliation note: permutations(10,3)
  is 720 — the formula *is* the permutations count.
- **C2.** Order-free: C(10,3) = 120; factor exactly 3! = 6; every key has
  exactly 6 digit-orderings, so the order-mattered keyspace is 6 copies
  of the order-free one. Verify 720/120 = 6 by brute force. The general
  lesson: divide by the size of the equivalence class only when the
  classes are all the same size — the same caution as A2's trap.
- **C3.** Good exchange questions: two paired roles (chair + deputy:
  ordered → 9×8); choosing a sub-committee of 4 with both co-presidents
  excluded (C(7,4) = 35); "at least one of ann/bo on a 3-person panel"
  (complement: C(9,3) − C(7,3) = 84 − 35 = 49). Adjudicate the *tool
  choice* (order matters or not; overlap handled by complement or not).
- **D1.** Any question about *how many* — production brute force at
  n = 10⁶ candidates is absurd when the count is closed-form; the count
  bought feasibility (and the answer) without running anything.
- **D2.** cs-059 (committee draw): combinations plus the complement/
  hypergeometric-style reasoning — the tool was "count all, subtract
  the bad". cs-060 (birthday): product of no-collision probabilities —
  the complement carried it. One sentence each; the mark is naming the
  *shape* (count-the-bad vs multiply-the-good).
- Completion bar as in Lab 1. Fast finishers: ask for the number of
  panels where the chair and at least one ordinary member share a
  birthday, given 365 equal-likely days (inclusion-exclusion preview of
  Block IV).
