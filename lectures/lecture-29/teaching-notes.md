# Teaching Notes — Lecture 29

*Instructor only - not rendered on the public site.*

## Board plan

- Left: model -> trials -> summary, with the seed recorded in the corner.
- Middle: the queue simulation beside its analytical zero-wait answer - agreeing.
- Right: the 1/sqrt(trials) precision curve; 'what do 4x trials buy?' annotated.

## Questions to ask students

- What does the known-answer case protect us from - give one bug it would catch.
- Why record the seed - what exactly becomes reproducible?
- Estimate: how many trials for one more decimal digit - and is it worth it?

## Alternative explanations

- Paper-dice simulation before code for the dice case - the model is the point.
- Advanced: plot estimate-vs-trials to SEE the wobble shrink.

## Expected student difficulties

- Reporting one run's number as the answer - mandate trials and wobble statements.
- Unseeded randomness mistaken for rigor - the seed is part of the method.

## Connections to neighbouring lectures

Evidence standards from testing (L8) return for models; optimisation decisions come next (L30).

## Quiz answer key

**A1.** Why record the seed?
- *Expected:* Reproducibility - the exact stream reruns; results become checkable.

**A2.** How does precision scale with trials?
- *Expected:* Standard error ~ 1/sqrt(trials).

**A3.** What is a validation run?
- *Expected:* Executing the model on a case with a known answer before trusting it.

**A4.** Simulation vs algebra: what does each give?
- *Expected:* Algebra: exact mean and why; simulation: the spread and complex cases.

**B1.** Dice sum-8: exact probability and a 10,000-trial estimate.
- *What earns marks:* 5/36 ~ 0.1389; estimate ~0.139 +- 0.003 (state trials and seed).

**B2.** Queue with 2-min arrivals, 1-min service: analytical max wait, and the simulation's job.
- *What earns marks:* Zero - the simulation must reproduce it; disagreement means a model bug.

## Exit ticket - expected answers

1. What does the seed control, and what must you report?
   - *Expected:* reproducibility; report seeds and trial counts with every estimate

2. When is simulation preferred to analysis?
   - *Expected:* when the model is realistic but the maths is intractable

3. What shrinks as trials grow?
   - *Expected:* the estimate's spread — roughly 1/sqrt(n)
