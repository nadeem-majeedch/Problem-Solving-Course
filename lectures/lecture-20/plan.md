# Lecture 20 — Brute Force and When It Wins

## Position in the course

This is lecture 20 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

This lecture runs as a **workshop** session (build-heavy; see the timing plan), not the standard four-case rhythm.

## Learning objectives

- Write clean brute-force solutions
- Estimate brute-force cost with rough arithmetic
- Decide when brute force is acceptable

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** Lectures 15 and 17 — enumeration and search

Assumed fluencies:

- nested loops as product of choices
- search-space size estimation

**Preparation task:** List all 16 outcomes of four binary switches; count those with exactly two on.

## Detailed topic outline

Core (mandatory):

1. search spaces and their sizes
2. brute force as a baseline and a checker
3. pruning the space honestly
4. divisors and number-theory scans

Extension (optional enrichment):

5. combinations vs subsets vs permutations
6. growth arithmetic: why 2^n dies

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-077 | The 4-Digit Lock | Beginner |
| cs-078 | Perfect Numbers | Foundational |
| cs-079 | The Meeting Triple | Intermediate |
| cs-080 | The Subset Riddle | Advanced |

Display each case full-screen from the student page (cases cs-077–cs-080);
instructor pages cs-077–cs-080 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts.

## Timing plan (120 minutes)

Format: **workshop session** — deliberately not the standard case rhythm.

| Minutes | Segment |
| --- | --- |
| 0–10 | Framing: the two patterns this workshop trains |
| 10–45 | Cases 1–2 (cs-077, cs-078): two 5-minute attempts back to back, one joint discussion, two reveals |
| 45–50 | Break |
| 50–90 | Cases 3–4 (cs-079, cs-080): same double rhythm, harder material |
| 90–110 | Deliberate-practice block: build or trace one of today's patterns end to end, instructor circulating |
| 110–120 | Synthesis, exit questions, homework |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-080 subset riddle: enumerate 4 items as 16 bitmasks, prune two branches honestly, and re-verify survivors by brute force.

**Instructor demonstration to open the lecture:** Four-digit lock (cs-077): count 10^4 aloud with the class, then halve it twice with honest pruning and re-count.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Space-size auction | 6 | Teams bid on the size of five search spaces (10^4, 2^10, C(20,3)...); arithmetic decides. |
| 2 | Pruning jury | 7 | For cs-079, each proposed prune is judged: sound (keeps the optimum) or cheating (might lose it). |
| 3 | Brute-force confession | 5 | Each team names one problem where brute force is the *right* answer and defends it. |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** Brute force is rehabilitated: it is the baseline that proves correctness of clever answers and the honest first attempt. The arithmetic of search spaces is the lecture's spine.

**Running the reveal.** Workshop format: the pruning jury is the pedagogical heart — sound pruning vs cheating pruning is exactly the discipline optimisation demands later.

**Lecture focus.** One sentence to repeat verbatim: *Count the space first; prune honestly; verify cleverness.*

## Common misconceptions

- Looping over 2^n 'just to see' without counting the space first.
- Pruning branches that might contain the optimum.
- Confusing subsets with combinations and with permutations.
- Verifying clever answers without any brute-force baseline.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. Enumerate the 4-digit lock space (cs-077) and count honest prunes for a given clue set.
2. List divisors of 28 and 12; classify perfect numbers (cs-078) up to 30 by hand.
3. Estimate C(12,3) meeting triples (cs-079) before counting them exactly.

Enrichment (optional):

- Estimate when 2^n exceeds C(50,25); reflect on subset vs combination search spaces.
- Write the sound-pruning checklist for cs-080 as pseudocode.

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. How big is the subset space of 25 items, roughly?
   *Expected: 2^25 ≈ 33 million — borderline; count before you loop*

2. What makes pruning sound?
   *Expected: it only removes branches that cannot contain a better answer*

3. When is brute force the right deliverable?
   *Expected: tiny spaces, correctness baselines, and verifying clever answers*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO10, LO7 — Search spaces, brute force as baseline, growth arithmetic.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
