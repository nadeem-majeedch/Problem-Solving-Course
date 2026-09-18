# Lecture Notes — Lecture 21: Binary Search Everywhere

Companion to the lecture plan and the worked examples. Read the *Definitions* before
class, the *Explanation* after it; the practice questions and the lecture quiz close the loop.

## Definitions

- **Binary search** — repeatedly halve a sorted search space by probing the middle
- **Search space** — the range of positions (or answers) still consistent with everything seen so far
- **Invariant** — a statement true before and after every loop step; here, 'the target is inside lo..hi'
- **Monotone predicate** — a yes/no question that flips from no to no... yes yes across an order
- **Probe** — one middle test; each probe discards half of the space
- **Logarithmic cost** — O(log n): doubling the data adds only one more probe

## Explanation

Binary search is a precondition turned into an algorithm: if the data is sorted (or the answer sits in a monotone yes/no landscape), every probe of the middle discards half the remaining space. Twenty probes cover a million items. The discipline is the invariant - 'the target, if present, lies in lo..hi' - maintained by every branch. The variant that unlocks the block is searching on the answer: 'smallest capacity that works' is findable by binary search whenever feasibility is monotone (works, works... fails, fails). Book allocation and first-bad-commit are that pattern in disguise: the predicate does the work, the halving does the speed. Common ground: every binary-search bug is an off-by-one or a broken invariant, which is why we write the invariant as a comment and test on 0, 1, and 2 elements. If you can state 'yes for small, no for large' (or vice versa), you can binary search it.

## Examples

The lecture's worked examples live in [examples.md](examples.md); the case studies this
lecture builds on are worked in class from the projector. The case sequence with difficulties:
- [cs-081](../../case-studies/student/cs-081.md) (Beginner)
- [cs-082](../../case-studies/student/cs-082.md) (Foundational)
- [cs-083](../../case-studies/student/cs-083.md) (Intermediate)
- [cs-084](../../case-studies/student/cs-084.md) (Expert)

## Common misconceptions

- Binary searching unsorted data - the invariant requires the precondition, not optimism.
- Computing mid as (lo+hi)//2 and forgetting it rounds down - test on even and odd lengths.
- Off-by-one exits: `lo < hi` versus `lo <= hi` change which cases are probed.
- Believing binary search always wins - sorting first costs O(n log n); one search on unsorted data should just scan.
- Forgetting the predicate version: 'smallest feasible cap' is a binary search on the answer, not on array positions.

## Summary and key takeaways

1. Sorted data (or a monotone yes/no landscape) converts scanning into halving.
2. Write the invariant first: 'the target lies in lo..hi' survives every branch.
3. Every binary-search bug is an off-by-one or a broken invariant - test on 0, 1, 2 elements.
4. The predicate variant searches answers, not arrays: smallest feasible cap, first bad commit.
5. O(log n): a million items in twenty probes - preconditions have this price tag.

## Practice questions

- Binary search a sorted list of 8 course codes by hand: write lo, hi, mid at every step.
- Adapt the first-bad-version loop to 'first day a sensor exceeded 50' on a monotone exceed-flag.
- Prove to yourself the loop terminates: what quantity strictly shrinks every iteration?
- Enrichment: smallest capacity that ships the boxes in 3 trips - feasibility sweep plus binary search on the cap.
- Enrichment: count probes for n = 1000 exactly; compare with the ceil(log2(n+1)) bound.

## Where this leads

Next lecture: **Recursion II: Divide and Conquer**. The quiz below checks this lecture's essentials before we build on them.
