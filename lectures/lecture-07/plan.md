# Lecture 07 — Debugging as a Method

## Position in the course

This is lecture 7 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

This lecture runs as a **clinic** session (protocol-driven defect hunting; see the timing plan), not the standard four-case rhythm.

## Learning objectives

- Reproduce a defect with a minimal input
- Form hypotheses and test them one at a time
- Read error messages as evidence, not noise

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** Lecture 06 — Traces and loop reasoning

Assumed fluencies:

- state-table tracing
- reading someone else's code without rewriting it

**Preparation task:** Re-trace one of last lecture's traced snippets and its fix.

## Detailed topic outline

Core (mandatory):

1. symptoms → hypotheses → experiments
2. the binary search of a bug
3. boundary and aliasing defect classes
4. regression thinking

Extension (optional enrichment):

5. debugging with prints versus a debugger
6. fixing without breaking neighbours

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-025 | The Case of the Missing Sales | Beginner |
| cs-026 | The Off-by-One Invoice | Foundational |
| cs-027 | The Ghost Duplicate | Intermediate |
| cs-028 | The Heisenbug | Advanced |

Display each case full-screen from the student page (cases cs-025–cs-028);
instructor pages cs-025–cs-028 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts.

## Timing plan (120 minutes)

Format: **clinic session** — deliberately not the standard case rhythm.

| Minutes | Segment |
| --- | --- |
| 0–10 | Recall: the protocol from earlier lectures, on one slide |
| 10–20 | Protocol refresh: reproduce, hypothesise, cheapest experiment, isolate, fix, re-test |
| 20–45 | Case 1 (cs-025): full clinic cycle with written hypothesis ladders |
| 45–50 | Break |
| 50–80 | Cases 2–3 (cs-026, cs-027): two attempts, one discussion, two reveals |
| 80–100 | Case 4 (cs-028): solo attempt under time pressure; reveal as a walkthrough |
| 100–110 | Deliberate-practice hunt: apply the protocol to a fresh defect |
| 110–120 | Protocol reflection, exit questions, homework |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-028 heisenbug: isolate by halving the input, twice, on the board — the defect is cornered in four experiments.

**Instructor demonstration to open the lecture:** Demonstrate the hypothesis ladder on the missing-sales defect (cs-025): three hypotheses, cheapest test first, nothing fixed until confirmed.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Hypothesis ladder | 8 | For cs-026, pairs rank five hypotheses by test cost and write the cheapest discriminating experiment. |
| 2 | Think-Pair-Debug | 8 | A fresh one-bug snippet, this time a boundary defect; connect to the ladder afterwards. |
| 3 | Bug triage | 5 | Six symptom reports are ranked: which block a release, which are cosmetic, and why. |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** The clinic format needs discipline: hypotheses before experiments, cheapest test first, no fixing until confirmed. Students who already debug by hacking will resist; make them write the ladder down.

**Running the reveal.** Connect every defect class to a test class from lecture 8 — the two lectures are one story told twice.

**Lecture focus.** One sentence to repeat verbatim: *Cheapest experiment first; nothing fixed until confirmed.*

## Common misconceptions

- Changing code before the defect has been reproduced.
- Testing hypotheses in a random order instead of cheapest first.
- Fixing the visible symptom and leaving the cause in place.
- Shipping the fix without re-running the surrounding tests.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. Apply the hypothesis ladder to a provided buggy invoice program (cs-026 family); write the experiments before any fix.
2. Classify five planted defects into boundary / aliasing / arithmetic / state / logic.
3. Write the regression test that would have caught cs-027's ghost duplicate.

Enrichment (optional):

- Keep a one-week defect diary: symptom, hypothesis, experiment, cause.
- Explain cs-028's heisenbug to a non-programmer in five sentences.

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. Order the clinic protocol steps.
   *Expected: reproduce, hypothesise, cheapest experiment, isolate, fix, re-test*

2. Why fix nothing before the hypothesis is confirmed?
   *Expected: unconfirmed fixes destroy the evidence and add new defects*

3. What is a regression test for?
   *Expected: to make a fixed defect fail permanently if it ever returns*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO5, LO6 — Debugging as a method, connected forward to testing.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
