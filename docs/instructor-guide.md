# Instructor Guide

## Before the semester

1. Read [Teaching Methodology](teaching-methodology.md) and this guide once, end to end.
2. Skim all 32 lecture plans and the [Course Outline](course-outline.md).
3. Build the instructor distribution and load it on your teaching laptop:
   `python scripts/build_instructor.py` → `public_instructor/`.
4. Decide your institution's grade weights (defaults in
   [Assessment Plan](assessment-plan.md)) and quiz dates.
5. Print or distribute: the [Resources](resources.md) setup page in week 1.

## Preparing one lecture (≈ 30 minutes)

- Read the lecture `plan.md` top to bottom: objectives, prerequisite knowledge
  (assign the preparation task!), topic outline, case sequence, timing plan.
- Note the session **format** — most lectures are the standard case rhythm,
  but workshops, clinics, the review, and the capstone run differently (see
  [Teaching Methodology](teaching-methodology.md)).
- Rehearse the **instructor demonstration** and rework the **worked example**
  on paper; both are scripted in the plan.
- Pick the **activities** you will run (three are listed with minutes) and
  choose your **exit question**.
- Open the day's case pages in two browser tabs: student and instructor.
- Note which cases are **Core** vs **Enrichment** and which is *submit today*.
- Choose your drop order: if time collapses, which case goes first? (The plan
  suggests one.)
- Skim each instructor solution's *Common pitfalls* — that is where the
  discussion value is.
- Skim the lecture's `teaching-notes.md` (instructor-only): the board plan,
  the questions to ask, the alternative explanations, and the expected
  difficulties. The quiz answer key for the day is at the bottom.

## Running the hour

1. **Project the student page only.** The instructor page must never be
   visible to the room — its title reveals the solution approach.
2. Give a full five minutes for the attempt. Silence is normal; do not narrate
   over it. Circulate, read shoulders, pick two contrasting approaches to
   invite.
3. **Discuss before revealing.** Write both approaches on the board using the
   plan's board layout. Ask the room to predict which fails where.
