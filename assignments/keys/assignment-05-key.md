# Assignment 5 — Marking Key (instructor only)

Not for publication. Companion to [rubric-05](../rubric-05.md).

## Problem 1 — reference solution

```python
def sweep(loans):
    totals = {}
    for member, days in loans:
        totals[member] = totals.get(member, 0) + fine(days)
    max_total = max(totals.values())
    top = sorted(m for m, t in totals.items() if t == max_total)
    heavy = sum(1 for t in totals.values() if t >= 20)
    return totals, top, heavy
```

- **(a) costs.** Map-pass: one visit per loan + one per member for the
  max/counts ⇒ ~10,000 + M work, memory M. Sort-group: sort 10,000
  entries (10,000·log₂10,000 ≈ 10,000×13.3 ≈ 133,000 comparisons) then
  one grouping pass ⇒ ~4× the map-pass cost at this size; both instant
  at 10,000 — which is exactly why (b)'s "either is fine, I choose the
  map because it streams" is a *full-mark* answer.
- **(c) invariant.** After the i-th iteration, `totals` holds the exact
  per-member sums of `loans[0..i)`. Exit at i = len(loans) ⇒ the map is
  the full total. Accept any equivalent; reject invariants mentioning
  `top`/`heavy` (computed after the loop — a second, separate loop with
  its own trivial invariant is fine).
- **(d) tie test.** `[("a", 30), ("b", 30)]` → top = ["a", "b"]; also
  the cross-tier tie: `("a", 7, 14)`... concretely `("a", 20 days)` vs
  `("b", 10 days)`: a = 10.00+... fine(20) = 7×0.5 + 13×1.0 = 16.50;
  fine(10) = 3.5 + 3×1.0 = 6.50 — use `("a", 20)` and `("b", 20)` for a
  clean tie at 16.50.

## Problem 2 — reference solution shape

```python
def seating(n, pairs, k):
    occ = [False] * (n * n)
    links = {}   # desk -> list of linked desks
    for a, b in pairs:
        links.setdefault(a, []).append(b)
        links.setdefault(b, []).append(a)
    nodes = [0]

    def ok(d):
        used = 0
        for nb in links.get(d, []):
            if occ[nb]:
                used += 1
        return used <= 1   # desk d would have ≤1 occupied neighbour

    def place(i, start):
        nodes[0] += 1
        if i == k:
            return True
        for d in range(start, n * n):
            if not occ[d] and ok(d):
                occ[d] = True
                if place(i + 1, d + 1):
                    return True
                occ[d] = False
        return False

    return place(0, 0), occ, nodes[0]
```

- **(b) pruning rules** (any two expected): (i) the `ok(d)` placement
  check itself; (ii) index-ordering `start` (each combination once);
  (iii) stronger: after placing, if any occupied desk already has 2
  occupied neighbours, fail immediately (only possible if `ok` checked
  neighbours *at placement* and a later placement invalidates an
  earlier desk — with rule (i) as given this cannot happen; students
  who *prove* that instead of adding a redundant check earn the +1);
  (iv) remaining-desks bound: if free desks < k − i, fail. Safety
  argument required per rule.
- **(c) reference node counts** (n = 4/6/8, 2n pairs, k = ⌊n²/3⌋,
  pairs deterministic from a stated list): expect ~3–10× reduction
  from `ok`-pruning alone at n = 6, growing with n. Accept any
  internally consistent instrumented table; the *sentence* must match
  the table's direction.
- **(d).** Better plan when k is tiny (k ≤ 3: C(n², k) is small) and
  the rule check per candidate is one pass over pairs — enumerate-test
  beats backtracking's deep stacks; the crossover is where backtracking
  wins.

## Common faults to name in feedback

- (a) costs stated as "O(n log n)" with no arithmetic — the task asked
  for the size arithmetic (the rubric's band 4 requires it).
- (c) invariants that are false mid-loop ("totals holds the answer"
  after entry 3 of 10,000).
- 2(b) prunes by "linked desks must be empty" — misreading the rule as
  "linked ⇒ both empty"; the actual rule allows one occupied
  neighbour. Code passing their own tests but violating the stated
  rule: recheck the rule read before the code.
- 2(c) node counts from a run without the counter (fabricated round
  numbers: 100, 1000, 10000).
