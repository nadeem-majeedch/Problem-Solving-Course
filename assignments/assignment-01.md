# Assignment 1 — From Mess to Method (Block I)

**Due: week 8 · Weight: see [assessment plan](../docs/assessment-plan.md) ·
Covers LO1, LO3 · Submit as a single PDF or a folder of files.**

This assignment is about the *thinking before the code*. Python is optional
and earns no extra marks; precision earns the marks.

## The scenario

Your university's sports centre runs this pay-as-you-go scheme:

> Students buy session credits. A credit costs 40. Buying 5 or more credits
> at once earns a 10% discount on the whole purchase. Students who attended
> 8 or more sessions last month get one bonus credit added to any purchase
> of 2 or more credits.

A student, Priya, attended 9 sessions last month and wants to end the month
with at least 12 credits. She currently holds 3.

## Task 1 — Decompose (5 marks)

Break "how many credits should Priya buy, and what will it cost?" into a
tree of subproblems no bigger than one pseudocode block each. State your
assumptions where the scenario is silent, and mark the one assumption that
most changes the answer.

## Task 2 — Rules as pseudocode (6 marks)

Write the pricing rules as pseudocode precise enough that a classmate could
translate it without asking you a question. Include:

- the purchase cost with and without the discount,
- the bonus-credit decision,
- what your pseudocode outputs when Priya buys a given quantity,
- the answer for Priya for every purchase size she might reasonably choose.

## Task 3 — Decision and flowchart (5 marks)

Draw a flowchart of the full decision: which purchase is best for Priya
under your assumptions, and what happens at each branch. Annotate one
branch where two reasonable people could disagree, and say why.

## Task 4 — The hostile friend (4 marks)

A friend claims your rules are wrong "because sometimes buying fewer is
smarter". Give the input for which your rules and your friend's intuition
disagree, explain both answers, and state which is right under your rules —
and what rule change would make the friend right.

## Submission checklist

- Assumptions listed before solutions (task 1's tree names them).
- Pseudocode follows the [style guide](../resources/pseudocode-style.md).
- Every output number traces to a stated rule — no mental arithmetic leaks.
- Length guide: 3–5 pages. Precision beats length.
