# Teaching Notes — Lecture 14

*Instructor only - not rendered on the public site.*

## Board plan

- Left: one monolithic script on top; its decomposition tree below - three functions circled.
- Middle: the contract template: PRE (assumptions) / POST (returns, and what it changes).
- Right: the pipeline sketch: clean -> tokenise -> count, arrows labelled with data types.

## Questions to ask students

- Which function can you test with zero knowledge of the others - what does that buy us?
- Where would a side effect (mutating the argument) hide in this pipeline - do we want one?
- What makes a function's name bad - give me a verb that hides two jobs.

## Alternative explanations

- Design-first students: let them decompose before seeing the monolith's code.
- Test-minded students: have them write the driver table BEFORE the functions exist.

## Expected student difficulties

- Functions that print instead of return - force the pure-helper style for the lab.
- Too many parameters (the seven-argument function) - teach grouping into records/dicts.

## Connections to neighbouring lectures

Reusable pieces need calling conventions - scope and the mutable-default trap arrive now (L15).

## Quiz answer key

**A1.** What two parts does a function contract have?
- *Expected:* PRE (assumptions about inputs) and POST (what it returns/changes).

**A2.** Why prefer return over print inside helpers?
- *Expected:* Returned values compose; printed values are dead ends.

**A3.** What is a pure helper?
- *Expected:* No side effects beyond its return value - same inputs, same output.

**A4.** Name one benefit of decomposition beyond reuse.
- *Expected:* Independent testing (or: failure isolation, parallel work, readable reviews).

**B1.** Write the contract (PRE/POST) for a phone-number validator.
- *What earns marks:* PRE: a string. POST: returns True iff digits-only length 10-11 after removing spaces; changes nothing.

**B2.** The log-parsing monolith: name the three functions you would extract and each one's single job.
- *What earns marks:* parse_line (line -> record or None), aggregate (records -> per-student totals), format_report (totals -> string).

## Exit ticket - expected answers

1. What makes a function name good?
   - *Expected:* it states the subproblem's contract: verb + object, no surprises

2. Why are mutable defaults dangerous?
   - *Expected:* the default object is created once and shared across calls

3. What does 'refactor without behaviour change' demand?
   - *Expected:* the same tests pass before and after, unchanged
