# Lecture Notes — Lecture 22: Recursion II: Divide and Conquer

Companion to the lecture plan and the worked examples. Read the *Definitions* before
class, the *Explanation* after it; the practice questions and the lecture quiz close the loop.

## Definitions

- **Divide and conquer** — split the problem, solve the parts recursively, combine.
- **Halving exponent** — x^n by squaring halves the exponent each step - O(log n) multiplications.
- **Recursion tree** — the picture of all calls; its size is the running time.
- **Overlapping subproblems** — the same subproblem computed many times - the disease dynamic programming cures.
- **Memoisation** — cache each subproblem's answer on first computation; reuse thereafter.

## Explanation

**Divide, conquer, combine - and measure all three.** Fast exponentiation halves the exponent (cheap split), multiplies to recombine (cheap combine); the recursion tree has log n levels: the whole cost.

**Power by halving traced.** x^10 = (x^5)^2; x^5 = x * (x^2)^2; the trace shows 4 multiplications versus 9. The 'odd exponent costs one extra multiply' detail is where most buggy implementations live.

**Overlapping subproblems made visible.** The tower-steps recursion tree for ways(5) shows ways(3) computed twice, ways(2) three times. The tree SIZE is the running time - draw it before optimising anything.

**Memoisation is a dictionary plus a question.** 'Have I seen this state?' - if yes, return the stored answer. The lecture implements memo by hand (dict keyed on the argument) before naming functools tools.

**Divide and conquer vs decrease and conquer.** Halving splits into independent halves (merge sort, powers); decrementing steps one at a time (factorial, digit sum). Recognising which family a problem belongs to predicts its cost.

## Examples

The lecture's worked examples live in [examples.md](examples.md); the case studies this
lecture builds on are worked in class from the projector. The case sequence with difficulties:
- [cs-085](../../case-studies/student/cs-085.md) (Beginner)
- [cs-086](../../case-studies/student/cs-086.md) (Foundational)
- [cs-087](../../case-studies/student/cs-087.md) (Intermediate)
- [cs-088](../../case-studies/student/cs-088.md) (Expert)

## Common misconceptions

- Assuming every recursion halves the work - decreasing by one is linear, halving is logarithmic.
- Forgetting the odd-exponent extra multiply in fast power - wrong answers on half the inputs.
- Memoising on the wrong key (a mutable list instead of its tuple).
- Drawing the recursion tree after optimising, instead of before.

## Summary and key takeaways

1. Divide-and-conquer cost = (tree width) x (tree depth) + combine cost.
2. Halving the exponent gives logarithmic algorithms.
3. Overlapping subproblems are the disease; memoisation is the cure.
4. Draw the recursion tree before optimising.

## Practice questions

- Trace fast power for 2^10 counting multiplications; mark the odd-exponent step.
- Draw the recursion tree for ways(5) (1 or 2 steps); count how many times ways(3) appears.
- Memoise the tower-steps recursion with a dictionary; report calls saved at n = 20.
- Classify five algorithms as divide-and-conquer or decrease-and-conquer; justify each.

## Where this leads

Next lecture: **Greedy and Dynamic Programming**. The quiz below checks this lecture's essentials before we build on them.
