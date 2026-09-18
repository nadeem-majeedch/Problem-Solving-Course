# Quiz 2 — Numbers, Traces, Debugging, Testing (Lectures 05–08)

**Time: 20 minutes · Closed book · Answer all questions.**
Show your reasoning; method marks are awarded even when the final answer is wrong.

## Q1. Remainders (4 marks)

A parking cycle repeats every 7 days: day 0 is Monday. A ticket starts on
day 41 and lasts 100 days.

(a) On which weekday does the ticket start? *(2)*
(b) On which weekday does it end (the last valid day)? *(2)*

## Q2. Predict the output (5 marks)

Without running it, state the output of:

```python
x = 5
while x > 1:
    if x % 2 == 0:
        x = x // 2
    else:
        x = 3 * x + 1
print(x)
```

Explain in one line how you arrived at the answer (a trace sketch is fine).

## Q3. Debugging method (5 marks)

A classmate's program should print the average of a list of positive exam
scores but sometimes prints a number larger than every score in the list.

(a) Give the smallest input you would use to reproduce the defect, and say
    why it is minimal. *(2)*
(b) State two competing hypotheses, ordered by how likely you would test
    them first. *(2)*
(c) Name the one piece of evidence that would eliminate one hypothesis. *(1)*

## Q4. Test design (6 marks)

A function `bonus(years)` must return 100 for 5 or more completed years of
service, and 0 otherwise. `years` is a whole number, 0 or more.

(a) Give a complete boundary test table: input, expected output, reason. *(4)*
(b) One test passed. A teammate says the function works. Correct them in one
    sentence. *(2)*
