# Pedagogical Review of the Case-Study Collection

**Scope:** all 128 case studies (cs-001 – cs-128) · reviewed September 2026 ·
findings and fixes below. Case IDs were preserved throughout; nothing was
deleted or merged — the collection already met the 100-case minimum with room
to spare, so the work was quality, not quantity.

## Method

Four audits were run over the whole collection, then targeted deep reads:

1. **Distribution audit** — tier vectors per block and per lecture computed
   from case metadata (not from plans, which can drift).
2. **Duplicate detection** — pairwise similarity of problem statements using
   distinctive-token overlap (a token counts only if it appears in ≤ 6 of the
   128 problems, which filters the shared house phrasing).
3. **Deep read of all 12 Expert cases** — prerequisites, clarity, algorithmic
   correctness, explainability, and justification of the tier.
4. **Machine verification** — every instructor reference program executed
   (twice, for determinism) and compared against the case's own
   "Expected result" prose; every student-side deliverable sentence checked
   against what its case actually asks.

## 1. Difficulty distribution

| Block | Beginner | Foundational | Intermediate | Advanced | Expert |
| --- | --- | --- | --- | --- | --- |
| I · Lectures 01–08 | 8 | 8 | 8 | 6 | 2 |
| II · Lectures 09–16 | 8 | 8 | 8 | 6 | 2 |
| III · Lectures 17–24 | 8 | 8 | 8 | 4 | 4 |
| IV · Lectures 25–32 | 8 | 8 | 8 | 4 | 4 |
| **Total** | **32** | **32** | **32** | **20** | **12** |

Every lecture carries exactly one case of each of the three lower tiers, so
the first minutes of every session are accessible to first-semester students
while the last case stretches advanced ones. Advanced and Expert cases are
concentrated in Blocks III–IV (algorithms, data science, strategy), which
matches the curriculum: early blocks need computing mechanics, later blocks
can assume them. **Verdict: the classification is justified and progressive;
no re-tiering was needed.**

## 2. Duplicate review

The tightest clusters found, and why each is a *designed family*, not a
duplicate:

- **cs-041/042/043/044 (slicing, lecture 11)** — reorder, deduplicate,
  rotate, and the aliasing trap: four different tasks sharing one lecture
  theme. cs-044 inverts the others (explain a bug, not build a feature).
- **cs-081/082/083/084 (binary search, lecture 21)** — game, boundary find,
  search-on-answer, and monotone-predicate generalisation: a deliberate
  escalation ladder within one technique.
- **cs-093/094/095/096 (graphs, lecture 24)** — model-first, BFS with
  distances, cycle detection, multi-source BFS: each adds exactly one new
  idea to the previous one.

The detector found **zero pairs** whose problem statements share more than a
third of their distinctive vocabulary outside these designed families. No
merges were necessary. The overlap that the detector *did* flag inside the
families turned out to be something else entirely — see finding F3.

## 3. Expert cases (deep read)

The 12 Expert cases all pass the tier test: each either demands integrated
reasoning across multiple earlier lectures (cs-052 fairness-from-data,
cs-056 function contracts as design, cs-084 binary search on an abstract
predicate, cs-088 the recursion→DP bridge), or requires clarifying genuinely
ambiguous requirements before anything can be computed (cs-004's waiver
rule, cs-100's weighting choice, cs-104's streak definition, cs-116's
estimator design, cs-120's constraint search with honest failure). Each has
a verified reference program, at least one named alternative approach, a
complexity statement, and an extension challenge. Prerequisites stated in
metadata were spot-checked against the lectures they cite — all valid.

## 4. Findings and fixes applied

**F1 — Worked-instance prose did not match the verified demo output
(24 cases).** The instructor "Expected result." line narrated *rules* or
*bug descriptions* instead of the demo's actual outcome, and a few hedged
with draft markers ("wait - trace carefully"). All 24 lines were rewritten
from the **executed** program output (e.g. cs-109 now states the demo prints
`{'mean': 527000.0, 'median': 30000.0}` and why both matter). Verified by
re-running the whole bank: 0 warnings remain.

**F2 — Content defects behind the prose (3 cases, substantive):**
- **cs-023** — instructor page claimed row 3 of the star pattern was `**..`;
  the actual code produces `***..`. Instructor text corrected; the student
  page (which was right) is unchanged.
- **cs-045** — the student page claimed the buggy median returns **2** for
  `[1, 2, 3, 4]`; the buggy code returns **3** (element at index `len//2`).
  Example fixed in both pages; demo line now prints `buggy 3 fixed 2.5`.
- **cs-071** — the stated closest pair was **wrong**: (3.1, 4.0) is 0.9
  apart, but (9.2, 9.9) is 0.7 apart. Both pages now state the correct pair;
  the mistake is even pedagogically useful (it shows why you sort before
  scanning), so the corrected text says so.

**F3 — Deliverable sentences graded the wrong skill (24 cases).** A
per-lecture house frame ("Your deliverable is…") was copied verbatim into
every case of a lecture, and for 24 of them it described a different task
than the case poses — e.g. cs-042 (three deduplication strategies) was
graded on "slice arithmetic", the number-theory cases of lecture 05 on a
decision-model frame, the greedy/DP cases of lecture 23 on "recurrence and
memoisation", and the data-ethics cases of lectures 25–31 on a generic
frame. Every affected case now has a deliverable sentence written for *its
own* task (cs-089: "the greedy choice justified with an exchange argument…";
cs-107: "the matching rule made precise, and one borderline pair with your
verdict"). Lecture frames that genuinely fit (tracing, testing, debugging,
searching, simulation) were left untouched.

**F4 — Title typos (3 cases, all references updated):** cs-096 "The epidemic
Alarm" → "The Epidemic Alarm", cs-091 "The Tollerance Ladder" → "The
Tolerance Ladder", cs-121 "The umbrella Decision" → "The Umbrella Decision"
(student page, instructor page, catalog, lecture plans, facilitation map).

**F5 — cs-115 premise contradiction (substantive).** The student page said
guess-all EV "= 0 exactly" under +1/−0.25 marking — arithmetic that its own
demo contradicted (EV = ¼(+1) + ¾(−0.25) = **+0.0625**). Corrected: blind
guessing is mildly *positive* under this marking; the true break-even
penalty is 1/3; the discussion now turns on why exam boards choose −0.25.

## 5. Instructor usability

Every case structurally supports the classroom cycle, and this is now
**validator-enforced**, not aspirational: the student page carries the
problem, worked example, hints, and a discussion starter; the instructor
page carries the five-minute teaching sequence, the scripted moment of
revealing the solution, alternative approaches, and an extension challenge —
and `validate.py` fails without them.
The solution programs are executable, so an instructor can run the demo
live; with this pass, the stated expected results finally match what the
projector shows.

## 6. Before → after

| Measure | Before | After |
| --- | --- | --- |
| Case count (student/instructor) | 128 / 128 | 128 / 128 (unchanged) |
| Worked-instance ↔ demo mismatches | 24 | **0** |
| Content errors in examples | 3 (cs-023, cs-045, cs-071) + cs-115 premise | **0** |
| Misfitting deliverable sentences | 24 | **0** |
| Title typos | 3 | **0** |
| Validator warnings | 24 | **0** |
| Duplicates merged | — | 0 (none found) |
| Case IDs changed | — | 0 |

Re-verify at any time with `python scripts/qa_report.py`.
