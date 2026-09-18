# Lecture 12 — Debugging Lab: Real Defects

## Position in the course

This is lecture 12 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

This lecture runs as a **clinic** session (protocol-driven defect hunting; see the timing plan), not the standard four-case rhythm.

## Learning objectives

- Localise defects in multi-step programs
- Use prints, asserts, and bisection to find faults
- Fix defects without introducing new ones

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** Lectures 07–08 — Debugging method and testing

Assumed fluencies:

- the hypothesis ladder
- test tables

**Preparation task:** Skim cs-045–cs-048 student pages; do not read solutions.

## Detailed topic outline

Core (mandatory):

1. a repeatable defect-hunt protocol
2. statistics defects that look correct
3. sentinel and default traps
4. tuple swap and reference traps

Extension (optional enrichment):

5. bisecting a regression
6. regression suites as memory

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-045 | The Median That Lies | Beginner |
| cs-046 | The Phantom Zero | Foundational |
| cs-129 | The Missing Marks | Foundational |
| cs-047 | The Swap That Wasn't | Intermediate |
| cs-130 | The Duplicate Rows | Intermediate |
| cs-048 | The Regression Zoo | Advanced |

Display each case full-screen from the student page (cases cs-045–cs-048);
instructor pages cs-045–cs-048 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts. Applied additions cs-129, cs-130 extend the session as optional extra attempts or homework;
they share the lecture's theme but teach an applied, real-world angle.

## Timing plan (120 minutes)

Format: **clinic session** — deliberately not the standard case rhythm.

| Minutes | Segment |
| --- | --- |
| 0–10 | Recall: the protocol from earlier lectures, on one slide |
| 10–20 | Protocol refresh: reproduce, hypothesise, cheapest experiment, isolate, fix, re-test |
| 20–45 | Case 1 (cs-045): full clinic cycle with written hypothesis ladders |
| 45–50 | Break |
| 50–80 | Cases 2–3 (cs-046, cs-047): two attempts, one discussion, two reveals |
| 80–100 | Case 4 (cs-048): solo attempt under time pressure; reveal as a walkthrough |
| 100–110 | Deliberate-practice hunt: apply the protocol to a fresh defect |
| 110–120 | Protocol reflection, exit questions, homework |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-048 regression zoo: bisect the history, name the culprit commit, write the regression test that would have caught it.

**Instructor demonstration to open the lecture:** Trace the median defect (cs-045) on three inputs where it answers correctly, then the fourth where it lies — the class predicts which.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Bug triage board | 8 | Four defect reports are triaged on a public board: reproduce, hypothesise, isolate — in that order. |
| 2 | Bisect demonstration | 7 | The regression zoo (cs-048) is halved twice on the board before any code is read. |
| 3 | Fix-the-zoo hunt | 15 | Teams get one defect each with a test suite; fix without breaking a single green test. |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** The second clinic. The protocol from lecture 7 is now executed under time pressure, with regression thinking added: fix nothing without a test that fails first.

**Running the reveal.** Choose the weakest-weak-spots live by poll; the clinic time is theirs, not the syllabus's.

**Lecture focus.** One sentence to repeat verbatim: *Reproduce, hypothesise, isolate, fix, re-test — in order.*

## Common misconceptions

- Debugging from the bug report alone, without reproducing.
- Bisecting history before isolating a reproducible input.
- Fixing without first writing the failing test.
- Declaring victory because one test passes now.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. Reproduce, isolate, and fix the phantom zero (cs-046) using the clinic protocol; log every experiment.
2. Write the regression suite for the swap-that-wasn't (cs-047) before fixing it.
3. Bisect a provided five-commit regression story; name the culprit commit.

Enrichment (optional):

- Build a three-test regression suite for one of your own past homework bugs.
- Reconstruct the zombie variable story of cs-047 as a memory diagram series.

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. Why must the reproduction step precede any hypothesis?
   *Expected: an unreproduced defect cannot be falsified; you would be guessing*

2. What does 'fix without breaking green tests' require?
   *Expected: a regression suite run before and after every change*

3. Name the isolation technique used on cs-048.
   *Expected: history bisect: halve the commit range each experiment*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO5, LO6 — The clinic consolidates debugging and regression thinking.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
