# Teaching Notes — Lecture 04

*Instructor only - not rendered on the public site.*

## Board plan

- Left: the pseudocode-to-Python side-by-side table (READ/input, WRITE/print, <-/=).
- Middle: the echo program typed live, one translation step at a time.
- Right: first variable-state box diagram: name, type, current value.

## Questions to ask students

- What type does input() return, and what does that force us to do with numbers?
- Which line of the pseudocode became TWO lines of Python - why?
- Where is the state in this program - name every variable that survives a loop turn.

## Alternative explanations

- Syntax-anxious students: keep the pseudocode column visible the whole translation; hide it only in the final exercise.
- Experienced students: give them the same case to translate without the table, plus an off-by-one to find.

## Expected student difficulties

- String-vs-number confusion ('2' + 2) - demo it crashing, then fix with int().
- Equality = vs == bleeds in from other languages - catch it in the first live typo.

## Connections to neighbouring lectures

Charts become executable; state becomes inspectable. Next: numbers and cycles exploit the arithmetic (L5).

## Quiz answer key

**A1.** What type does input() return in Python?
- *Expected:* A string - convert with int() or float() for numbers.

**A2.** What is the difference between = and == ?
- *Expected:* = assigns; == compares.

**A3.** What is 'state' in a running program?
- *Expected:* The set of variables and their current values at a moment in time.

**A4.** print writes a value for humans; what does return do?
- *Expected:* Hands a value back to the caller so it can be used in further computation.

**B1.** Translate the echo-with-limits pseudocode into Python, keeping the skip counter.
- *What earns marks:* for-loop over lines; break on sentinel; if len(line) > 20: skipped += 1 else print(line.upper()); print skipped.

**B2.** The change maker: amount 87 with coins 25/10/5/1 - write the loop using // and %, and give the output.
- *What earns marks:* 87//25=3, remainder 12; 12//10=1, rem 2; 2//5=0; 2//1=2 -> 25x3, 10x1, 5x0, 1x2.

## Exit ticket - expected answers

1. What does predict-then-run change about learning?
   - *Expected:* prediction makes the run informative; mismatches are the lesson

2. Name the three Python errors you met today and their causes.
   - *Expected:* e.g. NameError (typo/undefined), ValueError on int('3.5'), IndexError on range end

3. Why convert input strings before arithmetic?
   - *Expected:* input() returns strings; arithmetic on them concatenates or fails
