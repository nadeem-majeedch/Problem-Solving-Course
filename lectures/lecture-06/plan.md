# Lecture 06 — Traces and Loop Reasoning

## Position in the course

This is lecture 6 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

## Learning objectives

- Trace loops with a variable table
- Predict loop outputs before running code
- Identify off-by-one errors systematically

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** Lectures 04–05 — Python control flow and arithmetic

Assumed fluencies:

- reading loops fluently
- hand-tracing with a state table

**Preparation task:** Trace cs-021 by hand once before class.

## Detailed topic outline

Core (mandatory):

1. the state table as a universal tracer
2. loop invariants informally
3. nested loops and grid thinking
4. off-by-one taxonomy

Extension (optional enrichment):

5. termination questions
6. reading code you did not write

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-021 | Trace the Tally | Beginner |
| cs-022 | The Shrinking Loop | Foundational |
| cs-023 | Nested and Confused | Intermediate |
| cs-024 | The Off-By-One Museum | Advanced |

Display each case full-screen from the student page (cases cs-021–cs-024);
instructor pages cs-021–cs-024 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts.

## Timing plan (120 minutes)

| Minutes | Segment |
| --- | --- |
| 0–10 | Framing: where this fits; recall of the previous lecture |
| 10–30 | Case 1 (cs-021): 5-minute attempt, then discussion and reveal |
| 30–50 | Case 2 (cs-022): same rhythm |
| 50–70 | Case 3 (cs-023): same rhythm, harder case |
| 70–75 | Break |
| 75–100 | Case 4 (cs-024): same rhythm, hardest case |
| 100–115 | Synthesis: name the techniques; misconceptions check |
| 115–120 | Exit questions, homework, next-lecture preview |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-023 nested loops: a grid trace where rows are i and columns are j; the class colours the visited cells.

**Instructor demonstration to open the lecture:** Trace cs-021 with a full state table on the board, then delete a column and let the class feel what is lost.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Think-Pair-Debug | 8 | Run activities/think-pair-debug.md on a one-bug variant of cs-021. |
| 2 | State-table race | 6 | Same snippet, two teams, who completes a correct state table first — then compare columns. |
| 3 | Off-by-one museum tour | 7 | Walk the four exhibits of cs-024; for each, the class states the input class that triggers it. |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** Tracing is the course's most transferable skill. The state table is non-negotiable in week one of tracing: columns for every variable, one row per iteration, no skipping.

**Running the reveal.** Advanced students should be pushed from 'what does it print' to 'why must it terminate' — the invariant vocabulary starts here informally.

**Lecture focus.** One sentence to repeat verbatim: *The state table is the honest record of a loop's life.*

## Common misconceptions

- Tracing in the head instead of in a written state table.
- Filling state tables lazily — omitting the loop-condition column.
- Assuming nested loops multiply costs only when it is convenient.
- Declaring 'infinite loop' without naming the quantity that must shrink.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. Produce a full state table for a provided shrinking-loop snippet (cs-022 family).
2. Trace the nested grid loop of cs-023 for n = 3 and count the cells visited.
3. Write the one-sentence invariant that makes cs-021's tally correct.

Enrichment (optional):

- Trace cs-024's fourth exhibit for both boundary values.
- Invent a snippet whose state table has a repeating pattern; predict the exit.

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. What belongs in every column of a state table?
   *Expected: every variable whose value the loop reads or writes, plus the loop condition*

2. Give the two classic off-by-one causes.
   *Expected: boundary (≤ vs <) and initialisation (starting one early/late)*

3. When does a nested loop's inner count matter most?
   *Expected: when estimating cost: it multiplies, so grid thinking exposes growth*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO5, LO4 — Tracing and loop reasoning, the debugging foundation.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
