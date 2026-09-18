# Lecture 16 — Mid-Course Consolidation

## Position in the course

This is lecture 16 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

This lecture runs as a **review** session (stations chosen by student poll; see the timing plan), not the standard four-case rhythm.

## Learning objectives

- Combine loops, strings, lists, and dictionaries in one program
- Plan a solution on paper before coding
- Self-review against a checklist

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** Lectures 01–15 — everything

Assumed fluencies:

- all Block I–II techniques

**Preparation task:** Re-do your weakest quiz-1–3 question; bring it to the stations.

## Detailed topic outline

Core (mandatory):

1. integration: problems that need three techniques at once
2. plan-first under time pressure
3. weak-spot repair stations
4. strategy selection

Extension (optional enrichment):

5. exam-style pacing
6. consolidation before Block III

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-061 | The Gradebook Audit | Beginner |
| cs-062 | Text Stats on a Budget | Foundational |
| cs-141 | The Rollout Memo | Foundational |
| cs-063 | The Campus Survey | Intermediate |
| cs-064 | The Mini Challenge Cup | Advanced |

Display each case full-screen from the student page (cases cs-061–cs-064);
instructor pages cs-061–cs-064 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts. Applied additions cs-141 extend the session as optional extra attempts or homework;
they share the lecture's theme but teach an applied, real-world angle.

## Timing plan (120 minutes)

Format: **review session** — deliberately not the standard case rhythm.

| Minutes | Segment |
| --- | --- |
| 0–10 | Warm-up poll: students self-locate their weakest technique |
| 10–25 | Station setup: three review stations, tasks from the weakest areas |
| 25–55 | Stations, round 1: solve at your chosen station, instructor circulates |
| 55–60 | Break |
| 60–90 | Stations, round 2: rotate or stay; mini-reveals at each station |
| 90–105 | Integration case (cs-064): one full attempt under exam pacing |
| 105–115 | Mini-debrief: what the attempts revealed; technique map update |
| 115–120 | Exit questions and exam pointers |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-064 mini challenge cup: read the brief, choose two techniques, and sketch the plan in eight minutes under exam pacing.

**Instructor demonstration to open the lecture:** Decompose the gradebook audit (cs-061) into a three-technique plan on the board; keep the plan and grade the attempts against it.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Review stations | 12 | Three stations (tracing, data structures, plan-first); students go to their weakest, chosen by a show-of-hands poll. |
| 2 | Integration plan sketch | 8 | cs-063 campus survey: eight minutes to produce a plan naming three techniques; plans are peer-graded. |
| 3 | Strategy huddle | 5 | For cs-064, teams commit to a strategy before the attempt; commitments are compared after the reveal. |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** Consolidation is run like an exam rehearsal: stations chosen by the students' own poll, attempts under real time pressure, plans graded as strictly as code.

**Running the reveal.** Mine the quiz data for the weak-spot clinic; the lecture is different every year by design.

**Lecture focus.** One sentence to repeat verbatim: *Under pressure, the plan is worth more than the code.*

## Common misconceptions

- Re-solving from scratch instead of reusing named patterns.
- Spending the clock on a favourite technique rather than the required one.
- Writing code before the integration plan exists.
- Revising all topics equally instead of targeting known weak spots.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. Re-do your weakest question from quizzes 1–3 under a 10-minute timer.
2. Write an integration plan for cs-061 naming three techniques and their order.
3. Speed-run: two mini-problems from Block I and two from Block II, 6 minutes each.

Enrichment (optional):

- Write your own mini challenge cup case and its solution sketch.
- Teach one Block II technique to a beginner; note what you had to invent.

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. Name the three stations and why you chose yours.
   *Expected: tracing / data structures / plan-first; chosen by personal weak spot*

2. What must an integration plan name before code?
   *Expected: the techniques, their order, and the data each stage hands on*

3. What does exam pacing change about case attempts?
   *Expected: time-boxing: a complete partial plan beats an unfinished perfect one*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO1, LO2, LO4, LO5 — Integration of Blocks I–II under exam pacing.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
