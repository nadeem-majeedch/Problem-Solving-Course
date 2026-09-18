# Teaching Notes — Lecture 22

*Instructor only - not rendered on the public site.*

## Board plan

- Left: digit-sum recursion as a staircase of calls unwinding.
- Middle: power-by-halving: exponent path 13 -> 6 -> 3 -> 1 -> 0 drawn as a chain.
- Right: the ways(n) call tree, with repeated subproblems circled in red.

## Questions to ask students

- Where is the base case in each - and what proves the recursion reaches it?
- Why does power-by-halving have NO repeated subproblems, but ways(n) has many?
- What exactly does memoisation cache - and what is its lookup key?

## Alternative explanations

- Stack-shy students: draw the call stack as plates between frames.
- Advanced: convert ways(n) to a bottom-up two-variable loop - the DP preview.

## Expected student difficulties

- Infinite recursion from a missing base case - show the traceback, read it aloud.
- Believing recursion is 'slower' in principle - compare costs per problem, not per paradigm.

## Connections to neighbouring lectures

Repeated subproblems motivate memoisation and DP (L23); the halving pattern is L21's on recursion's stage.

## Quiz answer key

**A1.** What two parts must every recursive function have?
- *Expected:* Base case and recursive case.

**A2.** What proves a recursion terminates?
- *Expected:* Each call moves strictly toward the base case (a shrinking argument).

**A3.** Why is power-by-halving O(log n)?
- *Expected:* The exponent halves each call - a chain, not a tree.

**A4.** What are overlapping subproblems?
- *Expected:* The same smaller case recomputed many times (ways(3) in the stairs tree).

**B1.** Trace dsum(49206): calls and unwind.
- *What earns marks:* dsum(49206)=6+dsum(4920)=...=6+0+2+9+4=21.

**B2.** ways(8) = ? and what does memoisation change (conceptually)?
- *What earns marks:* 34; caches each ways(k) - recomputation disappears, cost O(n).

## Exit ticket - expected answers

1. What grounds a recursion?
   - *Expected:* a base case reachable for every input path

2. When does a table beat the tree?
   - *Expected:* when subproblems repeat — overlapping subproblems

3. What did cs-087 buy with halving?
   - *Expected:* multiplications dropped from ~13 to ~5 — logarithmic vs linear
