# Lecture 27 — Tables, Cleaning, and Anomalies

## Position in the course

This is lecture 27 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

This lecture runs as a **workshop** session (build-heavy; see the timing plan), not the standard four-case rhythm.

## Learning objectives

- Profile a table for missing and malformed values
- Write cleaning rules and justify them
- Detect duplicates and anomalies systematically

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** Lectures 10–13 — strings, lists, dictionaries

Assumed fluencies:

- validation rules
- deduplication patterns

**Preparation task:** Find two real data-entry errors in any form you use; classify them.

## Detailed topic outline

Core (mandatory):

1. auditing a table before analysing it
2. validation rules and their order
3. boundaries in graded data
4. entity resolution without unique IDs

Extension (optional enrichment):

5. time-series anomalies and dropouts
6. report the cleaning, always

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-105 | The Room Booking Audit | Beginner |
| cs-106 | The Grade Typos | Foundational |
| cs-107 | The Duplicate Students | Intermediate |
| cs-140 | The Sliced Anomaly | Intermediate |
| cs-108 | The Sensor Dropout | Advanced |

Display each case full-screen from the student page (cases cs-105–cs-108);
instructor pages cs-105–cs-108 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts. Applied additions cs-140 extend the session as optional extra attempts or homework;
they share the lecture's theme but teach an applied, real-world angle.

## Timing plan (120 minutes)

Format: **workshop session** — deliberately not the standard case rhythm.

| Minutes | Segment |
| --- | --- |
| 0–10 | Framing: the two patterns this workshop trains |
| 10–45 | Cases 1–2 (cs-105, cs-106): two 5-minute attempts back to back, one joint discussion, two reveals |
| 45–50 | Break |
| 50–90 | Cases 3–4 (cs-107, cs-108): same double rhythm, harder material |
| 90–110 | Deliberate-practice block: build or trace one of today's patterns end to end, instructor circulating |
| 110–120 | Synthesis, exit questions, homework |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-107 duplicate students: a matching key ladder (exact ID → name+DOB → fuzzy) with a public report of each rule's hit count.

**Instructor demonstration to open the lecture:** Room booking audit (cs-105): clean one week of bookings on the board with every rule reported in a public tally.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Audit stations | 15 | Three tables rotate between pairs; each station adds a rule to a shared cleaning report. |
| 2 | Key ladder debate | 7 | cs-107's matching keys ranked by precision; false merges are the cost of each. |
| 3 | Gap or spike | 5 | Six time-series excerpts classified: dropout, anomaly, or legitimate quiet period. |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** The second workshop of Block IV: real-shaped dirtiness is the material. Every cleaning action is reported — the public tally is the integrity lesson.

**Running the reveal.** Entity resolution (cs-107) is the hardest thinking; the key ladder makes it discussable without any fancy tooling.

**Lecture focus.** One sentence to repeat verbatim: *Clean nothing silently; report every rule and its toll.*

## Common misconceptions

- Cleaning silently — deleting or altering rows without reporting.
- Applying validation rules in an order that hides the real fault.
- Merging records on weak keys without weighing false merges.
- Treating a dropout gap as a zero reading.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. Audit the room bookings (cs-105): write every violated rule and its row references.
2. Fix grade typos (cs-106) under the first-failure rule; log each fix.
3. Propose a key ladder (cs-107) for the duplicate students and estimate its false-merge risk.

Enrichment (optional):

- Write the cleaning report as an executable checklist for cs-105.
- Propose a sensor-dropout imputation rule (cs-108) and defend its honesty limits.

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. Why report every cleaning rule?
   *Expected: silence is falsification of the analysis; the tally is the audit trail*

2. What is a false merge in cs-107?
   *Expected: two different students collapsed by a weak matching key*

3. When is a gap an anomaly?
   *Expected: when it breaks the series' established rhythm — context decides*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO9, LO4 — Data cleaning as audited engineering.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
