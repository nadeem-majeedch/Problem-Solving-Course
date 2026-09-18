# Lab 10 — Counting Without Counting Wrong (Lecture 15 follow-up)

**Machine lab · 2 hours · Pairs.** Lecture 15 counted with multiplication
and division; this lab makes you *earn* the formulas by checking them
against brute force — and then using counting to predict brute force's
cost before running it. Submit: the checkpoints at the end.

## Setup

- Python 3 as `python`; work in `lab10/`.
- `itertools` is allowed for Part B *only* (it is the brute-force oracle,
  not the tool under test).

## The task

A programme committee has 9 members. For a review panel you need a chair
plus 2 ordinary members; for a warp-speed deadline there is also a
"fast pair" (any 2 members, one of whom may be the chair).

## Part A — Reason first (20 min)

A1. Chair + 2 others: compute the count by reasoning (order matters in
    the *roles*, not among the ordinary members). Show the arithmetic.
A2. Fast pair: how many? Does the chair being in the pair double or halve
    anything? Justify in one sentence.
A3. Predict: if you brute-forced A1 by trying every ordered triple of
    distinct members and filtering, how many triples would you try? What
    fraction are wasted work?

## Part B — Verify by brute force (30 min)

B1. Write the brute-force counters with `itertools.permutations` and
    `itertools.combinations` for A1 and A2. They must agree with your
    Part A arithmetic — if not, find which one is wrong (it is usually
    the reasoning).
B2. Deliberately break one formula (e.g. use combinations for the
    chair-2-ordinary step), show the disagreement numerically, and
    explain in one sentence what the wrong formula is *counting*.
B3. Timing: time the brute force at n = 9 and extrapolate (double the
    size, quadruple the time?) to n = 18. Do not run n = 18 — say why
    your extrapolation is trustworthy (or isn't) in two sentences.

## Part C — Counting as a cost model (30 min)

C1. A password lock accepts 3 distinct digits from 0–9, order matters.
    Count the keyspace two ways (formula, then brute force with
    permutations) and reconcile.
C2. The lock's policy changes: order no longer matters. Which formula
    changes, by what factor, and why is the factor exactly 6? (Say it in
    terms of the 3! orderings — then verify by brute force.)
C3. Swap with another pair: each pair states one *new* counting question
    about the committee scenario (sub-committees? paired roles?); the
    other answers by formula first, brute force second.

## Part D — When counting replaces code (10 min)

D1. In two sentences: give one question from Part C where you would never
    write the brute force in production, and say what the count bought
    you instead.
D2. cs-059 counted draws from a hat; cs-060 counted shared birthdays.
    One sentence each: which counting tool (product, permutations,
    combinations, complement) carried each, and what made it the right one?

## Checkpoints (submit these as your report)

1. Your A1–A3 reasoning with arithmetic.
2. The B1 agreement check (numbers side by side).
3. Your B2 broken-formula demonstration and explanation.
4. Your B3 extrapolation and its two-sentence defence.
5. C1/C2 reconciliations, with the factor-6 argument.
6. The C3 exchange (your question and their answer, theirs and yours).
7. D1/D2.

## What completion looks like

Completion-graded as in Lab 1. The graded skill is *formula-oracle
agreement*: a formula with no brute-force check, or a brute force with no
formula to explain it, is half the work. Wrong numbers with honest
reconciliation notes earn more than clean numbers with no story.
