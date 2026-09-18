# Lecture Notes — Lecture 26: Counting and Probability in Data

Companion to the lecture plan and the worked examples. Read the *Definitions* before
class, the *Explanation* after it; the practice questions and the lecture quiz close the loop.

## Definitions

- **Frequency table** — each distinct value listed with the number of times it occurs
- **Conditional probability** — P(A given B) = the share of B-outcomes where A also happens
- **Independence** — knowing B does not change P(A); the 2x2 table factors cleanly
- **Base rate** — how common a condition is before any evidence; ignoring it misleads
- **Multiplication rule** — P(A and B) = P(A) x P(B given A)
- **Complement rule** — P(not A) = 1 - P(A); often the cheaper route

## Explanation

Counting graduates into probability: same arithmetic, plus a denominator of equally likely or observed outcomes. Frequency tables turn anecdote into arithmetic ('usually under 3 minutes' becomes 7 of 14 days - exactly half, not 'usually'). Conditional probability is the 2x2 table skill: P(mobile given double-click) and P(double-click given mobile) share a numerator and swap denominators - confusing them is the classic base-rate fallacy. Independence is the special case where conditioning changes nothing; its failure is exactly what 'the evidence changed my mind' means, quantified. The complement rule and the multiplication rule do most of the work in exercises; the birthday-style surprises come from multiplying complements (1 - 364/365 x ...). Throughout, we keep the data frame: these are counts from a table, not oracle probabilities - and small samples make every ratio jumpy.

## Examples

The lecture's worked examples live in [examples.md](examples.md); the case studies this
lecture builds on are worked in class from the projector. The case sequence with difficulties:
- [cs-101](../../case-studies/student/cs-101.md) (Beginner)
- [cs-102](../../case-studies/student/cs-102.md) (Foundational)
- [cs-103](../../case-studies/student/cs-103.md) (Intermediate)
- [cs-104](../../case-studies/student/cs-104.md) (Expert)

## Common misconceptions

- Swapping the conditioning: P(A|B) is not P(B|A) - same numerator, different denominator.
- Ignoring base rates: '8 of 10 double-clicks are mobile' says little without mobile's overall share.
- Reading 'usually' off a table without computing the exact fraction - 50% is a coin flip, not a habit.
- Believing independence means 'no relationship in the sample' - it is a model claim, and samples wobble.
- Applying the multiplication rule without the conditional - P(A and B) = P(A) x P(B given A), not P(A) x P(B) unless independent.

## Summary and key takeaways

1. Frequency tables turn adjectives into fractions.
2. P(A given B) and P(B given A) share a numerator and swap denominators - never conflate.
3. Base rates decide how impressive evidence is.
4. Complements multiply into surprises: the birthday result is subtraction-friendly.
5. Independence is a model, not an observation; test it, do not assume it.

## Practice questions

- Build the frequency table for 12 delays; restate 'usually late' as an exact fraction.
- Fill the 2x2 table (mobile x click) from 5 numbers and compute both conditionals.
- Complement-count: P(at least one shared birthday among 5 people) via the falling product.
- Enrichment: show independence in the 2x2 by checking P(A and B) = P(A)P(B) on your table.
- Enrichment: simulate 200 school-days of the bus and compare the empirical under-3 fraction with the table's.

## Where this leads

Next lecture: **Tables, Cleaning, and Anomalies**. The quiz below checks this lecture's essentials before we build on them.
