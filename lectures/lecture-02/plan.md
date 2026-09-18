# Lecture 02 — Pseudocode as Precision

## Position in the course

This is lecture 2 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

## Learning objectives

- Write pseudocode precise enough to translate mechanically
- Express input, processing, output as named steps
- Trace pseudocode by hand before trusting it

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** Lecture 01 — Thinking in Problems

Assumed fluencies:

- decomposition into subproblems
- stating assumptions explicitly

**Preparation task:** Re-read the two interpretation cases from lecture 1 (the fine formula and the coffee card).

## Detailed topic outline

Core (mandatory):

1. pseudocode grammar used all term (SEQUENCE/IF/WHILE/FOR)
2. precision levels: vague → precise → testable
3. state and assignment in pseudocode
4. validating input in stages

Extension (optional enrichment):

5. describing randomness and constraints
6. pseudocode as communication, not decoration

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-005 | Largest of Three | Beginner |
| cs-006 | Password Rules | Foundational |
| cs-007 | The Vending Machine Script | Intermediate |
| cs-008 | Shuffling a Playlist | Expert |

Display each case full-screen from the student page (cases cs-005–cs-008);
instructor pages cs-005–cs-008 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts.

## Timing plan (120 minutes)

| Minutes | Segment |
| --- | --- |
| 0–10 | Framing: where this fits; recall of the previous lecture |
| 10–30 | Case 1 (cs-005): 5-minute attempt, then discussion and reveal |
| 30–50 | Case 2 (cs-006): same rhythm |
| 50–70 | Case 3 (cs-007): same rhythm, harder case |
| 70–75 | Break |
| 75–100 | Case 4 (cs-008): same rhythm, hardest case |
| 100–115 | Synthesis: name the techniques; misconceptions check |
| 115–120 | Exit questions, homework, next-lecture preview |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-007 vending machine script: a state table for the session, then the pseudocode that implements each transition.

**Instructor demonstration to open the lecture:** Write largest-of-three (cs-005) twice: a vague one-line version and a precise testable version; let the class attack the vague one.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Case Relay | 12 | Run activities/case-relay.md with cs-006: model → plan → code → test, each team inheriting the previous stage. |
| 2 | Spot the ambiguity | 6 | Three pseudocode fragments are shown; teams find the sentence a compiler could not forgive. |
| 3 | Hand-trace verification | 6 | Pairs exchange pseudocode and trace it on one input; sign off only if every variable is explained. |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** Pseudocode is sold here as a contract: if a classmate cannot trace it, it is not finished. Resist letting strong students write Python 'to be helpful' — the delay is the point.

**Running the reveal.** Introduce the exact pseudocode grammar used all term (SEQUENCE, IF/ELSE, WHILE, FOR, functions) so later lectures can say 'as in lecture 2' instead of re-teaching.

**Lecture focus.** One sentence to repeat verbatim: *Pseudocode is a contract another human can execute.*

## Common misconceptions

- Writing pseudocode that is Python with semicolons — no abstraction gained.
- Mixing precision levels inside one solution: vague prose beside exact lines.
- Declaring variables without stating what they mean.
- Skipping the hand-trace check because the code 'looks right'.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. Write pseudocode for 'prompt until a valid 8-character student ID is entered' using the course grammar.
2. Hand-trace your cs-006 pseudocode on two inputs, one failing each rule.
3. Express cs-008's constraint 'no two consecutive tracks by the same artist' in one precise sentence plus one IF.

Enrichment (optional):

- Rewrite cs-007's state machine to handle the cancel button.
- Translate one of your pseudocode solutions into the pseudocode style guide's strictest form.

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. Name the three control shapes every pseudocode solution is built from.
   *Expected: SEQUENCE, IF/ELSE selection, WHILE/FOR iteration*

2. What makes a pseudocode line 'testable'?
   *Expected: it names variables and values precisely enough to hand-trace*

3. When is a state table required?
   *Expected: whenever a later statement depends on more than the current input line*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO3, LO2 — Pseudocode precision is the vehicle; the thinking patterns are named in passing.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