4. **Reveal with the script.** Every instructor solution carries a per-case
   reveal walkthrough you can deliver verbatim or adapt. The same page also
   holds the five-minute teaching sequence (what to expect in each minute,
   including the case's most common wrong turn), the difficulty ladder
   (simplify / extend / three hint levels), and an assessment-use note with a
   10-point mini-rubric and a follow-up check.
5. **Distribute the pack, not ad-hoc printouts.** Each lecture's `notes.md`,
   `examples.md`, and `quiz.md` are student-facing and safe to publish;
   `teaching-notes.md` is instructor-only and is excluded from the public
   build (see [Instructor-only materials](#instructor-only-materials-and-distribution)).
6. Close the cycle by naming the technique: "this was decomposition plus a
   running total."

## The hint ladder (from the methodology page)

Clarify → Nudge → Structure → Approach. If you find yourself explaining a
solution during the attempt phase, stop and convert it into a hint at the next
rung.

## The five-minute cycle in practice

The attempt phase of every Core case follows one repeatable loop. It is a
guideline, not a stopwatch ritual — shorten it for Beginner cases that most
of the room cracks in two minutes, and hold the full span for Advanced ones.

- **Minute 0–1 — silent read.** Project the student page and say nothing.
  Students identify inputs, outputs, and the rule themselves. Resist the urge
  to paraphrase the statement aloud; decoding the ask is part of the skill.
- **Minute 1–3 — individual or pair drafting.** Everyone writes an approach:
  pseudocode, a hand-trace, or a diagram. Circulate silently. Your goal is
  not to help but to *select*: find one promising conventional attempt and
  one interesting deviation.
- **Minute 3–5 — compare and commit.** Pairs compare drafts, pick one to
  defend, and note where they disagree. If the room is stuck, this is when a
  first hint (the ladder's *Clarify* rung) is legitimate.
- **Reveal and discussion** — see the next two sections.

## Facilitating the discussion

- **Board both approaches before saying which is right.** Label them A and
  B, in the students' own words, not yours.
- **Ask the room to attack, not to guess:** "Which of these breaks first,
  and on what input?" Students who failed to solve the case can still
  stress-test an approach — that keeps them in the game.
- **Use the instructor page's *Common pitfalls* entry as your probing
  question**, not as a lecture: "Someone in another section did exactly X —
  why did it fail?"
- **Name the technique at the close** (one sentence), then connect it to the
  lecture's concept and the next case in the sequence.
- **Protect wrong answers.** Thank the deviation, analyse why it fails, and
  point out what it *would* solve — wrong turns are the course's best
  teaching material, and each instructor solution's reasoning section lists
  the most common one for exactly this purpose.

## Handling multiple solution approaches

Most cases admit at least two honest approaches (the instructor page's
*Alternative approaches* section lists them). The default protocol:

1. Whichever approach the room produced first gets the board first, even if
   it is the naive one.
2. Compare on three axes only: **correctness** (does it handle the edge
   cases?), **clarity** (can a classmate trace it?), **cost** (steps or
   passes over the data).
3. Declare the *recommended* solution for this course and say why — but also
   say when the alternative is the better engineering choice. Complexity
   arguments come from Lecture 25 onward; before that, count operations on
   concrete inputs instead of using big-O language.
4. If the room produced only one approach, *you* supply the second — the
   instructor page's alternatives are written to be presented as "a section
   last year did this".

## Extensions without derailing the hour

Every student case page carries an *Extensions* block. Release it when the
room solves the case early (the *Fast class* move below), or assign it as
the follow-up homework. Extensions are always optional and never assessed —
they exist so strong students have somewhere to go that is not merely "more
of the same". If an extension sparks a long debate, park it: "office hours
question", and move on to the next case.

## Handling the room you actually have

- **Fast class**: release the *Extensions* on the student page after minute
  three of the attempt; run a second discussion round on them.
- **Quiet class**: switch one cycle per lecture to think-pair-share (pairs
  agree on one pseudocode before the discussion).
- **Mixed semesters**: seat third-semester students spread out, not clustered;
  invite them to lead the "what to notice" observation for Beginner cases.
- **Nobody solved it**: use the instructor solution's reasoning section as the
  reveal and say plainly that this one was a discussion-target case.

## Instructor-only materials and distribution

Instructor-only material lives in `case-studies/instructor/`,
`quizzes/keys/`, the answer keys inside activities, labs, and assignments,
and the audit reports in `docs/instructor-reports/` (the expert-tier
rationale and the quiz-key / lab-output audits — they quote reference
program output, so they are teaching answers in disguise).

- The public site build (`scripts/build_site.py`) **excludes** all of these
  directories (student-facing quizzes, labs, assignments, projects, and
  activities publish without their keys) and fails if any solution file
  appears in `site/`.
- The instructor build (`scripts/build_instructor.py`) produces
  `public_instructor/` containing everything, for your own devices.
- **Never deploy `public_instructor/` to GitHub Pages or any public host.** A
  private directory is not protection once a site is public; exclusion at
  build time is the only reliable control. Share solutions with your teaching
  team via your institution's access-controlled system (LMS or shared drive).
- If you fork this repository to publish your own student site, keep the
  instructor build output out of the Pages branch.

## The solution bank in brief

Every `case-studies/instructor/cs-NNN-*.md` page follows one layout:

- **Reasoning section** — the case's worked instance, expected result,
  method moves, and the most common wrong turn (per-case, hand-authored).
- **Five-minute teaching sequence** — minute-by-minute expectations and
  watch-fors, sized by difficulty.
- **Difficulty adaptation** — how to simplify, how to extend, and a
  three-level hint ladder (re-orient → structure → near-answer).
- **Reference pseudocode** — derived mechanically from the case's
  own verified Python (house dialect: `<-`, `FOR EACH`, `WHILE`, `RETURN`).
- **Reference Python** — runnable, smoke-tested on every build;
  executing the file prints the worked instance.
- **Edge cases / Alternative approaches / Common pitfalls** — derived from
  the case's own code shape and stated wrong turn, never generic.
- **Reveal walkthrough** — per-case: the opening question, the board walk of
  the worked instance, and the close that names the technique.
- **Assessment use** — formative-use note, a 10-point mini-rubric, and a
  follow-up question that tests understanding.
- **Connections / Extension challenge** — links to the neighbouring case and
  the enrichment task.

`scripts/validate.py` enforces the section set; nothing in this bank is
student-facing, and the public build never renders it.

## Mid-semester checklist

- Quiz average below 60%? Insert one consolidation lecture using the
  *Enrichment* cases from Lectures 11–16 as review material.
- Collect one anonymised "common error" slide per quiz for the feedback loop.
- Verify the project midpoint (decomposition documents) is scheduled.

## End-of-semester checklist

- Record which cases were discussion-targets (nobody solved) and which ran
  short — adjust next semester's timing budgets.
- Archive best anonymised student attempts (with permission) as future
  discussion material.
- Run `python scripts/validate.py` before any edits you contribute back.

## Adaptation notes

- **64 hours fixed, but a fast quarter system**: merge each block's last two
  lectures by teaching the Core cases only; keep all quizzes.
- **No labs room**: replace Lab sessions with the corresponding activities
  (`activities/`), which need only a projector and paper.
- **Students with no Python at all**: add the first 30 minutes of Lecture 04's
  Python ramp (`resources/python-setup.md`) as a pre-semester session.
