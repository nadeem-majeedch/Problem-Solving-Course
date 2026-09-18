# Assignment 6 — Marking Key (instructor only)

Not for publication. Companion to [rubric-06](../rubric-06.md).
This assignment is personal by construction — the key below is therefore
*grading guidance*, not a reference answer.

## Part 1 — what distinguishes bands

- **Ordered moves with reasons:** the mark is the *why before* argument
  ("assumptions before computation because a wrong assumption
  invalidates every later line"). Circular orderings ("first I
  understand, then I solve") are the band-6 tell.
- **Genuine counter-examples:** a strong page claims, e.g., "assumptions
  first — except in cs-045-style debugging, where reproducing the
  symptom comes first because the requirements are already exact and
  the defect is not in them." The counter-example must *use* the case
  it cites; token denials ("this might not always hold") score low.
- **Closed-book traces:** spot-check one number per student against the
  case's published expected result (the case pages list it). Numbers
  matching to two decimal places *with* matching phrasing are worth a
  second look — the −1 modifier exists for this.

## Part 2 — what to feed back to markers-of-markers

Challenges can be assessed for *specificity* without you re-deriving
the portfolio: a specific challenge names a case ID, a move, or an
input. "Rebuttals" that concede nothing and argue nothing ("no, my move
is fine") are acceptance-avoidance — band 2.

## Part 3 — quick program checks

1. Run it. Does not run ⇒ cap 4 regardless of prose.
2. Count functions; check each returns (no print-returns) — contract
   language from lecture 14.
3. Find the deliberate-failure row; it must show a *demonstrated* or
   *explained* failure, not a row that passes.
4. The mapping paragraph is checkable: (i) points at the loop, (ii) at
   the functions, (iii) at the table. Uncheckable mappings ("the whole
   program shows decomposition") are band 1.

## Suggested marks conversation

This assignment precedes the project midpoint: a portfolio showing
band-3 method language signals the student needs the decomposition-
document milestone meeting early. The portfolio pages are, in effect, a
dry run of the project's decomposition document — grade them with that
lens and say so in feedback.

## Common faults to name in feedback

- Three cases from the same block (check the ID ranges; the brief
  fixes them).
- Part 2 written as mutual praise between partners — the adversarial
  frame is the point; both partners lose the marks.
- Part 3's test table with 10 happy rows and no failure row.
- Traces with the published numbers but no intermediate steps (the
  method was skipped; the answer was looked up).
