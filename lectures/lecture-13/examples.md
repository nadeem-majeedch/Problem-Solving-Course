# Worked Examples — Lecture 13

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. The word tally: dictionary as counter](#1) | cs-049 | yes |
| [2. Course rosters: set operations as questions](#2) | cs-050 | yes |
| [3. The LRU cache: recency as a moving queue](#3) | cs-051 | yes |

---

## 1. The word tally: dictionary as counter (case cs-049)

**Problem.** Count how often each word occurs in "the cat the dog the bird cat", then name the most frequent word.

**Analysis.** A dictionary maps word -> count. One pass: for each word, add 1 to its slot, starting from 0 for unseen words. The tally answers 'how many' and 'which is most' in the same structure.

**Algorithm.**
1. create an empty dictionary
2. for each word: increase its count by 1
3. find the key with the largest count
4. report the tally and the winner

**Pseudocode.**

```
    tally <- empty dictionary
    FOR each word in text
        tally[word] <- tally.get(word, 0) + 1
    best <- key with maximum tally value
    WRITE tally, best
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
words = "the cat the dog the bird cat".split()
tally = {}
for w in words:
    tally[w] = tally.get(w, 0) + 1
best = max(tally, key=tally.get)
print(tally["the"], tally["cat"])
print(best, tally[best])
# expect: 3 2
# expect: the 3
```

**Trace (dry run).** 'the' -> tally {the:1}; 'cat' -> {the:1, cat:1}; 'the' -> {the:2, ...}; ... after all seven words: the:3, cat:2, dog:1, bird:1. max over values picks 'the' with 3.

**Expected output.** {'the': 3, 'cat': 2, 'dog': 1, 'bird': 1} and the (count 3)

**Edge cases.** Empty text -> empty tally, no 'most frequent' exists (report that, do not crash). All words distinct -> every count 1, any tie-break is a policy. Case matters: 'The' != 'the' unless you normalise first (lecture 10).

**Complexity.** O(n) time for n words, O(u) space for u distinct words - one pass, no nesting.

## 2. Course rosters: set operations as questions (case cs-050)

**Problem.** CS = {ada, bo, cy}; DS = {bo, dee, ada}. Who takes both? Either? Only CS? Only DS?

**Analysis.** Each question IS a set operation: intersection (both), union (either), difference (only one). Naming the operation is the whole solution; the code is a formality.

**Algorithm.**
1. represent each roster as a set
2. both = intersection
3. either = union
4. only CS = CS minus DS; only DS = DS minus CS

**Pseudocode.**

```
    both    <- CS INTERSECT DS
    either  <- CS UNION DS
    onlyCS  <- CS MINUS DS
    onlyDS  <- DS MINUS CS
    WRITE both, either, onlyCS, onlyDS
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
CS = {"ada", "bo", "cy"}
DS = {"bo", "dee", "ada"}
print(sorted(CS & DS))
print(sorted(CS | DS))
print(sorted(CS - DS))
print(sorted(DS - CS))
# expect: ['ada', 'bo']
# expect: ['ada', 'bo', 'cy', 'dee']
# expect: ['cy']
# expect: ['dee']
```

**Trace (dry run).** Intersection walks CS and keeps members DS also has: ada (yes), bo (yes), cy (no) -> {ada, bo}. Union collects all names once. Difference keeps CS-members not in DS: cy only.

**Expected output.** both {ada, bo}; either {ada, bo, cy, dee}; only CS {cy}; only DS {dee}

**Edge cases.** Empty roster -> every operation behaves (intersection empty, union the other set). Identical rosters -> 'only' sets are empty, 'both' is everything. Duplicates in the source list must be collapsed first - a set does it silently.

**Complexity.** Set operations are O(min(len)) on average; building sets is O(n).

## 3. The LRU cache: recency as a moving queue (case cs-051)

**Problem.** Capacity 2. Operations: put a, put b, get a, put c. Which entries survive, and which is evicted next?

**Analysis.** Model recency as a line: using an item moves it to the front; the back of the line is the eviction victim when capacity overflows. The operations map onto list remove/insert.

**Algorithm.**
1. keep an ordered list, most-recent first
2. get/put move the key to the front
3. on put beyond capacity: drop the back entry

**Pseudocode.**

```
    order <- empty list
    FOR each operation
        IF get(k) or put(k): move k to front of order
        IF put overflows capacity: remove last element of order
    WRITE order
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
order = []
def use(k):
    if k in order:
        order.remove(k)
    order.insert(0, k)
for op, k in [("put","a"),("put","b"),("get","a"),("put","c")]:
    use(k)
    if op == "put" and len(order) > 2:
        order.pop()
print(order)
use("d")
order.pop()
print(order)
# expect: ['c', 'a']
# expect: ['d', 'c']
```

**Trace (dry run).** put a -> [a]; put b -> [b, a]; get a -> [a, b]; put c -> [c, a, b] overflow, evict b -> [c, a]. Next eviction victim: a (the back). The trace IS the answer.

**Expected output.** after put c: {a, c} (b evicted); next eviction: a

**Edge cases.** get of a missing key must not change recency. put of an existing key updates in place, no eviction. Capacity 0 rejects everything; capacity 1 keeps exactly one item.

**Complexity.** O(capacity) per operation with a list; real caches use a hash map plus linked list for O(1).
