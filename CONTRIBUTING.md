# Contributing

Thank you for improving **Problem Solving — CS & DS**. This guide covers the
repo's conventions so content stays consistent, valid, and easy to teach from.

## Ground rules

1. **Content is Markdown.** One lecture per folder (`lectures/lecture-NN/plan.md`),
   one case per file. No third-party datasets or external resources are bundled.
2. **Students and instructors are separated.** Student-facing material goes in
   `case-studies/student/`; full solutions go in `case-studies/instructor/`.
   Never describe or hint at a solution's key insight in a student file.
3. **Every change must validate.** Run `python scripts/validate.py` before
   opening a PR — the CI workflow runs the same checks and fails on error.

## Case-study conventions

Each case lives in two files:

| File | Audience | Required sections |
| --- | --- | --- |
| `case-studies/student/cs-NNN-<slug>.md` | Students | Title, metadata table, problem statement, input format, output format, constraints, assumptions, examples, what to notice, discussion starter |
| `case-studies/instructor/cs-NNN-<slug>.md` | Instructors | Same identifier + solution reasoning, five-minute teaching sequence, difficulty adaptation, pseudocode and Python solution blocks, edge cases, alternative approaches, common pitfalls, a per-case reveal walkthrough, assessment use, connections, extension challenge |

Rules:

- IDs are `cs-001` … `cs-NNN` and are **immutable** once assigned. Never reuse
  or renumber an existing ID.
- The student and instructor files for one case must share the same slug and
  the same `id:` value in their metadata tables.
- Difficulty must be exactly one of `Beginner`, `Foundational`, `Intermediate`,
  `Advanced`, `Expert`.
- `lecture:` must name an existing lecture folder (`lecture-01` … `lecture-32`).
- Solutions must explain *why*, not only *what*: include the reasoning, at
  least one alternative approach where applicable, and edge cases.
- Python samples are allowed and encouraged; keep them dependency-free.

## Lecture-plan conventions

`lectures/lecture-NN/plan.md` must contain these headings:

```
# Lecture NN — <Title>
## Position in the course
## Learning objectives
## Case sequence
## Timing plan (120 minutes)
## Board plan
## Differentiation
## Common misconceptions
## Homework and preparation
```

## Teaching-pack conventions

Each lecture folder also carries a four-file teaching pack:

```
notes.md           Student lecture notes (definitions, explanation, misconceptions,
                   takeaways, practice) - starts "# Lecture Notes — Lecture NN"
examples.md        Worked examples with verified Python - starts "# Worked Examples — Lecture NN"
quiz.md            Section A / Section B / Exit ticket / Homework - starts "# Quiz — Lecture NN"
teaching-notes.md  Instructor-only (board plan, questions, alternatives, difficulties,
                   answer keys) - starts "# Teaching Notes — Lecture NN"; never built publicly
```

House rules: every ```` ```python ```` block in `examples.md` must run and its
printed output must match the trailing `# expect:` comment lines
(`scripts/validate.py` enforces this). Case references link by cs-ID and stay
within the lecture's own case sequence. The quiz's exit-ticket and homework
sections mirror the plan's Formative assessment / Homework sections - update
them together.

## Documentation conventions

- `docs/` pages use relative links only; the link validator enforces them.
- Do not add external URLs as required resources. Optional "go further" notes
  must describe *how to search* for a topic rather than invent links.
- Keep language at a level a first-semester student can read comfortably.
  Define any technical term at first use and add it to `docs/glossary.md`.

## Validation

```bash
python scripts/validate.py        # all structural and content checks
python -m pytest tests/ -q        # tooling tests
python scripts/build_site.py      # public build must succeed
python scripts/build_instructor.py  # instructor build must succeed
```

The validator checks: required files exist, case IDs are unique and
student/instructor files are paired, difficulty and lecture references are
valid, all internal Markdown links resolve, no student file contains
instructor-only content, and every lecture plan references at least four cases
that exist. Errors are reported with file and line numbers and never silently
skipped.

## Pull-request checklist

- [ ] `python scripts/validate.py` passes with no errors
- [ ] New cases follow the two-file convention and reuse the section headings
- [ ] Any new term is defined in the glossary
- [ ] The case catalogue was regenerated with
      `python scripts/generate_catalog.py`
- [ ] No instructor-only content appears in student-facing files
- [ ] No commits, pushes, or history rewrites were made by automated tooling
