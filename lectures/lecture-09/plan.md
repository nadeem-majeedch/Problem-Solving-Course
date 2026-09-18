# Lecture 09 — Aggregation Patterns

## Position in the course

This is lecture 9 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

## Learning objectives

- Implement running totals, min/max, and counting loops
- Combine aggregation with filtering
- Initialise accumulators correctly

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** Lectures 04–06 — Loops, state, accumulation

Assumed fluencies:

- running totals
- min/max tracking
- counting loops

**Preparation task:** Write a running-total loop for cs-033 from memory.

## Detailed topic outline

Core (mandatory):

1. running totals, counts, min/max, argmax
2. comparison against a best-so-far
3. streaks and state resets
4. fixed and variable windows

Extension (optional enrichment):

5. two-pass thinking
6. choosing the right aggregation for a question

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-033 | The Reading Log | Beginner |
| cs-142 | The Tallied Vote | Beginner |
| cs-034 | Stockroom Spikes | Foundational |
| cs-035 | The Longest Streak | Intermediate |
| cs-036 | Rainfall Windows | Advanced |

Display each case full-screen from the student page (cases cs-033–cs-036);
instructor pages cs-033–cs-036 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts. Applied additions cs-142 extend the session as optional extra attempts or homework;
they share the lecture's theme but teach an applied, real-world angle.

## Timing plan (120 minutes)

| Minutes | Segment |
| --- | --- |
| 0–10 | Framing: where this fits; recall of the previous lecture |
| 10–30 | Case 1 (cs-033): 5-minute attempt, then discussion and reveal |
| 30–50 | Case 2 (cs-034): same rhythm |
| 50–70 | Case 3 (cs-035): same rhythm, harder case |
| 70–75 | Break |
| 75–100 | Case 4 (cs-036): same rhythm, hardest case |
| 100–115 | Synthesis: name the techniques; misconceptions check |
| 115–120 | Exit questions, homework, next-lecture preview |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-036 rainfall windows: two passes — first totals, then the window answer — and why one pass is possible but harder.

**Instructor demonstration to open the lecture:** Compute the reading-log totals (cs-033) with running totals, then re-ask the question with min/max to show the pattern family.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Running-total simulation | 6 | One student reads numbers aloud, one keeps the total, one keeps the max; swap roles mid-stream. |
| 2 | Window slide demo | 7 | A meter-stick slides along a taped number line of rainfall values; the class calls out each window sum. |
| 3 | Pattern naming | 5 | Six aggregation questions are shown; teams name the pattern (total, count, min, argmax, streak, window) before solving. |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** Aggregation patterns are the workhorses of data science; name them precisely (total, count, min, max, argmax, streak, window) so later lectures can invoke them by name.

**Running the reveal.** The window cases (cs-036) are the hardest; two-pass thinking is the accessible route and is worth celebrating.

**Lecture focus.** One sentence to repeat verbatim: *Name the pattern, then write the loop.*

## Common misconceptions

- Recomputing totals inside the loop instead of maintaining them.
- Forgetting to reset streak state after a miss.
- Confusing max with argmax — the value versus its position.
- Sliding windows by recomputing each sum from scratch.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. Implement running total, count, min, and argmax over one provided reading log.
2. Compute the longest streak of on-target days for cs-035's sample data by hand, then in code.
3. Solve cs-036 for window size 3 with the two-pass method; then attempt one pass.

Enrichment (optional):

- Solve cs-036 with the one-pass method and compare its clarity honestly.
- Find an aggregation bug in any app you use (streaks and averages are fertile ground).

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. Name the aggregation pattern for 'which day had the most sales'.
   *Expected: argmax: track best-so-far value and its index/key*

2. Why reset streak state?
   *Expected: a streak is consecutive; a miss must zero the counter, not stop it*

3. What is two-pass thinking and when does it pay?
   *Expected: compute intermediate aggregates first, then answer; pays when one pass tangles state*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO4, LO9 — Aggregation patterns are the data-science workhorses.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
