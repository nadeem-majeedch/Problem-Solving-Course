# Lab 5 — Cycles, Remainders, and Cold Starts (Lecture 05 follow-up)

**Machine lab · 2 hours · Work in pairs.** You will implement rotation
schedules the way lecture 05 modelled them — with remainders, not calendars —
and then attack the cold-start questions that break naive cycle code. Submit:
a short report answering the checkpoints at the end.

## Setup

- Python 3 as `python`; work in `lab5/` (see [Python setup](../resources/python-setup.md)).
- Style: pseudocode first, following the [pseudocode style guide](../resources/pseudocode-style.md).

## The task

A five-person support team shares on-call duty: person 1 on day 1, person 2
on day 2, …, person 5 on day 5, person 1 again on day 6.

## Part A — Restate before you run (15 min)

A1. In two written lines: what does "day n" mean in remainder language?
    State what day 0 would be, and why the problem never asks for it.
A2. Predict (before any code): who is on call on day 47? On day 100?
    Write both predictions down — they become your test oracle.

## Part B — Implement (30 min)

B1. Write `on_call(day, people)` that returns the person number for any
    day ≥ 1. No `if`-chains over days; use the remainder operation.
B2. Verify your Part A predictions by running them. If prediction and
    program disagree, find which one is wrong and say why in one line.
B3. Extend: the team also waters the lab plants every 3rd day *counting
    from day 4* (so days 4, 7, 10, …). Write `waters(day)` and state the
    trap your first attempt fell into (the cold start is day 4, not day 1).

## Part C — Hostile inputs (30 min)

C1. What does your `on_call` return for day 0? For day −7? Decide and
    document: either define the behaviour (with a justification) or reject
    the input (with an error). "Crashes by accident" is the only wrong answer.
C2. A seventh person joins the team on day 30. The rotation becomes
    7-person from that day on. Does your function survive with a wrapper?
    Write `on_call_v2(day)` that handles the switch, and state the
    assumption that makes your answer *a* model rather than *the* model.
C3. Swap hostile-input lists with another pair (three inputs each). Run
    theirs. Record every disagreement as input / observed / expected /
    one-line mechanism.

## Part D — Trace and generalise (15 min)

D1. Hand-trace `on_call` for days 1, 2, 3 with `people = 5` in a two-column
    table (day, remainder). Mark where the remainder "wraps".
D2. One sentence: in lecture 05's language, what is the cycle length here,
    and what would change if the schedule skipped weekends?

## Checkpoints (submit these as your report)

1. Your A1 remainder statement and your two A2 predictions.
2. The B2 comparison: predictions vs program, and who was wrong.
3. `waters(day)` with the cold-start trap you hit in B3.
4. Your C1 decision for day 0 and day −7, with justification.
5. `on_call_v2` from C2 plus its stated assumption.
6. One row from the C3 exchange table.

## What completion looks like

Completion-graded as in Lab 1: full credit for a serious, honest attempt at
every checkpoint. A program that passes the two predictions but cannot say
*why* day 100 wraps to person 5 earns less than a wrong program with the
right remainder explanation.
