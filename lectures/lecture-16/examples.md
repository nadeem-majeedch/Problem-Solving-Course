# Worked Examples — Lecture 16

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. The gradebook audit: aggregates with honesty](#1) | cs-061 | yes |
| [2. Text stats on a budget: the O(n) reflex](#2) | cs-062 | yes |
| [3. The campus survey: coding scheme as specification](#3) | cs-063 | yes |
| [4. The mini challenge cup: two problems, one clock](#4) | cs-064 | yes |

---

## 1. The gradebook audit: aggregates with honesty (case cs-061)

**Problem.** Lines 'ada,CS1,80', 'bo,DS1,' (missing), 'ada,CS1,95', 'cy,CS1,300' (over 100). Produce per-student averages plus flags for missing and anomalous scores.

**Analysis.** Block I-II skills in one pipeline: parse strictly, drop-and-flag missing (never average over it silently), validate the range, then aggregate. The flag list is part of the output, not a side note.

**Algorithm.**
1. parse each line; missing score -> flag and skip
2. score outside 0..100 -> flag as anomaly
3. average remaining scores per student
4. print averages and both flag lists

**Pseudocode.**

```
    FOR each line
        IF score missing THEN flag_missing; skip
        IF score outside 0..100 THEN flag_anomaly
        ELSE accumulate
    WRITE averages, flags
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
lines = ["ada,CS1,80", "bo,DS1,", "ada,CS1,95", "cy,CS1,300"]
missing, anomaly, acc = [], [], {}
for ln in lines:
    name, course, score = [p.strip() for p in ln.split(",")]
    if score == "":
        missing.append(name)
        continue
    s = float(score)
    if not 0 <= s <= 100:
        anomaly.append((name, s))
        continue
    acc.setdefault(name, []).append(s)
avg = {k: sum(v) / len(v) for k, v in acc.items()}
print(avg["ada"], missing, anomaly)
# expect: 87.5 ['bo'] [('cy', 300.0)]
```

**Trace (dry run).** ada: 80 and 95 -> 87.5. bo: empty score -> missing flag. cy: 300 > 100 -> anomaly flag (policy decision: maybe a bonus scale, but flag first). Two flags, one average.

**Expected output.** ada 87.5; missing: bo; anomaly: cy with 300

**Edge cases.** A student with ONLY anomalous scores has no average - print name with no value rather than 0. Whitespace-only scores are missing, not zero. Decide once, code once, document in the flag.

**Complexity.** O(n) for n lines - one pass, flags accumulate alongside.

## 2. Text stats on a budget: the O(n) reflex (case cs-062)

**Problem.** For "Data science is twenty percent practice and eighty percent cleaning data." report word count, reading time (200 wpm), the longest word, and the two most frequent words - in one pass.

**Analysis.** Four aggregates, one pass, no nesting. Reading time is count/200*60 seconds. Longest tracks a champion; frequency uses a dictionary. 'One pass' is the design constraint.

**Algorithm.**
1. split into words; n = len
2. reading_time = n / 200 * 60
3. longest: track champion while iterating
4. frequency dictionary; take top two at the end

**Pseudocode.**

```
    FOR each word
        n <- n + 1
        IF longer than champion THEN champion <- word
        tally[word] <- tally[word] + 1
    reading <- n / 200 * 60
    top <- two largest tally entries
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
text = "Data science is twenty percent practice and eighty percent cleaning data."
words = text.split()
n = len(words)
longest = max(words, key=len)
tally = {}
for w in words:
    tally[w] = tally.get(w, 0) + 1
top = sorted(tally.items(), key=lambda kv: (-kv[1], kv[0]))[:2]
print(n, round(n / 200 * 60, 1), longest)
print(top)
# expect: 11 3.3 practice
# expect: [('percent', 2), ('Data', 1)]
```

**Trace (dry run).** 11 words (punctuation stays attached: 'data.'). Reading time 11/200x60 = 3.3 s. 'practice' (8 letters) is longest. 'percent' appears twice; everything else once - alphabetical tie-break puts 'data.' next.

**Expected output.** words 11; reading time 3.3 s; longest 'practice'; top: percent(2), then a one-count tie

**Edge cases.** Empty text: n=0, no longest word - define the behaviour (report '-') rather than crash. Case: 'Data' and 'data' count separately unless normalised (deliberately not done here; say so as an assumption).

**Complexity.** O(n) time, O(u) space; the naive alternative (recount per aggregate) is still O(n) but four passes.

## 3. The campus survey: coding scheme as specification (case cs-063)

**Problem.** Answers 'yes', 'no', 'YES!!', '', 'maybe, idk', and multi-select '1,3'. Define a coding scheme and apply it.

**Analysis.** The scheme is the spec: normalise case, strip punctuation, map yes->1, no->0, everything else missing. Multi-select splits on commas. The scheme is written BEFORE the code - that is the lesson.

**Algorithm.**
1. normalise: lowercase, strip punctuation/whitespace
2. map exact 'yes' -> 1, 'no' -> 0
3. anything else -> missing (flag, never guess)
4. multi-select: split on comma, code each part

**Pseudocode.**

```
    FUNCTION code(answer)
        a <- normalise(answer)
        IF a = 'yes' RETURN 1
        IF a = 'no'  RETURN 0
        RETURN MISSING
    FOR each answer: WRITE code(answer)
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
def code(answer):
    a = answer.strip().strip("!?").lower()
    return {"yes": 1, "no": 0}.get(a, None)

samples = ["yes", "no", "YES!!", "", "maybe, idk", "1,3"]
coded = [code(s) for s in samples]
print(coded)
# expect: [1, 0, 1, None, None, None]
```

**Trace (dry run).** 'YES!!' -> strip '!' -> 'yes' -> 1. '' -> None (missing, not zero!). 'maybe, idk' -> None; the split-on-comma rule applies only to declared multi-select fields - here it is a free-text answer, so it stays missing.

**Expected output.** yes=1, no=0, YES!!=1, ''=missing, 'maybe, idk'=missing, '1,3'=missing (not multi-select here)

**Edge cases.** 'yesss' is missing (exact match only - say so). 'NO ' with trailing space codes to 0 after strip. Ambiguity between missing and 'declined to answer' is a policy choice - document it.

**Complexity.** O(n) over answers; the scheme costs nothing at runtime because it was decided at design time.

## 4. The mini challenge cup: two problems, one clock (case cs-064)

**Problem.** Challenge 1: sum the digits of 2^15. Challenge 2: estimate the longest run of heads in 100 fair coin flips. Five minutes for both.

**Analysis.** Challenge 1 is exact arithmetic: 2^15 = 32768, digits 3+2+7+6+8 = 26 - digit extraction from lecture 5. Challenge 2 is simulation: flip 100 coins many times, track the best streak, report the typical value (~6-7).

**Algorithm.**
1. digits of 2^15: str or // % loop, sum
2. streak: repeat 100 flips many times, keep max run
3. report median of max-runs as the typical answer

**Pseudocode.**

```
    s <- sum of digits of 2^15
    FOR trial in 1..many
        run <- longest heads-run in 100 flips
        keep distribution of run
    WRITE s, typical run
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
big = 2 ** 15
s = sum(int(d) for d in str(big))
print(s)
# expect: 26
```

**Trace (dry run).** 2^15 = 32768. Digits 3, 2, 7, 6, 8 -> 26. (String conversion is exact for ints; the //10 %10 loop from lecture 5 gives the same 26.) For the streak: one 100-flip trial typically peaks at 6 or 7; over many trials the median lands there - the exact value varies by seed.

**Expected output.** 26; typical longest heads-run in 100 flips: 6-7

**Edge cases.** 2^0 = 1 -> digit sum 1. Negative exponents are not integers - out of contract. The streak estimate depends on the number of trials: report the trial count with the answer, never a bare number (lecture 28's honesty rule, foreshadowed).

**Complexity.** Digit sum O(digits). Streak simulation O(trials x 100); exact DP exists but is overkill here.
