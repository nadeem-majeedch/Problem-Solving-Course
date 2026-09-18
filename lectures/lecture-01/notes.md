# Lecture Notes — Lecture 01: Thinking in Problems

Companion to the lecture plan and the worked examples. Read the *Definitions* before
class, the *Explanation* after it; the practice questions and the lecture quiz close the loop.

## Definitions

- **Problem** — a goal plus obstacles: what is wanted, and what stands between the given information and that goal.
- **Specification** — a restatement of a problem so that two careful readers would produce the same answer for every input.
- **Input** — the information a solution is allowed to use. Everything not listed as input does not exist.
- **Output** — the exact form of the answer required (a number, a decision, a list) - agreed before solving.
- **Constraint** — a limit the solution must respect (time, memory, money, legal rules).
- **Assumption** — a statement you accept without proof to make the problem solvable; always written down.
- **Edge case** — an input at the boundary of the rules (zero, empty, maximum, exactly-at-a-limit).
- **Decomposition** — splitting a problem into smaller subproblems whose answers combine into the full answer.

## Explanation

**Problems before programs.** Every wrong program in this course traces back to a misread problem. The lecture trains four questions: What exactly is the input? What exactly must come out? What limits bind us? What are we assuming without proof?

**Ambiguity is normal.** Real requirements are written by humans and arrive ambiguous ('every 6th drink free'). Professionals do not guess silently: they surface the two readings, pick one, and write the assumption down. A stated assumption is a correct answer; a hidden one is a future bug.

**Decomposition as a tree.** Split the problem until each leaf is small enough to solve with one rule. Example: 'canteen bill' splits into read items, price each, apply discount, print - and the discount leaf splits again into 'which discount applies' and 'how much'.

**Same data, different models.** The elevator case can count 'stops' or count 'floors travelled'; both are defensible models, and the answer differs. Choosing the model is a problem-solving act, not arithmetic.

**From beginner to advanced.** Beginners learn to spot missing information. Advanced students practise *quantifying* the effect of an assumption: 'if we count the free drink as earning a stamp, the answer drops from 20 paid to 18.'

## Examples

The lecture's worked examples live in [examples.md](examples.md); the case studies this
lecture builds on are worked in class from the projector. The case sequence with difficulties:
- [cs-001](../../case-studies/student/cs-001.md) (Beginner)
- [cs-002](../../case-studies/student/cs-002.md) (Foundational)
- [cs-003](../../case-studies/student/cs-003.md) (Intermediate)
- [cs-004](../../case-studies/student/cs-004.md) (Expert)

## Common misconceptions

- Reading the problem once and starting to write - the spec phase is the solution.
- Treating assumptions as facts: 'of course returns include the due date' - says who?
- Confusing an example with a definition (one worked instance does not define the rule).
- Choosing a model silently, then defending the arithmetic instead of the model.

## Summary and key takeaways

1. Four questions before any attempt: input, output, constraints, assumptions.
2. Ambiguity is resolved by *stated* assumptions, never by silent guesses.
3. Decompose until each leaf is one rule.
4. The five-minute attempt produces the class's evidence; the reveal answers it.

## Practice questions

- Decompose 'the campus printing service charges per page' into a subproblem tree; mark every assumption.
- The rule says 'every 6th drink free'. Write the two defensible readings and the answer each gives for 13 drinks at 2.50.
- For the library fine policy, list every input class for which the fine is zero.
- A rule says 'large orders ship free'. State three questions you must ask before this rule is computable.

## Where this leads

Next lecture: **Pseudocode as Precision**. The quiz below checks this lecture's essentials before we build on them.
