# Lab 3 — Sort, Scan, and Measure (Lecture 18 follow-up)

**Machine lab · 2 hours · Work in pairs.** You will sort real-shaped records,
scan for adjacent-pair answers, and measure what sorting buys you. Submit: a
report answering the checkpoints.

## Setup

- Python 3 as `python`; files in `lab3/`.
- The dataset (paste into `lab3/data.py`):

```python
students = [
    ("ann", 82, "cs"), ("bo", 82, "ds"), ("cy", 91, "cs"),
    ("dee", 67, "ds"), ("eli", 74, "cs"), ("fay", 91, "math"),
    ("gus", 59, "cs"), ("hal", 74, "ds"), ("ivy", 88, "math"),
    ("jon", 59, "cs"),
]
```

Each record is `(name, marks, programme)`.

## Part A — Three sorts, three purposes (30 min)

A1. Produce the ranking: marks descending, ties by name ascending. Record
    the one-line sort and its output.
A2. Produce the grouping view: programme ascending, then marks descending
    within a programme. Record the sort.
A3. Produce "who is nearest to the pass mark of 60?" — sort by *distance
    from 60* and list the two closest names. Record the key function.

## Part B — Adjacent-pair scans (30 min)

B1. Using the ranking from A1, scan adjacent pairs to find every pair of
    students whose marks differ by at most 2. Print each pair.
B2. Do the same *without sorting* (all pairs, nested loops). Record both
    outputs — they must match — and count how many comparisons each version
    made. (Add a counter to each loop.)

## Part C — Does sorting pay? (25 min)

C1. Task: find whether any two students have identical marks. Write the
    nested-loop version and count comparisons on the 10-row data.
C2. Write the sort-then-scan version (equal marks must sit adjacent) and
    count its comparisons (sort cost: count comparisons in a `sorted` call
    by sorting a copy and incrementing a wrapper counter, or estimate it as
    n log n ≈ 10 × 3.3 ≈ 33 — state which you did).
C3. Now imagine 10,000 students instead of 10. Which version survives, and
    what is the arithmetic that decides it?

## Part D — Stability probe (15 min)

D1. Sort by marks only (descending), print, then re-sort that result by
    programme and print again. Do students with equal marks appear in the
    same relative order as after the first sort? Python sorts are stable —
    explain what that guaranteed here, in one or two sentences.

## Checkpoints (submit these as your report)

1. The three sorts from Part A with their key functions and outputs.
2. From B1–B2: the matching outputs and both comparison counts.
3. From C1–C3: both counts on 10 rows and the 10,000-row arithmetic.
4. From D1: your stability observation and explanation.
5. One sentence: which of A1–A3 was hardest to express as a key function,
   and what made it hard.

## What completion looks like

Completion-graded: every part attempted with recorded outputs and counts.
Where a count surprises you, write down the surprise — that is the report's
best content.
