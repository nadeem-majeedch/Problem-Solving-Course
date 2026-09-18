# Slides

Projection-ready slide decks for all 32 lectures, generated from the
course material so they can never drift from it.

## Preview (no toolchain needed)

Each deck is **one self-contained HTML file** — no application, no
network, no install.

```bash
python scripts/gen_slides.py        # regenerate decks from the curriculum
python -m http.server 8000          # from the repository root
# then open http://localhost:8000/slides/decks/index.html
```

Or simply open `slides/decks/lecture-01-slides.html` directly in any
browser. Keys: **→ / space** next · **←** back · **Home/End** jump ·
**Ctrl+P** prints the deck to PDF (one slide per page) for handouts.

The decks also ship inside the public site build (`site/slides/`), so
the same files serve as the course website's slide section.

## What is in a deck

Every deck follows the same instructional arc (the course's case rhythm):

1. **Title + learning objectives**
2. **The plan** — the four cases of the day
3. **Key definitions** (from the lecture notes)
4. **Worked examples** — problem, verified Python, expected output, cost
   (identical to the published `examples.md`, verification markers
   stripped for projection)
5. **Per case: attempt slide** (projected problem + the 5-minute
   instruction) **then a discussion slide** (student prompts; a hidden
   pointer to the instructor distribution)
6. **Common misconceptions** check
7. **Summary + exit question** — expected answers live only in the
   hidden speaker-notes layer

Design language: serif body at projection sizes, one accent colour pair,
dark code blocks with syntax highlighting, one idea per slide, no
paragraph walls. Speaker notes are embedded but hidden (`.notes`,
display:none) and can be surfaced by removing that CSS rule.

## Student/instructor separation

Decks contain **no solution content**: every reveal slide is a stub
pointing to the case's page in the instructor distribution
(`python scripts/build_instructor.py`). Exit-question answers ride in
the hidden notes layer only. The leak checker in `scripts/build_site.py`
runs over the copied decks exactly as over every other public page.

## Toolchain (for maintainers)

`scripts/gen_slides.py` extracts from the single sources of truth:

| Deck element | Extracted from |
| --- | --- |
| Title, objectives, exit questions | `lectures/lecture-NN/plan.md` |
| Definitions, misconceptions | `lectures/lecture-NN/notes.md` |
| Worked examples + verified Python | `lectures/lecture-NN/examples.md` |
| Case prompts, difficulties, discussion starters | `case-studies/student/cs-NNN*.md` |

Regeneration is idempotent and takes ~1 second. Edit the curriculum,
re-run, and the decks follow. The Python shown on slides is the same
code the validator executes, so slide snippets stay correct by
construction.
