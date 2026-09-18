# Lecture 14 — Functions and Reuse

## Position in the course

This is lecture 14 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

## Learning objectives

- Decompose programs into single-purpose functions
- Distinguish parameters from arguments, return from print
- Reason about scope and pass-by-object-reference

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** Lectures 04–13 — any core construct

Assumed fluencies:

- calling what you already wrote
- reading a function signature

**Preparation task:** Find one repeated block in your own homework and name it.

## Detailed topic outline

Core (mandatory):

1. functions as named subproblems
2. parameters, returns, and scope
3. refactoring a monolith
4. mutable default arguments

Extension (optional enrichment):

5. composition: pipelines of functions
6. interfaces before implementation

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-053 | The Validator Trio | Beginner |
| cs-054 | Refactor the Monolith | Foundational |
| cs-138 | The Downtime Ledger | Foundational |
| cs-055 | The Parameter Jungle | Intermediate |
| cs-056 | Pipelines as Functions | Expert |

Display each case full-screen from the student page (cases cs-053–cs-056);
instructor pages cs-053–cs-056 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts. Applied additions cs-138 extend the session as optional extra attempts or homework;
they share the lecture's theme but teach an applied, real-world angle.

## Timing plan (120 minutes)

| Minutes | Segment |
| --- | --- |
| 0–10 | Framing: where this fits; recall of the previous lecture |
| 10–30 | Case 1 (cs-053): 5-minute attempt, then discussion and reveal |
| 30–50 | Case 2 (cs-054): same rhythm |
| 50–70 | Case 3 (cs-055): same rhythm, harder case |
| 70–75 | Break |
| 75–100 | Case 4 (cs-056): same rhythm, hardest case |
| 100–115 | Synthesis: name the techniques; misconceptions check |
| 115–120 | Exit questions, homework, next-lecture preview |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-056 pipelines as functions: a box-and-arrow diagram of the pipeline, then the signatures that make it type-safe by construction.

**Instructor demonstration to open the lecture:** Refactor the validator trio (cs-053) live: extract one function, rename, re-run the same tests, and show nothing broke.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Refactor kata | 10 | Pairs extract one function from a provided monolith; two solutions are compared on naming and signature. |
| 2 | Interface sketch | 6 | Before any implementation, teams write only the signatures and docstrings for cs-056's pipeline. |
| 3 | Default trap discussion | 4 | The mutable-default classic is shown; predict, run, explain, and state the fix. |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** Functions are taught as named subproblems first and syntax second: if the name is wrong, the signature is wrong, and the code is wrong. Refactoring the monolith (cs-054) is the emotional peak — same behaviour, half the mess.

**Running the reveal.** Mutable defaults are demonstrated, not lectured; the trap is more convincing when it bites live.

**Lecture focus.** One sentence to repeat verbatim: *Name the subproblem before you write the function.*

## Common misconceptions

- Naming functions after their implementation instead of their purpose.
- Sharing data through globals rather than parameters and returns.
- Sharing a mutable default object across calls unknowingly.
- Changing behaviour while 'only' refactoring — tests must pin behaviour.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. Extract two single-purpose functions from a provided monolith; behaviour must not change.
2. Design signatures first for the cs-056 pipeline; then implement the smallest one.
3. Fix the mutable-default trap in a provided accumulator function and explain the mechanism.

Enrichment (optional):

- Write the pipeline version of the text-stats case from lecture 16 with three named functions.
- Design the interface (signatures only) for a gradebook module.

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. What makes a function name good?
   *Expected: it states the subproblem's contract: verb + object, no surprises*

2. Why are mutable defaults dangerous?
   *Expected: the default object is created once and shared across calls*

3. What does 'refactor without behaviour change' demand?
   *Expected: the same tests pass before and after, unchanged*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO1, LO4 — Decomposition is executed through functions.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
