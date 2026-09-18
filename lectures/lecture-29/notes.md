# Lecture Notes — Lecture 29: Simulation as a Way of Knowing

Companion to the lecture plan and the worked examples. Read the *Definitions* before
class, the *Explanation* after it; the practice questions and the lecture quiz close the loop.

## Definitions

- **Simulation** — running a model many times with randomness to observe the range of outcomes
- **Random seed** — the starting point of the pseudo-random stream; fixed seeds make runs reproducible
- **Trial** — one run of the model; a simulation is many trials
- **Estimate** — a trial-derived approximation of a theoretical quantity
- **Standard error** — how far the estimate typically wobbles; shrinks like 1/sqrt(trials)
- **Validation** — checking a simulation against a case with a known answer before trusting it

## Explanation

Some questions have no closed form; simulation answers them by counting. Build the model, run it many times with randomness, summarise the outcomes. Three disciplines make the results trustworthy. First, validation: run the simulation on a case with a known answer (the queue where nobody waits) - a model that fails the known case is wrong, and the disagreement is the diagnostic. Second, reproducibility: record the seed; an unseeded simulation is not a result, it is an anecdote. Third, honesty about precision: the estimate's standard error shrinks like 1/sqrt(trials), so four times the trials buy two times the digits - say how many trials and how far the answer wobbles. Simulation partners with algebra: the closed form gives the mean and the WHY; the simulation shows the spread of outcomes the algebra hides.

## Examples

The lecture's worked examples live in [examples.md](examples.md); the case studies this
lecture builds on are worked in class from the projector. The case sequence with difficulties:
- [cs-113](../../case-studies/student/cs-113.md) (Beginner)
- [cs-114](../../case-studies/student/cs-114.md) (Foundational)
- [cs-115](../../case-studies/student/cs-115.md) (Intermediate)
- [cs-116](../../case-studies/student/cs-116.md) (Expert)

## Common misconceptions

- Reporting a simulation without its seed or trial count - not reproducible, not a result.
- Assuming more trials help proportionally - standard error shrinks like 1/sqrt(trials).
- Trusting a model that was never run against a known-answer case.
- Confusing one unlucky trial with a bad model - look at the distribution, not one run.
- Believing simulation replaces algebra - it shows the spread; the algebra explains the mean.

## Summary and key takeaways

1. Simulation answers by counting trials what algebra cannot close-form.
2. Validate on a known answer first; a wrong model fails loudly there.
3. Seed recorded, trials stated, wobble estimated - or it is not a result.
4. Standard error ~ 1/sqrt(trials): precision is bought in square roots.
5. Algebra gives the mean and the why; simulation shows the spread.

## Practice questions

- Simulate 1000 two-dice sums with a fixed seed; compare the sum-8 share with 5/36.
- Validate a queue simulation on the no-wait case before adding randomness.
- Estimate the longest heads-run in 100 flips over 200 trials; report median, not max.
- Enrichment: halve and double the trial count; show the wobble moving like 1/sqrt(trials).
- Enrichment: explain (in three sentences) why the seed must be recorded in a report.

## Where this leads

Next lecture: **Optimization Formulations**. The quiz below checks this lecture's essentials before we build on them.
