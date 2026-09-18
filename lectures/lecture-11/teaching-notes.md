# Teaching Notes — Lecture 11

*Instructor only - not rendered on the public site.*

## Board plan

- Left: the two list identities: names vs contents; assignment as sticky-note.
- Middle: [[0]*3]*2 drawn as two arrows to ONE inner list - the aliasing picture.
- Right: slice operations as a menu: copy, reverse, window, stride.

## Questions to ask students

- After b = a and a.append(x), what is len(b) - and why is that the correct answer?
- Which slice makes a genuine copy, and what is the cheap full-copy idiom?
- When does in-place beat sorted(), and when is it a trap?

## Alternative explanations

- Draw-boxes-first policy: every aliasing question answered with a diagram before words.
- Advanced: introduce copy vs deepcopy with a 2-level example.

## Expected student difficulties

- The aliased-grid bug: writing [1,1] sets a whole column - trace it visually to a gasp.
- Confusing sort() and sorted() return semantics - one returns None, catch the chained call.

## Connections to neighbouring lectures

Mutation semantics prepare function calls (L14) and the debugging lab (L12) that weaponises today's traps.

## Quiz answer key

**A1.** After b = a, what does b.append(x) do to a?
- *Expected:* Changes a too - both names point at the same list.

**A2.** What is the idiom for a full list copy?
- *Expected:* a[:] (or list(a)).

**A3.** sort() vs sorted(): what is the difference?
- *Expected:* sort() mutates in place and returns None; sorted() returns a new list.

**A4.** What does a[len(a):] evaluate to?
- *Expected:* The empty list.

**B1.** grid = [[0]*3]*2: what goes wrong writing grid[0][0]=1, and what is the fix?
- *What earns marks:* Both rows change (they are one object); fix with a comprehension [[0]*3 for _ in range(2)].

**B2.** Rotate [1,2,3,4,5] left by 2 using slices; give the result.
- *What earns marks:* a[2:] + a[:2] -> [3, 4, 5, 1, 2].

## Exit ticket - expected answers

1. What is the difference between a = b and a = b[:] for lists?
   - *Expected:* the first aliases (one object, two names), the second copies

2. Give the slice for the last three items and for every second item.
   - *Expected:* lst[-3:] and lst[::2]

3. Why did the roster corrupt in cs-044?
   - *Expected:* two names referenced one list; an 'append' to one mutated the other
