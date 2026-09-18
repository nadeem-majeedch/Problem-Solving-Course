# Lecture 05 — Numbers, Remainders, and Cycles

## Position in the course

This is lecture 5 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

## Learning objectives

- Use integer division and remainder to model cycles
- Reason about divisibility and digit sums
- Recognise when modulo simplifies a problem

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** Lecture 04 — First Python

Assumed fluencies:

- integer division and remainders
- while loops
- accumulating a result

**Preparation task:** Practise `//` and `%` on small numbers; sketch cs-017 on paper.

## Detailed topic outline

Core (mandatory):

1. integer division and remainder as design tools
2. cycles, rotations, and schedules
3. digit extraction
4. reconstructing inputs from outputs

Extension (optional enrichment):

5. simulation of a ring process
6. when mathematics replaces loops

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-017 | The Pager Schedule | Beginner |
| cs-018 | Digits and Their Sum | Foundational |
| cs-019 | The Broken Keypad | Intermediate |
| cs-020 | The Josephus Ring | Advanced |

Display each case full-screen from the student page (cases cs-017–cs-020);
instructor pages cs-017–cs-020 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts.

## Timing plan (120 minutes)

| Minutes | Segment |
| --- | --- |
| 0–10 | Framing: where this fits; recall of the previous lecture |
| 10–30 | Case 1 (cs-017): 5-minute attempt, then discussion and reveal |
| 30–50 | Case 2 (cs-018): same rhythm |
| 50–70 | Case 3 (cs-019): same rhythm, harder case |
| 70–75 | Break |
| 75–100 | Case 4 (cs-020): same rhythm, hardest case |
| 100–115 | Synthesis: name the techniques; misconceptions check |
| 115–120 | Exit questions, homework, next-lecture preview |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-020 Josephus ring: simulate n = 5 by hand, tabulate survivors, conjecture, and only then generalise.

**Instructor demonstration to open the lecture:** Build the pager schedule (cs-017) as a table of n, n mod k, and the day name; the pattern falls out before any code.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Human clock circle | 6 | Students count around a circle; the remainder rule for 'who is on call on day n' is discovered physically. |
| 2 | Trace-table relay | 8 | cs-018 digit-sum trace: each pair does two rows of the table then passes it on. |
| 3 | Cycle spotter | 5 | Six remainders sequences on the board; spot which are cycles and give the period. |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** Modulo is the star, and it divides the room: some students see cycles instantly, others need the human clock. The Josephus case (cs-020) is marked Expert — it is a stretch goal, and the hand simulation at n = 5 is the accessible core.

**Running the reveal.** This is the first lecture where mathematics replaces a loop; name that trade-off explicitly.

**Lecture focus.** One sentence to repeat verbatim: *Remainder is a design tool, not an operator trivia.*

## Common misconceptions

- Treating % as a trick to memorise instead of a cycle tool.
- Off-by-one in cycle position: day 1 versus day 0 as the start.
- Extracting digits with strings when the arithmetic was the point.
- Simulating the Josephus ring for large n instead of tabulating small cases.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. Tabulate n mod 7 for n = 1..21 and mark the pager rotation pattern.
2. Extract the digits of 90210 by hand using // and %, then sum them.
3. Simulate the Josephus ring (cs-020) for n = 6, k = 3 and record the elimination order.

Enrichment (optional):

- Explore cs-020 for k = n-1 and conjecture a closed form.
- Find two real systems that schedule by remainder; describe their cycle lengths.

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. Compute 17 mod 5 and 17 // 5, and say what each means for a 5-day cycle.
   *Expected: 2 and 3: day-before-cycle position and completed cycles*

2. Why is remainder better than an if-chain for schedules?
   *Expected: one expression handles all positions; no special cases to maintain*

3. What replaced a loop in the Josephus analysis?
   *Expected: a table of small cases plus a conjecture (mathematics replacing simulation)*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO8, LO4 — Mathematical modelling (mod, cycles) drives the Python.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
