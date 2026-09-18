# Lecture 30 — Optimization Formulations

## Position in the course

This is lecture 30 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

## Learning objectives

- Express problems as objectives with constraints
- Search small solution spaces exhaustively and smartly
- Recognise greedy vs search vs DP formulations

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** Lectures 23 and 20 — greedy/DP and search spaces

Assumed fluencies:

- objective and constraint vocabulary
- greedy failure modes

**Preparation task:** Express your weekly study plan as: maximise marks subject to 20 hours.

## Detailed topic outline

Core (mandatory):

1. objectives, constraints, decisions
2. formulating before solving
3. LP-flavoured formulations
4. integer constraints and their difficulty

Extension (optional enrichment):

5. search heuristics for hard instances
6. verifying a claimed optimum

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-117 | The Poster Budget | Beginner |
| cs-118 | The Shift Schedule | Foundational |
| cs-119 | The Knapsack Twins | Intermediate |
| cs-120 | The Exam Seating | Expert |

Display each case full-screen from the student page (cases cs-117–cs-120);
instructor pages cs-117–cs-120 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts.

## Timing plan (120 minutes)

| Minutes | Segment |
| --- | --- |
| 0–10 | Framing: where this fits; recall of the previous lecture |
| 10–30 | Case 1 (cs-117): 5-minute attempt, then discussion and reveal |
| 30–50 | Case 2 (cs-118): same rhythm |
| 50–70 | Case 3 (cs-119): same rhythm, harder case |
| 70–75 | Break |
| 75–100 | Case 4 (cs-120): same rhythm, hardest case |
| 100–115 | Synthesis: name the techniques; misconceptions check |
| 115–120 | Exit questions, homework, next-lecture preview |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-119 knapsack twins: the same data as a greedy formulation (fails) and a DP formulation (works); the decision criterion stated.

**Instructor demonstration to open the lecture:** Poster budget (cs-117): extract objective, constraints, and decisions in three colours before any algorithm is mentioned.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Formulation trio | 8 | Three word problems become objective/constraints/decisions triples; no solving allowed yet. |
| 2 | Constraint elimination | 7 | cs-118's schedule is attacked by eliminating infeasible assignments first. |
| 3 | Optimum verification | 5 | A claimed optimum is challenged: bound argument vs exhaustive check — both are valid. |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** Optimisation is taught as formulation first: most real difficulty is saying precisely what 'best' means. Solution methods stay light; verification of optimality is the depth.

**Running the reveal.** The greedy-fails-DP-works contrast from lecture 23 is re-invoked; students should feel the continuum from heuristic to formulation.

**Lecture focus.** One sentence to repeat verbatim: *Formulate precisely before you compute anything.*

## Common misconceptions

- Optimising before the objective and constraints are written.
- Smuggling soft preferences in as hard constraints, or the reverse.
- Accepting a claimed optimum without a bound or exhaustive check.
- Reaching for integer constraints where a linear model suffices.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. Write the poster-budget formulation (cs-117): objective, decisions, constraints in three lines.
2. List infeasible assignments for the shift schedule (cs-118) before any search.
3. Verify a claimed optimum for cs-119's small instance by exhaustive check.

Enrichment (optional):

- Formulate cs-120's seating with hard and soft constraints; argue which are which.
- Write a greedy heuristic for cs-120 and construct its worst case.

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. Name the three parts of a formulation.
   *Expected: decisions, objective, constraints*

2. Why is 'minimise cost' often incomplete?
   *Expected: unstated service/quality constraints make it meaningless — cs-118*

3. How do you verify a claimed optimum?
   *Expected: bound argument or exhaustive check on a reduced instance*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO8, LO10 — Formulation of optimisation problems; verification.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
