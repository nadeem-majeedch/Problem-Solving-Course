# Lecture 32 — The Whole Toolbox: Capstone Cases

## Position in the course

This is lecture 32 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

This lecture runs as the **capstone** session (time-capped attempts with live defence; see the timing plan), not the standard four-case rhythm.

## Learning objectives

- Integrate the full toolbox on unfamiliar problems
- Communicate a solution: model, algorithm, tests
- Justify trade-offs under time pressure

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** Lectures 01–31 — the full toolbox

Assumed fluencies:

- all techniques at readiness level

**Preparation task:** Re-attempt the mid-course challenge cup (lecture 16) and compare with your old plan.

## Detailed topic outline

Core (mandatory):

1. integration under a time cap
2. technique selection from a brief
3. the plan-first discipline at capstone level
4. defending choices in a live Q&A

Extension (optional enrichment):

5. course-level retrospective
6. what to learn next

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-125 | The Library Robot | Beginner |
| cs-126 | The Open-Day Planner | Foundational |
| cs-127 | The Data Clinic | Intermediate |
| cs-128 | The 20-Minute Final | Advanced |

Display each case full-screen from the student page (cases cs-125–cs-128);
instructor pages cs-125–cs-128 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts.

## Timing plan (120 minutes)

Format: **capstone session** — deliberately not the standard case rhythm.

| Minutes | Segment |
| --- | --- |
| 0–10 | Framing: what the capstone certifies; how defence works |
| 10–15 | Brief (cs-125–cs-128): rules, time caps, deliverables |
| 15–25 | Planning: written plans, techniques named, no code yet |
| 25–55 | Attempt 1: cs-125 under the clock |
| 55–60 | Break |
| 60–90 | Attempt 2 (cs-128): the capstone case, full integration |
| 90–110 | Live defence: 90-second plan presentations; the room asks falsifying questions |
| 110–120 | Course retrospective map, what-to-learn-next, exit questions |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-127 data clinic: a full pipeline — audit, clean, analyse, report — assembled live from named lecture techniques.

**Instructor demonstration to open the lecture:** Run the 20-minute final (cs-128) yourself, badly, on purpose: the class diagnoses which plan mistakes cost the most.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Toolbox auction | 6 | Teams allocate their 20 minutes across four cases and must justify the split. |
| 2 | Live plan defence | 10 | cs-125 plans presented in 90 seconds each; the room asks one falsifying question per plan. |
| 3 | Course retrospective map | 8 | The 32 lectures are pinned on a wall map of techniques; each student marks their growth edge. |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** The capstone is a rehearsal of professional practice: briefs, time caps, live defence. Grade the plan and the defence as heavily as the answer.

**Running the reveal.** Leave 15 minutes for the retrospective map and the what-next pointers — the course's closing argument is that the toolbox is now theirs.

**Lecture focus.** One sentence to repeat verbatim: *Under a cap: plan first, defend live, integrate everything.*

## Common misconceptions

- Abandoning the plan at the first obstacle instead of adapting it.
- Spending the whole cap polishing one case and abandoning the rest.
- Defending choices with 'it works' instead of trade-offs.
- Leaving the retrospective to memory instead of writing the map.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. Produce a 10-line integration plan for the library robot (cs-125) naming three techniques.
2. Time-capped run: cs-126 in 18 minutes, plan first, then exchange plans for peer review.
3. Write the data-clinic (cs-127) pipeline sketch: audit → clean → analyse → report.

Enrichment (optional):

- Write the capstone case you wish had been in the course, with solution sketch.
- Map your five strongest and five weakest techniques; set a study plan.

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. What did the plan-first discipline buy you today?
   *Expected: a defensible partial answer under a hard cap*

2. Name two cases where two techniques had to combine.
   *Expected: cs-125 (graphs + greedy), cs-127 (cleaning + statistics)*

3. What is your next technique to strengthen, and where will you practise it?
   *Expected: student's own map from the retrospective*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO1, LO2, LO10 — Capstone integration, defence, and strategy selection.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
