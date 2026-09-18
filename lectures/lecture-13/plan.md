# Lecture 13 — Dictionaries and Sets

## Position in the course

This is lecture 13 of 32. It belongs to the course arc described in the
[course outline](../../docs/course-outline.md) and uses the standard
interactive case method: display, attempt (5 minutes), discuss, reveal,
name the technique.

## Learning objectives

- Model lookups as key-value mappings
- Use sets for uniqueness and membership
- Count with dictionaries idiomatically

By the end of this lecture students can do all three under time pressure,
which is what the four cases exercise.

## Prerequisite knowledge

**Before this lecture:** Lectures 09 and 11 — Aggregation and lists

Assumed fluencies:

- building totals and counts
- keys as labels (informal intuition is enough)

**Preparation task:** Tally the words of one paragraph on paper, twice, faster.

## Detailed topic outline

Core (mandatory):

1. dictionaries as label → value maps
2. counting and grouping patterns
3. sets and membership
4. set operations on rosters

Extension (optional enrichment):

5. caches and last-seen maps
6. voting and consensus logic

## Case sequence

| Case | Title | Difficulty |
| --- | --- | --- |
| cs-049 | The Word Tally | Beginner |
| cs-050 | Course Rosters | Foundational |
| cs-051 | The Cache Simulator | Intermediate |
| cs-132 | The Silent Roster | Intermediate |
| cs-052 | The Consensus Checker | Expert |

Display each case full-screen from the student page (cases cs-049–cs-052);
instructor pages cs-049–cs-052 under `case-studies/instructor/` hold the
full solutions, reveal guides, and discussion prompts. Applied additions cs-132 extend the session as optional extra attempts or homework;
they share the lecture's theme but teach an applied, real-world angle.

## Timing plan (120 minutes)

| Minutes | Segment |
| --- | --- |
| 0–10 | Framing: where this fits; recall of the previous lecture |
| 10–30 | Case 1 (cs-049): 5-minute attempt, then discussion and reveal |
| 30–50 | Case 2 (cs-050): same rhythm |
| 50–70 | Case 3 (cs-051): same rhythm, harder case |
| 70–75 | Break |
| 75–100 | Case 4 (cs-052): same rhythm, hardest case |
| 100–115 | Synthesis: name the techniques; misconceptions check |
| 115–120 | Exit questions, homework, next-lecture preview |

Timing flexes with the room: if a case ignites the class, let the
discussion run and compress the synthesis; if the attempts stall,
harvest partial attempts rather than extending the clock.

## Worked examples

- cs-052 consensus checker: a logic table over agreement counts before any code is written.

**Instructor demonstration to open the lecture:** Build the word tally (cs-049) as a living table: one student reads words, one updates the map, one audits.

## Classroom activities

| # | Activity | Minutes | Format and prompt |
| --- | --- | --- | --- |
| 1 | Human dictionary | 6 | Words are read aloud; three students act as key, value, and updater of a living tally. |
| 2 | Venn stations | 7 | Roster operations (union, intersection, difference) are performed with name cards at three stations. |
| 3 | Consensus debate | 6 | cs-052's agreement rule is debated: majority, unanimity, or quorum — what does each hide? |

## Board plan

- Left third: the case statement, kept visible for the whole cycle.
- Middle third: students' contrasting attempts (two maximum).
- Right third: the reference trace or table, revealed last.
- Bottom strip, written during the cycle: the name of the technique and
  the one-line invariant or rule this case taught.

## Instructor explanation notes

**Reading the room.** Dictionaries are introduced as 'lists with meaningful indices' — counting is the bridge. Sets arrive through roster questions where duplication is the enemy.

**Running the reveal.** The consensus case (cs-052) is a logic lecture in disguise; the table before the code is the whole lesson.

**Lecture focus.** One sentence to repeat verbatim: *Choose the structure that answers the question directly.*

## Common misconceptions

- Using a list of pairs where dictionary lookup is the actual question.
- Forgetting that set membership ignores duplicates — by design.
- Writing if-chains that a single dictionary operation would replace.
- Building consensus logic ad hoc instead of tabulating the rule first.

Each case's instructor page lists the specific wrong turn to expect; the reveal should address it by name.

## Student practice exercises

Core:

1. Tally the words of a provided paragraph with a dictionary; print the top three by count.
2. Compute roster intersections and differences for cs-050's three course lists.
3. Build the agreement table for cs-052's four reviewers and decide the verdict.

Enrichment (optional):

- Add a cache eviction rule to cs-051 and defend its fairness.
- Model cs-052 with sets instead of counts; where does it break?

## Formative assessment

**Exit questions (choose one; answer on a card in 60 seconds):**

1. When do you choose a dictionary over a list?
   *Expected: when lookup is by meaningful key, not position*

2. What single operation do sets make O(1)-ish and lists O(n)?
   *Expected: membership testing (in)*

3. Restate the consensus rule of cs-052 precisely.
   *Expected: a decision passes only when agreement count meets the quorum threshold*

Cards are skimmed before the next lecture; three answers become the
framing. Persistent wrong answers route students to the review
stations of lecture 16 or to office hours.

## Homework and preparation

- Before: skim the four student pages; attempt case 1 on paper.
- After: write a five-line pseudocode solution for any case you did not
  finish in class; bring one question to the next lecture.
- Enrichment (optional): the stretch question on each case page.

## Learning-outcome mapping

- **Primary outcomes:** LO4, LO9 — Dictionaries and sets as data structures for real data.
- Coverage details: [learning outcomes](../../docs/learning-outcomes.md);
  assessed via the scheduled quizzes, labs, assignments, and term
  project in the [assessment plan](../../docs/assessment-plan.md).

## Differentiation

- Beginners: aim for a correct *plan* in pseudocode; Python is optional.
- Intermediate: full Python on cases 1–3, plan on case 4.
- Advanced students: finish early, then answer "what breaks at 10x scale?"
  and present the alternative-approach bullet from the instructor page.
- Everyone: state one assumption out loud before writing anything.
