# Lecture 01 — Thinking in Problems

## Position in the course

This is lecture 1 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

## Learning objectives

- Decompose a messy requirement into precise subproblems
- State assumptions and constraints before solving
- Choose between alternative interpretations of a task

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** — (course start)

Assumed fluencies:


**Preparation task:** None. Students who feel behind should read the pseudocode style guide once; everything else is built in class.

## Detailed topic outline

Core (mandatory):

1. What makes a problem statement precise
2. inputs, outputs, constraints, assumptions
3. decomposition trees
4. choosing between interpretations

Extension (optional enrichment):

5. the display–attempt–discuss–reveal rhythm
6. naming techniques so they can be reused

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-001 | The Coffee Card | Beginner |
| cs-002 | The Elevator Debate | Foundational |
| cs-003 | Two Vending Machines | Intermediate |
| cs-004 | The Library Fine Formula | Expert |

Display each case full-screen from the student page (cases cs-001–cs-004);
instructor pages cs-001–cs-004 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts.

## Timing plan (120 minutes)

| Minutes | Segment |
| --- | --- |
| 0–10 | Framing: where this fits; recall of the previous lecture |
| 10–30 | Case 1 (cs-001): 5-minute attempt, then discussion and reveal |
| 30–50 | Case 2 (cs-002): same rhythm |
| 50–70 | Case 3 (cs-003): same rhythm, harder case |
| 70–75 | Break |
| 75–100 | Case 4 (cs-004): same rhythm, hardest case |
| 100–115 | Synthesis: name the techniques; misconceptions check |
| 115–120 | Exit questions, homework, next-lecture preview |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-004 library fine formula: full decomposition, both readings of the grace rule, and the edge cases that decide the answer.

**Instructor demonstration to open the lecture:** Model the coffee card (cs-002) on the board: extract inputs, outputs, two defensible readings of 'every 6th drink free', and show how the reading changes the answer.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Assumption hunt | 6 | In pairs, list every hidden assumption in the two vending machines case (cs-003); the longest defensible list wins. |
| 2 | Sketch That Flow | 7 | Run the standard activity (activities/sketch-that-flow.md) on a numbers-free restatement of cs-004. |
| 3 | Interpretation vote | 5 | Two defensible readings of a rule are presented; vote, then argue the minority case for one minute. |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** Week one mixes complete beginners with students who already code. The equaliser is that every case rewards *precision*, not syntax: experienced coders lose points for unspoken assumptions, beginners win them for careful reading. Keep Python out of the room entirely today.

**Running the reveal.** The five-minute attempt is a discipline, not a suggestion: time it visibly, collect two contrasting attempts, and only then reveal. The technique name at the end of each cycle is the thread the whole course hangs on.

**Lecture focus.** One sentence to repeat verbatim: *Precision before code; assumptions spoken aloud, always.*

## Common misconceptions

- Jumping to code before the problem is understood.
- Treating unstated assumptions as facts.
- Believing a precise answer exists without first choosing an interpretation.
- Confusing decomposition with merely listing steps.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. Decompose the campus printing service's pricing page into a subproblem tree with stated assumptions.
2. Rewrite the two defensible readings of cs-003's discount rule as two precise specifications.
3. For cs-001, list every input class for which the fine is zero.

Enrichment (optional):

- Attempt the extension on the cs-004 page: fines that compound weekly.
- Bring one real-world ambiguous specification to the next lecture.

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. State the four questions you must answer before attempting any case.
   *Expected: inputs, outputs, constraints, assumptions (edge cases named from them)*

2. Give one example of two defensible readings of the same rule.
   *Expected: e.g. 'every 6th drink free' — counting only paid drinks vs all drinks*

3. Why is the five-minute attempt not wasted time?
   *Expected: it generates the class's own attempts, making the reveal answer a question already asked*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO1, LO2 — Decomposition and computational thinking are introduced as explicit, named moves.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
