# Lecture 15 — Counting, Combinatorics, and Choice

## Position in the course

This is lecture 15 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

## Learning objectives

- Apply the multiplication and addition principles
- Compute combinations and permutations from first principles
- Justify over-counting corrections

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** Lecture 05 — numbers and cycles; Lecture 13 — dictionaries

Assumed fluencies:

- systematic enumeration by hand
- factorial intuition

**Preparation task:** List all orderings of three items by hand, then count them.

## Detailed topic outline

Core (mandatory):

1. systematic counting without tears
2. permutations and constraints
3. combinations and the complement trick
4. probability from counting

Extension (optional enrichment):

5. simulation as a counting check
6. surprising coincidences, quantified

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-057 | The Locker Problem | Beginner |
| cs-058 | Team Photo Lineups | Foundational |
| cs-133 | The Late Bus Ledger | Foundational |
| cs-059 | The Committee Draw | Intermediate |
| cs-060 | The Birthday Question | Advanced |

Display each case full-screen from the student page (cases cs-057–cs-060);
instructor pages cs-057–cs-060 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts. Applied additions cs-133 extend the session as optional extra attempts or homework;
they share the lecture's theme but teach an applied, real-world angle.

## Timing plan (120 minutes)

| Minutes | Segment |
| --- | --- |
| 0–10 | Framing: where this fits; recall of the previous lecture |
| 10–30 | Case 1 (cs-057): 5-minute attempt, then discussion and reveal |
| 30–50 | Case 2 (cs-058): same rhythm |
| 50–70 | Case 3 (cs-059): same rhythm, harder case |
| 70–75 | Break |
| 75–100 | Case 4 (cs-060): same rhythm, hardest case |
| 100–115 | Synthesis: name the techniques; misconceptions check |
| 115–120 | Exit questions, homework, next-lecture preview |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-060 birthday question: complement counting on the board, 23 students, and the simulation that confirms it.

**Instructor demonstration to open the lecture:** Act the locker problem (cs-057) out with 10 lockers and 10 volunteers; the square-number pattern emerges physically.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Locker act-it-out | 7 | Ten lockers, ten students, two passes; the square pattern is discovered before it is explained. |
| 2 | Counting stations | 8 | Three stations: orderings, committees, complement counting; two minutes each, answers posted. |
| 3 | Birthday poll | 5 | Poll the room for real birthdays, then compare against the 23-student prediction from cs-060. |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** Counting is made concrete: act it out, tabulate, then generalise. The complement trick (cs-060) is the lecture's transferable gem — 'count the opposite, subtract'.

**Running the reveal.** Probability here is counting with fair assumptions; keep formality out, simulation as a check in.

**Lecture focus.** One sentence to repeat verbatim: *Enumerate small, tabulate, generalise; complement when stuck.*

## Common misconceptions

- Counting orderings where order does not matter.
- Multiplying probabilities of dependent events.
- Ignoring the complement until direct counting becomes tangled.
- Trusting intuition about coincidences instead of computing them.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. Count the committees of 3 from 7 students by hand, then verify with the formula.
2. List and count the team photo lineups (cs-058) for 4 students with the height constraint.
3. Compute the birthday question's complement for n = 10, 23, 30 without simulation.

Enrichment (optional):

- Estimate the committee probability in cs-059 by exact counting, then verify.
- Invent a locker-problem variant with two passes and analyse it.

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. When is the complement trick the right tool?
   *Expected: when counting the desired set directly is tangled but its opposite is simple*

2. Permutations vs combinations in one phrase each.
   *Expected: order matters / order does not*

3. How does simulation back up counting?
   *Expected: many random trials approximate the counted probability*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO8, LO10 — Combinatorics and the first taste of strategy under uncertainty.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
