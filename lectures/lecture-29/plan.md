# Lecture 29 — Simulation as a Way of Knowing

## Position in the course

This is lecture 29 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

This lecture runs as a **workshop** session (build-heavy; see the timing plan), not the standard four-case rhythm.

## Learning objectives

- Design a simulation from a story of randomness
- Run repeated trials and summarise results
- Validate simulations against exact reasoning

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** Lectures 26 and 04 — probability and Python

Assumed fluencies:

- random module basics
- collecting many trials

**Preparation task:** Write a 10-line dice roller and print the average of 100 rolls.

## Detailed topic outline

Core (mandatory):

1. simulation as a way of knowing
2. randomness sources and seeds
3. Monte Carlo estimation
4. queues and arrival processes

Extension (optional enrichment):

5. strategy evaluation by simulation
6. confidence from trial counts

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-113 | Dice Before Data | Beginner |
| cs-114 | The Queue Waiting Game | Foundational |
| cs-115 | The Exam Gambler | Intermediate |
| cs-116 | The Buffon Needle | Expert |

Display each case full-screen from the student page (cases cs-113–cs-116);
instructor pages cs-113–cs-116 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts.

## Timing plan (120 minutes)

Format: **workshop session** — deliberately not the standard case rhythm.

| Minutes | Segment |
| --- | --- |
| 0–10 | Framing: the two patterns this workshop trains |
| 10–45 | Cases 1–2 (cs-113, cs-114): two 5-minute attempts back to back, one joint discussion, two reveals |
| 45–50 | Break |
| 50–90 | Cases 3–4 (cs-115, cs-116): same double rhythm, harder material |
| 90–110 | Deliberate-practice block: build or trace one of today's patterns end to end, instructor circulating |
| 110–120 | Synthesis, exit questions, homework |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-116 Buffon needle: the geometry set up in three lines, then 1,000,000 simulated drops yielding π to two decimals.

**Instructor demonstration to open the lecture:** Dice before data (cs-113): 10 rolls by hand, 10,000 by program; the law of large numbers is felt, not stated.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Estimation casino | 8 | Teams estimate four quantities by simulation, then post confidence intervals from trial counts. |
| 2 | Queue relief race | 7 | cs-114's two queue disciplines simulated by hand for 6 arrivals; tension measured. |
| 3 | Seed honesty check | 5 | Same simulation, three seeds: which conclusions survive? The class writes the rule. |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** Simulation is positioned as a way of knowing when analysis is out of reach. Seeds, trial counts, and honest confidence intervals are the craft taught.

**Running the reveal.** Workshop format: machines needed. The estimation casino runs on prepared harnesses; publish them the night before.

**Lecture focus.** One sentence to repeat verbatim: *When analysis stalls, simulate — and report the trials.*

## Common misconceptions

- Running few trials and reporting the result to many decimals.
- Forgetting to fix seeds, making results irreproducible.
- Simulating a process that was never written down as a model.
- Reporting estimates without any spread or interval.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. Estimate dice-before-data (cs-113) probabilities with 200 manual tally marks, then with a seeded program.
2. Simulate the queue game (cs-114) for 20 arrivals under both disciplines; tabulate waiting times.
3. Run the streak simulation from lecture 26 with three seeds; report the spread honestly.

Enrichment (optional):

- Estimate π with Buffon's needle (cs-116); plot error vs trials.
- Add a confidence interval to cs-115's strategy comparison.

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. What does the seed control, and what must you report?
   *Expected: reproducibility; report seeds and trial counts with every estimate*

2. When is simulation preferred to analysis?
   *Expected: when the model is realistic but the maths is intractable*

3. What shrinks as trials grow?
   *Expected: the estimate's spread — roughly 1/sqrt(n)*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO9, LO8 — Simulation as estimation with honest uncertainty.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
