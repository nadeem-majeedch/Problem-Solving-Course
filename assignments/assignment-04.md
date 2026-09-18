# Assignment 4 — Data Honesty (Block IV)

**Due: week 28 · Weight: see [assessment plan](../docs/assessment-plan.md) ·
Covers LO7, LO9, LO10 · Submit code + report.**

This assignment is about the two data-science skills the course has been
building since Block I: making a summary that survives scrutiny, and
simulating what you cannot measure — *without* pretending the simulation
is measurement.

## The scenario

The university's sports centre claims: *"Average gym visit lasts 52
minutes."* You are given its log for one week — as a *described* dataset,
not a file (construct it yourself per the spec below, with your generation
code submitted).

The log (per visit): a start minute (0–959), a duration in minutes, and a
member flag. The week's reality, which you must reproduce exactly:

- 400 visits on weekdays (Mon–Fri) in total, 150 at the weekend;
- durations: typical visits 30–70 minutes, but 5% of visits are
  equipment-tour sessions of exactly 15 minutes and 2% are half-day
  passes logged as 240 minutes;
- 30 of the weekday logs have duration missing (recorded as −1);
- 8 visits are exact duplicates of other visits (the door reader
  re-uploads them).

## Task 1 — The claim audit (6 marks)

(a) Compute the claim's value *as stated* from your constructed log
    (the mean including everything, after your cleaning decisions) and
    say whether 52 is defensible on your numbers. Show the arithmetic.
    *(3)*
(b) Re-compute the mean under two defensible alternative cleanings
    (e.g. with and without the 240-minute passes; with −1 rows dropped
    vs repaired). Present all three numbers in a table. *(2)*
(c) In three sentences: which number would you put on the notice, and
    what must the notice say next to it? *(1)*

## Task 2 — Cleaning ledger (5 marks)

Write the cleaning ledger for your log: every rule applied, the count of
rows it touched, and the reason. Duplicates, missing durations, and the
extreme values must each appear — with *drop / fix / keep-and-label*
decisions argued, not defaulted. End with the total rows before and
after, and reconcile the difference (numbers must add up).

## Task 3 — Simulate the uncovered case (5 marks)

The centre plans a third gym floor and needs "how many visitors are
inside at the peak minute?" (a) Define one simulation trial precisely:
what is random, what comes from the log, when does the trial end?
*(2)* (b) Implement it (standard library only), run 10,000 trials, and
report the peak headcount distribution in five buckets. State your seed.
*(2)* (c) Name the assumption in your simulation that the log *cannot*
justify, and say what data would justify it. *(1)*

## Task 4 — The honesty paragraph (4 marks)

One paragraph, ≤ 120 words, addressed to the sports centre: what the
data supports, what it does not, and the one number you refuse to print
without more data — with the reason. This is marked on calibration
(claiming neither more nor less than the evidence), not on length.

## Independent-reasoning component

Task 3(c) and Task 4 must be written from your own cleaning and
simulation choices — they cannot be copied, because the numbers differ
by the decisions earlier tasks forced. State any collaboration in one
line at the top (see [integrity](../docs/assessment-plan.md)).

## Submission checklist

- Generation code + cleaning code + simulation code (standard library
  only; seed recorded).
- The cleaning ledger with reconciled row counts.
- The three-mean table and the notice paragraph.
- Length guide: code + 3–5 report pages.
