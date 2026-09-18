# Lecture Notes — Lecture 07: Debugging as a Method

Companion to the lecture plan and the worked examples. Read the *Definitions* before
class, the *Explanation* after it; the practice questions and the lecture quiz close the loop.

## Definitions

- **Defect (bug)** — code that does not meet its specification - distinct from a mistake you have not yet observed.
- **Symptom** — the observed wrong behaviour; often far from the defect's location.
- **Reproduction** — a specific input and sequence that makes the symptom appear on demand.
- **Hypothesis** — a testable claim about the cause; good hypotheses predict an experiment's result.
- **Isolation** — cutting the search space in half (or deleting code) until the defect is cornered.
- **Regression test** — a test that fails if a fixed defect ever returns.
- **Heisenbug** — a defect that changes or vanishes when you try to observe it (logging, timing, different input).

## Explanation

**Debugging is a method, not luck.** The clinic protocol: 1) reproduce, 2) hypothesise, 3) cheapest experiment first, 4) isolate, 5) fix, 6) re-test. The order is the method - improvising is how defects get 'fixed' twice.

**Reproduction first.** An unreproduced defect cannot be falsified; you would be guessing and mutating code on faith. The reproduction is also your acceptance test for the fix.

**Hypotheses as experiments.** 'The loop runs one time too many' predicts: input of size 1 still fails. Cheap, decisive, and it halves your hypothesis list either way. Binary-search your belief list by experiment cost, not by suspicion.

**Isolation by halving.** Delete or bypass half the code (comment out, hardcode an input); does the symptom survive? Four halvings pin a defect among 16 suspects. This is lecture 21's binary search applied to code.

**The heisenbug lesson.** cs-028 shows a defect that hides when observed: print statements change behaviour. Response: reduce the program, not add instrumentation - and suspect state (aliasing, order, timing) over arithmetic.

**Fix without breaking neighbours.** Re-run the surrounding tests after every change. 'It compiles' is not a test; lecture 8 will formalise this as the regression habit.

## Examples

The lecture's worked examples live in [examples.md](examples.md); the case studies this
lecture builds on are worked in class from the projector. The case sequence with difficulties:
- [cs-025](../../case-studies/student/cs-025.md) (Beginner)
- [cs-026](../../case-studies/student/cs-026.md) (Foundational)
- [cs-027](../../case-studies/student/cs-027.md) (Intermediate)
- [cs-028](../../case-studies/student/cs-028.md) (Advanced)

## Common misconceptions

- Editing code before reproducing the defect - destroys the evidence.
- Experiments ordered by suspicion rather than by cost.
- 'Fixing' by deleting the failing feature (the defect remains, the symptom hides).
- Declaring victory on one green test; neighbours must still pass.

## Summary and key takeaways

1. Reproduce, hypothesise, cheapest experiment, isolate, fix, re-test - in order.
2. Halve the search space; four halvings corner 16 suspects.
3. A fix without a re-run of neighbours is not a fix.
4. Heisenbugs: reduce the program instead of adding prints.

## Practice questions

- Apply the protocol to a provided buggy invoice program: write the reproduction, three hypotheses, and the cheapest experiment before any fix.
- Classify five planted defects: boundary, aliasing, arithmetic, state, logic.
- Write the regression test that would have caught the ghost duplicate.
- Halve-isolate a 16-line broken function in at most four experiments; log each experiment and result.

## Where this leads

Next lecture: **Testing Before Trusting**. The quiz below checks this lecture's essentials before we build on them.
