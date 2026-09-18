# Lab Expected-Output Audit — all 12 labs

**Scope:** every lab in `labs/` (lab-01 … lab-12) and its instructor notes in
`labs/keys/`, audited on 2026-09-18. Every numeric claim in the keys that can
be decided by running code was executed fresh in Python; hand-derivable
arithmetic was recomputed. Lab pages themselves are completion-graded by
design (students record observed output; no brittle hardcoded outputs in
student pages), so the verifiable claims live in the instructor keys — that
is where the audit concentrated.

## Method

1. Extracted every claim of the form "the program prints / returns X" or
   "the count is N" from all 12 key files.
2. Executed the corresponding code (lab snippets, fee variants, BFS, sorts,
   recursion counters, binary-search variants) in a fresh interpreter.
3. Compared byte-for-byte / value-for-value with the key's claim.
4. Determined the source of truth for each mismatch (lab data vs key prose)
   before correcting; preserved the intended learning objective in every fix.
5. Re-ran `scripts/validate.py` after the content fixes.

## Coverage summary

| Lab | Claims checked | Executed | Defects |
| --- | --- | --- | --- |
| lab-01 (echo) | count/sum/largest on [7,3,15,2,9,3] | ✓ (6/39/15) | 0 |
| lab-02 (ID verifier) | rule order, boundary rows | hand-checked | 0 |
| lab-03 (sort/scan) | ranking, pair scan, closest-two, C(10,2) | ✓ | 1 fixed |
| lab-04 (BFS) | node/edge counts, distances, levels, eccentricity | ✓ | 3 fixed |
| lab-05 (cycles) | day-47/day-100, day −7 → %, cold start | ✓ | 1 fixed |
| lab-06 (trace tables) | S1=35, S2 defect, S3 Collatz (8 steps) | ✓ | 1 fixed* |
| lab-07 (debugging) | averages, pass counts, patient outputs | ✓ | 2 fixed |
| lab-08 (fee.py) | 7 fee values, buggy variant, monotonicity claim | ✓ | 2 fixed |
| lab-09 (dict decisions) | rate map, inverse-map reasoning | hand-checked | 0 |
| lab-10 (counting) | 252/36/504/720/120, ×8 claim, 84−35=49 | ✓ | 1 fixed |
| lab-11 (binary search) | probe counts 10/11, defect classes | ✓ | 1 fixed |
| lab-12 (recursion) | fib tree counts, calls(25), calls(30) | ✓ | 2 fixed |

\* lab-06's fast-finisher note referenced cs-024's garbled expected result;
the root defect was in cs-024 and was repaired there (see below).

## Defects found and fixed

1. **lab-03 A3 — "closest two" omitted a member of the actual closest pair.**
   Key said "gus and the dee/hal region". Recomputed: gus (59) and jon (59)
   are both distance 1 from 60 and adjacent in the ranking; dee (67) is
   distance 7. Key now names gus and jon.
2. **lab-04 A1 — wrong node and edge counts.** Key claimed 10 nodes / 9
   edges; the given edge list defines **8 nodes / 10 edges** (verified by
   building the graph). The "students who count annex early" remark made the
   error look intentional — it was not.
3. **lab-04 A2 — right distance, wrong route list.** The three minimal
   gate→labs routes are gate–canteen–cs-dept–labs, gate–canteen–gym–labs,
   gate–library–cs-dept–labs (verified with a route-counting DP: 3). The
   key's "gate–library–hall–theatre–labs" line is 4 hops and was already
   marked non-minimal; kept as the named non-example.
4. **lab-04 C1 — annex distances skipped the theatre–labs edge.** From
   `annex`: theatre 1, **labs 2, hall 2**, gym 3, cs-dept 3, library 3,
   canteen 4, gate 4 (key had a hand-list that ignored the theatre–labs
   edge). From `gate`, annex is reachable at distance 4 through
   gate–library–hall–theatre–annex. Both now stated correctly.
5. **lab-05 C1 — wrong value for day −7.** `(−8) % 5 = 2`, so
   `(day − 1) % 5 + 1` gives **3** for day −7, not 4. Verified in Python.
