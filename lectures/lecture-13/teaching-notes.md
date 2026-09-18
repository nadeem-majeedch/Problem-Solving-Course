# Teaching Notes — Lecture 13

*Instructor only - not rendered on the public site.*

## Board plan

- Left: the three-structure menu: list (order), dict (about-what), set (presence).
- Middle: the tally pattern written once - get-or-zero, add one - reused all hour.
- Right: the roster questions mapped to set operations BEFORE any code.

## Questions to ask students

- Why is `tally.get(w, 0) + 1` the whole counting idea in one line?
- What does the dictionary give us that a list of counts could not - and vice versa?
- Which set operation answers 'who takes exactly one course'? (Symmetric difference - or two subtractions.)

## Alternative explanations

- Students who know dicts already: give them the inverted index challenge (word -> list of positions).
- Structure-shy students: run the same tally with two parallel lists first, then show the dict version.

## Expected student difficulties

- KeyError on missing keys - make `get` with default the reflex.
- Believing dict iteration order is sorted - it is insertion order (state the version caveat).

## Connections to neighbouring lectures

The tally pattern formalises L9's count-if; next: functions package these patterns for reuse (L14).

## Quiz answer key

**A1.** When is a dictionary the right structure rather than a list?
- *Expected:* When you look up by key/name, not by position.

**A2.** What does tally.get(w, 0) do?
- *Expected:* Returns the count if the word exists, else 0 - the get-or-zero idiom.

**A3.** Which set operation answers 'in both rosters'?
- *Expected:* Intersection.

**A4.** What is the cost of `x in some_list` vs `x in some_set`?
- *Expected:* List: O(n) scan; set: O(1) average.

**B1.** Tally 'mississippi': give the dictionary and the two most frequent letters with a tie rule.
- *What earns marks:* m1 i4 s4 p2; tie i/s at 4 -> alphabetical first = i (state the rule).

**B2.** CS = {ada, bo}, DS = {bo, cy}: express and compute 'exactly one course'.
- *What earns marks:* Symmetric difference = (CS-DS) union (DS-CS) = {ada, cy}.

## Exit ticket - expected answers

1. When do you choose a dictionary over a list?
   - *Expected:* when lookup is by meaningful key, not position

2. What single operation do sets make O(1)-ish and lists O(n)?
   - *Expected:* membership testing (in)

3. Restate the consensus rule of cs-052 precisely.
   - *Expected:* a decision passes only when agreement count meets the quorum threshold
