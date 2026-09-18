# Lecture Notes — Lecture 08: Testing Before Trusting

Companion to the lecture plan and the worked examples. Read the *Definitions* before
class, the *Explanation* after it; the practice questions and the lecture quiz close the loop.

## Definitions

- **Test case** — one input plus the output the specification demands.
- **Test table** — a systematic list of cases grouped by purpose: normal, boundary, adversarial.
- **Normal case** — typical use the code was written for.
- **Boundary case** — an input exactly at a rule's edge (0, empty, the allowed maximum).
- **Adversarial case** — an input designed to break careless code (negatives, junk text, huge values).
- **Black-box testing** — designing cases from the specification alone.
- **White-box testing** — designing cases using knowledge of the code's branches.
- **Flaky test** — a test that passes and fails without code changes - often unfair to randomness.

## Explanation

**The test table is the specification.** A requirement like 'valid age is 0-120' implies at least five tests (below, both edges, above, typical) *before any code exists*. Writing the table first is cheaper than debugging later.

**Three case classes.** Normal (typical use), boundary (exactly at edges), adversarial (designed to break naive code: empty, negative, huge, wrong type). Boundary finds the most defects per case; adversarial finds the embarrassing ones.

**Black-box vs white-box.** Black-box: from the spec, so it also catches missing features. White-box: from the code, so it reaches awkward branches. They are complements, not rivals - cs-031 makes students feel the difference.

**Coverage, honestly.** Aim for 'every branch is reached by at least one case', not percentage badges. 100% line coverage with zero boundary cases is a common and worthless achievement.

**Testing randomness.** A random function cannot be pinned by one outcome. Either fix the seed (deterministic, reproducible) or assert distribution invariants over many trials (mean in range, values in range, repeats allowed). cs-032 builds the habit.

**Cost arithmetic.** A test costs minutes; a defect found by a user costs days. Three boundary tests before the five-minute attempt is the best time investment in this course.

## Examples

The lecture's worked examples live in [examples.md](examples.md); the case studies this
lecture builds on are worked in class from the projector. The case sequence with difficulties:
- [cs-029](../../case-studies/student/cs-029.md) (Beginner)
- [cs-030](../../case-studies/student/cs-030.md) (Foundational)
- [cs-031](../../case-studies/student/cs-031.md) (Intermediate)
- [cs-032](../../case-studies/student/cs-032.md) (Advanced)

## Common misconceptions

- Testing only the happy path - boundaries are where defects live.
- One random outcome deciding a random function's fate.
- Full line coverage mistaken for correctness.
- Adversarial cases dismissed as 'unrealistic' - users are adversarial by nature.

## Summary and key takeaways

1. Write the test table before the code; it is the spec made executable.
2. Normal, boundary, adversarial - three classes, always.
3. Black-box and white-box complement each other.
4. Randomness: fix the seed or assert distributions - never one outcome.

## Practice questions

- Build the complete test table for the age gate: normal, boundary, adversarial.
- Convert your triangle-classifier table into asserts at the top of a provided implementation.
- Design a fair test for a function that returns different values on identical calls; explain your design.
- Trade-off paragraph: when is skipping the adversarial class defensible? When never?

## Where this leads

Next lecture: **Aggregation Patterns**. The quiz below checks this lecture's essentials before we build on them.
