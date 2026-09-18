# Expert-Tier Rationale — the 12 Expert Cases

**Scope:** all 12 cases whose metadata declares `difficulty | Expert` (derived
from the case pages themselves, not from lecture plans): cs-004, cs-008,
cs-052, cs-056, cs-068, cs-072, cs-084, cs-088, cs-100, cs-104, cs-116,
cs-120. Case IDs were preserved; **no tier was changed** — every rationale
below was checked against the case's own metadata, problem, and verified
reference solution.

Why a rationale document: an Expert case is the most expensive thing in a
lecture pack. It needs prerequisites the instructor can name, ambiguity that
is productive rather than careless, and a reveal that pays for the attempt.
This file records, case by case, why the tier is deserved and what evidence
backs it. Reviewers changing any Expert case should re-derive the matching
row here.

## How to read the entries

Every entry answers the same eleven fields: ID and title · lecture and topic ·
why it is Expert · prior knowledge · ambiguity or complexity · algorithmic or
strategic reasoning · alternative approaches · complexity considerations ·
exact / simulation / search · extension · evidence. All twelve cases share the
common Expert contract (from student metadata): the deliverable is
assumptions + rules + worked-instance decision + one contested case, the
time-box is ~5 minutes for the attack plan with the full argument allowed to
run past it, and a stated assumption is explicitly part of a good answer.

The tier is a claim about *reasoning required*, not about code volume. Most
Expert reference programs are short — that is the point. The difficulty lives
in deciding what the rules are, defending the decisions, and proving the
method sound; the code is transcription.

## Block I — foundations used at Expert level

### cs-004 · The Library Fine Formula · lecture-01 (Thinking in Problems)

