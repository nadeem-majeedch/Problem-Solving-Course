# Lecture Notes — Lecture 13: Dictionaries and Sets

Companion to the lecture plan and the worked examples. Read the *Definitions* before
class, the *Explanation* after it; the practice questions and the lecture quiz close the loop.

## Definitions

- **Dictionary** — a collection of key -> value pairs; you look things up by key, not by position
- **Key uniqueness** — each key appears at most once; assigning to an existing key overwrites its value
- **Set** — an unordered collection with no duplicates; membership tests are fast
- **Set operations** — union (in either), intersection (in both), difference (in one but not the other)
- **Membership test** — asking 'is x present?' - the `in` operator, O(1) average on dict/set
- **Accumulator pattern** — initialise a structure before a loop and grow it inside the loop

## Explanation

Lists answer 'in what order?'; dictionaries answer 'about what?'. A dictionary maps keys to values, so 'how many times did the appear?' is one lookup instead of a scan. Building a tally is the canonical first use: walk the items, add one to each key's slot, starting from zero for newcomers. Sets are the sibling structure for presence questions: who is in both courses, who is in exactly one. The set operations (union, intersection, difference) are the questions themselves - naming the operation IS the solution. The advanced step is choosing the structure on purpose: lists preserve order and allow duplicates; dictionaries preserve insertion order and give fast lookup by key; sets give fast membership and deduplicate. The same tally written over a list of words becomes quadratic if you count with list scans - the structure choice is the complexity choice. By the end you should ask, for every accumulation task: am I counting (dictionary), membership-testing (set), or sequencing (list)?

## Examples

The lecture's worked examples live in [examples.md](examples.md); the case studies this
lecture builds on are worked in class from the projector. The case sequence with difficulties:
- [cs-049](../../case-studies/student/cs-049.md) (Beginner)
- [cs-050](../../case-studies/student/cs-050.md) (Foundational)
- [cs-051](../../case-studies/student/cs-051.md) (Intermediate)
- [cs-052](../../case-studies/student/cs-052.md) (Expert)

## Common misconceptions

- 'A dictionary is just a fancy list' - it answers different questions: lookup by key, not position.
- Assuming keys are sorted or ordered by insertion in every language - only some languages guarantee it.
- Using `dict[key]` to read a possibly-missing key - use `get` or `in` first; crashes are not policies.
- Confusing set union with list concatenation - union deduplicates, concatenation does not.
- Believing `in` on a list is as fast as `in` on a set - the list scan is O(n); the set hash is O(1) average.

## Summary and key takeaways

1. Dictionaries count, sets test membership, lists order - choose the structure that matches the question.
2. The tally pattern (get-or-zero, add one) solves most first-pass data problems.
3. Set operations ARE the questions: union = either, intersection = both, difference = only.
4. Structure choice is complexity choice: list scans are O(n); dict/set lookups are O(1) average.
5. State what happens for a missing key before writing the lookup.

## Practice questions

- Tally the letters of 'mississippi' with a dictionary; print the two most frequent with a stated tie rule.
- Two course rosters as sets: who takes both, exactly one, neither? State each as a set operation first.
- Rewrite a list-based membership check as a set; explain when the rewrite is pointless (n tiny).
- Enrichment: invert a dictionary (value -> list of keys) and discuss when two values collide.
- Enrichment: implement a tiny phone book with add, lookup, and delete; define the missing-key behaviour.

## Where this leads

Next lecture: **Functions with Purpose**. The quiz below checks this lecture's essentials before we build on them.
