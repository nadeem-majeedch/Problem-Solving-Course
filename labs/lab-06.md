# Lab 6 — Loop Reasoning and the Trace Table (Lecture 06 follow-up)

**Machine lab · 2 hours · Pairs, then swap.** You will *predict* loop
behaviour before running anything, then verify — the discipline lecture 06
taught with cs-021–cs-024. Submit: the report checkpoints at the end.

## Setup

- Python 3 as `python`; work in `lab6/`.
- No running code in Part A — predictions on paper only.

## The snippets

```python
# S1
total = 0
i = 1
while i <= 5:
    total = total + i * i
    i = i + 2
```

```python
# S2
xs = [4, 1, 3, 1, 5]
best = 0
for x in xs:
    if x > best:
        best = x
print(best)
```

```python
# S3
n = 6
count = 0
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    count = count + 1
```

## Part A — Predict on paper (25 min)

A1. For each snippet, write the full trace table before touching a
    keyboard: every variable, one row per iteration. For S3, also predict
    whether the loop terminates — and *why* you believe it.
A2. Mark the line in each snippet where a student is most likely to make
    an off-by-one or a wrong-initialisation error. One sentence each.

## Part B — Verify and explain the gaps (25 min)

B1. Run each snippet (add the prints you need). Compare with your table.
    For every disagreement: which row diverged first, and what does that
    say about your mental model?
B2. S2 has a latent defect. Name the input class that breaks it, give the
    input, and state the minimal fix. (Lecture 06's accumulator rule:
    initial values must come from the data's own range.)

## Part C — The prediction game (30 min)

C1. Each pair writes one 5–8 line loop snippet with a *deliberate* subtle
    defect (off-by-one, wrong initialisation, update in the wrong branch,
    non-terminating edge). Keep a correct version for yourselves.
C2. Swap snippets (not answers) with another pair. Each traces the other's
    snippet on paper, states the expected output, then runs it. Score one
    point per correct diagnosis: symptom, mechanism line, fix.
C3. For the snippet you received: write a one-sentence loop invariant —
    what is true before and after every iteration — and say whether the
    defective version violates it.

## Part D — Termination as a first-class question (10 min)

D1. S3 is the Collatz process. Your prediction in A1 was unfalsifiable for
    n = 6 without running it. In two sentences: what would you need to
    *prove* termination, and why is "I ran it and it stopped" weaker?
D2. Note one loop you have written this semester whose termination you
    never questioned. What invariant made it obvious?

## Checkpoints (submit these as your report)

1. The three A1 trace tables (photographs of paper are fine).
2. Your A2 predicted error sites, and whether B1 confirmed them.
3. The B2 defect class, input, and fix for S2.
4. Your C1 snippet (defect + correct version) and your C2 diagnosis of
   the received snippet with its score.
5. The C3 invariant sentence.
6. Your D1/D2 answers.

## What completion looks like

Completion-graded as in Lab 1. The graded skill is the *quality of the
prediction*: a wrong trace table with the divergence row honestly marked
earns full credit; a table copied after running earns none of it.