- **Why Expert.** The input is deliberately vague policy ("tiered, capped,
  waived") and the solution is the *policy made exact*. Nothing about
  transcription is hard; every mark is earned by decisions — chiefly
  whether the return day itself is charged.
- **Prior knowledge.** The whole Block I–III toolbox, plus proof-shaped
  reasoning: the student page says exactly that in its prerequisites row.
- **Ambiguity/complexity.** "What happens on the return day itself" has no
  answer in the prompt; the deliberate trap is hiding a value judgement
  inside 'obvious' arithmetic.
- **Algorithmic/strategic reasoning.** Turn a story into entities, quantities,
  and a rule list; run the rules on the instance; sanity-check against
  the cap.
- **Alternatives.** Rule-first vs table-first; the hand-filled table doubles
  as the test oracle.
- **Complexity.** Constant — fixed by a defect fix on 2026-09-18; the
  template's "logarithmic" claim was wrong for a closed-form evaluation.
- **Method class.** Exact reasoning (specification), no code needed.
- **Extension.** Re-solve under a second assumption and compare the answers.
- **Evidence.** Reference program prints `0 0.0 / 5 2.5 / 12 7.0 / 40 10.0`
  (validated on 2026-09-18); the case is the lecture's capstone, slot 4.

### cs-008 · Shuffling a Playlist · lecture-02 (Pseudocode as Precision)

- **Why Expert.** The ask is pseudocode precise enough to execute — for a
  *constraint-satisfaction* shuffle (every song once, no two same-artist
  neighbours), where a majority artist may make the constraint unsatisfiable
  and a repair rule must exist.
- **Prior knowledge.** Greedy placement, queues by artist, and the Lecture 02
  precision standard.
- **Ambiguity/complexity.** "Randomness" in the topics row tempts students
  into luck; the real question is what the repair rule is when same-artist
  songs outnumber the gaps.
- **Algorithmic/strategic reasoning.** Round-robin by artist, then fix
  remaining adjacent pairs by reinsertion; the answer is judged on stated
  constraints and repair steps, not on a lucky playlist.
- **Alternatives.** Round-robin by artist vs round-robin by queue length;
  reinsertion vs full rebuild.
- **Complexity.** n log n; the sort of artist queues dominates.
- **Method class.** Exact reasoning (constraint formulation) + a greedy
  construction.
- **Extension.** Express the solution so precisely a classmate can execute it
  without questions.
- **Evidence.** Reference program prints `['A', 'C', 'B', 'E', 'D']` for the
  worked instance (validated on 2026-09-18); the instructor page names the
  unsatisfiable-majority case as the sticky point.

## Block II — data structures at Expert level

### cs-052 · The Consensus Checker · lecture-13 (Dictionaries and Sets)

- **Why Expert.** A three-option Condorcet cycle — A beats B, B beats C,
  C beats A — has no majority winner, so the "obvious" deliverable (find the
  winner) does not exist. Students must discover that pairwise majorities can
  form a circle and say what the data then means.
- **Prior knowledge.** Dictionaries keyed by pairs, counting over ballots,
  and enough comfort with the result being "no winner exists".
- **Ambiguity/complexity.** The cycle detection *is* the ambiguity: the fair
  outcome is a finding, not a bug.
- **Algorithmic/strategic reasoning.** For each pair (X, Y), count ballots
  ranking X above Y; test the three majority inequalities.
- **Alternatives.** Pair-count dict vs tallying per ballot; both are on the
  instructor page.
- **Complexity.** Quadratic in options (constant here, 3 options), linear in
  ballots.
- **Method class.** Exact reasoning (social-choice argument).
- **Extension.** Invert the lookup (value to keys) and state when collisions
  appear.
- **Evidence.** Reference program prints the 2-1/2-1/2-1 cycle and
  `cycle: True True True` (validated on 2026-09-18).

### cs-056 · Pipelines as Functions · lecture-14 (Functions and Reuse)

- **Why Expert.** The case asks students to *invent* contract boundaries —
  which stages exist, what each hands to the next, why no stage prints — and
  to defend one cut line against another. Design, not implementation.
- **Prior knowledge.** Function contracts, return-vs-print discipline from
  the preceding lecture cases.
- **Ambiguity/complexity.** Many valid decompositions; the contested case is
  which function to split or merge, defended by argument.
- **Algorithmic/strategic reasoning.** clean → tokenise → count → report as
  composable stages; composition `report(count(tokenise(clean(t))))` is the
  deliverable.
- **Alternatives.** More, smaller stages vs fewer, richer ones — the
  discussion starter asks which cut line to move.
- **Complexity.** Linear over the text.
- **Method class.** Exact reasoning (design), compositionality.
- **Extension.** Split one function into two and defend the new contract
  boundary.
- **Evidence.** Reference program prints
  `{'the': 2, 'cat': 1, 'dog': 1}` for the worked instance (validated on
  2026-09-18).

## Block III — algorithms at Expert level

### cs-068 · Peak Finding · lecture-17 (Searching and Linear Scans)

- **Why Expert.** The task is easy to *do* and hard to *justify*: "a peak
  always exists" is the expert content — the climb-uphill argument — and the
  deliverable explicitly includes the precondition and not-found behaviour
  (which, given the theorem, must be defined away, not returned).
- **Prior knowledge.** Linear scans and edge handling (treat outside as
  −infinity); enough maturity to distinguish "my loop found one" from "one
  must exist".
- **Ambiguity/complexity.** The not-found case cannot occur, and *saying so
  precisely* is the contested deliverable.
- **Algorithmic/strategic reasoning.** Single pass with safe neighbour
  comparisons; the proof argument for existence.
- **Alternatives.** Linear scan vs divide-and-conquer peak (O(log n)) — added
  to the instructor page's alternatives on 2026-09-18 as named enrichment for
  strong students.
- **Complexity.** Linear for the scan; log n for the divide-and-conquer
  variant.
- **Method class.** Exact reasoning + a correctness argument.
- **Extension.** Re-solve with the divide-and-conquer variant and prove it
  terminates.
- **Evidence.** Reference program prints the peak index for the worked
  instance and the edge cases (validated on 2026-09-18).

### cs-072 · The Kth Element · lecture-18 (Sorting and Pair Scans)

- **Why Expert.** Two algorithms that both answer the question, with a real
  trade-off the student must quantify: sort-then-index (n log n) vs
  repeated-min selection (O(kn)) — and the case names the comparison that
  decides it (n = 10000, k = 3).
- **Prior knowledge.** Sorting as an idea, selection, cost intuition from the
  Block III analysis thread.
- **Ambiguity/complexity.** "Without fully sorting" rules out the easy route
  and forces the trade-off discussion.
- **Algorithmic/strategic reasoning.** Choose the algorithm from the
  parameters, not habit: the right answer *changes with k and n*.
- **Alternatives.** Sort-then-index; repeated-min; (enrichment) partition
  selection — median-of-medians is named in the lecture's advanced thread.
- **Complexity.** n log n vs O(k·n) vs average-linear partition selection.
- **Method class.** Exact reasoning + complexity-based design choice.
- **Extension.** Design the input where repeated-min beats sorting, and the
  one where it loses.
- **Evidence.** Reference program demonstrates the k = 1, k = 3, k = 6
  answers on the worked instance (validated on 2026-09-18).

### cs-084 · The Rotten Timeline · lecture-21 (Binary Search Everywhere)

- **Why Expert.** Binary search generalised to an *abstract monotone
  predicate* ("state at time t is testable"), with the deliverable being the
  predicate, the bound updates, and one full trace — the move from searching
  data to searching answers.
- **Prior knowledge.** Binary search on sorted data (the lecture's earlier
  cases), loop invariants for the half-open interval.
- **Ambiguity/complexity.** The predicate is only "testable", never listed;
  the student must define what a test returns and trust monotonicity.
- **Algorithmic/strategic reasoning.** Maintain the interval that must
  contain the switch; each test halves it; termination on a width-one
  interval.
- **Alternatives.** Linear sweep of the timeline (the obvious fallback) vs
  the halving search — cost argument is part of the reveal.
- **Complexity.** Logarithmic in the window's minutes; the demo's 877 is
  reached in ~10 tests.
- **Method class.** Exact reasoning; search-on-answer.
- **Extension.** Find the switch minute to a tolerance of one second.
- **Evidence.** Reference program prints `877` and `None`
  (validated on 2026-09-18); the all-healthy None path is an explicit
  deliverable.

### cs-088 · The Tower Steps · lecture-22 (Recursion and Divide-and-Conquer)

- **Why Expert.** The canonical bridge to dynamic programming, taught as an
  *argument*: define the subproblem in words, derive
  `ways(n) = ways(n-1) + ways(n-2)`, show the recursion tree recomputing, and
  prove memoisation preserves the answer.
- **Prior knowledge.** Recursion with base cases; enough analysis vocabulary
  to name exponential vs linear cost.
- **Ambiguity/complexity.** Ambiguity is minimal by design — the expert
  content is the derivation chain and the memoisation argument.
- **Algorithmic/strategic reasoning.** Recurrence → recursion tree →
  memoisation → (tabulation as the iteration twin).
- **Alternatives.** Memoised recursion vs bottom-up table; the instructor
  page names both.
- **Complexity.** Exponential without memo, linear with — the demo's
  instant ways(30) = 1346269 is the punchline.
- **Method class.** Exact reasoning; recurrence derivation.
- **Extension.** Generalise to steps of {1, 2, 3} and re-derive.
- **Evidence.** Reference program prints `8 8` (plain = memo) and `1346269`
  (validated on 2026-09-18).

## Block IV — data science and strategy at Expert level

### cs-100 · The Survey Skew · lecture-25 (Thinking with Data)

- **Why Expert.** Two defensible summaries of one dataset: the naive average
  and the population-weighted mean disagree (0.6 vs 0.59), and the expert
  deliverable is the one-sentence statement of what the weighting *assumes* —
  data-science judgement, not arithmetic.
- **Prior knowledge.** Aggregation, mean vs median, and weighting from the
  Block IV data thread.
- **Ambiguity/complexity.** "Fairer" is undefined; segment-wise reporting is
  an explicitly valid alternative answer.
- **Algorithmic/strategic reasoning.** Compute both summaries, then argue
  which population question each answers.
- **Alternatives.** Reweighting vs segmentation — both accepted, and the
  assumption sentence is the graded part.
- **Complexity.** Linear in rows (not the point of the case).
- **Method class.** Exact reasoning on a small dataset; statistical
  reasoning.
- **Extension.** State a dataset where reweighting and segmentation disagree
  in direction.
- **Evidence.** Worked instance numbers (500/300/200 population, 0.6/0.5/0.7
  yes-rates → 0.59 weighted) are given in the instructor page and are hand-
  checkable; no demo print is required by this case's deliverable.

### cs-104 · The Streak Simulation · lecture-26 (Counting and Probability in Data)

- **Why Expert.** Two computation paradigms on one question — exact recursion
  vs Monte Carlo — must agree to about two decimals, and the student must
  explain *why* they differ at all. Comparing an estimator to an exact answer
  is the expert move.
- **Prior knowledge.** Recursion with states, probability framing, seeds and
  spread from Lecture 29's preview.
- **Ambiguity/complexity.** "A streak of 5 somewhere in 20 games" needs the
  event defined precisely (overlapping windows count once).
- **Algorithmic/strategic reasoning.** Exact recursion over game positions
  with current-streak state vs seeded simulation; reconcile the outputs.
- **Alternatives.** Exact-only or simulation-only (each half-credit by the
  rubric); complement counting as a third route.
- **Complexity.** Linear in games for the recursion (fixed on 2026-09-18;
  the template's "quadratic" claim was wrong), linear in trials for the
  simulation.
- **Method class.** Exact + simulation, deliberately combined.
- **Extension.** Compute the expected *first* game index where the streak
  completes.
- **Evidence.** Reference program prints `0.3559 0.3565` (validated on
  2026-09-18) — the two-paradigm agreement is the printed evidence.

### cs-116 · The Buffon Needle · lecture-29 (Simulation as a Way of Knowing)

- **Why Expert.** Simulation as an *estimator of a constant*: the deliverable
  is the error law (shrinking like 1/√n) with the spread across seeds, i.e.
  arguing about the quality of a random answer — a fundamentally different
  skill from producing one.
- **Prior knowledge.** Seeded simulation, aggregation, and basic probability
  framing.
- **Ambiguity/complexity.** Which discrete cousin (quarter-circle points vs
  true needles) is the student's choice, stated as an assumption.
- **Algorithmic/strategic reasoning.** One-trial story → many trials →
  spread across seeds → the 1/√n argument.
- **Alternatives.** Quarter-circle estimator vs Buffon needle; fixed-n vs
  doubling-n designs.
- **Complexity.** Linear in trials; error rate 1/√n (the expert content).
- **Method class.** Simulation with an exact-value comparison.
- **Extension.** Fit the 1/√n line to the three printed sample sizes.
- **Evidence.** Reference program prints `1000 3.128 | 10000 3.126 |
  100000 3.1373` (validated on 2026-09-18).

### cs-120 · The Exam Seating · lecture-30 (Optimization Formulations)

- **Why Expert.** Constraint search with honest failure: state the space
  (choose 6 seats of 16 with adjacency exclusions), prune, count nodes, and
  — the expert move — *report impossible correctly* rather than searching
  forever. Competing objectives are explicit: validity vs measured pruning
  effort.
- **Prior knowledge.** Backtracking with pruning from the lecture's earlier
  cases; combinatorial counting for the space size.
- **Ambiguity/complexity.** The instance could be unsatisfiable; the
  deliverable includes the pruning rule's *measured* effect, so hand-waving
  fails.
- **Algorithmic/strategic reasoning.** Backtracking over seat assignments
  with adjacency pruning; node counting as evidence.
- **Alternatives.** Cell-by-cell placement vs seat-graph independent-set
  formulation (named in the lecture's advanced thread).
- **Complexity.** Exponential in the worst case (fixed on 2026-09-18; the
  template's "linear" claim was wrong) — pruning is what makes it tractable,
  and the node count shows it.
- **Method class.** Search with pruning; exact enumeration.
- **Extension.** Find the smallest grid where the pruning factor exceeds
  100.
- **Evidence.** Reference program prints a valid seating or `impossible`
  with the node count (validated on 2026-09-18).

## Cross-cutting observations

- **Distribution.** The 12 Expert cases sit in slots chosen so every block
  ends with at least one: Block I (cs-004, cs-008), Block II (cs-052,
  cs-056), Block III (cs-068, cs-072, cs-084, cs-088), Block IV (cs-100,
  cs-104, cs-116, cs-120). Lectures 1, 2, 13, 14, 17, 18, 21, 22, 25, 26,
  29, 30 each carry exactly one.
- **Method mix.** Exact reasoning dominates (cs-004, cs-008, cs-052, cs-056,
  cs-068, cs-072, cs-084, cs-088, cs-100), with deliberate exact+simulation
  (cs-104, cs-116) and exact+search (cs-120) pairings — students meet
  every method class at least once at Expert level.
- **No tier was inflated to balance numbers.** The 32/32/32/20/12 vector is
  an outcome of case design, reviewed in `docs/case-review.md`; this file
  only records the justification.

## Verification record

- Expert list derived programmatically from the 128 student pages on
  2026-09-18 (12 found; no hand-built list).
- Every reference program cited above was executed and validated by
  `scripts/validate.py` on 2026-09-18 (0 errors, 0 warnings).
- Three complexity claims in instructor pages were corrected as part of this
  review (cs-004 constant, cs-104 linear, cs-120 exponential); cs-068 gained
  the divide-and-conquer alternative. No other changes were needed — the
  remaining eight cost lines already matched their cases.
