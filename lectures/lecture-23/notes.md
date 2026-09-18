# Lecture Notes — Lecture 23: Greedy and Dynamic Programming

Companion to the lecture plan and the worked examples. Read the *Definitions* before
class, the *Explanation* after it; the practice questions and the lecture quiz close the loop.

## Definitions

- **Greedy choice** — take the locally best option now and never reconsider it
- **Exchange argument** — a proof that any optimal solution can be reshaped into the greedy one
- **Counterexample** — a small input where a proposed rule gives a provably wrong answer
- **Overlapping subproblems** — a recursive computation that recomputes the same smaller cases many times
- **Memoisation** — cache each subproblem's answer the first time it is computed
- **Dynamic programming** — solve every needed subproblem once, in an order that makes each answer ready when required

## Explanation

Two strategies for optimisation problems. Greedy: sort by a rule, take while legal, never look back. It is fast and often right - but 'often' is not 'always', so each greedy claim needs an exchange argument (any optimal answer can be re-arranged into the greedy one) or falls to a counterexample. Interval scheduling (earliest end wins) survives; coin systems with weird denominations do not. Dynamic programming is the fallback when greedy fails: if a recursive definition keeps recomputing the same cases, cache them (memoisation) or fill a table bottom-up. The four declarations - state (what dp[j] means), transition (how answers compose), base case, evaluation order - turn any DP from magic into bookkeeping. Knapsack is the standard bearer: greedy by points-per-hour fails a tiny example, the dp-over-budget table succeeds. Rule of thumb: try greedy (with proof), fall back to DP when the greedy counterexample appears.

## Examples

The lecture's worked examples live in [examples.md](examples.md); the case studies this
lecture builds on are worked in class from the projector. The case sequence with difficulties:
- [cs-089](../../case-studies/student/cs-089.md) (Beginner)
- [cs-090](../../case-studies/student/cs-090.md) (Foundational)
- [cs-091](../../case-studies/student/cs-091.md) (Intermediate)
- [cs-092](../../case-studies/student/cs-092.md) (Advanced)

## Common misconceptions

- Assuming the greedy that works on one example is proven - exchange argument or counterexample, no exceptions.
- Sorting by the wrong key: earliest start fails interval scheduling where earliest end succeeds.
- Memoising without a base case - the cache never fills, the stack never unwinds.
- Iterating the knapsack budget ascending with 0/1 items - that allows reusing an item twice.
- Conflating DP with recursion - DP is the recursion plus an evaluation order that never recomputes.

## Summary and key takeaways

1. Greedy needs a proof (exchange argument) or a counterexample - then retreat to DP.
2. Earliest-end wins interval scheduling; the same data defeats start-first and shortest-first.
3. Memoisation fixes recomputation: cache the answer, halve the tree.
4. DP in four declarations: state, transition, base, order.
5. 0/1 knapsack iterates the budget descending - ascending silently reuses items.

## Practice questions

- Interval scheduling on 6 meetings: sort by end, sweep, and write the taken set.
- Break cheapest-first coin change with the denominations 1, 3, 4 and amount 6.
- Memoise ways(n) (1-or-2 stairs) and report the call counts for plain vs cached at n = 12.
- Enrichment: knapsack dp table for 3 items, budget 4 - fill it by hand, then check in code.
- Enrichment: write the exchange argument for earliest-end in four sentences.

## Where this leads

Next lecture: **Graphs as Models**. The quiz below checks this lecture's essentials before we build on them.
