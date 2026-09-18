# Quiz 6 — Answer Key (instructor only)

Not for publication. Marking notes in *italics*.

## Q1. Loop invariants (4)

(a) *(2)* Invariant: after the loop body runs with counter value `i`,
`p` equals `(i−1)!` — i.e. "at the top of each iteration, p holds the
product 1×2×…×(i−1)". *(Accept any sentence that is (i) true before and
after every iteration and (ii) connects p to i. "p is the factorial of
the previous i" is the expected shape. A bare "p grows every time" is
not an invariant — 1 mark.)*

(b) *(2)* Exit: `i = n+1`. Substituting into the invariant: p holds
1×2×…×n = n!. *(The mark is for *using* the exit condition with the
invariant — substitution, not re-tracing.)*

## Q2. Binary search mechanics (5)

(a) *(3)* n = 8; test false for 1–5, true for 6–8:

| step | lo | hi | mid | test(mid) | new interval |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | 8 | 4 | false | [5, 8] |
| 2 | 5 | 8 | 6 | true | [5, 6] |
| 3 | 5 | 6 | 5 | false | [6, 6] |

Loop ends (lo = hi = 6). Answer: first true position is 6.

*(1 mark per correct row up to 3; accept an equivalent trace with mid
rounded the other way only if the interval sequence stays correct —
with (lo+hi)//2 the table above is the canonical one.)*

(b) *(2)* With `lo TO mid` in the ELSE branch, an interval of size two
where mid = lo and test(mid) is false sets `lo TO lo` — the interval
stops shrinking while the loop condition `lo < hi` still holds, so the
loop spins forever. *(The mark needs both halves: no shrinkage AND
why the condition still holds. "Infinite loop" alone earns 1.)*

## Q3. Recursion structure (5)

(a) *(2)* Missing: the base case. Smallest exposing input: `[]` —
infinite self-calls ending in `IndexError` (slicing an empty list gives
`[]` forever until Python's recursion limit; the observable symptom may
be the RecursionError rather than the IndexError — accept either
symptom named, the mark is for `[]` as the smallest input).

(b) *(1)*

```python
def total(xs):
    if not xs:
        return 0
    return total(xs[1:]) + xs[0]
```

*(Name changed to `total` to avoid shadowing the built-in `sum` —
accept the student keeping `sum` but note the shadowing in feedback;
do not deduct.)*

(c) *(2)* Each call holds its own slice `xs[1:]` alive — a fresh list of
n−1, n−2, … elements — so memory grows with the *sum of slice lengths*
(≈ n²/2 elements) plus n stack frames; the loop needs one frame and no
copies. *(Full marks for slice-copies or stack-frames with the growth
direction stated; 1 mark for "uses more memory because of the stack"
alone.)*

## Q4. Divide and conquer (6)

(a) *(3)* Input `[4, 3, 2, 1]`: halves are `[4, 3]` and `[2, 1]`; inside-half
inversions: (4,3) and (2,1) = 2. Total inversions in the full array:
6 — the missed pairs are the cross-half ones: (4,2), (4,1), (3,2),
(3,1). *(1 mark for a correct total (6), 1 for the halves' internal
count (2), 1 for naming the missed cross pairs. Any 4-element input
with cross-half inversions is acceptable — the lexicographically
smallest is [1, 3, 2, 4], whose single inversion (3, 2) is cross-half.)*

(b) *(2)* The combine step must count *cross* inversions — pairs (i, j)
with i in the left half, j in the right half, and left value > right
value — which merge-sort's merge step can count in one linear pass
over the sorted halves. *(The mark: cross-half counting named; bonus
language about merge doing it cheaply is welcome but not required for
the 2.)*

(c) *(1)* "Missing the combine step" — in course terms: *forgetting the
work that happens when the two solved halves meet* (the divide-and-
conquer trio is divide, conquer, **combine**). *(Accept any phrasing
that names the combine step; "divide and conquer minus the conquer" is
wrong but close — 0 or 1 by whether the cross-half work is mentioned.)*

Grade boundaries suggestion: 16–20 excellent · 11–15 good · 7–10
satisfactory · below 7 revisit lectures 19–22.
