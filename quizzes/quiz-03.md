# Quiz 3 — Aggregation and Strings (Lectures 09–10)

**Time: 20 minutes · Closed book · Answer all questions.**
Show accumulators and initial values explicitly.

## Q1. Aggregation (5 marks)

A queue log is a list of waiting times in minutes, e.g. `[3, 12, 7, 12, 20]`.
Write pseudocode or Python that outputs, in one pass: the longest wait, the
average wait, and how many waits were over 10 minutes.

(a) List every accumulator with its initial value. *(2)*
(b) Write the loop. *(3)*

## Q2. The zero bug (4 marks)

This line is meant to find the shortest word in a list:

```python
shortest = ""
for w in words:
    if len(w) < len(shortest):
        shortest = w
```

Give one input for which it produces a wrong (or empty) answer, explain the
mechanism, and give the initialisation that fixes it.

## Q3. String reasoning (5 marks)

A student ID is valid when it has exactly 8 characters, starts with a letter,
and ends with a digit.

(a) Write the check as pseudocode or Python, returning a different verdict
    message for each failed rule. *(3)*
(b) Give two inputs at the boundaries of the length rule. *(2)*

## Q4. Trace the code (6 marks)

```python
s = "abca"
seen = ""
for ch in s:
    if ch not in seen:
        seen = seen + ch
print(seen, len(s) - len(seen))
```

(a) Trace: after each iteration, state `seen`. *(4)*
(b) State the printed output. *(1)*
(c) What does the second printed number count, in words? *(1)*
