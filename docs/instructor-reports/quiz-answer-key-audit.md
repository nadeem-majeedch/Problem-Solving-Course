# Quiz Answer-Key Audit — all 8 quizzes

**Scope:** every question in `quizzes/quiz-01.md` … `quizzes/quiz-08.md` against
its key in `quizzes/keys/`, verified by hand-checking and by executing every
code block. Audit date: 2026-09-18. Case IDs, tiers, and question numbering
were preserved; fixes were corrections only.

## Method

For each quiz: (1) every question re-answered independently before looking at
the key; (2) every code/output question executed fresh in Python (traces and
outputs compared byte-for-byte with the key's claims); (3) numeric claims
recomputed (arithmetic, probability, combinatorics); (4) multiple-choice
options checked for duplicate-correct and for plausible-but-wrong distractors;
(5) complexity claims cross-checked against the algorithm actually described.

## Coverage

| Quiz | Questions | Code executed | Numeric claims recomputed | Verdict |
| --- | --- | --- | --- | --- |
| quiz-01 (L01–04) | 5 | trace `8 2` ✓ | 108-arithmetic ✓ | PASS |
| quiz-02 (L05–08) | 5 | Collatz trace `1` ✓ | day-140 boundary ✓ | PASS |
| quiz-03 (L09–12) | 5 | `abc 1` ✓, tally ✓ | boundary table ✓ | PASS |
| quiz-04 (L13–16) | 5 | `second_largest` on 4 inputs ✓ | aliasing trace ✓ | PASS |
| quiz-05 (L17–18) | 5 | factorial loop ✓ | sort-key outputs ✓ | PASS |
| quiz-06 (L19–22) | 4 | recursion base-case ✓ | cross-half inversions ✓ | **1 defect fixed** |
| quiz-07 (L23–24) | 5 | — | mean 250 ✓, ruin 2/5 ✓, EV +0.75 ✓ | PASS |
| quiz-08 (L25–32) | 5 | — | knapsack/greedy comparison ✓ | **1 defect fixed** |

33 questions audited in total; 9 code blocks executed; every numeric key
claim recomputed independently.

## Defects found and fixed

1. **quiz-06 Q4(a) — key claimed a counterexample that isn't one.**
   The key proposed `[2, 1, 4, 3]` as "the smallest 4-element input" where
   the combine-free inversion count fails, calling its inversions
   "cross-half". Verified: both inversions of `[2, 1, 4, 3]` — (2,1) and
   (4,3) — lie *inside* halves, so the student's missing-combine algorithm
   returns the correct answer on it. The lexicographically smallest exposing
   input is `[1, 3, 2, 4]`: the missed pair is (3, 2) with 3 in the left
   half and 2 in the right. Key corrected; distractor logic preserved.
2. **quiz-08 Q1 — stem self-contradiction.** The question said both
   "fund exactly three events" and "maximise the number of events funded";
   the key worked around the contradiction instead of the question being
   well-posed. Stem corrected to the maximisation reading (which the key
   and marks already assumed); the key's phrase "exactly ≤ 300" repaired.

## Checks that passed everywhere

- No duplicate-correct options in any multiple-choice set; distractors are
  plausible and demonstrably wrong (each traceable to a named misconception).
- Every answer key exists and matches its question numbering 1:1.
- All trace questions re-traced independently (quiz-01 loop, quiz-02
  Collatz, quiz-03 dedupe, quiz-04 aliasing/tally, quiz-05 factorial,
  quiz-06 first-ge interval, quiz-08 greedy run) — all key traces correct.
- Complexity answers correct wherever claimed (O(n) scan vs O(log n)
  search in quiz-05; n log n vs O(k·n) reasoning preserved in quiz-06 Q4).
- Deliberately tricky items (quiz-03's falsy-`""` guard, quiz-06 Q3's
  missing base case) are pedagogically justified and their keys explain
  the trap, not just the answer.

## Post-audit verification

- `python scripts/validate.py` — PASS (quiz files, links, case references).
- `python -m pytest tests/ -q` — all tests pass.
- Public build excludes `quizzes/keys/` (verified by the site audit).
