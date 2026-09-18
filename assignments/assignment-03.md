# Assignment 3 — Cost and Model (Block III)

**Due: week 22 · Weight: see [assessment plan](../docs/assessment-plan.md) ·
Covers LO7, LO8 · Submit code + report.**

This assignment has two halves: measure what an algorithm *costs*, and
model a messy situation with mathematics you can defend. Every claim needs
arithmetic or a run behind it.

## Part A — Measuring cost (10 marks)

A teammate proposes three ways to answer "did any student score exactly the
class average?" on a list `marks` of n integers:

1. `V1`: compute the average once, then scan the list for it.
2. `V2`: for each element, recompute the average of the whole list and
   compare.
3. `V3`: sort a copy, binary-search for the average.

### Tasks

(a) State, with n-expressions, the number of element-visits for each
    version (count the average's computation and the scan separately).
    *(3)*
(b) Time V1 and V2 empirically at n = 1,000 and n = 10,000 (use lists of
    even numbers so the average is an integer; report both timings and the
    ratio). Do your measurements agree with (a)? *(4)*
(c) The average being searched for may not exist in the list. Give one
    concrete list where V3's binary search is *incorrect* unless the list
    was sorted first, and explain the fix V3 already contains. *(2)*
(d) One sentence: which version would you ship, and what would change your
    mind? *(1)*

## Part B — Modelling a waiting list (10 marks)

The campus clinic runs a walk-in slot of exactly 120 minutes. Patients
arrive with consultation needs of 15, 20, or 30 minutes. The nurse sees
patients in arrival order and stops when the next patient cannot fit in
the remaining time (that patient is referred to tomorrow).

### Tasks

(a) Model the day: define the state (remaining minutes), the decision, and
    the stopping rule, precisely enough to trace by hand. *(3)*
(b) Trace your model on arrivals `[15, 20, 30, 20, 15, 30]`. Show the
    remaining time after each decision. Who is referred? *(3)*
(c) The clinic proposes: "serve the shortest consultation first". On the
    same arrivals, does the reordering serve more patients? Show the
    trace. Is reordering fair? One sentence each. *(3)*
(d) Name one input where *no* ordering serves more patients than arrival
    order — or argue none exists. *(1)*

## Submission checklist

- Part A timings: machine, n values, and raw numbers pasted; ratios shown.
- Part B: traces as tables (arrivals × remaining time).
- Every claim of "this is fair/unfair" is argued, not asserted.
- Length guide: code + 3–5 report pages.
