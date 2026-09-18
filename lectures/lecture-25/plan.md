# Lecture 25 — Thinking with Data

## Position in the course

This is lecture 25 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

## Learning objectives

- Formulate questions a dataset can answer
- Compute counts, shares, and distributions
- Choose the right summary for a question

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** Lectures 09 and 13 — aggregation and dictionaries

Assumed fluencies:

- group-by intuition
- rates vs counts

**Preparation task:** Tally one week of your own screen time by app category.

## Detailed topic outline

Core (mandatory):

1. questions before queries
2. aggregation on real-shaped data
3. distributions, not just averages
4. rates, per-capita and cohort views

Extension (optional enrichment):

5. bias in collection
6. from answer to decision

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-097 | The Canteen Queue Log | Beginner |
| cs-098 | Screen Time by Cohort | Foundational |
| cs-099 | The Churn Story | Intermediate |
| cs-139 | The Attendance Frame | Intermediate |
| cs-100 | The Survey Skew | Expert |

Display each case full-screen from the student page (cases cs-097–cs-100);
instructor pages cs-097–cs-100 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts. Applied additions cs-139 extend the session as optional extra attempts or homework;
they share the lecture's theme but teach an applied, real-world angle.

## Timing plan (120 minutes)

| Minutes | Segment |
| --- | --- |
| 0–10 | Framing: where this fits; recall of the previous lecture |
| 10–30 | Case 1 (cs-097): 5-minute attempt, then discussion and reveal |
| 30–50 | Case 2 (cs-098): same rhythm |
| 50–70 | Case 3 (cs-099): same rhythm, harder case |
| 70–75 | Break |
| 75–100 | Case 4 (cs-100): same rhythm, hardest case |
| 100–115 | Synthesis: name the techniques; misconceptions check |
| 115–120 | Exit questions, homework, next-lecture preview |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-100 survey skew: the same question answered three ways (voluntary, random, stratified) and the honest confidence of each.

**Instructor demonstration to open the lecture:** Canteen queue log (cs-097): pose three questions first, then show how each dictates a different aggregation.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Question surgery | 7 | A vague request is sharpened into three answerable data questions with named aggregates. |
| 2 | Distribution sketch | 6 | Three datasets' shapes sketched from five-number summaries only. |
| 3 | Cohort flip | 5 | One overall trend reverses within cohorts (Simpson preview); the class finds the hidden variable. |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** Block IV opens with data discipline: questions before computations. Every case asks 'what decision does this answer serve?' — that framing is the DS habit.

**Running the reveal.** Beginners thrive here; strong coders must be prevented from jumping to code. The five-minute attempts are answered on paper today, deliberately.

**Lecture focus.** One sentence to repeat verbatim: *The question picks the computation, not the reverse.*

## Common misconceptions

- Computing before stating the decision the number will serve.
- Reporting averages without the underlying distribution.
- Ignoring collection bias because the analysis itself is sound.
- Comparing cohorts of different sizes and calling the result a trend.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. Answer three sharpened questions on the canteen log (cs-097) with named aggregation patterns.
2. Sketch the screen-time distribution (cs-098) from a five-number summary; mark the skew.
3. Compute week-over-week churn (cs-099) for provided counts and say which week is worst and why.

Enrichment (optional):

- Redesign the cs-100 survey to remove the skew; predict the remaining bias.
- Find one published chart and rewrite its caption honestly.

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. Why state the decision before the computation?
   *Expected: the decision determines which aggregate is meaningful*

2. Why is the average alone dangerous in cs-098?
   *Expected: distributions with the same mean differ; skew hides in the shape*

3. What made cs-100's survey skew?
   *Expected: voluntary response — collection bias, not analysis error*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO9, LO8 — Data-oriented reasoning: questions, distributions, bias.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
