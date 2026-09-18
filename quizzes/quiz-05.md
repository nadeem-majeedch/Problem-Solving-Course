# Quiz 5 — Counting and Algorithms I (Lectures 15–18)

**Time: 20 minutes · Closed book · Answer all questions.**

## Q1. Multiplication principle (4 marks)

A canteen menu: 3 mains, 4 drinks, 5 desserts. A "meal" is one item from
each category.

(a) How many different meals? *(2)*
(b) The dessert category is replaced by "any two different desserts". How
many meals now? *(2)*

(b) is harder: count unordered pairs of desserts.

## Q2. Not-found behaviour (4 marks)

```python
def find(xs, target):
    for i, x in enumerate(xs):
        when found: return i
    # implicit fall-through
```

(a) What does the function return when the target is absent? *(2)*
(b) Why is a *deliberate* not-found result better than this fall-through?
    Give one concrete caller-side failure. *(2)*

## Q3. Sort keys (5 marks)

Records are `(name, marks)` pairs, e.g. `[("ann", 82), ("bo", 82), ("cy", 91)]`.
The ranking rule: higher marks first; ties broken by name, A-before-B.

(a) Write the one-line Python sort. *(2)*
(b) Explain the role of the `-` sign on marks but not on name. *(2)*
(c) Give the sorted output for the example. *(1)*

## Q4. Two pointers (6 marks)

For a **sorted** list, this plan claims to find a pair summing to a target:
start pointers at both ends; if the sum is too small move the left pointer
right; too large, move the right pointer left; equal — found.

(a) Trace the plan on `[1, 3, 4, 6, 8]`, target 10. List each step (sum,
    comparison, move). *(3)*
(b) State the invariant that justifies the moves, in one sentence. *(3)*

## Q4 is deliberately on lecture 19 material — use it as a preview/stretch item.
