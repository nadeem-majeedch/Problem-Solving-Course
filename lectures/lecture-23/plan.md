# Lecture 23 — Greedy and Dynamic Programming

## Position in the course

This is lecture 23 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

This lecture runs as a **workshop** session (build-heavy; see the timing plan), not the standard four-case rhythm.

## Learning objectives

- Argue when greedy choices are safe
- Formulate DP states and transitions
- Memoise a recursive solution

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** Lectures 18, 20, 22 — sorting, brute force, recursion

Assumed fluencies:

- exchange arguments
- overlapping subproblems (from the tower-steps case)

**Preparation task:** Re-read the tower-steps case (lecture 22) solution; bring its recurrence table.

## Detailed topic outline

Core (mandatory):

1. greedy choice and the exchange argument
2. counterexamples as falsification
3. interval scheduling
4. dynamic programming: states and transitions

Extension (optional enrichment):

5. knapsack formulations
6. greedy vs DP: the decision

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-089 | The Coin Conjecture | Beginner |
| cs-090 | The Meeting Room Marathon | Foundational |
| cs-091 | The Tolerance Ladder | Intermediate |
| cs-131 | The Two-Desk Counter | Intermediate |
| cs-143 | The Shelf Replenishment | Intermediate |
| cs-092 | The Budgeted Syllabus | Advanced |

Display each case full-screen from the student page (cases cs-089–cs-092);
instructor pages cs-089–cs-092 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts. Applied additions cs-131, cs-143 extend the session as optional extra attempts or homework;
they share the lecture's theme but teach an applied, real-world angle.

## Timing plan (120 minutes)

Format: **workshop session** — deliberately not the standard case rhythm.

| Minutes | Segment |
| --- | --- |
| 0–10 | Framing: the two patterns this workshop trains |
| 10–45 | Cases 1–2 (cs-089, cs-090): two 5-minute attempts back to back, one joint discussion, two reveals |
| 45–50 | Break |
| 50–90 | Cases 3–4 (cs-091, cs-092): same double rhythm, harder material |
| 90–110 | Deliberate-practice block: build or trace one of today's patterns end to end, instructor circulating |
| 110–120 | Synthesis, exit questions, homework |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-092 budgeted syllabus: the DP table over topics × budget filled on the board, one row narrated in full.

**Instructor demonstration to open the lecture:** Coin conjecture (cs-089): the greedy is run and confirmed on three inputs, then killed by one input — falsification in action.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Counterexample lab | 9 | Greedy strategies for three problems; each team's job is one falsifying input. |
| 2 | DP table relay | 10 | cs-092's table filled row by row by relay teams; errors are caught at row handoffs. |
| 3 | Greedy-or-DP court | 6 | Two new problems argued both ways; the class is the jury with a decision criterion. |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** Two giant ideas share a lecture by design: their contrast is the lesson. Greedy is falsified by counterexample; DP is justified by overlapping subproblems.

**Running the reveal.** Workshop format with extended blocks; expect fatigue — the DP relay works best right after the break.

**Lecture focus.** One sentence to repeat verbatim: *Falsify greedy with one input; justify DP with overlap.*

## Common misconceptions

- Trusting greedy because it worked on the first examples.
- Hunting counterexamples only among easy inputs.
- Defining DP states that omit what future decisions need.
- Treating DP tables as formulas to memorise rather than relations to fill.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. Find the falsifying input for cs-089's greedy from its instructor page; verify it by hand.
2. Schedule cs-090's six meetings greedily by earliest-end; prove the exchange step for one swap.
3. Fill two rows of cs-092's DP table and explain one cell's max in words.

Enrichment (optional):

- Implement the 0/1 knapsack table for cs-092 fully; recover the chosen set.
- Write a one-page memo: when is greedy defensible in practice?

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. What one input kills cs-089's greedy?
   *Expected: the non-canonical coin set instance from its instructor page*

2. State the exchange argument for earliest-end scheduling.
   *Expected: swapping a later-ending chosen meeting for an earlier-ending one never hurts*

3. What makes a DP state adequate?
   *Expected: it captures everything the future decisions need to know*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO10, LO7 — Greedy vs DP: falsification and justification of strategies.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
