# Lecture Notes — Lecture 20: Brute Force Workshop

Companion to the lecture plan and the worked examples. Read the *Definitions* before
class, the *Explanation* after it; the practice questions and the lecture quiz close the loop.

## Definitions

- **Brute force** — enumerate the candidate space directly; correct by construction, fast only when the space is small.
- **Candidate space** — the set of possibilities the enumeration walks; its size is the real cost.
- **Counting first** — size the space with arithmetic BEFORE writing enumeration code.
- **Constraint propagation** — apply constraints during generation, not after, so dead branches die early.
- **Exhaustive search** — brute force over combinations/subsets; 2^n is the wall that motivates smarter design.

## Explanation

**Count before you enumerate.** 10^4 PINs is seconds; 2^30 subsets is years. The workshop's rule: arithmetic first, code second. The cost curve is plotted from real timings.

**Brute force is the correctness oracle.** For every clever algorithm in Blocks III-IV, a brute-force version checks it on small inputs. 'Slow but surely right' is an asset, not an embarrassment.

**Prune early, pray less.** Applying constraints during generation (skip a PIN whose partial sum already exceeds 12) cuts whole subtrees. The difference between generate-then-filter and generate-with-constraints is measured live.

**Structure the space.** Enumerating triples as nested loops is fine when the depth is small and fixed; recursion (lecture 22) generalises it. Today's workshop stays nested.

**Worst case vs typical case.** Subset-sum brute force is 2^n worst case but often finds an answer early; average-case thinking is introduced here and formalised much later.

## Examples

The lecture's worked examples live in [examples.md](examples.md); the case studies this
lecture builds on are worked in class from the projector. The case sequence with difficulties:
- [cs-077](../../case-studies/student/cs-077.md) (Beginner)
- [cs-078](../../case-studies/student/cs-078.md) (Foundational)
- [cs-079](../../case-studies/student/cs-079.md) (Intermediate)
- [cs-080](../../case-studies/student/cs-080.md) (Advanced)

## Common misconceptions

- Writing enumeration code before counting the space.
- Filtering after full generation when constraints could prune during generation.
- Assuming brute force is always too slow - at classroom scale it is the oracle.
- Confusing permutations (order matters) with combinations (it does not).

## Summary and key takeaways

1. Count the space with arithmetic before writing any enumeration.
2. Brute force is the correctness oracle for everything fancier.
3. Prune during generation, not after.
4. 2^n is the wall; the next blocks teach the doors around it.

## Practice questions

- Count 4-digit PINs with digit sum exactly 12 by arithmetic; then enumerate and compare the counts.
- List perfect numbers below 10000 with the sqrt divisor bound; time it against the naive scan.
- Enumerate all subsets of a 4-item list by hand; verify there are 16 and none is missed.
- Generate meeting triples from availability masks with constraints applied during generation; compare the candidate count.

## Where this leads

Next lecture: **Binary Search Everywhere**. The quiz below checks this lecture's essentials before we build on them.
