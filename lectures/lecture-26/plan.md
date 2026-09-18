# Lecture 26 — Counting and Probability in Data

## Position in the course

This is lecture 26 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

## Learning objectives

- Estimate probabilities from frequencies
- Reason with independence and complementary events
- Use simulation to check combinatorial intuition

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** Lectures 15 and 26's own sibling — counting and probability basics

Assumed fluencies:

- frequencies as probabilities
- independence informally

**Preparation task:** Flip a coin 20 times, record runs of heads; bring the longest run.

## Detailed topic outline

Core (mandatory):

1. frequencies and estimation
2. independence and its failures
3. conditional probability
4. false positives and base rates

Extension (optional enrichment):

5. streaks and waiting times
6. simulation cross-checks

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-101 | The Late Bus Frequency | Beginner |
| cs-102 | The Double-Click Question | Foundational |
| cs-103 | The Grid Decision Review | Intermediate |
| cs-137 | The Backup Window | Advanced |
| cs-104 | The Streak Simulation | Expert |

Display each case full-screen from the student page (cases cs-101–cs-104);
instructor pages cs-101–cs-104 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts. Applied additions cs-137 extend the session as optional extra attempts or homework;
they share the lecture's theme but teach an applied, real-world angle.

## Timing plan (120 minutes)

| Minutes | Segment |
| --- | --- |
| 0–10 | Framing: where this fits; recall of the previous lecture |
| 10–30 | Case 1 (cs-101): 5-minute attempt, then discussion and reveal |
| 30–50 | Case 2 (cs-102): same rhythm |
| 50–70 | Case 3 (cs-103): same rhythm, harder case |
| 70–75 | Break |
| 75–100 | Case 4 (cs-104): same rhythm, hardest case |
| 100–115 | Synthesis: name the techniques; misconceptions check |
| 115–120 | Exit questions, homework, next-lecture preview |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-103 grid decision review: the 2×2 of test result vs truth, base rates included, PPV computed by hand.

**Instructor demonstration to open the lecture:** Double-click question (cs-102): two coins, independence assumed, then the dependency trap exposed with real paired flips.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Coin-run statistics | 6 | 20 real flips per pair; runs of heads pooled on the board and compared with theory. |
| 2 | Base-rate theatre | 8 | A rare-disease scenario with volunteers as 1 positive among 99 negatives; PPV is experienced. |
| 3 | Independence test | 5 | Paired vs unpaired events classified with reasons. |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** Probability is taught as calibrated intuition: frequencies first, formulas second. The base-rate theatre activity is the emotional core — book the volunteers early.

**Running the reveal.** cs-104's streak simulation links back to lecture 15's birthday complement and forward to lecture 29's estimation.

**Lecture focus.** One sentence to repeat verbatim: *Frequencies calibrate intuition; base rates humble it.*

## Common misconceptions

- Multiplying probabilities of dependent events.
- Ignoring base rates when judging a positive test result.
- Reading a 20-flip run as evidence about long-run frequency.
- Simulating without seeds or trial counts, then over-trusting the output.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. Convert the late-bus frequency table (cs-101) to estimated probabilities; check they sum to 1.
2. List the 4 outcomes of two double-clicks (cs-102); mark which assume independence.
3. Compute the decision review's PPV (cs-103) with base rate 2% by hand.

Enrichment (optional):

- Simulate cs-104 for 10,000 runs; compare with the complement-counting answer.
- Derive the waiting-time distribution for cs-101's uniform assumption.

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. What is a base rate and what does it do to PPV?
   *Expected: prior prevalence; low base rates collapse PPV even with good tests*

2. When may two events not be multiplied?
   *Expected: when they are dependent — cs-102's paired clicks*

3. What did simulation add to the streak question?
   *Expected: an empirical check that the counting was right*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO8, LO9 — Probability with base rates; simulation cross-checks.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
