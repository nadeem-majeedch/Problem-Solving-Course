# Resources

This course deliberately requires almost nothing beyond a computer and a
browser. No datasets, libraries, or accounts are needed; every case generates
its own data.

## Software setup (students)

**Python.** You need Python 3.10 or newer. Install it from the installer your
institution provides, or search the web for "python download" and follow the
official result for your operating system. On the first screen of the
installer, tick "Add Python to PATH" (Windows) or use the defaults
(macOS/Linux). Verify in a terminal:

```bash
python --version   # or: python3 --version on macOS/Linux
```

**Editor.** Any of these is fine; pick one and stay with it for the semester:

- the editor that ships with your operating system + a terminal;
- a free code editor such as VS Code (search "VS Code download" for the
  official installer), with the Python extension;
- IDLE, which installs together with Python.

**Running programs.** From a terminal in the folder containing your file:

```bash
python my_solution.py
```

For quick experiments, open the interactive console by typing `python3` with
no file name. Type `exit()` to leave.

**This course site.** The public site is static Markdown. To read it locally,
build it (`python scripts/build_site.py`) and open `site/index.html` in a
browser — no server needed for reading, though `python -m http.server 8000`
from `site/` also works.

## Pseudocode style

Use the course's pseudocode conventions from
[resources/pseudocode-style.md](../resources/pseudocode-style.md) — the same
style is used in solutions, so early alignment pays off.

## Flowcharts

Draw on paper first. Standard shapes only: rounded box = start/end, rectangle
= process, diamond = decision, parallelogram = input/output, arrow = flow.
Lecture 03 teaches the notation; every later case may be answered with one.

## Study strategy that matches this course

1. **Attempt before you read anything.** The five-minute in-class attempt is
   the learning event; reading solutions without attempting teaches almost
   nothing.
2. **Keep an error journal.** One line per bug: symptom → cause → fix. By week
   eight you will see your personal top-three error patterns.
3. **Re-solve from scratch.** A week after each lecture, re-do one case
   without notes. If you cannot, reread the lecture plan's synthesis section.
4. **Explain out loud.** Pseudocode is a language for explaining; practising
   the explanation is practising the skill the course grades.
5. **Use extensions honestly.** Extensions are enrichment, not obligations.
   Attempting one extension deeply beats skimming five.

6. **Navigate by the catalog, not by file listing.** The
   [Case-Study Catalog](../case-studies/CATALOG.md) sorts all 144 cases by
   lecture, difficulty, and topic; the [Topic-Coverage
   Heatmap](topic-coverage-heatmap.md) shows which lectures exercise which
   skills — use both to plan revision.
7. **Keep a weekly rhythm.** After each lecture: redo one case cold (rule 3),
   attempt the next lecture's first Beginner case as a warm-up, and file your
   error-journal entries (rule 2). Fifteen minutes, three times a week,
   beats one long cram.
8. **Prepare for quizzes and the exam by re-deriving, not rereading.** Each
   lecture's `quiz.md` is the honest check: attempt it closed-book, then
   rework anything you missed. For the exam, rebuild one case per block from
   a blank page — if you can produce the pseudocode and the trace, you are
   ready; if you cannot, the gap is specific and findable.

## For instructors

- Lecture plans and solution walkthroughs are in the instructor build
  (`scripts/build_instructor.py` → `public_instructor/`).
- The [Glossary](glossary.md) doubles as a source of definitions you can paste
  into slides.
- All materials are Markdown; you can adapt them with any editor. Keep case
  IDs stable when editing (see [CONTRIBUTING](../CONTRIBUTING.md)).

## Searching for more

The course avoids bundling external links so nothing rots. When you want more
on a topic, search for the exact technique name from the lecture (for example
"binary search visualization", "trace table practice", "dynamic programming
introduction") and prefer official documentation or university pages in the
results. Verify anything you read against a case from this course.
