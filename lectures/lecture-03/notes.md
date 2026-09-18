# Lecture Notes — Lecture 03: Flowcharts and Control Flow

Companion to the lecture plan and the worked examples. Read the *Definitions* before
class, the *Explanation* after it; the practice questions and the lecture quiz close the loop.

## Definitions

- **Flowchart** — a diagram of control flow: processes in rectangles, decisions in diamonds, one start and one end.
- **Process box** — a rectangle: one action or computation.
- **Decision diamond** — exactly two labelled exits (true/false); both must be reachable.
- **Terminator** — the rounded start/end nodes; every path eventually reaches the end.
- **Connector** — a labelled circle joining arrows across the page (avoids spaghetti).
- **Dead branch** — a path that no input can ever take - usually a bug in the conditions.
- **Termination argument** — the reason a loop must stop: some quantity shrinks every pass and has a floor.

## Explanation

**What flowcharts add over pseudocode.** Termination and reachability become visible: a diamond with one exit, an arrow into a dead end, a loop whose exit condition can never be true - all obvious in a picture, easy to miss in text.

**The arrow discipline.** Every diamond has exactly two labelled exits. Every path from start reaches end. Nothing floats unattached. Four symbols total (terminator, process, decision, connector) - resist flowchart libraries with 20 shapes.

**From words to diamonds.** Each 'otherwise', 'unless', and 'until' in the requirements is a decision. Extract them first, then wire the normal path around them.

**Tracing arrows = tracing state.** Walk a real input through the arrows with a finger. If you cannot say which branch a concrete input takes, the flowchart (or the spec) is broken.

**State machines.** A vending machine is four states (idle, accepting credit, vending, sold-out) and the arrows are the events. This is the flowchart idea wearing a different hat - and it returns in cs-007 and lecture 12's clinics.

## Examples

The lecture's worked examples live in [examples.md](examples.md); the case studies this
lecture builds on are worked in class from the projector. The case sequence with difficulties:
- [cs-009](../../case-studies/student/cs-009.md) (Beginner)
- [cs-010](../../case-studies/student/cs-010.md) (Foundational)
- [cs-011](../../case-studies/student/cs-011.md) (Intermediate)
- [cs-012](../../case-studies/student/cs-012.md) (Advanced)

## Common misconceptions

- Diamonds with one exit or unlabelled arrows - half the class does this on day one.
- A loop whose exit arrow leaves from a process box - exit decisions belong in diamonds.
- Trusting the picture without tracing a concrete input through it.
- Drawing 20 symbols where 5 suffice - diagrams are for clarity, not decoration.

## Summary and key takeaways

1. Four symbols, two exits per diamond, every path reaches the end.
2. Every loop names the quantity that shrinks.
3. Trace arrows with a real input before believing the picture.
4. Flowcharts expose dead branches and bad termination that text hides.

## Practice questions

- Draw the flowchart for 'keep reading numbers until 0, then print the count of negatives'.
- Mark the two exits on every diamond of your ATM flowchart; name what shrinks for the loop.
- Find the dead branch in a provided discount flowchart (10% over 100, 20% over 200, else 5%).
- Trace the guess-the-number flowchart with target 7 and guesses 4, 8, 7 - list every arrow taken.

## Where this leads

Next lecture: **First Python: State and Sequences**. The quiz below checks this lecture's essentials before we build on them.
