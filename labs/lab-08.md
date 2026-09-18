# Lab 8 — Writing Tests Before Trusting (Lecture 08 follow-up)

**Machine lab · 2 hours · Pairs; adversarial rounds.** You will build a
test table *from requirements* for an untrusted implementation, run
adversarial rounds against another pair's table, and end with a property
that no single test can prove but every test can strengthen. Submit: the
checkpoints at the end.

## Setup

- Python 3 as `python`; work in `lab8/`.
- The program under test: `fee.py` (your instructor distributes it, or
  you type it from below into `lab8/fee.py`).

## The program under test

```python
"""fee.py — lab library fee.

Rules (from the library's stated policy):
  * base fee 2.00 for any loan;
  * 0.30 per day for each day late, days 1..14;
  * after day 14 the daily rate drops to 0.10 per day (days 15+);
  * the total fee is capped at 8.00;
  * returning early or on time costs only the base fee.
"""
def fee(days_late):
    if days_late <= 0:
        return 2.00
    total = 2.00
    total = total + min(days_late, 14) * 0.30
    if days_late > 14:
        total = total + (days_late - 14) * 0.10
    return min(total, 8.00)
```

The implementation above contains **no deliberate defect** — or it does;
you are not told. Your job is to test it as if you did not write it.

## Part A — Requirements to tests (25 min)

A1. From the docstring's rules alone, build a test table: input,
    expected output (computed by hand from the rules, not from running
    the code), and which requirement each row exercises. Include at
    least: both sides of every boundary (0/1, 14/15), one mid-range day,
    the cap region, and one "return early" row.
A2. Mark the two rows you expect to be *most likely* to fail a sloppy
    implementation, with one sentence of reasoning each.

## Part B — Run and adjudicate (20 min)

B1. Run the table against `fee.py`. For every mismatch: recompute the
    expected value by hand before claiming the program is wrong — your
    table is guilty until proven innocent.
B2. Verdict: defect found or no defect found. If found: the exposing
    input, observed vs expected, and the mechanism in one sentence. If
    not: which of your rows came closest, and why "closest" is not proof.

## Part C — Adversarial rounds (30 min)

C1. Write three new rows designed to break another pair's *verdict*
    confidence, not the program: one boundary pair, one cap-edge row,
    one row where two rules interact (e.g. the cap reached exactly on a
    day boundary). Exchange tables; run theirs against the same `fee.py`.
C2. Report: did the received table contain a row you had not thought of?
    Did any row *fail*? If a row "failed", adjudicate: program wrong or
    expected-value wrong?
C3. The instructor reveals the ground truth about `fee.py`. Score: one
    point per row that was executable (expected value pre-computed), one
    point per defect correctly adjudicated.

## Part D — The property (15 min)

D1. State one property that should hold for *all* inputs (e.g. "fee is
    non-decreasing in days late", "fee is at least 2.00 and at most
    8.00"). Check it by hand on your table rows.
D2. One sentence: why does even a 30-row table not *prove* the property,
    and what kind of argument would?

## Checkpoints (submit these as your report)

1. Your A1 table with the requirement column filled.
2. Your A2 two most-suspect rows with reasoning.
3. The B2 verdict with your adjudication argument.
4. Your C1 three rows and the C2 adjudication of the received table.
5. Your D1 property and the D2 sentence.

## What completion looks like

Completion-graded as in Lab 1. The graded skill is *expectation
discipline*: every row needs a pre-computed expected value and a named
requirement. A table that "passes" because its expected values were read
off the program's output earns nothing — that tests nothing.
