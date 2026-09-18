# Lecture Notes — Lecture 02: Pseudocode as Precision

Companion to the lecture plan and the worked examples. Read the *Definitions* before
class, the *Explanation* after it; the practice questions and the lecture quiz close the loop.

## Definitions

- **Pseudocode** — a structured half-way language between English and code: precise enough to trace, free of syntax detail.
- **Statement** — one pseudocode line doing exactly one job (read, assign, decide, repeat, output).
- **SEQUENCE** — statements executed one after another, top to bottom.
- **Selection** — IF/ELSE - choose between two continuations based on a condition.
- **Iteration** — WHILE (repeat while a condition holds) and FOR (repeat once per item or count).
- **State** — the set of variable values a program holds at one moment.
- **Invariant (informal)** — a fact that stays true every time you reach a marked point in a loop.
- **Hand-trace** — executing pseudocode with pencil and paper, tracking every variable in a table.

## Explanation

**Why not just Python?** Syntax is noise when you are learning to think. Pseudocode keeps only the reasoning: sequence, selection, iteration, state. Block I-II work is required in pseudocode first for exactly this reason.

**The course grammar.** READ / WRITE for input-output; `x <- expression` for assignment; IF/ELSE for selection; WHILE and FOR for iteration. One statement per line, one job per statement. This grammar is small on purpose - it fits on an index card and in your head.

**Precision levels.** 'Check the password' (vague) → 'check length is 8-12, then first char is a letter, then at least one digit' (precise) → 'on failure, name the FIRST rule broken' (testable). Push every statement down one level before coding.

**State and assignment.** Assignment `c <- c + 1` is not algebra; it is an order: compute the right side with current values, then store. Traces make this visible.

**Order of tests matters.** Validation must report the first failing rule, so the tests must be ordered deliberately. Writing the tests in a random order produces messages that contradict the spec.

## Examples

The lecture's worked examples live in [examples.md](examples.md); the case studies this
lecture builds on are worked in class from the projector. The case sequence with difficulties:
- [cs-005](../../case-studies/student/cs-005.md) (Beginner)
- [cs-006](../../case-studies/student/cs-006.md) (Foundational)
- [cs-007](../../case-studies/student/cs-007.md) (Intermediate)
- [cs-008](../../case-studies/student/cs-008.md) (Expert)

## Common misconceptions

- Pseudocode that is Python with the punctuation removed - no abstraction gained.
- One line doing three jobs ('read and validate and loop') - untraceable by design.
- Assignment read as equality: 'c <- c + 1' is an order, not a claim.
- Tests written in a random order, producing messages that contradict the spec.

## Summary and key takeaways

1. One statement, one job; trace before you trust.
2. Assignment is an order, not an equation.
3. Order the validation tests; report the first failure.
4. Pseudocode is a contract another human can execute.

## Practice questions

- Write pseudocode to prompt until a valid 8-character student ID is entered; trace it on 'a1b2' and 'a1b2c3d4'.
- Hand-trace your largest-of-three pseudocode on (7, 7, 3). Which branch does the tie take?
- Express 'no two consecutive tracks by the same artist' as one precise sentence plus one IF.
- Write the password validator's tests in the correct order; explain what breaks if two are swapped.

## Where this leads

Next lecture: **Flowcharts and Control Flow**. The quiz below checks this lecture's essentials before we build on them.
