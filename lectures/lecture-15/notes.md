# Lecture Notes — Lecture 15: Counting, Combinatorics, and Choice

Companion to the lecture plan and the worked examples. Read the *Definitions* before
class, the *Explanation* after it; the practice questions and the lecture quiz close the loop.

## Definitions

- **Factorial** — n! = n x (n-1) x ... x 1; the number of ways to arrange n items in order
- **Permutation** — an ordered selection; order matters, so AB and BA are different
- **Combination** — an unordered selection; order does not matter, so AB and BA are the same
- **Complement counting** — count the opposite of what you want, then subtract from the total
- **Pigeonhole principle** — if more than n items go into n boxes, some box holds two
- **Binomial coefficient** — C(n, k) = n! / (k! (n-k)!); the number of k-sized teams from n people

## Explanation

Counting is problem solving without code. Start with the multiplication principle: if a task has stages with a and b choices, the whole task has a x b outcomes - outfits, PINs, routes. Factorials count arrangements: 5 students in a line, 5! = 120. Divide by the duplicated order when order should not matter: choosing 4 committee members from 10 is C(10,4) = 210, not 10 x 9 x 8 x 7, because each team was counted 4! times. Two habits carry the lecture: complement counting (count the forbidden, subtract from the total - usually far fewer cases) and the pigeonhole principle (with 13 students and 12 months, some month holds two birthdays). The advanced move is counting with constraints: glue the two students who refuse to separate, then count blocks. Every formula should be re-derived on a tiny case (n = 3) you can check by hand - formulas you cannot verify on paper you cannot trust in code.

## Examples

The lecture's worked examples live in [examples.md](examples.md); the case studies this
lecture builds on are worked in class from the projector. The case sequence with difficulties:
- [cs-057](../../case-studies/student/cs-057.md) (Beginner)
- [cs-058](../../case-studies/student/cs-058.md) (Foundational)
- [cs-059](../../case-studies/student/cs-059.md) (Intermediate)
- [cs-060](../../case-studies/student/cs-060.md) (Advanced)

## Common misconceptions

- Multiplying when you should add: 'and' stages multiply, 'or' cases add.
- C(10,4) computed as 10x9x8x7 - the order of a chosen team was counted 4! times.
- Applying complement counting with overlapping cases - subtraction needs disjoint sets.
- Believing the pigeonhole principle needs large numbers - 3 socks, 2 colours is already enough.
- Treating 'at least one' as hard - complement often converts it into one subtraction.

## Summary and key takeaways

1. Stages multiply, cases add - and 'at least one' often falls to complement counting.
2. C(n, k) divides out the order that should not matter; permute only when order is real.
3. Verify every formula on n = 3 by hand before trusting it at scale.
4. Pigeonhole needs no code: 13 students, 12 months, someone shares.
5. Constraints reshape counts - glue the pair that must stay together.

## Practice questions

- How many 5-character codes from 26 letters (repeats allowed)? Then without repeats. Which formula, and why?
- A committee of 3 from 4 CS and 5 DS students must include at least one of each: complement-count it.
- Glue-count: 6 friends, two refuse to separate - acceptable lineups?
- Enrichment: pigeonhole - show some 3-digit set from 100 numbers must contain two summing to a multiple of 9 (or find the right modulus).
- Enrichment: derive C(n,1) = n and C(n,n) = 1 from the formula, then explain why both make sense.

## Where this leads

Next lecture: **Review and Mini Challenge**. The quiz below checks this lecture's essentials before we build on them.
