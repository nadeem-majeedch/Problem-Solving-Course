# Teaching Notes — Lecture 32

*Instructor only - not rendered on the public site.*

## Board plan

- Left: the method poster: specify -> plan -> execute -> verify -> present.
- Middle: the capstone clock: visible countdowns per phase.
- Right: the assumption list growing per team - defended at the plan checkpoint.

## Questions to ask students

- Which assumption did you negotiate first, and what did it change in the plan?
- Where did your verification find something your plan had missed?
- What would you defend as the single best decision of your solution - and why that one?

## Alternative explanations

- Anxious teams: pre-shaped plan templates; the defence focuses on justification quality.
- Strong teams: a hidden twist released at the half-hour (an input-format change) to test plan robustness.

## Expected student difficulties

- Code-first under pressure - hold the plan checkpoint; marks live there too.
- Silent cleaning in the data case - the audit trail is a capstone deliverable, not a nicety.

## Connections to neighbouring lectures

Everything since L1 converges here; the post-mortem feeds the exam's case format.

## Quiz answer key

**A1.** List the method's phases under exam conditions.
- *Expected:* Specify, plan, execute, verify, present - with a defended checkpoint after plan.

**A2.** What does 'defend an assumption' mean in the capstone?
- *Expected:* State it, justify it, and say what changes if it is flipped.

**A3.** Verification's role before presentation?
- *Expected:* Named edge cases with expected values - a result nobody can check is not a result.

**A4.** What does the post-mortem capture?
- *Expected:* Where the plan failed, what the fix was, what transfers to the next problem.

**B1.** Library robot: requests at 2,3,7,7,9 - compute idle time and the busiest shelf with tie rule.
- *What earns marks:* Idle 2 + 3 = 5; tally A2/B2/C1 -> alphabetical tie-break -> A.

**B2.** Data clinic: 4 rows (one dup, one missing, one impossible) - order the cleaning steps and defend.
- *What earns marks:* Dedupe after normalisation -> policy on missing -> reject impossible (logged) -> aggregate; the log is a deliverable.

## Exit ticket - expected answers

1. What did the plan-first discipline buy you today?
   - *Expected:* a defensible partial answer under a hard cap

2. Name two cases where two techniques had to combine.
   - *Expected:* cs-125 (graphs + greedy), cs-127 (cleaning + statistics)

3. What is your next technique to strengthen, and where will you practise it?
   - *Expected:* student's own map from the retrospective
