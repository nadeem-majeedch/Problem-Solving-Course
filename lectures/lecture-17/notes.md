# Lecture Notes — Lecture 17: Searching and Linear Scans

Companion to the lecture plan and the worked examples. Read the *Definitions* before
class, the *Explanation* after it; the practice questions and the lecture quiz close the loop.

## Definitions

- **Linear scan** — visit items one by one until the target or the end; O(n) always, but works on ANY sequence.
- **Early exit** — stop scanning the moment the answer is known - found it, or proved nothing ahead can match.
- **Sentinel value** — a reserved answer (-1, None) meaning 'not found'; must be impossible to confuse with a real result.
- **Filter** — a scan that collects all matches instead of the first - the accumulator list applied to search.
- **Precondition** — a promise about the input (e.g. 'sorted', 'two runs') that a faster method may rely on.
- **Best/worst case** — the same algorithm has a cost range; the target's position decides which you get.

## Explanation

**Scan first, cleverness later.** A linear scan is always available, always correct, and the baseline every faster method must beat. Students who can write a clean scan can debug anything fancier.

**Early exit is a correctness question too.** Stopping early must be justified: found the first match (scanning order guarantees it), or a monotone property proves nothing ahead can match. Unjustified exits are bugs.

**Sentinels are contracts.** Returning -1 for 'not found' collides with real data unless the spec forbids negatives; returning None is safer in Python. The class debates which convention the spec should pin.

**Preconditions unlock speed.** The two-sorted-halves case: knowing the structure, the minimum sits at the run boundary - check two candidates instead of n. The scan still exists as the fallback when the promise fails.

**Counting the cost.** Best case 1 step, worst n, average n/2 for a found target. On 10^6 items that is real time; on 10 it is irrelevant - students learn when the distinction matters.

## Examples

The lecture's worked examples live in [examples.md](examples.md); the case studies this
lecture builds on are worked in class from the projector. The case sequence with difficulties:
- [cs-065](../../case-studies/student/cs-065.md) (Beginner)
- [cs-066](../../case-studies/student/cs-066.md) (Foundational)
- [cs-067](../../case-studies/student/cs-067.md) (Intermediate)
- [cs-068](../../case-studies/student/cs-068.md) (Expert)

## Common misconceptions

- Returning the loop index 0 as 'not found' - zero is a legitimate position; use None or -1 by spec.
- Breaking early without justification on multi-match scans.
- Assuming linear scan is 'the dumb way' - on unsorted data it is the ONLY way.
- Confusing best case with typical case when reasoning about cost.

## Summary and key takeaways

1. Scan is the baseline; speed requires a precondition you can verify.
2. Early exit needs a reason: found-first or proof-nothing-ahead.
3. Sentinel answers are contracts written in the spec.
4. Best/worst case is a range; know which matters at your input size.

## Practice questions

- Write a scan returning the first index of a target, or None; justify your early exit in one sentence.
- Filter a course list by two predicates and count matches; state the order you applied them and whether it matters.
- For the two-sorted-halves input, find the minimum with at most two comparisons; state the precondition you used.
- Find a peak in a list by comparing neighbours safely at the edges; explain why a peak always exists.

## Where this leads

Next lecture: **Sorting as an Idea**. The quiz below checks this lecture's essentials before we build on them.
