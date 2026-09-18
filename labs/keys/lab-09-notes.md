# Lab 9 — Checkpoint Notes (instructor only)

Not for publication; discuss after the lab.

- **A1/A2.** Branch version: four branches plus the unknown case; adding
  a category touches the branch chain (1 place) but the *cap policy* (B3)
  would touch it again. Students typically count "1" — press them: the
  change-place count that matters is per-policy-change, not per-branch.
  `None` over a guessed price: a silent wrong price corrupts every
  downstream total; `None` (or an exception) fails loudly. Same principle
  as quiz 4's not-found discussion.
- **B1/B2.** Map version: adding a category = adding one `RATES` entry,
  zero code changes. The sentence must connect "policy as data" to
  "change without editing logic". This is the lab's core insight and the
  same one cs-049–cs-052 build on.
- **B3.** The rule decision is genuinely open: truncate (charge up to the
  cap, remainder free), refuse (job rejected once the cap is hit), or
  partial (last job partially charged). What matters is that the choice is
  *stated* — all three produce different month-totals for the same log.
  The honest structural point: per-month state cannot live in a
  stateless per-call function; the wrapper carries the state. Exactly
  the function-contract lesson from cs-053–cs-056.
- **C1.** Inversion breaks twice: `0` maps ambiguously (honorary, or
  anyone with 0 pages — actually 0 pages isn't a price, so strictly the
  inverse domain is {0.05, 0.08, 0.15, 0.00}); the real breakage is if
  two categories ever share a rate (say staff and honorary both 0 — the
  inverse is not a function). Students discover: inverse of a map is a
  relation, not a map, unless the original is injective. Vocabulary
  optional; the phenomenon mandatory.
- **C2.** Totality rules seen in past runs: return a list of all
  categories at that price (first-match), or raise on ambiguity, or
  return `"ambiguous"`. The test table must include the shared-price row
  and the missing-price row. Adjudicate rule-consistency, not rule-choice.
- **C3.** Common adjudication trap: using your own rule to judge theirs.
  The mark is for restating their rule first, then testing.
- **D1.** Pattern: grouped aggregation — accumulator is a dict keyed by
  category, values accumulate revenue (not counts — worth naming the
  difference). Where the mapping earned its keep: the per-category
  dispatch is a lookup, not a branch chain; the aggregation loop never
  mentions a category name.
- Completion bar as in Lab 1. Fast finishers: add a `caps` map
  (`category → monthly cap or None`) and push the whole cap policy into
  data; then ask what happens when a cap policy itself needs a condition
  (caps only for visitors *below year 1*) — where data ends and code
  must resume.
