# Lab 12 — Checkpoint Notes (instructor only)

Not for publication; discuss after the lab.

- **A1.** power2: base `n = 0 → 1`; recursive `2 * power2(n-1)`. The
  discipline being graded is *separate lines with comments* — the same
  base-first order lecture 22 taught with cs-085.
- **A2.** sum_digits: base `n < 10 → n` is the value-form; the
  digit-count form (`n ≤ 0`) accidentally works if written as
  `n == 0 → 0` but breaks for negative n unless guarded. The
  distinction matters because the recursion's *shape* should mirror the
  value's structure, and because the wrong base silently returns wrong
  totals for the negatives the spec excludes — say so.
- **A3.** power2(4): 5 boxes, 5 distinct arguments (4, 3, 2, 1, 0).
  Linear chain — this is the anchor for D2's "linear tree needs no
  memo".
- **B1.** fib(5) tree: 15 boxes; computed-count per argument: fib(4) 1×,
  fib(3) 2×, fib(2) 3×, fib(1) 5×, fib(0) 3× (verified by execution on
  2026-09-18 with fib(0)=0, fib(1)=1). (Have pairs verify against the
  counter — miscounted hand trees are common and instructive.)
- **B2.** fib(25) naive: 242,785 calls (fib(k) calls total =
  2·fib(k+1) − 1). Prediction route: "each level roughly doubles" →
  expect ~2²⁵ scale; measurement should land near 2.4×10⁵ — the ratio
  story (2⁵ offset) is the accepted argument. The growth rule sentence:
  calls(k) = calls(k−1) + calls(k−2) + 1, i.e. the call count itself
  obeys the Fibonacci recurrence — the beautiful reveal; say it.
- **B3.** Waste: recomputing identical subproblems (boxes for the same
  argument). Smallest change: remember results — memoisation (C1) or
  restructure to fill a table bottom-up (C2).
- **C1.** Memoised: exactly k+1 distinct computations (arguments 0..k);
  total calls ≈ 2k+1 (each new value triggers two cached lookups).
  Remaining cost: depth k on the call stack — which is why fib(100000)
  memoised still dies (RecursionError) while the C2 loop does not; try
  it live if time allows.
- **C2.** Loop: `(a, b) = (0, 1)` then k times `(a, b) = (b, a+b)`.
  Easier to *justify*: two named variables with an obvious invariant
  (a = fib(i), b = fib(i+1)) — lecture 19's invariant discipline.
  Easier to *derive*: the recursion mirrors the problem statement's own
  definition. Both sentences must appear; "loop is faster" is not the
  question.
- **C3.** Decisions to accept: any problem where each call spawns ≥ 2
  calls on *overlapping* subproblems → recursion without memo is the
  wrong cost band (memo or loop); linear chains (cs-085 dolls) are fine
  as plain recursion; non-overlapping branching (divide-and-conquer
  merges) are fine without memo because the tree does not repeat
  arguments. The justification sentence must mention overlap.
- **D1.** The criterion: when distinct subproblems ≪ total boxes
  (branching with overlap), the tree pays exponentially for a linear
  amount of real work — memoise or flip the loop.
- **D2.** cs-085: linear tree (one recursive call per doll) — no memo
  needed, depth is the only concern. cs-088 (tower steps, ways(n) =
  ways(n−1) + ways(n−2)): branching with massive overlap — naive
  recursion is exponential; memoise or loop. The single fact deciding
  it: does the same argument reappear in the tree?
- Completion bar as in Lab 1. Fast finishers: have them predict calls(30)
  exactly from calls(k) = calls(k−1) + calls(k−2) + 1 and verify —
  2,692,537 calls (verified by execution on 2026-09-18; the identity
  calls(k) = 2·fib(k+1) − 1 gives the same number); their first
  derivation of a cost formula from a recurrence.
