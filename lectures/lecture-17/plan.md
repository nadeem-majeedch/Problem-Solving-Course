# Lecture 17 — Searching and Linear Scans

## Position in the course

This is lecture 17 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

## Learning objectives

- Implement and reason about linear search
- State preconditions for search correctness
- Return useful 'not found' information

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** Lectures 09–11 — iteration and lists

Assumed fluencies:

- writing scan loops
- boolean predicates over items

**Preparation task:** Write a contains-style loop for cs-065 from memory.

## Detailed topic outline

Core (mandatory):

1. linear scans and their cost
2. search with early exit
3. predicates as search conditions
4. finding first/last/all matches

Extension (optional enrichment):

5. preconditions that enable faster search
6. peak finding with neighbours

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-065 | Find the First Freeze | Beginner |
| cs-066 | The Course Finder | Foundational |
| cs-067 | Two Sorted Halves | Intermediate |
| cs-068 | Peak Finding | Expert |

Display each case full-screen from the student page (cases cs-065–cs-068);
instructor pages cs-065–cs-068 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts.

## Timing plan (120 minutes)

| Minutes | Segment |
| --- | --- |
| 0–10 | Framing: where this fits; recall of the previous lecture |
| 10–30 | Case 1 (cs-065): 5-minute attempt, then discussion and reveal |
| 30–50 | Case 2 (cs-066): same rhythm |
| 50–70 | Case 3 (cs-067): same rhythm, harder case |
| 70–75 | Break |
| 75–100 | Case 4 (cs-068): same rhythm, hardest case |
| 100–115 | Synthesis: name the techniques; misconceptions check |
| 115–120 | Exit questions, homework, next-lecture preview |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-068 peak finding: a three-way neighbour comparison, traced on a mountain-shaped array, including the plateau trap.

**Instructor demonstration to open the lecture:** Freeze scan (cs-065): run it on 8 temperatures, insert the target at position 0 and at the end, and let the class time the two exits.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Scan countdown | 5 | Three search tasks on a 20-item board list; teams must state exit time before running the scan. |
| 2 | Predicate workshop | 7 | Write three predicates for cs-066 (offered, fits timetable, not full) and compose them. |
| 3 | Early-exit debate | 5 | When does early exit change the answer? (never for existence, always for counting) — settle with examples. |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** Block III opens with the least glamorous but most used algorithm: the scan. Establish cost vocabulary (each item touched once = linear) before any formalism.

**Running the reveal.** The preconditions theme begins here: cs-067's sorted halves are only exploitable because the structure is trusted — that trust becomes binary search in lecture 21.

**Lecture focus.** One sentence to repeat verbatim: *Touch each item once; exit early when the question allows.*

## Common misconceptions

- Scanning to the end when the question allows an early exit.
- Forgetting the not-found case in the return contract.
- Ignoring preconditions that a faster method would require.
- Declaring peak finding hard without first checking neighbours.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. Write first-freeze scan (cs-065) with and without early exit; time both on 1,000 items.
2. Compose two predicates for the course finder (cs-066) and count matches in provided data.
3. Hand-trace peak finding (cs-068) on 7 values with one plateau.

Enrichment (optional):

- Find the last match and the all-matches variant of cs-065; adapt the invariant.
- Implement cs-068 for plateaus and defend your tie-breaking rule.

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. Cost of a full scan vs early exit, in words.
   *Expected: always n touches vs stops at the first match; existence searches often exit early*

2. What precondition made cs-067 fast?
   *Expected: the two halves are each sorted — structure enables strategy*

3. Name one search where early exit is wrong.
   *Expected: counting all matches; you must see every item*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO7, LO4 — Analysis vocabulary (linear cost, preconditions) grounded in scans.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
