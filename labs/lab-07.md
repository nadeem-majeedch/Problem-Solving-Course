# Lab 7 — The Debugging Clinic (Lecture 07 follow-up)

**Machine lab · 2 hours · Pairs; rotating patients.** Three "patient"
programs, each with one planted defect, each failing a different way. You
will practise the method from lecture 07 — reproduce, isolate, hypothesise,
test, fix, re-run — under time pressure, then trade your method notes.
Submit: the checkpoints at the end.

## Setup

- Python 3 as `python`; work in `lab7/`.
- Your instructor hands out `patient_a.py`, `patient_b.py`, `patient_c.py`
  (prepared versions of the snippets below, wrapped so each runs and
  prints a wrong answer rather than crashing — silent wrong answers are
  the hardest kind and the point of this lab).

## The patients

```python
# Patient A — "average marks"  (prints a plausible but wrong average)
marks = [72, 85, 90, 60, 55, 91]
total = 0
for i in range(1, len(marks)):
    total = total + marks[i]
print("average:", total / len(marks))
```

```python
# Patient B — "pass counter"   (counts one student twice / one never)
marks = [72, 85, 90, 60, 55, 91]
passes = 0
for m in marks:
    if m >= 60:
        passes = passes + 1
    if m > 60:
        passes = passes + 1
print("passed:", passes)
```

```python
# Patient C — "last over first" (reports the wrong record)
marks = [72, 85, 90, 60, 55, 91]
names = ["ann", "bo", "cy", "di", "el", "fay"]
best = 0
best_name = ""
for k in range(len(marks)):
    if marks[k] >= best:
        best = marks[k]
        best_name = names[k]
print("top student:", best_name)
```

## Part A — Reproduce and observe (15 min)

A1. Run each patient. For each: the observed output, the expected output
    (derive it by hand first — do not guess), and a one-line symptom
    description ("off by one mark", "counts 90 twice", …).

## Part B — Isolate and fix, methodically (45 min)

B1. For each patient, *before* fixing: state the hypothesis ("the loop
    starts at the wrong index"), the observation that confirms it (a
    print of the loop variable), and *then* the minimal fix.
B2. After each fix, re-run the patient **and** one input where it was
    already behaving (regression check). A fix that changes correct
    behaviour elsewhere is a new defect.
B3. Log each patient as: symptom → hypothesis → confirming observation →
    fix → re-run result. The log is the deliverable, not the fix.

## Part C — The method swap (20 min)

C1. Swap logs with another pair. For each of their patients, answer:
    did their hypothesis come *before* their fix? Was their confirming
    observation actually confirming (would it also fit a different
    hypothesis)?
C2. One paragraph: which patient's defect was found fastest by your
    method and which would have been found faster by just reading the
    code? Say what that means for when the method pays.

## Part D — Beyond the given (10 min)

D1. Patient C has a second, subtler issue tied to its tie behaviour.
    Find it, and state the input where it matters.
D2. One sentence: why does a *silent* wrong answer (no crash) demand a
    different working style than an exception does?

## Checkpoints (submit these as your report)

1. The A1 symptom table (observed vs expected, derived by hand).
2. The three B3 logs, in full.
3. Your C1 review of another pair's log.
4. Your C2 paragraph.
5. D1's tie-behaviour defect and its exposing input.
6. Your D2 sentence.

## What completion looks like

Completion-graded as in Lab 1. Full credit requires the log order
(hypothesis before fix) even for the patients you solved at first sight —
the discipline is the deliverable; speed comes later.
