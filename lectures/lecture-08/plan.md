# Lecture 08 — Testing Before Trusting

## Position in the course

This is lecture 8 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

## Learning objectives

- Design test cases from requirements, not from the code
- Choose boundary and edge cases deliberately
- Write simple assert-based checks

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** Lectures 06–07 — Tracing and debugging method

Assumed fluencies:

- hypothesis-test-fix loop
- boundary thinking

**Preparation task:** Bring one bug you met this week (any course, any language).

## Detailed topic outline

Core (mandatory):

1. test cases as specifications
2. normal / boundary / adversarial classes
3. black-box versus white-box design
4. coverage without obsession

Extension (optional enrichment):

5. testing randomness honestly
6. the flaky test problem

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-029 | Triangle Classifier | Beginner |
| cs-030 | The Age Gate | Foundational |
| cs-031 | Black Box vs White Box | Intermediate |
| cs-032 | The Flaky Function | Advanced |

Display each case full-screen from the student page (cases cs-029–cs-032);
instructor pages cs-029–cs-032 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts.

## Timing plan (120 minutes)

| Minutes | Segment |
| --- | --- |
| 0–10 | Framing: where this fits; recall of the previous lecture |
| 10–30 | Case 1 (cs-029): 5-minute attempt, then discussion and reveal |
| 30–50 | Case 2 (cs-030): same rhythm |
| 50–70 | Case 3 (cs-031): same rhythm, harder case |
| 70–75 | Break |
| 75–100 | Case 4 (cs-032): same rhythm, hardest case |
| 100–115 | Synthesis: name the techniques; misconceptions check |
| 115–120 | Exit questions, homework, next-lecture preview |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-032 flaky function: design a seed-controlled test harness in five lines, then explain why the original test was unfair.

**Instructor demonstration to open the lecture:** Build the triangle classifier test table (cs-029) with the class: normal rows first, then boundaries, then the adversarial row that kills naive code.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Test-table duel | 8 | Two teams design test tables for cs-030 age gate; the table that finds a planted bug wins. |
| 2 | Boundary sprint | 5 | 90 seconds: list every boundary of 'valid age is 0–120 inclusive'; then count them together. |
| 3 | Coverage map discussion | 6 | A small function and its branches are mapped; the class marks which tests actually reach each branch. |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** Testing is reframed from chore to specification: the test table *is* the requirement, written executable. The flaky-function case (cs-032) ends the lecture on honesty about randomness.

**Running the reveal.** Keep coverage light: branches reached, not percentages. The goal is a habit, not a metric.

**Lecture focus.** One sentence to repeat verbatim: *The test table is the specification, executable.*

## Common misconceptions

- Writing tests that exercise only the happy path.
- Treating boundaries as unlucky coincidences instead of targets.
- Believing full line coverage implies correctness.
- Testing randomness with a single outcome and calling the test flaky.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. Build a complete test table for the age gate (cs-030): normal, boundary, adversarial.
2. Convert your cs-029 table into executable asserts.
3. Design a fair test for a function that behaves differently on different runs (cs-032 family).

Enrichment (optional):

- Design adversarial tests for the vending machine script from lecture 2.
- Research flaky tests: write one paragraph on why they erode trust.

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. Name the three test-case classes and one example of each.
   *Expected: normal (typical use), boundary (edges: 0, 120), adversarial (empty, negatives, junk)*

2. Black-box vs white-box in one sentence each.
   *Expected: black-box: from the spec only; white-box: from the code's known branches*

3. What makes a randomness test fair?
   *Expected: control the seed or test the distribution over many runs, never a single outcome*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO6, LO5 — Testing mindset with boundary discipline.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
