# Lab 9 — Dictionaries as Decisions (Lecture 13 follow-up)

**Machine lab · 2 hours · Pairs.** You will replace a wall of `if`-branches
with a mapping, then discover what the mapping version makes *easier* (and
one thing it makes harder). Submit: the checkpoints at the end.

## Setup

- Python 3 as `python`; work in `lab9/`.

## The task

A campus printer charges by user category: `student` 0.05/page, `staff`
0.08/page, `visitor` 0.15/page, `honorary` free. New categories appear
every term, and one category (`visitor`) also has a per-month cap.

## Part A — The branch version (20 min)

A1. Write `cost_branches(category, pages)` using an `if`/`elif` chain.
    Handle an unknown category by returning `None` (and say why `None`
    beats guessing a price).
A2. Count the places in your function that must change when the business
    adds a category. Write the number down.

## Part B — The mapping version (25 min)

B1. Rewrite as `cost_map(category, pages)` with a module-level dictionary
    `RATES` and no category branches. The unknown-category case must
    behave identically to A1.
B2. Count the change-places again. Compare with A2 and explain the
    difference in one sentence (the word "data" should appear in it).
B3. The visitor cap: a visitor's *monthly* total cannot exceed 5.00.
    Your function sees only (category, pages) — so the cap cannot live
    inside it honestly. Write the wrapper `visitor_month_cost(pages_list)`
    that enforces the cap, and state which rule decision you had to make
    (truncate the last job? refuse it? charge partially?).

## Part C — Inverting the map (30 min)

C1. Build the inverse map `who_pays(price)` from price back to category.
    What breaks? (Hint: two categories can share a price — and one price
    is 0 for `honorary` but also for zero pages of anyone.)
C2. Make `who_pays` total: decide and document a rule for ambiguous and
    missing prices. Your rule must be checkable by a one-line test table.
C3. Swap test tables with another pair; adjudicate their `who_pays`
    against *their* stated rule, not yours.

## Part D — Aggregation (15 min)

D1. Given the day's log `[(category, pages), ...]`, produce revenue per
    category in one pass using the mapping version. Two sentences: which
    accumulator pattern from lecture 09 this is, and where the mapping
    earned its keep.

## Checkpoints (submit these as your report)

1. `cost_branches` with its A2 change-place count.
2. `cost_map` with its B2 count and the comparison sentence.
3. Your B3 cap decision, stated as a rule.
4. The C1 breakage story and your C2 totality rule with its test table.
5. Your C3 adjudication notes.
6. The D1 one-pass aggregation and its pattern name.

## What completion looks like

Completion-graded as in Lab 1. The graded insight is the A2/B2 contrast:
the branch version hides its policy in control flow, the mapping version
exposes it as data. Code that "works both ways" without the sentence
earns less than broken code with the sentence.
