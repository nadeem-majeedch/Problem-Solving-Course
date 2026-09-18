# Teaching Notes — Lecture 31

*Instructor only - not rendered on the public site.*

## Board plan

- Left: the umbrella decision tree with both branches costed.
- Middle: the game-show enumeration table: three equally likely prize doors.
- Right: the flip-point line: where EV ranking swaps, marked at 20%.

## Questions to ask students

- At what rain probability does the umbrella decision flip - and why is that number more useful than the verdict?
- In the game show, what exactly is the information the host's door reveals?
- Insurance loses on EV - under which decision rule does it win?

## Alternative explanations

- Play the game show live with envelopes - the 2/3 lands viscerally.
- Advanced: 100-door variant argued before any arithmetic.

## Expected student difficulties

- Answering with a verdict instead of a threshold - train the flip-point habit.
- Believing intuition over enumeration in conditional probability - the table settles it.

## Connections to neighbouring lectures

Decision rules synthesise L26's conditionals and L30's formulations; the capstone integrates everything (L32).

## Quiz answer key

**A1.** Define expected value of an action.
- *Expected:* Probability-weighted average of its outcomes.

**A2.** What is a flip point?
- *Expected:* The probability where the ranking of two actions swaps - more useful than one verdict.

**A3.** What information does the host's opened door carry in the game show?
- *Expected:* It is forced exactly when your first pick was wrong - that asymmetry is the 2/3.

**A4.** EV is one decision rule; name another for catastrophic stakes.
- *Expected:* Ruin avoidance / utility-based choice (e.g. buying insurance).

**B1.** Umbrella: cost 2, rain cost 10, p = 0.3 - decide and give the flip point.
- *What earns marks:* EV carry 2 < EV leave 3 -> carry; flips below p = 0.2.

**B2.** Game show: enumerate three doors for stay vs switch.
- *What earns marks:* Prize 1: stay; prize 2/3: switch (host forced) -> switch wins 2/3.

## Exit ticket - expected answers

1. What does expected value compare, and what does it ignore?
   - *Expected:* average outcomes; it ignores variance (risk) unless you add it

2. Why does switching win in cs-122?
   - *Expected:* the host's reveal leaks information; 2/3 of outcomes favour switching

3. When is a dominated strategy visible instantly?
   - *Expected:* one option's payoffs are worse in every column of the table
