# Lecture Notes — Lecture 12: Debugging Lab: Real Defects

Companion to the lecture plan and the worked examples. Read the *Definitions* before
class, the *Explanation* after it; the practice questions and the lecture quiz close the loop.

## Definitions

- **Regression** — old behaviour breaking again after a change; caught by regression tests.
- **Sentinel value** — a magic input (0, -1, empty) used to mean 'stop' - collides with real data.
- **Default argument** — a parameter's pre-set value; a *mutable* default is created once and shared across calls.
- **Scope defect** — a variable visible where it should not be (counter defined outside a function).
- **History bisect** — finding the change that introduced a defect by testing the middle of the change history, repeatedly.
- **Deletion loop** — removing items while iterating the same list - skips neighbours; iterate over a copy instead.

## Explanation

**Today the defects are adult-sized.** The lecture-7 protocol (reproduce → hypothesise → cheapest experiment → isolate → fix → re-test) now runs on defects that *look* correct: a median that answers correctly on odd-length input (cs-045), a sentinel that eats real zeros (cs-046).

**The median that lies.** cs-045: [1,2,3,4] → buggy 2 (element at len//2), correct 2.5 (average the two middles). The three-case experiment (odd, even, empty) is the whole diagnosis; 'empty: define or reject' is the spec question the defect exposes.

**Sentinels collide with data.** cs-046: readings [0,5,0,7] with 'stop at 0' - the reference prints [] (all eaten) vs the full list without the sentinel rule. Lesson: prefer explicit end markers; if a sentinel is mandated, document the collision.

**Shared defaults are time bombs.** cs-048(b): def add_tag(tag, tags=[]) - the default list is created once; calls accumulate. The reference's ['a','b'] ['a','b'] pair makes the sharing undeniable; fix: default None, create inside.

**Bisect the history.** cs-048's regression zoo: the deletion-loop crash (range(len(xs)) while removing) is found by testing the middle commit, then halving. Four tests pin one culprit among sixteen changes.

## Examples

The lecture's worked examples live in [examples.md](examples.md); the case studies this
lecture builds on are worked in class from the projector. The case sequence with difficulties:
- [cs-045](../../case-studies/student/cs-045.md) (Beginner)
- [cs-046](../../case-studies/student/cs-046.md) (Foundational)
- [cs-047](../../case-studies/student/cs-047.md) (Intermediate)
- [cs-048](../../case-studies/student/cs-048.md) (Advanced)

## Common misconceptions

- Debugging from the bug report alone, without reproducing.
- Bisecting history before isolating a reproducible input.
- Fixing without first writing the failing test.
- Declaring victory because one test passes now.

## Summary and key takeaways

1. Reproduce first; the repro is the acceptance test.
2. Cheapest experiment halves the hypothesis list.
3. Identity (is) vs equality (==) - aliasing bugs die by 'is'.
4. Fix nothing without a failing test written first.

## Practice questions

- Median defect (cs-045 family): write the three-case experiment and the fix; what does 'empty' return and why?
- Sentinel collision (cs-046 family): readings [0,5,0,7] with stop-at-0; propose two honest alternatives to the sentinel.
- Shared default (cs-048 family): trace def add_tag(tag, tags=[]) over three calls; write the fix and the test that catches it.
- Bisect a provided five-commit regression story; log each test and its verdict.

## Where this leads

Next lecture: **Dictionaries and Sets**. The quiz below checks this lecture's essentials before we build on them.
