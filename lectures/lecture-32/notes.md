# Lecture Notes — Lecture 32: Capstone: The Method Applied

Companion to the lecture plan and the worked examples. Read the *Definitions* before
class, the *Explanation* after it; the practice questions and the lecture quiz close the loop.

## Definitions

- **Capstone** — unseen problems solved end-to-end under time pressure, then debriefed against the method.
- **The method** — specify, model, attempt, verify, compare, communicate - the course's spine in six verbs.
- **Plan defence** — a two-minute oral justification of approach, complexity, and test plan before coding.
- **Post-mortem** — the written what-happened, why, and what-check-would-have-caught-it.
- **Transfer** — applying the method to problems whose surface stories are new - the real learning outcome.

## Explanation

**The capstone format.** Two unseen problems, 20 minutes each: 2 minutes specify, 2 minutes plan defence (oral, complexity and tests named), 12 minutes execute, 4 minutes verify and summarise. The clock is part of the lesson.

**Problem A is a balancing task** (assign people by skill to equal teams): greedy with a size cap, verified against brute force on small inputs - Block III's proof discipline applied.

**Problem B is a route-and-budget task** (visit required shelves within battery): BFS distances plus a knapsack-style selection - Block IV's modelling under a constraint.

**The debrief maps every step to the method.** Each team writes which of the six verbs was weakest under pressure; the class aggregates the histogram - the course's own retrospective.

**After the capstone.** The exam-style variants (provided for practice), the personal error taxonomy, and the honest-summary checklist are the take-home kit; the course ends by handing over its own tools.

## Examples

The lecture's worked examples live in [examples.md](examples.md); the case studies this
lecture builds on are worked in class from the projector. The case sequence with difficulties:
- [cs-125](../../case-studies/student/cs-125.md) (Beginner)
- [cs-126](../../case-studies/student/cs-126.md) (Foundational)
- [cs-127](../../case-studies/student/cs-127.md) (Intermediate)
- [cs-128](../../case-studies/student/cs-128.md) (Advanced)

## Common misconceptions

- Starting to code at minute one instead of specifying first - the capstone penalises it explicitly.
- Defending the plan with 'it should work' instead of named complexity and tests.
- Treating verification as optional when time is short - it is scored.
- Reading the post-mortem as blame; it is a checklist upgrade.

## Summary and key takeaways

1. Specify, defend, execute, verify - the method under a clock.
2. Plan defence names complexity and tests BEFORE code.
3. The post-mortem upgrades your personal checklist.
4. Transfer is the goal: unseen stories, same method.

## Practice questions

- Solve the exam-style variant of Problem A under a 20-minute clock; write the post-mortem.
- Solve the exam-style variant of Problem B; mark which method verb was weakest.
- Exchange post-mortems with a partner; adopt one of their checklist items.
- Assemble your personal error taxonomy from all eight quizzes into a one-page pre-exam checklist.

## Where this leads

This is the final lecture - the capstone consolidates every phase of the method into exam-ready form.
