# Lecture 31 — Strategy Under Uncertainty

## Position in the course

This is lecture 31 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

## Learning objectives

- Frame decisions with payoffs and probabilities
- Use expected value to compare strategies
- Recognise when more information changes the decision

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** Lectures 26 and 29 — probability and simulation

Assumed fluencies:

- expected value arithmetic
- simulation as an estimator

**Preparation task:** Compute the expected value of a 10-ticket lottery with published odds.

## Detailed topic outline

Core (mandatory):

1. expected value as a decision tool
2. payoff tables
3. the switch question resolved by listing
4. risk aversion beyond expectation

Extension (optional enrichment):

5. dominance arguments
6. mechanism thinking: how rules shape behaviour

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-121 | The Umbrella Decision | Beginner |
| cs-122 | The Game Show Switch | Foundational |
| cs-123 | The Insurance Riddle | Intermediate |
| cs-124 | The Auction Bluff | Advanced |

Display each case full-screen from the student page (cases cs-121–cs-124);
instructor pages cs-121–cs-124 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts.

## Timing plan (120 minutes)

| Minutes | Segment |
| --- | --- |
| 0–10 | Framing: where this fits; recall of the previous lecture |
| 10–30 | Case 1 (cs-121): 5-minute attempt, then discussion and reveal |
| 30–50 | Case 2 (cs-122): same rhythm |
| 50–70 | Case 3 (cs-123): same rhythm, harder case |
| 70–75 | Break |
| 75–100 | Case 4 (cs-124): same rhythm, hardest case |
| 100–115 | Synthesis: name the techniques; misconceptions check |
| 115–120 | Exit questions, homework, next-lecture preview |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-124 auction bluff: a payoff table completed for both bidders, dominant strategies found, and the equilibrium read off.

**Instructor demonstration to open the lecture:** Umbrella decision (cs-121): the payoff table drawn once, expected values computed twice — with rain 30% and 70%.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Payoff table gallery | 8 | Four decision scenarios turned into payoff tables; the class tours and votes on best actions. |
| 2 | Switch simulation | 7 | cs-122 played 30 times by pairs with forced switch vs forced stay; results pooled. |
| 3 | Risk interview | 5 | Same expected value, different variances: which do you choose? Answers are discussed, not graded. |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** Expected value is a decision tool, not a gambling lesson: the payoff-table discipline applies to project choices and policy. Risk attitudes are discussed, never mocked.

**Running the reveal.** cs-122's switch question is resolved by listing, the course's signature move, one last time.

**Lecture focus.** One sentence to repeat verbatim: *Build the payoff table; let expectation argue, then judge risk.*

## Common misconceptions

- Comparing options on intuition when a payoff table is cheap.
- Reading expected value as a promise about a single outcome.
- Ignoring variance when stakes or ruin matter.
- Missing dominance that the payoff table would reveal instantly.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. Build the umbrella payoff table (cs-121) for both rain probabilities and pick the action.
2. List the six outcomes of the switch question (cs-122) and compute both strategies' expectations.
3. Argue the insurance riddle (cs-123) from both sides: expected value says no, risk says yes.

Enrichment (optional):

- Design a fair mechanism for a shared fridge; analyse its equilibria informally.
- Compute the variance of cs-121's two options; connect to risk preference.

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. What does expected value compare, and what does it ignore?
   *Expected: average outcomes; it ignores variance (risk) unless you add it*

2. Why does switching win in cs-122?
   *Expected: the host's reveal leaks information; 2/3 of outcomes favour switching*

3. When is a dominated strategy visible instantly?
   *Expected: one option's payoffs are worse in every column of the table*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO8, LO10 — Expected value and strategic reasoning.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
