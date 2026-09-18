# Teaching Notes — Lecture 23

*Instructor only - not rendered on the public site.*

## Board plan

- Left: the greedy protocol: propose rule -> find counterexample or write the exchange argument.
- Middle: interval scheduling sorted by end; the taken set boxed.
- Right: the knapsack dp table filling column by column (budget axis).

## Questions to ask students

- What would the exchange argument for earliest-end need to establish?
- Which dp entry does the final answer live in - and what does each cell MEAN?
- Why does the budget loop run descending for 0/1 items - what breaks ascending?

## Alternative explanations

- Counterexample-hunt as a game: each pair gets a rule to break.
- Advanced: reconstruct the knapsack's chosen items from the filled table.

## Expected student difficulties

- Students accept greedy after one success - force the counterexample hunt every time.
- dp[j] meaning drift during coding - have them write the one-line state definition first.

## Connections to neighbouring lectures

DP formalises L22's memoisation; graphs next (L24) restart the modelling thread at scale.

## Quiz answer key

**A1.** What does a greedy claim need to be accepted?
- *Expected:* An exchange argument (or it falls to a counterexample).

**A2.** Which rule wins interval scheduling and why informally?
- *Expected:* Earliest end - it leaves the most room; exchange argument works.

**A3.** Name the four DP declarations.
- *Expected:* State, transition, base case, evaluation order.

**A4.** Why descending budget order for 0/1 knapsack?
- *Expected:* So dp[j-h] is still the previous item's row - no double use.

**B1.** Meetings (9,10.5),(9.5,11),(11,12),(10.5,12.5): greedy pick and count.
- *What earns marks:* Sort by end: take (9,10.5), skip (9.5,11), take (11,12), skip (10.5,12.5) -> 2.

**B2.** Coins 1,3,4 amount 6: greedy vs optimal.
- *What earns marks:* Greedy 4+1+1 (3 coins); optimal 3+3 (2 coins) - counterexample.

## Exit ticket - expected answers

1. What one input kills cs-089's greedy?
   - *Expected:* the non-canonical coin set instance from its instructor page

2. State the exchange argument for earliest-end scheduling.
   - *Expected:* swapping a later-ending chosen meeting for an earlier-ending one never hurts

3. What makes a DP state adequate?
   - *Expected:* it captures everything the future decisions need to know
