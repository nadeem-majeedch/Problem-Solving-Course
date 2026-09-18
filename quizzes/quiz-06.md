# Quiz 6 — Algorithms II (Lectures 19–22)

**Time: 20 minutes · Closed book · Answer all questions.**

## Q1. Loop invariants (4 marks)

A loop is meant to compute `n!` (factorial):

```python
p = 1
i = 1
while i <= n:
    p = p * i
    i = i + 1
```

(a) State an invariant for this loop — one sentence describing what is true
    before and after every iteration. *(2)*
(b) Use the invariant plus the exit condition to justify that `p` holds
    `n!` when the loop ends. *(2)*

## Q2. Binary search mechanics (5 marks)

For the "first position where test(mid) is true" pattern:

```
lo TO 1; hi TO n
WHILE lo < hi DO
    mid TO (lo + hi) / 2   (integer division)
    IF test(mid) THEN hi TO mid ELSE lo TO mid + 1
END WHILE
```

(a) Show the interval `[lo, hi]` after each step when `n = 8` and test is
    false for 1–5, true for 6–8. *(3)*
(b) Explain in one sentence why `lo TO mid` (without the +1) in the ELSE
    branch could loop forever. *(2)*

## Q3. Recursion structure (5 marks)

A recursive `sum(xs)` over a list is written:

```python
def sum(xs):
    return sum(xs[1:]) + xs[0]
```

(a) Name what is missing and give the smallest input that exposes it. *(2)*
(b) Write the corrected function. *(1)*
(c) The corrected function is called on a 1000-item list. Explain why it is
    memory-hungry compared with a loop, in one sentence. *(2)*

## Q4. Divide and conquer (6 marks)

Merge-style thinking: to count inversions in `xs` (pairs i < j with
xs[i] > xs[j]), a student proposes: split the list in half, count inversions
inside each half recursively, and return the sum of the two counts.

(a) Give a 4-element input where this returns the wrong answer, and show the
    pair it misses. *(3)*
(b) State in one sentence what the combine step must add. *(2)*
(c) What is this missing-combine error called, colloquially, in course
    terms? *(1)*
