# Teaching Notes — Lecture 18

*Instructor only - not rendered on the public site.*

## Board plan

- Left: three sort intuitions as pictures: select (pick smallest), insert (slot in), merge (zip winners).
- Middle: the two-key sort on the leaderboard: negated score, then name.
- Right: the merge step of cs-070 traced with two fingers.

## Questions to ask students

- Why does the merge step never need to re-compare an element it has passed?
- What does 'stable' buy us in the two-pass sorting trick?
- Where does O(n log n) come from intuitively - what is log n here?

## Alternative explanations

- Card-sorting demo: have students physically sort and reverse-engineer their algorithm.
- Advanced: argue why comparison sorts cannot beat n log n (decision-tree sketch).

## Expected student difficulties

- Hand-rolled sorts with subtle bugs - prefer built-ins plus keys in practice; hand-rolls for insight only.
- Key confusion: sorting tuples by second element needs the key function, not indexing tricks.

## Connections to neighbouring lectures

Sorted data is the precondition that unlocks halving (L21); pair scans over sorted arrays come next (L19).

## Quiz answer key

**A1.** What does 'stable sort' preserve?
- *Expected:* The relative order of equal keys.

**A2.** Give the two-key sort for 'score desc, name asc'.
- *Expected:* key = (-score, name).

**A3.** What is the merge step's guarantee?
- *Expected:* Each output element is the smallest remaining front - no re-comparisons needed.

**A4.** Roughly why is sorting O(n log n)?
- *Expected:* Halving structure: log n levels of n-ish work (or: n picks into a shrinking heap).

**B1.** Rank ada 90, bo 75, cy 90 (ties alphabetical).
- *What earns marks:* ada, cy, bo.

**B2.** Merge [9, 10, 12] with [9.5, 11]: list the comparisons.
- *What earns marks:* 9<=9.5 take 9; 10>9.5 take 9.5; 10<=11 take 10; 12>11 take 11; leftover 12.

## Exit ticket - expected answers

1. What does sorting buy for interval merging?
   - *Expected:* overlaps become adjacent; one sweep suffices

2. Why must the leaderboard sort be stable or fully keyed?
   - *Expected:* ties must resolve deterministically or the order is arbitrary

3. What does the kth-element question really ask?
   - *Expected:* selection, not full sorting — sorting is the simple correct baseline
