# Lecture 03 — Flowcharts and Control Flow

## Position in the course

This is lecture 3 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

## Learning objectives

- Read and draw flowcharts for decisions and loops
- Convert flowcharts to pseudocode and back
- Identify unreachable branches and infinite loops

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** Lecture 02 — Pseudocode as Precision

Assumed fluencies:

- sequence, selection, iteration in pseudocode
- variables and assignment

**Preparation task:** Redraw one of last lecture's pseudocode solutions as a flowchart before class.

## Detailed topic outline

Core (mandatory):

1. flowchart symbols and when each applies
2. translating pseudocode ⇄ flowcharts
3. loop preconditions and termination
4. state machines as flowcharts

Extension (optional enrichment):

5. tracing arrows with real data
6. finding dead branches before coding

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-009 | The ATM Loop | Beginner |
| cs-010 | Rain or Shine | Foundational |
| cs-144 | Two Paths, One Post | Foundational |
| cs-011 | The Dispatch Loop | Intermediate |
| cs-012 | Guess and Check | Advanced |

Display each case full-screen from the student page (cases cs-009–cs-012);
instructor pages cs-009–cs-012 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts. Applied additions cs-144 extend the session as optional extra attempts or homework;
they share the lecture's theme but teach an applied, real-world angle.

## Timing plan (120 minutes)

| Minutes | Segment |
| --- | --- |
| 0–10 | Framing: where this fits; recall of the previous lecture |
| 10–30 | Case 1 (cs-009): 5-minute attempt, then discussion and reveal |
| 30–50 | Case 2 (cs-010): same rhythm |
| 50–70 | Case 3 (cs-011): same rhythm, harder case |
| 70–75 | Break |
| 75–100 | Case 4 (cs-012): same rhythm, hardest case |
| 100–115 | Synthesis: name the techniques; misconceptions check |
| 115–120 | Exit questions, homework, next-lecture preview |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-011 dispatch loop: flowchart first, then prove termination by naming the quantity that strictly decreases.

**Instructor demonstration to open the lecture:** Draw the rain-or-shine flowchart (cs-010) live, deliberately leaving one diamond without an exit; the class must catch it.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Sketch That Flow | 7 | The main event: a numbers-free statement of cs-012, four minutes, then peer review of arrows. |
| 2 | Trace the arrows | 6 | Given a completed flowchart with one dead branch, each pair traces two inputs and must state which branch is unreachable. |
| 3 | Termination vote | 4 | Show two loop flowcharts; vote which terminates and name the quantity that guarantees it. |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** Flowcharts earn their keep on termination and dead-branch questions, where pseudocode is weak. Emphasise the arrow discipline: every diamond has exactly two labelled exits.

**Running the reveal.** Mixed-background note: beginners draw, experienced students verify — assign roles deliberately in pair work.

**Lecture focus.** One sentence to repeat verbatim: *Every diamond exits twice; every loop names what shrinks.*

## Common misconceptions

- Drawing decision diamonds with one exit or unlabelled arrows.
- Trusting a flowchart that was never traced with real data.
- Confusing the direction of arrows with the flow of time in loops.
- Modelling a state machine as a tangle of branches instead of named states.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. Redraw your cs-009 ATM pseudocode as a flowchart; mark the diamond exits.
2. Prove on the flowchart that cs-011 terminates by naming the decreasing quantity.
3. Find and fix the dead branch in a provided guess-the-game flowchart.

Enrichment (optional):

- Model cs-012 as a state machine diagram with named states.
- Prove the ATM loop (cs-009) cannot accept a fourth withdrawal.

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. Every decision diamond must have how many exits, and how labelled?
   *Expected: exactly two, labelled with mutually exclusive conditions*

2. What is the standard proof that a loop terminates?
   *Expected: name a quantity that strictly decreases (or increases) and is bounded*

3. What is a dead branch and how do flowcharts expose one?
   *Expected: an unreachable path; exposed by tracing arrows from start with all conditions*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO3, LO5 — Flowcharts plus early tracing of arrows begins the tracing habit.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
