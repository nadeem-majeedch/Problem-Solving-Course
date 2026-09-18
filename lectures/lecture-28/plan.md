# Lecture 28 — Summaries That Don't Mislead

## Position in the course

This is lecture 28 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

## Learning objectives

- Choose mean vs median deliberately
- Read percentages with their bases
- Spot misleading summaries and fix them

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** Lecture 25 — thinking with data

Assumed fluencies:

- mean vs median
- percentages and their bases

**Preparation task:** Bring one published statistic and guess its base.

## Detailed topic outline

Core (mandatory):

1. mean vs median under skew
2. percentage bases and their traps
3. the inspection paradox
4. Simpson's paradox informally

Extension (optional enrichment):

5. dashboard ethics
6. defending a summary to a sceptical room

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-109 | The Salary Parable | Beginner |
| cs-110 | The Percentage Maze | Foundational |
| cs-111 | The Waiting-Time Twist | Intermediate |
| cs-112 | The Dashboard Defence | Advanced |
| cs-135 | The Split That Leaks | Expert |

Display each case full-screen from the student page (cases cs-109–cs-112);
instructor pages cs-109–cs-112 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts. Applied additions cs-135 extend the session as optional extra attempts or homework;
they share the lecture's theme but teach an applied, real-world angle.

## Timing plan (120 minutes)

| Minutes | Segment |
| --- | --- |
| 0–10 | Framing: where this fits; recall of the previous lecture |
| 10–30 | Case 1 (cs-109): 5-minute attempt, then discussion and reveal |
| 30–50 | Case 2 (cs-110): same rhythm |
| 50–70 | Case 3 (cs-111): same rhythm, harder case |
| 70–75 | Break |
| 75–100 | Case 4 (cs-112): same rhythm, hardest case |
| 100–115 | Synthesis: name the techniques; misconceptions check |
| 115–120 | Exit questions, homework, next-lecture preview |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-111 waiting-time twist: the bus paradox simulated with 100 simulated passengers and reconciled with the arithmetic.

**Instructor demonstration to open the lecture:** Salary parable (cs-109): add one billionaire to a row of nine salaries and watch the mean betray; the median holds.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Mean-vs-median showdown | 6 | Ten salary strips; instant votes, then the skew that decides them. |
| 2 | Percentage court | 7 | Three published claims are tried: is the base stated, and is the comparison legal? |
| 3 | Dashboard redesign | 6 | A misleading chart is redesigned under the constraint 'honest but still persuasive'. |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** Summaries are arguments, and this lecture teaches students to cross-examine them. The inspection paradox (cs-111) is the intellectual peak; simulation makes it believable.

**Running the reveal.** Ethics is treated as design under constraint (cs-112), not as a bolt-on sermon.

**Lecture focus.** One sentence to repeat verbatim: *Every summary is an argument; cross-examine it.*

## Common misconceptions

- Defending a mean in the presence of obvious skew.
- Comparing percentages that use different bases.
- Sampling waits without noticing length bias — the inspection paradox.
- Optimising a dashboard for persuasion over honesty.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. Recompute the salary parable's (cs-109) mean and median with and without the outlier.
2. Untangle the percentage maze (cs-110): identify each base and restate the claims correctly.
3. Explain the waiting-time twist (cs-111) in four sentences to a commuter.

Enrichment (optional):

- Rebuild cs-112's dashboard under three conflicting stakeholder demands; document choices.
- Explain Simpson's reversal with a made-up admission-rate example.

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. When must the median replace the mean?
   *Expected: under skew or outliers — any time a tail can dominate*

2. What is the percentage maze's core error?
   *Expected: comparing percentages with different bases*

3. State the inspection paradox in one line.
   *Expected: sampled experiences oversample long waits/stays — the sampling is length-biased*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO9, LO8 — Statistical honesty: summaries cross-examined.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
