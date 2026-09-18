# Lab 3 — Checkpoint Notes (instructor only)

Not for publication.

- **A1.** `sorted(students, key=lambda r: (-r[1], r[0]))`. Same technique as
  quiz 5 Q3 — expect it to be quick now.
- **A2.** `key=lambda r: (r[2], -r[1])` — programme ascending, marks
  descending within programme. Watch for students sorting twice without
  understanding why stability makes the two-key sort unnecessary; either
  approach is fine, the checkpoint is the key tuple.
- **A3.** `key=lambda r: abs(r[1] - 60)`. Closest two: gus (59, distance 1) and jon (59, distance 1). The teaching point: keys map records to comparable
  numbers, and "distance from a target" is just another key.
- **B1.** Sorted-adjacent version: comparisons = n − 1 = 9. Pairs within 2
  marks in the ranking: (ann 82, bo 82), (dee 67, eli 74)? no — 7 apart.
  Expected pairs: ann/bo (0), cy/fay (0), eli/hal (0), gus/jon (0), plus
  dee→? dee 67 to eli 74 is 7. So four pairs. *(Accept the pairs found
  correctly rather than memorised — the checkpoint is the scan.)*
- **B2.** Nested loops: C(10,2) = 45 comparisons. The outputs must match;
  if they do not, the adjacent-scan is likely comparing `i` and `i+1`
  inclusively wrong (off-by-one at the last pair).
- **C1.** 45 comparisons on 10 rows.
- **C2.** Sort-then-scan: ~n log n sort + (n − 1) scan. If they instrument
  a real sort, fine; if they estimate, fine — the *stated method* is the
  checkpoint.
- **C3.** At n = 10,000: nested loops ≈ 50,000,000 comparisons; sort-then-
  scan ≈ 10,000 × 13.3 + 9,999 ≈ 143,000. Three orders of magnitude — the
  arithmetic that decides it is n² vs n log n. Students should show the
  arithmetic, not quote it.
- **D1.** After sorting by marks, equal-mark students (ann/bo, cy/fay,
  dee order, eli/hal, gus/jon) keep their data order. Re-sorting by
  programme preserves that relative order within each programme group —
  stability is what makes the two-pass multi-key sort correct.
- **Checkpoint 5.** Common honest answers: A3 (distance key) because "key"
  had to be a *function*, not a field; A2 because two directions had to
  coexist.
- Completion bar: outputs and counts recorded for every part; the C3
  arithmetic present. Early finishers: have them find the smallest dataset
  where the nested-loop version becomes visibly slow (timeit), and report
  the number.
