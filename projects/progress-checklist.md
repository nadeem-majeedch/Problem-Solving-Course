# Project Progress Review Checklist

Used at the week-28 midpoint check-in (10 minutes per project, in the
lab session) and by students as a self-check at the end of weeks 26 and
27. The midpoint decomposition document is worth 5 of the 30 project
points; this checklist is how the conversation is structured — it is
not a form to submit.

## Before the meeting (student)

- [ ] The decomposition document exists (subproblem tree, assumptions,
      data plan, test plan — see the
      [proposal](proposal-template.md) you grew out of).
- [ ] Some program runs — anything: even reading the data format.
- [ ] You can name the subproblem you are stuck on, in one sentence.

## The six checkpoints (instructor ticks each)

### 1. The tree is real

- [ ] Subproblems match what the code will actually contain (a tree
      from week 26 that no longer matches reality is fine — say what
      changed and why; a tree that *never* changed is a warning sign).
- [ ] The hardest subproblem is marked, and the student can say what
      makes it hard (unknown technique? unclear data? too big?).

### 2. The data exists

- [ ] The dataset (or generator) is in the repo and loads.
- [ ] Its size matches the proposal's claim (± a factor of 2 is fine;
      "no data yet" at midpoint is a red flag — the fallback is
      generating it that week, decided in the meeting).

### 3. One vertical slice works

- [ ] At least one end-to-end path runs: input → one real output.
      Depth of one slice beats width of five stubs at midpoint.

### 4. The test plan has rows

- [ ] ≥ 5 rows exist with expected outputs written before running.
- [ ] At least one row currently *fails* — and the student can say
      whether the row or the code is wrong.

### 5. Assumptions survived contact

- [ ] Each assumption in the document is marked kept / changed /
      abandoned, with one line on what changed it. Assumptions that
      were all "kept" usually mean the data was never looked at.

### 6. The cut order still holds

- [ ] The proposal's §6 fallback is still the plan (or was consciously
      revised). "We will do everything" at midpoint is the classic
      week-4 crisis in formation.

## The three outcomes

| Outcome | Meaning |
| --- | --- |
| **On track** (5–6 ticks) | Proceed; the 5 midpoint points are recorded. |
| **On track with cuts** (3–4) | Proceed *with the cut decided in the meeting* — write the cut on the document; both sign. |
| **Rescue needed** (≤ 2) | Scope is reduced to the vertical slice + one question; a new one-page plan is agreed; the project can still reach the "good" band of the [rubric](project-rubric.md) — say so explicitly, mid-semester panic is the enemy. |

## After the meeting (student)

- [ ] The decomposition document is updated (not rewritten) with the
      meeting's decisions dated.
- [ ] The next week's single milestone is written in one sentence.
