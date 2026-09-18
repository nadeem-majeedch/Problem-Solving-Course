# Lecture 11 — Lists and Slicing

## Position in the course

This is lecture 11 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

This lecture runs as a **workshop** session (build-heavy; see the timing plan), not the standard four-case rhythm.

## Learning objectives

- Mutate, slice, and rebuild lists
- Distinguish aliasing from copying
- Choose the right traversal (index vs element vs enumerate)

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** Lectures 09–10 — Iteration patterns and strings

Assumed fluencies:

- index vs value loops
- mutating a list in place

**Preparation task:** Predict-then-run: three slice expressions of your own making.

## Detailed topic outline

Core (mandatory):

1. list operations and slicing views
2. aliasing versus copying
3. in-place mutation
4. rotation and reorder patterns

Extension (optional enrichment):

5. lists of records
6. shared references as a debugging skill

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-041 | The Queue Reorder | Beginner |
| cs-042 | Deduplication Patterns | Foundational |
| cs-043 | Rotate and Roll | Intermediate |
| cs-044 | The Aliasing Trap | Advanced |

Display each case full-screen from the student page (cases cs-041–cs-044);
instructor pages cs-041–cs-044 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts.

## Timing plan (120 minutes)

Format: **workshop session** — deliberately not the standard case rhythm.

| Minutes | Segment |
| --- | --- |
| 0–10 | Framing: the two patterns this workshop trains |
| 10–45 | Cases 1–2 (cs-041, cs-042): two 5-minute attempts back to back, one joint discussion, two reveals |
| 45–50 | Break |
| 50–90 | Cases 3–4 (cs-043, cs-044): same double rhythm, harder material |
| 90–110 | Deliberate-practice block: build or trace one of today's patterns end to end, instructor circulating |
| 110–120 | Synthesis, exit questions, homework |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-044 aliasing trap: before/after memory diagrams for the exact line that corrupts the roster.

**Instructor demonstration to open the lecture:** Draw the queue-reorder slices (cs-041) as boxes and arrows; then alias two names to one list and mutate, watching the class notice.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Aliasing diagrams | 8 | Pairs draw memory diagrams for four list statements, two of which alias; find the corruption. |
| 2 | Slice prediction quiz | 5 | Ten slice expressions, ten seconds each, answers revealed immediately. |
| 3 | Human array rotation | 6 | Twelve students are an array; two rotation algorithms are executed with physical moves. |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** Aliasing is the lecture's deep idea and the term's best debugging gift. Memory diagrams are mandatory for cs-044; students who skip them will rediscover the trap in the project.

**Running the reveal.** Workshop format: keep builds short and predictions public.

**Lecture focus.** One sentence to repeat verbatim: *Assignment binds a name; it rarely copies a list.*

## Common misconceptions

- Assuming assignment copies a list.
- Slicing when a copy is needed — aliasing corruption follows.
- Reversing by popping while still iterating over the same list.
- Rotating with a modulo applied to the wrong length.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. Draw memory diagrams for assignment, copy, and alias of a 3-element list.
2. Rotate cs-043's queue by k with slicing, then without any slicing.
3. Predict-then-run five provided aliasing statements; keep score honestly.

Enrichment (optional):

- Implement cs-041's reorder both stably and unstably; describe the difference with an example.
- Explain why tuple unpacking avoids the swap trap from the debugging clinic of lecture 12.

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. What is the difference between a = b and a = b[:] for lists?
   *Expected: the first aliases (one object, two names), the second copies*

2. Give the slice for the last three items and for every second item.
   *Expected: lst[-3:] and lst[::2]*

3. Why did the roster corrupt in cs-044?
   *Expected: two names referenced one list; an 'append' to one mutated the other*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO4, LO5 — Lists, slicing, and aliasing as a debugging superpower.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
