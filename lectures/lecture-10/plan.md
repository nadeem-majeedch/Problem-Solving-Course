# Lecture 10 — Strings Under the Lens

## Position in the course

This is lecture 10 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

## Learning objectives

- Index, slice, and walk strings safely
- Classify characters and build derived strings
- Reason about palindromes and reversal

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** Lecture 04 + Lecture 09 — Python basics and iteration

Assumed fluencies:

- indexing and slicing strings
- looping over characters

**Preparation task:** Solve cs-038 by hand with paper slices.

## Detailed topic outline

Core (mandatory):

1. string immutability and slicing
2. character classification
3. parsing with split/join
4. normalisation before comparison

Extension (optional enrichment):

5. building strings efficiently
6. palindromes and two-ended scans

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-037 | Username Auditor | Beginner |
| cs-038 | The Reversal Family | Foundational |
| cs-039 | Template Mail-Merge | Intermediate |
| cs-040 | The Anagram Detector | Advanced |

Display each case full-screen from the student page (cases cs-037–cs-040);
instructor pages cs-037–cs-040 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts.

## Timing plan (120 minutes)

| Minutes | Segment |
| --- | --- |
| 0–10 | Framing: where this fits; recall of the previous lecture |
| 10–30 | Case 1 (cs-037): 5-minute attempt, then discussion and reveal |
| 30–50 | Case 2 (cs-038): same rhythm |
| 50–70 | Case 3 (cs-039): same rhythm, harder case |
| 70–75 | Break |
| 75–100 | Case 4 (cs-040): same rhythm, hardest case |
| 100–115 | Synthesis: name the techniques; misconceptions check |
| 115–120 | Exit questions, homework, next-lecture preview |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-040 anagram detector: the normalisation ladder (case → spaces → order) applied to three nasty pairs.

**Instructor demonstration to open the lecture:** Audit one bad username (cs-037) rule by rule on the board, in the exact order the rules must run, and show why order matters.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Character desk check | 6 | A loop over a word is traced one character per desk; the class chants the state after each character. |
| 2 | Normalisation ladder debate | 6 | For cs-040, argue which normalisation step is risky and give a pair of words that proves it. |
| 3 | Anagram duel | 5 | Two pairs, one word each, fastest correct sorted-signature wins; losers explain their slower route. |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** Strings punish sloppy thinkers delightfully: normalisation before comparison is the lecture's big idea. The normalisation ladder is drawn once and reused all term.

**Running the reveal.** Beginners should work one character at a time physically; advanced students meet the two-ended scan that lecture 19 formalises.

**Lecture focus.** One sentence to repeat verbatim: *Normalise before you compare; slices before loops.*

## Common misconceptions

- Comparing strings before normalising case and spaces.
- Trying to mutate strings in place — immutability surprise.
- Off-by-one in slices: the end boundary is exclusive.
- Parsing with hand-managed indexes when split/join states the intent.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. Write the normalisation ladder for a case-insensitive, space-blind anagram check.
2. Parse 'Doe, Jane; Mathi, Aron' into two records using split only.
3. Hand-slice your way through cs-038's reversal family for 'lecture'.

Enrichment (optional):

- Extend cs-039 to handle optional fields and defaults.
- Write the two-ended palindrome scan (a lecture 19 preview) in pseudocode.

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. Why normalise before comparing strings?
   *Expected: so equal-meaning strings compare equal (case, spaces, order)*

2. What does immutability of strings imply for building output?
   *Expected: each change builds a new string; accumulate in a list and join*

3. When is slicing clearer than a loop?
   *Expected: when the operation is positional (reverse, prefix, step) rather than conditional*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO4, LO9 — String processing as data preparation in miniature.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
