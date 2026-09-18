# Lecture 19 — Invariants and Two Pointers

## Position in the course

This is lecture 19 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

## Learning objectives

- State and defend loop invariants
- Apply two-pointer scans to arrays and strings
- Prove a loop terminates

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** Lectures 10 and 18 — strings/sorting

Assumed fluencies:

- two-ended thinking from anagram work
- sorted order as a precondition

**Preparation task:** Redo cs-073's palindrome walk with pen and two fingers.

## Detailed topic outline

Core (mandatory):

1. invariants: the property that never breaks
2. two pointers from both ends
3. pair-sum contracts on sorted data
4. partitioning in one pass

Extension (optional enrichment):

5. slow/fast pointers and cycle detection
6. proving correctness by invariant

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-073 | The Palindrome Walk | Beginner |
| cs-074 | The Pair Sum Contract | Foundational |
| cs-075 | Partition by Parity | Intermediate |
| cs-076 | The Slow-Fast Cycle | Advanced |

Display each case full-screen from the student page (cases cs-073–cs-076);
instructor pages cs-073–cs-076 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts.

## Timing plan (120 minutes)

| Minutes | Segment |
| --- | --- |
| 0–10 | Framing: where this fits; recall of the previous lecture |
| 10–30 | Case 1 (cs-073): 5-minute attempt, then discussion and reveal |
| 30–50 | Case 2 (cs-074): same rhythm |
| 50–70 | Case 3 (cs-075): same rhythm, harder case |
| 70–75 | Break |
| 75–100 | Case 4 (cs-076): same rhythm, hardest case |
| 100–115 | Synthesis: name the techniques; misconceptions check |
| 115–120 | Exit questions, homework, next-lecture preview |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-075 partition by parity: state the invariant ('left of i all even, right of j all odd'), then execute one pass on 8 items.

**Instructor demonstration to open the lecture:** Palindrome walk (cs-073) with two students as pointers walking inward; every disagreement is announced aloud.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Invariant announcement | 6 | Pairs state cs-074's invariant aloud before any code; the class falsifies weak versions. |
| 2 | Two-pointer dance | 7 | Nine students, one sum target, pointers move physically; each move justified. |
| 3 | Tortoise-and-hare trace | 6 | cs-076 on a 6-node drawn ring; the meeting point is predicted then traced. |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** Invariants are introduced as promises, not proofs: state the promise, keep the promise, and correctness follows. The physical two-pointer demos carry the lecture.

**Running the reveal.** cs-076 (slow/fast) is Expert; the accessible core is the termination argument — the gap that closes — rather than the full cycle-detection story.

**Lecture focus.** One sentence to repeat verbatim: *State the invariant as a promise; never break the promise.*

## Common misconceptions

- Moving both pointers without stating which one moves and why.
- Violating the invariant mid-loop with an eager advance.
- Applying pair-sum logic to data that was never sorted.
- Mixing up slow/fast purposes: termination proof versus cycle detection.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. State and verify the pair-sum invariant (cs-074) on sorted data for three targets.
2. Partition 10 numbers by parity in one pass (cs-075); annotate the invariant at each swap.
3. Trace the slow/fast walk (cs-076) on a drawn 8-node ring until pointers meet.

Enrichment (optional):

- Prove cs-075's partition terminates by the gap argument.
- Research Floyd's algorithm; relate it to cs-076's meeting point.

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. State cs-074's invariant in one sentence.
   *Expected: the answer pair, if it exists, lies within the current window*

2. Why do two pointers give linear cost?
   *Expected: each pointer moves at most n times; total moves 2n*

3. What ends the slow/fast walk's doubt?
   *Expected: the gap strictly shrinks — termination is provable*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO10, LO7 — Invariants and two-pointer strategy; correctness reasoning.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
