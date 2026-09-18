# Lecture 21 — Binary Search Everywhere

## Position in the course

This is lecture 21 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

## Learning objectives

- Implement binary search on arrays
- Generalise binary search to answer functions (search on answer)
- Reason about halves, bounds, and termination

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** Lectures 17 and 19 — scans and invariants

Assumed fluencies:

- halving intuition
- sorted preconditions

**Preparation task:** Play the number-guessing game optimally on 1–100; count your guesses.

## Detailed topic outline

Core (mandatory):

1. binary search on arrays
2. the boundary family (first true/first false)
3. invariants of lo/hi
4. search on the answer

Extension (optional enrichment):

5. monotonic predicates
6. logarithmic cost, counted

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-081 | Guess the Number, Formally | Beginner |
| cs-082 | The First Bad Version | Foundational |
| cs-083 | Book Allocation | Intermediate |
| cs-084 | The Rotten Timeline | Expert |

Display each case full-screen from the student page (cases cs-081–cs-084);
instructor pages cs-081–cs-084 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts.

## Timing plan (120 minutes)

| Minutes | Segment |
| --- | --- |
| 0–10 | Framing: where this fits; recall of the previous lecture |
| 10–30 | Case 1 (cs-081): 5-minute attempt, then discussion and reveal |
| 30–50 | Case 2 (cs-082): same rhythm |
| 50–70 | Case 3 (cs-083): same rhythm, harder case |
| 70–75 | Break |
| 75–100 | Case 4 (cs-084): same rhythm, hardest case |
| 100–115 | Synthesis: name the techniques; misconceptions check |
| 115–120 | Exit questions, homework, next-lecture preview |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-083 book allocation: define 'feasible(maxLoad)' as a monotonic predicate, then binary-search the answer with a full trace.

**Instructor demonstration to open the lecture:** Guess-the-number (cs-081) played against the class: 7 questions guaranteed; then a wrong guess strategy that needs 100.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Halving relay | 6 | 1–1000 guessed by relay; the question count is graphed against 1000's log2. |
| 2 | Boundary drill | 7 | Five first-true boundaries written as lo/hi tables; common off-by-one exhibited and fixed. |
| 3 | Monotone or not | 5 | Six predicates voted monotone/non-monotone; binary search eligibility is the lesson. |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** Binary search generalises beyond arrays: any monotone predicate is searchable. The boundary family (first true) prevents the classic off-by-ones; drill it.

**Running the reveal.** Search-on-the-answer (cs-083) is the lecture's stretch; the feasibility predicate is the bridge from this lecture to optimisation in lecture 30.

**Lecture focus.** One sentence to repeat verbatim: *Halve, and halve again; the predicate must be monotone.*

## Common misconceptions

- Off-by-one at the midpoint or in the boundary update.
- Binary-searching a predicate that is not monotone.
- Forgetting that search-on-the-answer needs a feasibility check.
- Halving the wrong half after the comparison.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. Play optimal guessing (cs-081) on 1–512; write your question sequence.
2. Build the lo/hi table for first-bad-version (cs-082) on 16 versions with the bad set {9..16}.
3. Trace the feasibility predicate (cs-083) for maxLoad = 7 and maxLoad = 8 on provided books.

Enrichment (optional):

- Binary-search the answer for a painted-per-day variant of cs-084; state the monotone predicate.
- Count the exact number of comparisons for one full binary search on 1,000 items.

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. Why must the predicate be monotone for binary search?
   *Expected: so that one test discards half the space forever*

2. What is searched in search-on-the-answer?
   *Expected: the feasibility boundary over candidate answers, not the items*

3. How many halvings for 1,000,000?
   *Expected: about 20 — log2 of a million*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO7, LO10 — Binary search generalised to monotone predicates.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
