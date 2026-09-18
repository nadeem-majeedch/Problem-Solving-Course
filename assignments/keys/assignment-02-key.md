# Assignment 2 — Marking Key (instructor only)

Not for publication. Companion to [rubric-02](../rubric-02.md).

## Task 1 — reference answers

- (a) `"CS101"` → `"bad"` (length 5 ≠ 8).
- (b) `"cs101abc"` (8 chars) → `"bad"` (last character `c` is not a digit).
- (c) `"1CS0 1AB9"` (8 chars) → `"bad"` (first character `1` not a letter;
  also the space fails nothing *named* — the rule only checks positions 0
  and 7, which is worth surfacing in class: interior garbage is invisible
  to this contract).
- (d) `"CS0 1AB9"` → `"bad"` (7 characters).

## Task 2 — what a strong table covers

Rule × {pass, fail} = 6 base rows; length boundaries 7/8/9; empty string;
8 chars with letter first and digit last but junk inside (e.g.
`"A@#$%1239"` — passes the contract as written: an excellent row for the
spec-ambiguity discussion); trailing newline from file input
(`"CS101AB9\n"` is 9 characters); all-letter; all-digit; unicode letters
(`isalpha` accepts `"é"` — an honest surprise to report).

Predicted failures against `check` (the given code returns only ok/bad, so
*every* row's "expected first-failure verdict" mismatches — the marked
predictions should focus on rows where even ok/bad is wrong: rows where the
length passes but positions fail, and vice versa).

## Task 3 — reference verdict

```python
def verdict(sid):
    if len(sid) != 8:
        return "length"
    if not sid[0].isalpha():
        return "first character"
    if not sid[-1].isdigit():
        return "last character"
    return "valid"
```

Empty string → `"length"` (first rule fails). Pseudocode equivalent
acceptable; the contract point is *ordering* and the explicit empty case.

## Task 4 — what the runs must show

- `check` run: every row either "ok" or "bad"; rows like
  `("cs101abc", "last character")` and `("1CS0 1AB9", "first character")`
  discriminate.
- `verdict` run: all PASS if the table was right; a FAIL row means either
  the row or the code is wrong — the report must say which and why.
- The three-sentence comparison should land on: a suite with a deliberate
  failure *demonstrated* the defect; a suite where everything passes only
  says "these inputs behaved"; discriminating rows are the informative
  ones.

## Common faults to name in feedback

- Tables with 10 happy rows and one boundary (then claiming 12).
- `verdict` implementations that check the last character first (order
  bug, exactly the contract the task tests).
- Empty string answered by crash in the pasted run (the task told them to
  state it).
- Predictions marked after running (walk the room during the deadline
  week if submission format allows ordering evidence: task 2 tables saved
  before task 4 runs).
