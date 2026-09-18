# Lecture Notes — Lecture 14: Functions with Purpose

Companion to the lecture plan and the worked examples. Read the *Definitions* before
class, the *Explanation* after it; the practice questions and the lecture quiz close the loop.

## Definitions

- **Function** — a named, parameterised piece of computation with one job and (ideally) one return type.
- **Parameter** — a placeholder named in the definition; the argument fills it at call time.
- **Return value** — the single object handed back to the caller; a function without return yields None.
- **Contract** — what a function needs from its inputs and promises about its output, written in one sentence (its docstring).
- **Refactoring** — restructuring code without changing behaviour - verified by running the same tests before and after.
- **Pure helper** — a function that computes and returns, printing nothing - the building block of testable pipelines.

## Explanation

**Functions are nouns for computation.** Naming a computation (parse_score, average_of) lets you reason about it, test it, and compose it without holding its body in your head.

**The contract sentence.** Every function gets one line: needs / does / returns. If you cannot write it, the function does not yet have one job - split it.

**Pure helpers make pipelines.** Functions that only return values can be chained and tested independently; printing inside helpers breaks both. The pipeline case shows text flowing through clean -> tokenise -> count.

**Refactoring is behaviour-preserving surgery.** The rule: tests first (green), restructure, tests again (still green). The monolith-to-functions case is done live under this discipline.

**Return, do not print.** A printing function returns None and cannot be composed. The rule of thumb taught: helpers return; the main script prints.

## Examples

The lecture's worked examples live in [examples.md](examples.md); the case studies this
lecture builds on are worked in class from the projector. The case sequence with difficulties:
- [cs-053](../../case-studies/student/cs-053.md) (Beginner)
- [cs-054](../../case-studies/student/cs-054.md) (Foundational)
- [cs-055](../../case-studies/student/cs-055.md) (Intermediate)
- [cs-056](../../case-studies/student/cs-056.md) (Expert)

## Common misconceptions

- Functions that print instead of return - untestable and uncomposable.
- One function doing parse + compute + print - the monolith, admired as 'efficient'.
- Passing and then mutating the argument when the caller needed the original intact.
- Contracts written after the code, if at all - the contract is the design.

## Summary and key takeaways

1. One function, one job, one sentence contract.
2. Helpers return values; the main script prints.
3. Refactor under test: green, restructure, green.
4. Pipelines emerge from pure helpers chaining output to input.

## Practice questions

- Write the one-sentence contract for a function that normalises a name (strip, lowercase); implement it.
- Refactor a provided monolith that averages scores into parse / compute / report functions; keep the output identical.
- Turn a printing helper into a returning one and show the pipeline call it now enables.
- Write a function docstring that would let another student call your function without reading its body.

## Where this leads

Next lecture: **Counting, Combinatorics, and Choice**. The quiz below checks this lecture's essentials before we build on them.
