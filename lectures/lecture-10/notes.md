# Lecture Notes — Lecture 10: Strings Under the Lens

Companion to the lecture plan and the worked examples. Read the *Definitions* before
class, the *Explanation* after it; the practice questions and the lecture quiz close the loop.

## Definitions

- **String** — an immutable sequence of characters; every 'change' builds a new string.
- **Indexing** — s[0] is the first character; s[-1] the last; out-of-range is an error.
- **Slicing** — s[a:b] is characters a..b-1; the end is exclusive; s[::-1] reverses.
- **Normalisation** — putting strings into a canonical form (case, spacing, order) before comparison.
- **Parsing** — turning one structured string into pieces (split on separators, strip noise).
- **Character class** — a test like isdigit/isalpha/isspace applied per character.
- **Palindrome** — reads the same forwards and backwards after normalisation.

## Explanation

**Immutable means rebuild.** s.upper() does not change s; it returns a new string. Building output = accumulate in a list, join at the end (cs-039's template fill).

**Normalise before you compare.** cs-040: 'Dormitory' vs 'dirty room!' agree only after lowercasing, removing non-letters, and sorting characters. The ladder: case → strip noise → order. Skipping a rung gives wrong answers that look like logic bugs.

**Slices as positional thought.** cs-038's reversal family: s[::-1] reverses; word reversal needs split → reverse each → join. Each is one line *because* the problem is positional, not conditional.

**Parse, don't crawl.** cs-039 uses {name} placeholders and split/strip; hand-managed index arithmetic is where string bugs live. Rule: if you are counting characters by hand, look for a split/join formulation first.

**Classify per character.** cs-037's username audit is a per-character classifier plus an adjacency rule ('no two underscores in a row' - track the *previous* character). State that carries one character of history is a streak pattern from lecture 9 in disguise.

## Examples

The lecture's worked examples live in [examples.md](examples.md); the case studies this
lecture builds on are worked in class from the projector. The case sequence with difficulties:
- [cs-037](../../case-studies/student/cs-037.md) (Beginner)
- [cs-038](../../case-studies/student/cs-038.md) (Foundational)
- [cs-039](../../case-studies/student/cs-039.md) (Intermediate)
- [cs-040](../../case-studies/student/cs-040.md) (Advanced)

## Common misconceptions

- Comparing strings before normalising case and spaces.
- Trying to mutate strings in place - immutability surprise.
- Off-by-one in slices: the end boundary is exclusive.
- Parsing with hand-managed indexes when split/join states the intent.

## Summary and key takeaways

1. Normalise (case, noise, order) before any comparison.
2. Strings are immutable: build new ones, accumulate-then-join.
3. Prefer split/join over hand-managed indexes.
4. One character of history (previous char) powers adjacency rules.

## Practice questions

- Normalise 'Dormitory' and 'dirty room!' to a comparable form; state each ladder rung you applied.
- Reverse the words of 'the quick brown fox' without reversing the letters.
- Fill the template 'Dear {name}, ...' where the record lacks 'item' - what should print? (cs-039 family)
- Write the adjacency rule for usernames (no '__') using one variable of history.

## Where this leads

Next lecture: **Lists and Slicing**. The quiz below checks this lecture's essentials before we build on them.
