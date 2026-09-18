# Lecture 22 — Recursion and Divide-and-Conquer

## Position in the course

This is lecture 22 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

## Learning objectives

- Identify base and recursive cases
- Trace recursive calls with a call diagram
- Solve problems by divide, solve, combine

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** Lectures 06 and 21 — tracing and halving

Assumed fluencies:

- state tables for calls
- logarithmic cost intuition

**Preparation task:** Trace factorial(4) as a tree of calls on paper.

## Detailed topic outline

Core (mandatory):

1. recursion as self-similar subproblems
2. base cases and the call tree
3. recurrence relations
4. divide and conquer: power by halving

Extension (optional enrichment):

5. recursion to table: the DP preview
6. when recursion clarifies and when it costs

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-085 | The Russian Dolls | Beginner |
| cs-086 | Digit Sum, Twice | Foundational |
| cs-087 | Power by Halving | Intermediate |
| cs-088 | The Tower Steps | Expert |

Display each case full-screen from the student page (cases cs-085–cs-088);
instructor pages cs-085–cs-088 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts.

## Timing plan (120 minutes)

| Minutes | Segment |
| --- | --- |
| 0–10 | Framing: where this fits; recall of the previous lecture |
| 10–30 | Case 1 (cs-085): 5-minute attempt, then discussion and reveal |
| 30–50 | Case 2 (cs-086): same rhythm |
| 50–70 | Case 3 (cs-087): same rhythm, harder case |
| 70–75 | Break |
| 75–100 | Case 4 (cs-088): same rhythm, hardest case |
| 100–115 | Synthesis: name the techniques; misconceptions check |
| 115–120 | Exit questions, homework, next-lecture preview |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-087 power by halving: the recursion tree for a^13 with only 5 multiplications, and the cost arithmetic that explains it.

**Instructor demonstration to open the lecture:** Tower steps (cs-088): build the call tree for n = 5, then fill the table bottom-up — recursion becomes a table before their eyes.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Call-tree drawing | 7 | cs-086's digit-sum tree drawn and annotated with call counts. |
| 2 | Recursion vs table | 8 | The tower steps (cs-088) solved both ways; the table's speed is felt. |
| 3 | Base-case hunt | 5 | Three recursive definitions; teams find the input that never reaches a base case. |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** Recursion is taught as trust: assume the smaller call works, solve the step, and the base case grounds it. Call trees precede code; tables follow code.

**Running the reveal.** The DP preview (cs-088) is planted deliberately: lecture 23's tables should feel like an old friend, not a new topic.

**Lecture focus.** One sentence to repeat verbatim: *Trust the smaller call; ground it in the base case.*

## Common misconceptions

- Missing the base case, or making it unreachable.
- Trusting recursion without drawing the call tree once.
- Recomputing overlapping subproblems instead of tabulating them.
- Converting to iteration before the recursion itself is understood.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. Draw the call tree for digit-sum(9876) (cs-086) and count calls.
2. Implement power-by-halving (cs-087) and count multiplications for a^13 vs naive.
3. Fill the tower-steps table (cs-088) for n = 1..8 bottom-up.

Enrichment (optional):

- Convert three recursive solutions to explicit stacks; compare clarity honestly.
- Prove cs-087's halving cost with the recurrence T(n) = T(n/2) + 1.

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. What grounds a recursion?
   *Expected: a base case reachable for every input path*

2. When does a table beat the tree?
   *Expected: when subproblems repeat — overlapping subproblems*

3. What did cs-087 buy with halving?
   *Expected: multiplications dropped from ~13 to ~5 — logarithmic vs linear*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO10, LO7 — Recursion, recurrences, divide-and-conquer cost.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
