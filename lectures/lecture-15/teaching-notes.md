# Teaching Notes — Lecture 15

*Instructor only - not rendered on the public site.*

## Board plan

- Left: scope diagram: outer box (globals), inner boxes (call frames) with arrows for lookups.
- Middle: the mutable-default bug: three calls, ONE list drawn shared between them.
- Right: pass-by-object-reference: a variable as a sticky note on an object.

## Questions to ask students

- When the default list is created - at call time or definition time? What follows?
- Why does assigning inside a function NOT change the caller's variable, but appending does?
- What is the standard fix for the mutable default, and why None specifically?

## Alternative explanations

- Diagram-first: every aliasing/scope question answered by drawing boxes and notes before words.
- Advanced: show `is` vs `==` to distinguish identity from equality in the shared-list demo.

## Expected student difficulties

- The mutable default works in the first test - regression tests (L8) are what catch it later.
- Confusing reassignment with mutation - the sticky-note picture settles most arguments.

## Connections to neighbouring lectures

Counting without code next (L16's consolidation prepares the combinatorics week); the sentinel default returns as a design pattern.

## Quiz answer key

**A1.** When is a mutable default argument created?
- *Expected:* Once, at definition time - shared by all calls.

**A2.** What is the standard fix?
- *Expected:* Default None; create a fresh list inside when None.

**A3.** Reassigning a parameter vs mutating it: which does the caller see?
- *Expected:* Only mutation (append etc.); reassignment rebinds the local name.

**A4.** `is` vs `==`: what does each test?
- *Expected:* Identity (same object) vs equality (same value).

**B1.** Fix def add_tag(tag, tags=[]) and explain in one sentence.
- *What earns marks:* tags=None sentinel, fresh list inside - because the default list is created once and shared.

**B2.** Predict the output: def f(x, acc=[]): acc.append(x); return acc - called f(1), f(2).
- *What earns marks:* First call [1]; second [1,2] (shared default) - then state the fix.

## Exit ticket - expected answers

1. When is the complement trick the right tool?
   - *Expected:* when counting the desired set directly is tangled but its opposite is simple

2. Permutations vs combinations in one phrase each.
   - *Expected:* order matters / order does not

3. How does simulation back up counting?
   - *Expected:* many random trials approximate the counted probability
