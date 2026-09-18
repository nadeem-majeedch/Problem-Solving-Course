# Teaching Notes — Lecture 20

*Instructor only - not rendered on the public site.*

## Board plan

- Left: 'count before you code': the candidate-space arithmetic for each case (10^4, 2^n).
- Middle: the lock enumeration running live with a progress counter.
- Right: brute force as proof: the empty-sweep conclusion is a theorem.

## Questions to ask students

- How many candidates for n = 30 subsets - and what does that number forbid?
- Which is more trustworthy: the counting argument or the enumeration - and why agree?
- What is the smallest input where brute force becomes unusable here?

## Alternative explanations

- Counting-averse students: let them enumerate 3-dial locks, then extrapolate the formula.
- Advanced: meet-in-the-middle sketch as the escape hatch from 2^n.

## Expected student difficulties

- Writing brute force for spaces they never counted - mandate the count line first.
- Forgetting the empty subset in subset enumeration - decide its legality explicitly.

## Connections to neighbouring lectures

Brute force sets the baseline costs that divide-and-conquer and DP will attack (L22-L23).

## Quiz answer key

**A1.** Why count the candidate space before coding?
- *Expected:* To know the cost (10^4 fine, 2^30 impossible) and pick the right tool.

**A2.** What does an empty enumeration sweep prove?
- *Expected:* No solution exists - brute force as theorem.

**A3.** How many subsets does a 30-element set have?
- *Expected:* 2^30, about a billion.

**A4.** What must you decide about the empty subset before enumerating?
- *Expected:* Whether it counts as a solution (e.g. sum 0) - a policy, stated.

**B1.** Write the count-line for the 4-digit lock (sum 12) and the exact answer.
- *What earns marks:* Candidates 0000-9999 (10^4); answer 415 codes.

**B2.** Enumerate subsets of [3, 5, 2] for target 8: which mask wins with first-found exit?
- *What earns marks:* {3,5} (mask 0b011) - early exit stops before {8}-style later hits.

## Exit ticket - expected answers

1. How big is the subset space of 25 items, roughly?
   - *Expected:* 2^25 ≈ 33 million — borderline; count before you loop

2. What makes pruning sound?
   - *Expected:* it only removes branches that cannot contain a better answer

3. When is brute force the right deliverable?
   - *Expected:* tiny spaces, correctness baselines, and verifying clever answers
