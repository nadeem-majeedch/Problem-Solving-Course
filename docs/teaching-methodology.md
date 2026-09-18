# Teaching Methodology

## The five-minute case method

Every lecture is a sequence of **case cycles**. One cycle has four phases:

| Phase | Time | What happens |
| --- | --- | --- |
| 1. Display | ~1 min | The instructor projects the student case page. Students read. |
| 2. Attempt | ~5 min | Students work individually (pseudocode, flowchart, or Python). The instructor circulates and notes approaches. |
| 3. Discuss | ~8–12 min | Two or three students describe their approach. The class compares them before any solution is shown. |
| 4. Reveal | ~5–8 min | The instructor opens the instructor page and walks through the model solution, edge cases, and alternatives. |

The case pages are written to be projected: short statements, visible
constraints, and examples that fit on one screen.

## Rhythm of a two-hour lecture

- **0:00–0:10** Warm-up: recap of the previous lecture via one quick question,
  plus the quiz/assignment handback when scheduled.
- **0:10–1:50** Four case cycles (three on weeks with a lab or quiz).
- **1:50–2:00** Synthesis: name the techniques seen today, connect to the
  learning outcomes, assign homework and preview the next lecture.

Lecture plans include a per-case timing budget and mark which cases may be
dropped if time runs short. Every timing table ends with the same flex note:
let an ignited discussion run and compress the synthesis; harvest partial
attempts rather than extending the clock.

## Session formats

The standard case rhythm above is the default, but eleven lectures
deliberately use a different structure. Each plan's timing table names its
format at the top:

| Format | Lectures | Shape |
| --- | --- | --- |
| Standard | 21 of 32 | Four case cycles + synthesis |
| Workshop | 04, 11, 18, 20, 23, 27, 29 | Build-heavy: paired attempts back to back, one joint discussion per pair of cases, a deliberate-practice block |
| Clinic | 07, 12 | Protocol-driven defect hunting: reproduce, hypothesise, cheapest experiment, isolate, fix, re-test |
| Review | 16 | Station-based consolidation; students choose stations by a self-assessment poll |
| Capstone | 32 | Time-capped integration attempts with live plan defence and a course retrospective |

All formats keep the attempt-first rule and the reveal discipline — only the
packaging changes. Do not force a workshop lecture back into four identical
cycles; the format *is* the pedagogy for that lecture.

## What every lecture plan contains

All 32 plans share one anatomy (see any `lectures/lecture-NN/plan.md`):

1. Position in the course, learning objectives, and **prerequisite knowledge**
   with a concrete preparation task to assign beforehand.
2. A **detailed topic outline** split into core (mandatory) and extension
   (optional enrichment).
3. The case sequence with difficulties, and the format-specific **timing plan**.
4. A **worked example** plus the **instructor demonstration** that opens the
   lecture.
5. At least three **classroom activities** with minutes and prompts (reusing
   the standard activity formats where suitable).
6. The board plan, **instructor explanation notes** (reading the room, running
   the reveal, the one-sentence lecture focus), and **common misconceptions**
   to address by name.
7. **Student practice exercises** (core and enrichment), the **formative
   assessment** (exit questions with expected answers), homework, and the
   **learning-outcome mapping** back to the course outcomes.

## The attempt-first rule

Students must produce *something* before the reveal — even a wrong approach, a
diagram, or a question. Wrong attempts are treated as data for the discussion.
This rule is what makes the method work: the reveal answers a question the
student already has.

## The hint ladder

During the attempt phase the instructor gives hints only in this order:

1. **Clarify** — restate what is being asked; point at the example.
2. **Nudge** — "what is the first thing you would need to know?"
3. **Structure** — suggest a decomposition or a table to fill in.
4. **Approach** — name a technique from an earlier lecture.

Never reveal during the attempt phase; the reveal phase belongs to the class
discussion.

## Mixed-ability design

Every student page separates:

- **Core task** — required of everyone, sized for five minutes at Beginner/Intermediate level.
- **Extensions** — optional, labelled *Extension (enrichment)*, aimed at Advanced/Expert students.
- **What to notice** — a low-floor observation question so a struggling student still contributes to the discussion.

First-semester students are expected to master core tasks in Blocks I–II.
Third-semester students should be attempting extensions routinely and can act
as discussion leaders for Beginner cases.

## Pseudocode before Python

Blocks I–II require a pseudocode or flowchart attempt before any Python. This
keeps students without prior programming on equal footing and forces the
reasoning to be explicit. From Block III, students may go straight to Python,
but the discussion still asks "why does this work?" rather than "does it run?"

## Discussion culture

- Volunteer first; cold-call only for *observations*, never for full solutions.
- Compare two approaches before evaluating either.
- Praise the diagnosis of a bug as highly as a working solution.
- The instructor writes student ideas on the board before opening the
  instructor page — the board plan in each lecture plan shows the layout.

## What if nobody solves it?

That is a designed outcome for several Advanced and Expert cases. The plan
marks them as *discussion-target* cases: the reveal becomes a mini-lecture
driven by the instructor solution's reasoning section. Record in the course
log which cases behaved this way — it informs next semester's pacing.

## Enrichment vs mandatory

Each lecture plan tags cases **Core** or **Enrichment**. Core cases are the
mandatory sequence; enrichment cases exist for fast classes, extra sessions,
and self-study. Skipping every enrichment case still covers all learning
outcomes (see [Learning Outcomes](learning-outcomes.md)).
