# Lecture Notes — Lecture 19: Two Pointers and Invariants

Companion to the lecture plan and the worked examples. Read the *Definitions* before
class, the *Explanation* after it; the practice questions and the lecture quiz close the loop.

## Definitions

- **Two pointers** — two indices moving through one list under a rule - from the ends inward, or a trailing/leading pair.
- **Invariant** — a statement true before, during, and after every loop iteration; the correctness argument in miniature.
- **Movement rule** — which pointer moves when, and why that rule can never skip the answer.
- **Partition** — rearrange elements around a predicate (evens first) in place, preserving no order within groups.
- **Slow/fast pointers** — two pointers advancing at different speeds; used to detect cycles without extra memory.

## Explanation

**Invariants turn loops into proofs.** Before writing the two-pointer loop, write the sentence that stays true ('everything outside the pointers is verified'). The loop is then just maintenance of that sentence.

**The movement rule is the algorithm.** Pair sum too small: only moving the left pointer can help. Too large: only the right. Ambiguity is impossible when the array is sorted - that is why sorting is the precondition.

**Partitions trade order for speed.** Evens-first in place with two pointers does n swaps and preserves nothing inside each group. When order matters, the accumulator filter costs O(n) extra space - a genuine trade-off, not a right/wrong.

**Slow/fast and the cycle.** If one pointer chases another around a cycle, the gap shrinks by one each step and they must meet. The invariant is about relative distance - the hardest idea of the week, taught by simulation on paper.

**Termination needs a shrinking measure.** Every two-pointer loop must name what decreases (r - l, or distance to target). No measure, no proof, usually an infinite loop.

## Examples

The lecture's worked examples live in [examples.md](examples.md); the case studies this
lecture builds on are worked in class from the projector. The case sequence with difficulties:
- [cs-073](../../case-studies/student/cs-073.md) (Beginner)
- [cs-074](../../case-studies/student/cs-074.md) (Foundational)
- [cs-075](../../case-studies/student/cs-075.md) (Intermediate)
- [cs-076](../../case-studies/student/cs-076.md) (Advanced)

## Common misconceptions

- Writing the two-pointer loop before stating the invariant - then being unable to debug it.
- Moving both pointers in the same iteration of pair-sum search - can skip the unique answer.
- Believing partition must preserve within-group order - it deliberately does not; that is the speed.
- Assuming slow/fast meeting requires knowing the cycle length in advance - it does not.

## Summary and key takeaways

1. State the invariant first; the loop maintains it.
2. The movement rule is the algorithm; justify why it cannot skip the answer.
3. Partitions trade order for in-place speed; filters buy order with space.
4. Termination needs a shrinking measure - name it.

## Practice questions

- Palindrome check with two pointers; write the invariant above your loop before coding.
- Pair-sum on a sorted list for three targets; state the movement rule and why it never skips the answer.
- Partition a list evens-first in place; count swaps and state what order property you gave up.
- Simulate slow/fast on a drawn 4-node cycle; show the gap shrinking to zero.

## Where this leads

Next lecture: **Brute Force Workshop**. The quiz below checks this lecture's essentials before we build on them.
