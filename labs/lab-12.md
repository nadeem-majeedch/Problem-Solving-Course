# Lab 12 — Recursion You Can Reason About (Lecture 22 follow-up)

**Machine lab · 2 hours · Pairs.** You will build recursions from their
base cases up, watch the call tree explode, then pay it down with
memoisation — and finish with the one-line criterion that decides when a
loop beats a recursion. Submit: the checkpoints at the end.

## Setup

- Python 3 as `python`; work in `lab12/`.
- `functools.lru_cache` allowed in Part C only.

## Part A — Base cases first (25 min)

A1. Write recursive `power2(n)`: 2ⁿ for n ≥ 0. Write the base case
    *before* the recursive case, as separate lines with a comment each.
A2. Write recursive `sum_digits(n)`. State your base case in terms of
    the *value* (not the digit count) and say why the distinction matters.
A3. Hand-trace `power2(4)` as a call tree (draw it: one box per call).
    How many boxes? How many *distinct* arguments?

## Part B — The tree that explodes (30 min)

B1. Write naive recursive `fib(k)` (fib(0)=0, fib(1)=1). Draw the call
    tree for fib(5): count the boxes and the number of times fib(2) is
    computed.
B2. Add a call counter (global or wrapper). Verify your fib(5) drawing
    against the counter's number. Then predict fib(25)'s call count
    *from the tree's growth rule* before measuring; measure and compare.
B3. In one sentence each: what does the tree waste, and what is the
    smallest structural change that stops the waste?

## Part C — Paying the tree down (25 min)

C1. Add `lru_cache` to fib. Re-measure fib(25) and fib(100). The call
    count collapses — state what the memoised call count *is* in terms
    of k, and why (each distinct argument computed once; the recursion
    depth is now the only remaining cost).
C2. Rewrite fib as a loop with two variables. Verify against the
    memoised version for k up to 30. Two sentences: which version is
    easier to *justify* (connect to Part A's base-case discipline), and
    which is easier to *derive* from the problem statement?
C3. Swap with another pair: each pair brings one recursive problem
    (their choice from lecture 22's cases); the other decides, with a
    one-sentence justification, loop-or-recursion before writing any.

## Part D — The criterion (10 min)

D1. State the lab's criterion in one sentence: *when does a recursion's
    call tree cost more than the problem itself?* (Hint: count distinct
    subproblems vs total boxes.)
D2. cs-085 (dolls) and cs-088 (tower steps) are both recursive. One
    sentence each: linear tree or branching tree — and what does that
    single fact decide about needing memoisation?

## Checkpoints (submit these as your report)

1. The three Part A base-case-first functions and the A3 tree.
2. Your fib(5) drawing with box and repeat counts.
3. The B2 prediction-vs-measurement comparison.
4. B3's two one-sentence answers.
5. C1's collapsed counts and the in-terms-of-k claim.
6. C2's loop version and the justify/derive comparison.
7. The C3 exchange decisions.
8. D1/D2.

## What completion looks like

Completion-graded as in Lab 1. The graded skill is the *tree accounting*:
box counts predicted before measuring, growth rules stated before
extrapolating. A memoised fib with no story about *why* the tree
collapsed earns half.

## Safety valve

If the naive fib(25) measurement takes longer than about ten seconds on
your machine, stop it (Ctrl+C) and measure fib(20) instead — then
explain the ratio between your two measurements using the growth rule.
Waiting is not data.
