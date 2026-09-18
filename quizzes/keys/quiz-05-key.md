# Quiz 5 — Answer Key (instructor only)

Not for publication. Marking notes in *italics*.

## Q1. Multiplication principle (4)

(a) *(2)* 3 × 4 × 5 = 60 meals.

(b) *(2)* Unordered pairs of different desserts: C(5,2) = 10; meals:
3 × 4 × 10 = 120. *The question's hint says unordered — ordered pairs
(5×4 = 20, giving 240) earns 1 of 2 with the note "order of choosing
desserts is not a distinction". Common error: 5 + 4 = 9 (adding instead
of multiplying for the pair).*

## Q2. Not-found behaviour (4)

(a) *(2)* The function returns `None` (Python's implicit fall-through
return). *Accept "nothing / None / undefined"; the mark is for knowing
it is implicit, not designed.*

(b) *(2)* A deliberate not-found value (e.g. `return -1` documented, or
`raise ValueError`) lets the caller branch on absence; the implicit
`None` flows silently into arithmetic — e.g. `found + 1` raises
`TypeError` far from the actual bug site, or `xs[None]` crashes with an
error pointing at the *caller*, not the finder. *(One concrete
caller-side failure is the mark; "it's bad practice" alone is not.)*

## Q3. Sort keys (5)

(a) *(2)* `sorted(records, key=lambda r: (-r[1], r[0]))`
*(accept the equivalent tuple-key form; accept `reverse=True` variants
only if ties are still name-ascending — most such answers break the
tie rule, which is (b)'s point).*

(b) *(2)* `-marks` turns descending-by-marks into ascending order under
the default sort, so one ascending sort serves both criteria; the name
must stay un-negated (strings have no negation) because its natural
alphabetical order *is* the required A-before-B tie order. *The mark is
for "negation encodes descending for numbers; strings rely on their
natural order".*

(c) *(1)* `[("cy", 91), ("ann", 82), ("bo", 82)]`
*(ann before bo on the tie — the rule working as stated).*

## Q4. Two pointers (6)

(a) *(3)* On `[1, 3, 4, 6, 8]`, target 10:

| step | lo val | hi val | sum | comparison | move |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | 8 | 9 | 9 < 10 | lo right |
| 2 | 3 | 8 | 11 | 11 > 10 | hi left |
| 3 | 3 | 6 | 9 | 9 < 10 | lo right |
| 4 | 4 | 6 | 10 | equal | found |

*(1 mark for a correct sequence of sums/moves, 1 for the found row, 1
for a table with no arithmetic slips. The found pair is (4, 6).)*

(b) *(3)* Invariant: at every step, the answer pair — if it exists —
lies within `[lo, hi]`; the current endpoints cannot both be in any
valid pair (their sum is too small ⇒ lo's only possible partner is
larger, already excluded by being inside the window... precisely: if
sum < target, no pair using lo can reach the target since hi is the
largest remaining; if sum > target, no pair using hi can, since lo is
the smallest remaining), so discarding an endpoint never discards the
answer. *(Full marks for a sentence that justifies ONE of the two
discards correctly; 2 marks for naming the invariant without the
justification; 1 for "the window always contains the answer" alone.)*

*Note for the mark book: quiz-05's Q4 is a preview of lecture 19
material — mark generously and treat the invariant as stretch; the
header note in the quiz says the same.*

Grade boundaries suggestion: 15–20 excellent · 10–14 good · 7–9
satisfactory · below 7 revisit lectures 15–18.
