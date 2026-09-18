# Lecture 18 — Sorting and Pair Scans

## Position in the course

This is lecture 18 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

This lecture runs as a **workshop** session (build-heavy; see the timing plan), not the standard four-case rhythm.

## Learning objectives

- Sort with keys; sort tuples and parallel data
- Scan sorted data for nearest/adjacent pairs
- Explain why sorting enables simpler scans

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** Lecture 17 — searching and scans

Assumed fluencies:

- predicates over data
- swapping two list items

**Preparation task:** Sort a hand of 8 playing cards by two different strategies; note which felt cheaper.

## Detailed topic outline

Core (mandatory):

1. sorting as a precondition for everything
2. stable sort keys and multi-level ordering
3. adjacent-pair scans after sorting
4. intervals: merge overlapping meetings

Extension (optional enrichment):

5. selection: the kth element
6. what sorting buys versus what it costs

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-069 | Rank the Leaderboard | Beginner |
| cs-070 | The Meeting Merge | Foundational |
| cs-071 | Closest Pair, Small n | Intermediate |
| cs-134 | The Sliding Sensor Window | Advanced |
| cs-072 | The Kth Element | Expert |

Display each case full-screen from the student page (cases cs-069–cs-072);
instructor pages cs-069–cs-072 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts. Applied additions cs-134 extend the session as optional extra attempts or homework;
they share the lecture's theme but teach an applied, real-world angle.

## Timing plan (120 minutes)

Format: **workshop session** — deliberately not the standard case rhythm.

| Minutes | Segment |
| --- | --- |
| 0–10 | Framing: the two patterns this workshop trains |
| 10–45 | Cases 1–2 (cs-069, cs-070): two 5-minute attempts back to back, one joint discussion, two reveals |
| 45–50 | Break |
| 50–90 | Cases 3–4 (cs-071, cs-072): same double rhythm, harder material |
| 90–110 | Deliberate-practice block: build or trace one of today's patterns end to end, instructor circulating |
| 110–120 | Synthesis, exit questions, homework |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-070 meeting merge: sort by start, sweep with an active-interval variable, and prove each merge case with a timeline.

**Instructor demonstration to open the lecture:** Sort 10 meeting cards by start on the board, then merge overlaps with two fingers as pointers — the interval pattern made physical.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Human sort race | 8 | Two lines of 8 students sorted by height via merge-vs-selection strategies; time and compare. |
| 2 | Interval merge drill | 7 | Six meeting pairs merged on the board with a running active interval. |
| 3 | Stability spotlight | 5 | A two-key sort order question; predict the output before revealing. |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** Workshop format: sorting is learned through the body and through data, not through sorting-network diagrams. Keep the stable-key discussion concrete (leaderboards with ties).

**Running the reveal.** The merge-on-sort pattern (cs-070) is the term's most reused trick; name it and expect to invoke it in lectures 23 and 30.

**Lecture focus.** One sentence to repeat verbatim: *Sort to create structure, then exploit the structure.*

## Common misconceptions

- Fully sorting when the question only asks for selection.
- Leaving ties unresolved, producing arbitrary output.
- Merging intervals with pairwise comparisons instead of one sweep.
- Forgetting that the merge pattern needs sorted input to be valid.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. Sort the leaderboard (cs-069) by score, then by score-then-name; state why the second is well-defined.
2. Merge cs-070's six intervals by hand with a sweep table.
3. Find the kth element (cs-072) of provided data by sorting; then argue a cheaper route.

Enrichment (optional):

- Prove the merged-interval result stays sorted; formalise the sweep.
- Design a stable three-key leaderboard sort for cs-069 with tie-breakers of your choosing.

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. What does sorting buy for interval merging?
   *Expected: overlaps become adjacent; one sweep suffices*

2. Why must the leaderboard sort be stable or fully keyed?
   *Expected: ties must resolve deterministically or the order is arbitrary*

3. What does the kth-element question really ask?
   *Expected: selection, not full sorting — sorting is the simple correct baseline*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO7, LO10 — Sorting as structure creation; the merge-on-sort pattern as strategy.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