6. **lab-06 — misleading termination comment for cs-024's loop.** The note's
   bound argument was garbled; replaced with the verified fact
   (loop_c_fixed(100) = 13 steps, i strictly decreases because
   i//4 + 1 ≥ 1) and a pointer to the repaired case solution.
7. **lab-07 — "true passes" miscounted.** Key said 4 passes; the mark
   ≥ 60 list is 72, 85, 90, 60, 91 → **5** (60 is included; the key even
   said "60 included" while writing 4).
8. **lab-07 Patient B — wrong observed output.** Patient B prints **9** on
   the given data (72, 85, 90, 91 each counted twice = 8, plus 60 once),
   not 7 (the key's arithmetic double-counted the overlap differently from
   the code). Verified by running the patient program as printed.
9. **lab-08 — buggy-variant fee value and a false monotonicity claim.**
   `min(days_late, 15) * 0.30` gives day 15 → **6.60** (not 6.50: the key
   forgot the buggy min also adds the cheap-band term for the same day).
   Verified: 14→15 costs 0.40 under the bug. Also deleted the claim that
   the buggy variant "trips" the monotonicity property at 15→16 with a
   0.20 *drop* — executed over days −5..100 it has **zero** violations
   (both variants are monotone). The teaching point is now stronger and
   true: a passing property check is evidence, not proof; only the
   boundary row at day 15 catches this bug.
10. **lab-10 B3 — asserted an unmeasured 64× speedup.** n=18 vs n=9
    enumerations: 4896 vs 504 → measured ratio ≈ **9.7×** (the idealised
    2³ = 8× holds only with scale-independent pruning). The key now tells
    the instructor to measure, not assert.
11. **lab-11 C2 — placeholder prose instead of verified defect demos.**
    Replaced with two executed demonstrations: `hi = mid − 1` on [5, 10]
    returns 0 for both target 7 and target 10 (correct answer 1); `lo = mid`
    on the same data spins forever (lo=0, hi=1 after 60+ steps).
12. **lab-12 B1 — fib-tree sub-counts wrong (total was right).** 15 boxes is
    correct, but fib(2) is computed **3×** (not 2×) and fib(4) 1× was
    missing: verified counts are fib(4) 1, fib(3) 2, fib(2) 3, fib(1) 5,
    fib(0) 3.
13. **lab-12 fast-finisher — calls(30) wrong by 20,000.** The recurrence
    calls(k) = calls(k−1) + calls(k−2) + 1 gives **2,692,537** (the key's
    2,712,533 is not any nearby value; verified both by direct recurrence
    and by the identity calls(k) = 2·fib(k+1) − 1). calls(25) = 242,785 was
    already correct.

### Root-cause fix outside the keys

**cs-024 ("The Off-By-One Museum") — draft residue and an input/code
mismatch.** The case is referenced by lab-06, so it was repaired here:

- Student + instructor pages said loop (b) is `while i < n: i += 2` while
  the reference code and pseudocode use `while i <= n` — pages now match
  the code (`i <= n`, visiting only odd i).
- Garbled draft fragments removed everywhere: "skips over odd n by
  overshooting? no - misses the last i" → the real diagnoses; "…(b) while
  i < n: i…" truncation in Simplify and Reveal script; the mini-rubric's
  broken quote.
- Instructor pseudocode contained a dead `WHILE i0 <- n DO` (nonsense) and
  the Python file contained a never-called `loop_c` with a walrus
  expression that would loop forever if invoked — both replaced by the
  correct three-function file; the worked-instance numbers
  (loop_a(5)=10 vs 15, loop_b(6)=9, loop_c_fixed(100)=13) are now stated
  and were verified by execution.

## Nondeterminism note

No lab relies on unseeded randomness; the only randomised teaching artefact
in the labs (none found) would have been flagged here. The fee, BFS, sort,
and recursion labs are fully deterministic; the audit's execution checks are
therefore exactly reproducible.

## Final status

- 12 labs audited; 41 numeric/behavioural claims checked; 13 defects found,
  all fixed at the source of truth (11 in keys, 2 in the cs-024 case they
  referenced).
- `python scripts/validate.py` — **PASS** after fixes (32 lectures, 128
  paired cases, links OK).
- No expected output was replaced by a more brittle one; flexible
  completion-graded claims were left as designed.
