# Lecture 04 — First Python: State and Sequences

## Position in the course

This is lecture 4 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

This lecture runs as a **workshop** session (build-heavy; see the timing plan), not the standard four-case rhythm.

## Learning objectives

- Translate pseudocode into runnable Python
- Explain variables as named state
- Use input/output and simple sequence iteration

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** Lectures 02–03 — Pseudocode and flowcharts

Assumed fluencies:

- translating pseudocode shapes into Python
- print/input, assignment, if/while

**Preparation task:** Work through resources/python-setup.md; run any cs-013-style echo program once.

## Detailed topic outline

Core (mandatory):

1. Python as executable pseudocode
2. state: variables, names, reassignment
3. input/output and conversion
4. lists and basic sequence operations

Extension (optional enrichment):

5. a first debugger encounter
6. from plan to run to check

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-013 | Echo with Limits | Beginner |
| cs-014 | Course List Cleaner | Foundational |
| cs-015 | The Change Maker | Intermediate |
| cs-016 | The Meeting Scheduler | Advanced |

Display each case full-screen from the student page (cases cs-013–cs-016);
instructor pages cs-013–cs-016 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts.

## Timing plan (120 minutes)

Format: **workshop session** — deliberately not the standard case rhythm.

| Minutes | Segment |
| --- | --- |
| 0–10 | Framing: the two patterns this workshop trains |
| 10–45 | Cases 1–2 (cs-013, cs-014): two 5-minute attempts back to back, one joint discussion, two reveals |
| 45–50 | Break |
| 50–90 | Cases 3–4 (cs-015, cs-016): same double rhythm, harder material |
| 90–110 | Deliberate-practice block: build or trace one of today's patterns end to end, instructor circulating |
| 110–120 | Synthesis, exit questions, homework |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-015 change maker: pseudocode → Python → trace table for 2.35; then the greedy question that keeps it honest.

**Instructor demonstration to open the lecture:** Type echo-with-limits (cs-013) from its pseudocode while narrating each decision; run it; break it with a boundary input on purpose.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Build stations | 15 | Three stations (echo, list cleaner, change maker skeleton); pairs rotate every five minutes leaving a running program behind. |
| 2 | Predict-then-run | 6 | Five short snippets are shown one at a time; everyone writes the output before it is run aloud. |
| 3 | Error bingo | 5 | Cards with classic first-day errors (NameError on a typo, int('3.5'), off-by-one range); first pair to diagnose all five calls bingo. |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** The first machine lab of the course. Expect enormous speed differences; the build stations exist so nobody is idle and nobody is bored. Publish the python-setup page a week ahead.

**Running the reveal.** Insist on predict-then-run for every demonstration: prediction converts watching into learning.

**Lecture focus.** One sentence to repeat verbatim: *Predict, then run, then check — never just run.*

## Common misconceptions

- Reading input without converting it, then 'adding' strings.
- Predicting output by hope instead of a trace table.
- Blaming the machine for a NameError caused by a typo.
- Reusing one variable for two meanings inside a single loop.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. Run the change maker (cs-015) for 4.19 and record the trace table.
2. Write a program that reads numbers until 0 and prints the count of negatives.
3. Break cs-013 with the nastiest legal input you can construct; explain the failure.

Enrichment (optional):

- Read resources/python-setup.md's debugger section and step through cs-015.
- Write the change maker's extension: fewest coins with a 2.00 cap.

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. What does predict-then-run change about learning?
   *Expected: prediction makes the run informative; mismatches are the lesson*

2. Name the three Python errors you met today and their causes.
   *Expected: e.g. NameError (typo/undefined), ValueError on int('3.5'), IndexError on range end*

3. Why convert input strings before arithmetic?
   *Expected: input() returns strings; arithmetic on them concatenates or fails*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO4, LO3 — Python fundamentals arrive as executable pseudocode.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
