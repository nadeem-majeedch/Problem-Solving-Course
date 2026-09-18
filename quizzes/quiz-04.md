# Quiz 4 — Lists, Debugging, Dictionaries, Functions (Lectures 11–14)

**Time: 20 minutes · Closed book · Answer all questions.**

## Q1. Aliasing (4 marks)

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```

(a) State the output and explain the mechanism in one sentence. *(2)*
(b) Rewrite one line so that `a` stays `[1, 2, 3]`. *(2)*

## Q2. Dictionary reasoning (5 marks)

```python
votes = ["ann", "bo", "ann", "cy", "bo", "ann"]
tally = {}
for v in votes:
    if v in tally:
        tally[v] = tally[v] + 1
    else:
        tally[v] = 1
```

(a) State the dictionary after the loop. *(2)*
(b) Add pseudocode after the loop to report the winner, assuming a rule for
    ties (state your rule). *(3)*

## Q3. Debug a function (5 marks)

This function should return the second-largest value in a list of distinct
numbers, but it returns the largest:

```python
def second_largest(nums):
    best = nums[0]
    for n in nums:
        if n > best:
            best = n
    return best
```

(a) Give a test input and expected output that exposes the defect. *(1)*
(b) Locate the mechanism: which line, and why does it cause the symptom? *(2)*
(c) Rewrite the function minimally (track two values). *(2)*

## Q4. Functions and contracts (6 marks)

A teammate writes one function `process(names)` that: lowercases every name,
removes duplicates, sorts, prints the sorted list, and prints the count.

(a) State the contract problem with this function in one sentence. *(2)*
(b) Redesign it as two functions; give each a name, parameters, and what it
    returns (one line each). *(2)*
(c) Give one input that tests the boundary of the dedup step. *(2)*
