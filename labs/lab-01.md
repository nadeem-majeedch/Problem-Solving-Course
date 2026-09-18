# Lab 1 — From Problem to Program (Lecture 04 follow-up)

**Machine lab · 2 hours · Work in pairs.** You will take one case from paper
to running program, then break each other's programs on purpose. Submit: a
short report answering the six checkpoints at the end.

## Setup

- Python 3 available as `python` (see [Python setup](../resources/python-setup.md)).
- Create `lab1/` in your workspace; every file goes there.
- Style: follow the [pseudocode style guide](../resources/pseudocode-style.md).

## The task

Take case **cs-013** ("Echo with Limits": read numbers until sentinel 0,
then report how many were read, their sum, and the largest). Your version
today works on a fixed list instead of live input:

```python
session = [7, 3, 15, 2, 9, 3]
```

## Part A — Plan first (20 min)

A1. State your assumptions in two or three written lines *before* any code
    (What if the list is empty? What is "the largest" then?).
A2. Write pseudocode for: count, sum, and largest, in **one** pass.

## Part B — Translate and run (30 min)

B1. Translate your pseudocode to Python in `lab1/echo.py`, printing the
    three results.
B2. Run it on `session` above. Record the output.
B3. Change the list to `[]` and to `[4]`. Record both outputs. If either
    crashes or prints nonsense, fix the program minimally and note what you
    changed.

## Part C — Break and fix (40 min)

C1. Pair with another pair. Exchange only your *test lists* (not code):
    each pair sends three lists designed to expose flaws — one boundary
    list, one "all identical" list, one of your choice.
C2. Run their lists against your program. For every wrong output, write the
    input, the observed result, the expected result, and one sentence on
    the mechanism.
C3. Fix each defect at the mechanism. Re-run the whole exchange list again
    after each fix (regression thinking).

## Part D — Trace on paper (15 min)

D1. Swap programs (not computers: print or read the code). Hand-trace the
    other pair's program on `session = [2, 8]` with a two-column variable
    table. Mark any line whose behaviour differs from your own version.

## Checkpoints (submit these as your report)

1. Your stated assumptions from A1, and whether the code ended up matching them.
2. Your pseudocode from A2 and the final Python from B1 — point at the line
   where translation was hardest and say why.
3. The three recorded outputs from B2–B3.
4. From C2: one defect table row (input / observed / expected / mechanism).
5. The fix you made in C3, and the re-run that proved it.
6. From D1: one difference you found in the other pair's program, and
   whether it was a defect or a style difference.

## What completion looks like

The lab is completion-graded: full credit for a serious attempt at every
checkpoint with honest notes, including notes about things that did not
work. Correctness matters less than the evidence of method.
