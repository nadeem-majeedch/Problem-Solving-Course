# Assignment 2 — Trace, Test, Fix (Block II)

**Due: week 14 · Weight: see [assessment plan](../docs/assessment-plan.md) ·
Covers LO4, LO5, LO6 · Submit code + report.**

This assignment is about *evidence*: tracing what code really does,
designing tests that could fail, and fixing defects at the mechanism.
Python is required; every claim must be backed by a run you can reproduce.

## The scenario

The registry stores student IDs as 8-character strings: exactly 8
characters, first character a letter, last character a digit. A junior
assistant wrote this checker:

```python
def check(sid):
    if len(sid) == 8:
        if sid[0].isalpha() and sid[-1].isdigit():
            return "ok"
    return "bad"
```

Registry staff report: *"Sometimes valid IDs are called bad, and it never
explains why anything is bad."*

## Task 1 — Trace and explain (5 marks)

For each input, give the returned value and the reason in one sentence:

(a) `"CS101"`  (b) `"cs101abc"` (that is 8 characters)  (c) `"1CS0 1AB9"`
(d) `"CS0 1AB9"` (contains a space)

## Task 2 — Test table from requirements (6 marks)

Design a test table of **at least 12 rows** from the *requirements* (not
from reading the code first — write the table before looking again at
`check`). Columns: input, expected verdict, why this row exists. Mark the
three rows you predict will fail against the given code, with one line of
predicted mechanism each.

## Task 3 — Better contract (4 marks)

The staff want the verdict to name the *first* failed rule, in the order
length, first character, last character. Write the pseudocode (or Python)
for `verdict(sid)` with that contract, and state what it returns for the
empty string.

## Task 4 — Fix and prove (5 marks)

(a) Implement `verdict` in Python. *(2)*
(b) Run your task-2 table against both `check` and `verdict`; include the
    full output of both runs (12+ rows each). *(2)*
(c) In three sentences: which rows distinguished the two implementations,
    and why a suite in which every row passes proves less than one with a
    deliberate failure? *(1)*

## Submission checklist

- Task-2 table written from requirements, marked predictions included.
- Both runs' outputs pasted verbatim (no tidying).
- The empty-string answer stated, not discovered by crash.
- Length guide: code + 2–4 report pages.
