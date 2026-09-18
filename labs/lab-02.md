# Lab 2 — Strings and Test Tables in Practice (Lecture 10 follow-up)

**Machine lab · 2 hours · Work in pairs.** You will build a small text tool
driven by a test table you design *before* the code, then exchange test
tables with another pair. Submit: a report answering the checkpoints.

## Setup

- Python 3 as `python`; files in `lab2/`.
- The tool you will build: an **ID verifier**. A student ID is valid when it
  has exactly 8 characters, starts with a letter, and ends with a digit —
  the same rule as quiz 3, now as a tested program.
- The verdict must name the *first* rule that fails, in this order:
  length, first character, last character. Valid → `"valid"`.

## Part A — Test table first (25 min)

A1. On paper, design a test table with **at least 10 rows**: columns are
    `input`, `expected verdict`, `why this row exists`. Cover: every rule's
    pass and fail side, every boundary of the length rule, and at least two
    inputs you think are clever.
A2. Circle the two rows you believe are most likely to catch a defect.

## Part B — Implement (35 min)

B1. Write `lab2/verify.py` with a function `verdict(sid)` returning the
    verdict string, plus a driver that runs your Part-A table:
    for each row, print input, expected, observed, and PASS/FAIL.
B2. Run it. If any row fails, fix `verdict` — *never* change the expected
    column to make a row pass unless you can argue the row itself was wrong.

## Part C — Exchange (30 min)

C1. Exchange test tables with another pair. Run their rows against your
    `verdict`. Report any failure in their format: input / expected /
    observed.
C2. Negotiate: either their row encodes a rule yours lacks (fix your code),
    or the two tables disagree about the spec (write down the ambiguity —
    you will need it for checkpoint 5).
C3. Add the best two of their rows to your table and re-run everything.

## Part D — Normalisation stretch (20 min, optional)

D1. Real ID lists arrive with stray spaces and case noise: `" CS101  "` or
    `"cs101"`. Add a preprocessing step and discuss: does normalising before
    verifying change any verdict? Which row of your table proves it?

## Checkpoints (submit these as your report)

1. Your Part-A table (photograph or transcription), with the circled rows.
2. The final `verify.py` driver output for your table (all rows).
3. Any row that failed in B2, the mechanism, and the fix.
4. From C1–C2: one row your table lacked and one genuine spec ambiguity
   you and the other pair resolved.
5. From D1 (if attempted): the normalisation rule and the row that shows
   its effect.
6. One sentence: which circled row from A2 actually caught something, and
   which caught nothing — and what that taught you about designing tests
   before code.

## What completion looks like

Completion-graded: a table of ≥ 10 deliberate rows, an honest driver run,
and the exchange analysis. A table where every row passes *and* every row
is obviously safe is a red flag — the exchange exists to break that comfort.
