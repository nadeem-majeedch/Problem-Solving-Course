# Lecture Notes — Lecture 11: Lists and Slicing

Companion to the lecture plan and the worked examples. Read the *Definitions* before
class, the *Explanation* after it; the practice questions and the lecture quiz close the loop.

## Definitions

- **Aliasing** — two names bound to the same list object; mutation through one is visible through the other.
- **Copy (shallow)** — lst[:] or list(lst) makes a new outer list; nested items are still shared.
- **In-place mutation** — methods like append/sort/reverse change the object; they usually return None.
- **Rotation** — moving items from one end of a list to the other by k positions (wraparound).
- **Deduplication** — keeping first occurrences only - order-preserving vs set-based variants.
- **Slicing view** — a slice produces a *new* list; it is not a live window onto the original.
- **Grid (list of lists)** — an outer list whose items are inner lists; the aliasing trap of [[0]*3]*2.

## Explanation

**Assignment binds names; it rarely copies.** a = b makes one list with two names. cs-044's grid = [[0]*3]*2: grid[0][0] = 9 shows up in BOTH rows (aliasing), while the fix [[0]*3 for _ in range(2)] keeps rows independent - the reference prints exactly this pair.

**Slices copy; views do not exist.** lst[a:b] hands you a new list. There is no live window - which is why cs-043's rotation by slicing is safe while a shared-reference rotation would corrupt.

**In-place methods return None.** lst.sort() returns None; sorted(lst) returns a new list. Chaining lst = lst.sort() destroys your list - the single most common Block II crash.

**Rotation is arithmetic on indices.** cs-043: left by 2 on [1,2,3,4,5] is [3,4,5,1,2]; the formula is lst[k:] + lst[:k] (mod len for big k: the reference shows k=7 ≡ k=2). Right rotation is lst[-k:] + lst[:-k].

**Deduplicate with intent.** cs-042: order-preserving dedupe ([3,1,3,2,1,3] → [3,1,2]) needs a seen-set and appends; sorting first ([1,2,3]) destroys the requested order. Both are 'correct' - the spec picks.

## Examples

The lecture's worked examples live in [examples.md](examples.md); the case studies this
lecture builds on are worked in class from the projector. The case sequence with difficulties:
- [cs-041](../../case-studies/student/cs-041.md) (Beginner)
- [cs-042](../../case-studies/student/cs-042.md) (Foundational)
- [cs-043](../../case-studies/student/cs-043.md) (Intermediate)
- [cs-044](../../case-studies/student/cs-044.md) (Advanced)

## Common misconceptions

- Assuming assignment copies a list.
- Slicing when a copy is needed - aliasing corruption follows.
- Reversing by popping while still iterating over the same list.
- Chaining lst = lst.sort() and losing the list to None.

## Summary and key takeaways

1. Assignment aliases; slices and explicit copies duplicate.
2. In-place methods return None - do not chain them.
3. Rotation is index arithmetic: lst[k:] + lst[:k].
4. Dedupe: order-preserving needs a seen-set; sorting changes the spec.

## Practice questions

- Predict grid = [[0]*3]*2; grid[0][0] = 9 - then write the fix and predict again (cs-044 family).
- Rotate [1,2,3,4,5] left by 2, right by 2, and left by 7 - all with slices (cs-043 family).
- Dedupe [3,1,3,2,1,3] preserving order; then produce the sorted-unique version; state which the spec wanted.
- Draw memory diagrams for: a = [1,2]; b = a; b = a[:]; b.append(3) - what does a hold after each?

## Where this leads

Next lecture: **Debugging Lab: Real Defects**. The quiz below checks this lecture's essentials before we build on them.
