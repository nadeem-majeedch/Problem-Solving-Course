# Worked Examples — Lecture 14

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. The validator trio: three contracts, one driver](#1) | cs-053 | yes |
| [2. Refactor the monolith: same output, new shape](#2) | cs-054 | yes |
| [3. The parameter jungle: the mutable default](#3) | cs-055 | yes |
| [4. Pipelines as functions: clean, tokenise, count](#4) | cs-056 | yes |

---

## 1. The validator trio: three contracts, one driver (case cs-053)

**Problem.** Write three independent checks - email-ish, phone-ish, student-ID - and a driver that prints a verdict table for sample values.

**Analysis.** Each check is a function: input string -> boolean. The driver is dumb plumbing. Splitting them means each rule can be tested alone - the reuse lesson in miniature.

**Algorithm.**
1. define looks_like_email(s): one '@', a '.' after it
2. define looks_like_phone(s): digits, spaces, plus, right length
3. define looks_like_id(s): letter + digits pattern
4. drive: print each value with its three verdicts

**Pseudocode.**

```
    FUNCTION looks_like_email(s) RETURN boolean
    FUNCTION looks_like_phone(s) RETURN boolean
    FUNCTION looks_like_id(s)    RETURN boolean
    FOR each value in samples
        WRITE value, three verdicts
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
def looks_like_email(s):
    return s.count("@") == 1 and "." in s.split("@")[1]

def looks_like_phone(s):
    digits = s.replace(" ", "")
    return digits.isdigit() and len(digits) in (10, 11)

def looks_like_id(s):
    return len(s) >= 2 and s[0].isalpha() and s[1:].isdigit()

for v in ["ada@uni.edu", "07123 456789", "S2023/4471"]:
    print(v, looks_like_email(v), looks_like_phone(v), looks_like_id(v))
# expect: ada@uni.edu True False False
# expect: 07123 456789 False True False
# expect: S2023/4471 False False False
```

**Trace (dry run).** 'ada@uni.edu': one @, domain has a dot -> email True; digits only after removing the space -> phone True; 'S2023/4471' has a slash -> id False. Each column is independent - exactly the design goal.

**Expected output.** three verdict columns for the three sample values

**Edge cases.** Empty string fails all three (good). Multiple '@' fails email. IDs with leading zeros survive because we check types, not numeric value.

**Complexity.** Each check O(len(s)); the trio demonstrates decomposition, not performance.

## 2. Refactor the monolith: same output, new shape (case cs-054)

**Problem.** One script parses 'name,course,score' lines, drops blanks, averages per student, prints a report. Refactor it into functions without changing behaviour.

**Analysis.** Find the three jobs hiding in the script: parse one line, aggregate, format. Behaviour is locked by testing on the ORIGINAL output first - refactor under test protection.

**Algorithm.**
1. capture the monolith's output on fixed input (the contract)
2. extract parse_line(line) -> (name, course, score) or None
3. extract averages(rows) -> dict
4. extract format_report(avgs) -> string
5. re-run: output must be identical

**Pseudocode.**

```
    expected <- run original on sample
    FUNCTION parse_line / averages / format_report
    actual <- run refactored on same sample
    CHECK actual = expected
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
def parse_line(line):
    parts = [p.strip() for p in line.split(",")]
    if len(parts) != 3 or not parts[2]:
        return None
    return parts[0], parts[1], float(parts[2])

def averages(rows):
    acc = {}
    for name, _course, score in rows:
        acc.setdefault(name, []).append(score)
    return {k: sum(v) / len(v) for k, v in acc.items()}

lines = ["ada,CS1,80", "bo,DS1,", "ada,CS1,95"]
rows = [r for r in (parse_line(l) for l in lines) if r]
avg = averages(rows)
print(round(avg["ada"], 1), len(rows))
# expect: 87.5 2
```

**Trace (dry run).** 'bo,DS1,' -> empty score -> None -> dropped. ada contributes 80 and 95 -> 175/2 = 87.5. Two rows survive. The output line proves both the filter and the average.

**Expected output.** averages: ada 87.5 (bo flagged, not silently dropped)

**Edge cases.** A line with extra commas -> None (strict). Score 'abc' -> ValueError; a robust parse_line catches it and returns None - flag, do not crash (lecture 12's rule).

**Complexity.** Unchanged O(n) - refactoring changes shape, not cost.

## 3. The parameter jungle: the mutable default (case cs-055)

**Problem.** def add_tag(tag, tags=[]): called three times accumulates instead of starting fresh. Explain, then fix.

**Analysis.** The default list is created ONCE, at definition time, and shared by every call. This is not a style quirk; it is a correctness bug with a standard fix: None sentinel.

**Algorithm.**
1. demonstrate the bug: three calls, print
2. explain: default evaluated once at definition
3. fix: default None, create a fresh list inside

**Pseudocode.**

```
    BUGGY:  FUNCTION add_tag(tag, tags = new list)
    FIXED:  FUNCTION add_tag(tag, tags = NULL)
                IF tags = NULL THEN tags <- new list
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
def add_tag(tag, tags=None):
    if tags is None:
        tags = []
    tags.append(tag)
    return tags

a = add_tag("x")
b = add_tag("y")
print(a, b, a is b)
# expect: ['x'] ['y'] False
```

**Trace (dry run).** With the buggy default: call 1 appends into the shared list ['x']; call 2 appends into the SAME list ['x','y']; call 3 -> ['x','y','z']. With the sentinel each call starts empty; the identity check prints False, proving two distinct lists.

**Expected output.** buggy: calls accumulate in one shared list; fixed: each call gets its own list

**Edge cases.** The bug only bites for mutable defaults (list, dict, set) - an int default cannot accumulate. Any function returning the mutated default spreads the shared object further.

**Complexity.** No performance argument either way - this is a semantics lesson.

## 4. Pipelines as functions: clean, tokenise, count (case cs-056)

**Problem.** Turn '  the CAT, the dog!  ' into a word count. Build it as three small functions composed in a pipeline.

**Analysis.** Each stage's output is the next stage's input: clean (strip, collapse spaces) -> tokenise (split) -> count (dictionary). Functions make each stage testable and the order swappable.

**Algorithm.**
1. clean(s): strip and squeeze whitespace
2. tokenise(s): split on spaces
3. count(words): dictionary tally
4. pipeline: count(tokenise(clean(s)))

**Pseudocode.**

```
    FUNCTION clean(s)    RETURN normalised string
    FUNCTION tokenise(s) RETURN list of words
    FUNCTION count(ws)   RETURN dictionary
    WRITE count(tokenise(clean(text)))
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
def clean(s):
    return " ".join(s.split())

def tokenise(s):
    return s.split(" ")

def count(words):
    d = {}
    for w in words:
        d[w] = d.get(w, 0) + 1
    return d

text = "  the CAT, the dog!  "
words = tokenise(clean(text))
tally = count(words)
print(words)
print(tally["the"] == 2, tally.get("CAT,"))
# expect: ['the', 'CAT,', 'the', 'dog!']
# expect: True 1
```

**Trace (dry run).** clean removes the doubled spaces -> 'the CAT, the dog!'. tokenise splits -> four tokens. count gives the:2, CAT,:1, dog!:1. Note punctuation clings to tokens - real pipelines add a punctuation-stripping stage (lecture 10's normalisation).

**Expected output.** the:2, CAT,:1, dog!:1 (punctuation shows why cleaning rules matter)

**Edge cases.** Empty string: clean gives '', tokenise gives [''] - one empty token! A production tokenise returns [] for empty input. This off-by-one is a classic pipeline bug.

**Complexity.** O(n) total; the pipeline adds no cost, only clarity.
