# Lecture 24 — Graphs as Models

## Position in the course

This is lecture 24 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

## Learning objectives

- Model problems as graphs (nodes, edges)
- Represent graphs with adjacency lists
- Perform breadth-first search and explain levels

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** Lectures 13 and 17 — dictionaries and scans

Assumed fluencies:

- adjacency intuition
- queues as FIFO lists

**Preparation task:** Draw your close friends as a 'knows' map; count connection hops to a classmate.

## Detailed topic outline

Core (mandatory):

1. graphs as relationships made explicit
2. vertices, edges, degree
3. BFS: levels are distances
4. topological order for dependencies

Extension (optional enrichment):

5. modelling choices: what becomes a node
6. BFS simulation on infection timelines

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-093 | The Friend Circle | Beginner |
| cs-094 | The Campus Walk | Foundational |
| cs-095 | The Prerequisite Chain | Intermediate |
| cs-096 | The Epidemic Alarm | Advanced |
| cs-136 | The Timetable Collision | Advanced |

Display each case full-screen from the student page (cases cs-093–cs-096);
instructor pages cs-093–cs-096 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts. Applied additions cs-136 extend the session as optional extra attempts or homework;
they share the lecture's theme but teach an applied, real-world angle.

## Timing plan (120 minutes)

| Minutes | Segment |
| --- | --- |
| 0–10 | Framing: where this fits; recall of the previous lecture |
| 10–30 | Case 1 (cs-093): 5-minute attempt, then discussion and reveal |
| 30–50 | Case 2 (cs-094): same rhythm |
| 50–70 | Case 3 (cs-095): same rhythm, harder case |
| 70–75 | Break |
| 75–100 | Case 4 (cs-096): same rhythm, hardest case |
| 100–115 | Synthesis: name the techniques; misconceptions check |
| 115–120 | Exit questions, homework, next-lecture preview |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-096 epidemic alarm: model days as levels, run BFS on a 6-node contact graph, and derive the quarantine day from level numbers.

**Instructor demonstration to open the lecture:** Friend circle (cs-093) mapped from the room itself: each student names two acquaintances; BFS colours the components live.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Campus graph build | 8 | Rooms and corridors become a graph on the board; shortest paths argued before BFS runs. |
| 2 | BFS wave simulation | 7 | Students as nodes; rumours spread in waves; each wave number is a distance. |
| 3 | Cycle or order | 5 | cs-095's dependency map checked for cycles by hand; the vote precedes the algorithm. |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** Graphs are sold as the honest model of relationships, not as a new data structure to memorise. Modelling choices (what is a node?) get more airtime than BFS code.

**Running the reveal.** cs-096 ties simulation and BFS together; it is the Block III synthesis and the direct bridge to Block IV's simulation lecture.

**Lecture focus.** One sentence to repeat verbatim: *Model relationships explicitly; levels are distances.*

## Common misconceptions

- Modelling meetings as nodes or people as edges — modelling is the skill.
- Reading BFS visit order as if it were distance.
- Hunting shortest paths where a topological order is the question.
- Forgetting that any cycle invalidates a prerequisite ordering.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. Model cs-093's friend data as an adjacency map; count components by BFS by hand.
2. Compute the BFS levels for cs-094's campus map from the library.
3. Check cs-095's prerequisite map for a cycle; produce a valid order if none exists.

Enrichment (optional):

- Model the campus as weighted edges and discuss what BFS no longer answers.
- Design a contact-tracing privacy policy for cs-096's data; defend it.

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. What is a node in the campus model, and why?
   *Expected: junctions/rooms — decisions and meetings happen there*

2. What does BFS level number mean?
   *Expected: minimum number of steps from the source*

3. When is there no valid ordering in cs-095?
   *Expected: exactly when the prerequisite graph has a cycle*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO10, LO4 — Graph modelling and BFS; simulation integrated.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
