# Teaching Notes — Lecture 02

*Instructor only - not rendered on the public site.*

## Board plan

- Left: bad pseudocode (vague verb, no initialisation) vs good (numbered, one action per line).
- Middle: the password-rule order-of-tests ladder, redrawn per student proposal.
- Right: 'words that lie in pseudocode' - simply, some, maybe - banned list grows all semester.

## Questions to ask students

- Which line of this pseudocode would a confused friend misread first?
- What does 'and' mean in 'letters and digits and length 8' - one test or three?
- Why initialise before the loop - what breaks if we do not?

## Alternative explanations

- Grammar-shy students: allow sentence-form pseudocode; require only unambiguity.
- Fast finishers: have them write TWO readings of the same ambiguous rule in pseudocode.

## Expected student difficulties

- Students conflate precision with verbosity - show the same step written tightly and loosely.
- Initialisation is invisible until a trace breaks - run the no-init trace live.

## Connections to neighbouring lectures

L1's assumptions become L2's specified behaviour; next: flowcharts make the same logic visible (L3).

## Quiz answer key

**A1.** What makes a line of pseudocode ambiguous?
- *Expected:* It allows more than one execution; e.g. 'add some water' - which water, how much.

**A2.** Why initialise a counter before the loop?
- *Expected:* So every use of it has a defined value; traces without initialisation read garbage.

**A3.** In the password rule (letters, digits, length 8), which test order avoids confusing error messages?
- *Expected:* One test at a time in a fixed order; report the FIRST failing test.

**A4.** What is a sentinel value?
- *Expected:* A pre-agreed input (like 'done') that means 'stop reading', not data.

**B1.** Write pseudocode that checks a password rule (at least 8 characters, at least one digit) and prints the FIRST failing reason.
- *What earns marks:* IF length < 8: print 'too short'; ELSE IF no digit: print 'no digit'; ELSE print 'ok' - with an explicit digit-scan loop.

**B2.** Write the vending machine's accept-coin step so another student could implement it without asking you a question.
- *What earns marks:* Coin values, credit update, sold-out branch first, explicit change calculation; no vague verbs.

## Exit ticket - expected answers

1. Name the three control shapes every pseudocode solution is built from.
   - *Expected:* SEQUENCE, IF/ELSE selection, WHILE/FOR iteration

2. What makes a pseudocode line 'testable'?
   - *Expected:* it names variables and values precisely enough to hand-trace

3. When is a state table required?
   - *Expected:* whenever a later statement depends on more than the current input line
