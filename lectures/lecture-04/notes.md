# Lecture Notes — Lecture 04: First Python: State and Sequences

Companion to the lecture plan and the worked examples. Read the *Definitions* before
class, the *Explanation* after it; the practice questions and the lecture quiz close the loop.

## Definitions

- **Variable** — a name bound to a value; reassignment re-binds the name, it does not change history.
- **Expression** — a piece of Python that produces a value (`2 + 3 * 4`, `len(name)`).
- **Statement** — an instruction (`x = 5`, `print(x)`) - note the difference from an expression.
- **Type** — the kind of value: int, float, str (text), bool. `"3" + 4` fails because types disagree.
- **Type conversion** — `int(...)`, `float(...)`, `str(...)` translate between kinds; `int("3.5")` fails.
- **List** — an ordered, changeable sequence: `scores = [8, 6, 9]`; positions start at 0.
- **Index** — the position of an item; `scores[0]` is the first; the last of n items is at n-1.
- **input()** — always returns a string; convert before arithmetic.

## Explanation

**Python as executable pseudocode.** The course grammar maps line to line: READ → `input()`, WRITE → `print()`, `x <- 5` → `x = 5`, IF/ELSE and WHILE look nearly the same. New this week is only the punctuation.

**State, names, and order.** Python runs top to bottom; using a name before assignment is an error, not zero. Reassignment `x = x + 1` is the pseudocode `x <- x + 1` exactly.

**Types are safety rails.** `input()` gives strings; `"3" * 4` is `'3333'`, not 12. Convert deliberately: `int(...)`, `float(...)`. When something odd happens, the first question is 'what type is this really?'

**Lists as sequences.** Positions start at 0; `len()` counts; `for item in lst` visits every element. The last valid index is `len(lst) - 1` - remember this number, lecture 6 will show you every way to get it wrong.

**First debugging tool.** `print()` between lines is the honest first debugger: show the state you assumed, compare with reality. (The editor's debugger arrives in the lab.)

## Examples

The lecture's worked examples live in [examples.md](examples.md); the case studies this
lecture builds on are worked in class from the projector. The case sequence with difficulties:
- [cs-013](../../case-studies/student/cs-013.md) (Beginner)
- [cs-014](../../case-studies/student/cs-014.md) (Foundational)
- [cs-015](../../case-studies/student/cs-015.md) (Intermediate)
- [cs-016](../../case-studies/student/cs-016.md) (Advanced)

## Common misconceptions

- Adding a number to a string ('3' + 4) - types must agree, so convert first.
- Forgetting input() returns strings and 'multiplying' text by accident.
- Off-by-one on the last element (index n of an n-length list).
- Using a variable before any assignment and expecting zero.

## Summary and key takeaways

1. Predict, then run, then check - never just run.
2. input() gives strings; convert before arithmetic.
3. Lists start at index 0; the last index is len-1.
4. print() the state you assumed; compare with the state you got.

## Practice questions

- Write a program that reads three numbers and prints their average, rounded to one decimal.
- Read numbers until 0 and print the count of negatives and the sum of positives.
- Given scores = [8, 6, 9, 7], predict print(scores[1], scores[-1], len(scores)) - then run it.
- Break the echo program with the nastiest legal input you can construct; explain the failure precisely.

## Where this leads

Next lecture: **Numbers, Remainders, and Cycles**. The quiz below checks this lecture's essentials before we build on them.
