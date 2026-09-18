# Lecture Notes — Lecture 18: Sorting as an Idea

Companion to the lecture plan and the worked examples. Read the *Definitions* before
class, the *Explanation* after it; the practice questions and the lecture quiz close the loop.

## Definitions

- **Stable sort** — equal keys keep their original relative order - the property that makes sort-by-one-key-at-a-time compose.
- **Composite key** — a tuple used as the sort key so ties break on later components.
- **Merge** — combine two sorted lists into one in a single linear pass - the engine of merge sort.
- **Selection sort (idea)** — repeatedly pick the smallest remaining element; O(n^2) comparisons regardless of input.
- **Insertion sort (idea)** — grow a sorted prefix by sliding each new item left into place; fast on nearly-sorted data.
- **Comparison sort** — any sort that only asks 'is a before b?'; log(n!) is its information-theoretic floor.

## Explanation

**Sorting is a family, not a function.** The lecture builds three intuitions - select the smallest, insert into a sorted prefix, merge two sorted runs - before naming any real algorithm.

**Stability is the quiet hero.** Sort by name, then by score, and equal scores stay alphabetical - because each pass is stable. Unstable sorts force composite keys; the leaderboard case shows both paths.

**Merge is where the speed comes from.** Merging two sorted halves is linear; halving the problem log n times gives n log n total. The merge itself is done on paper with two fingers.

**The merge rule and its tie-break.** Take from the left run when values are equal (or the tie-break says otherwise); arbitrary choices break stability and reproduce-ability.

**Almost-sorted inputs are special.** Insertion sort on nearly-sorted data is nearly linear - a practical lesson: measure your data's shape before choosing a method.

## Examples

The lecture's worked examples live in [examples.md](examples.md); the case studies this
lecture builds on are worked in class from the projector. The case sequence with difficulties:
- [cs-069](../../case-studies/student/cs-069.md) (Beginner)
- [cs-070](../../case-studies/student/cs-070.md) (Foundational)
- [cs-071](../../case-studies/student/cs-071.md) (Intermediate)
- [cs-072](../../case-studies/student/cs-072.md) (Expert)

## Common misconceptions

- Believing sorted() sorts in place - it returns a new list; the original is untouched.
- Sorting by one key then overwriting with another, expecting both to apply - order of passes matters.
- Assuming stability without checking the documented contract of the sort used.
- Treating n log n vs n^2 as academic - on 100k items it is the difference between instant and minutes.

## Summary and key takeaways

1. Three intuitions: select, insert, merge - every sort is one of these plus engineering.
2. Stability composes multi-key sorts; check it before relying on it.
3. Merging is linear; halving logarithmically gives n log n.
4. Nearly-sorted data changes the best choice - measure the shape.

## Practice questions

- Merge two sorted lists with two fingers on paper, then in code; note your tie-break rule.
- Rank a leaderboard by score then name two ways: composite key, and two stable passes.
- Trace selection sort on [4, 1, 3, 2] counting comparisons; do the same for insertion sort on [1, 2, 3, 4].
- Explain to a friend why merging sorted halves beats rescanning everything.

## Where this leads

Next lecture: **Two Pointers and Invariants**. The quiz below checks this lecture's essentials before we build on them.
