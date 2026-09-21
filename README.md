# Problem Solving — Computer Science & Data Science

**32 lectures · 2 hours each · 64 teaching hours · 144 interactive case studies**

**Published website:** https://nadeem-majeedch.github.io/Problem-Solving-Course/

A complete, classroom-ready course in problem solving for first-, second-, and
third-semester students of Computer Science and Data Science. Every lecture is
built around short, projector-displayed case studies: students get about five
minutes to attempt each case, then the class discusses the solution, the
reasoning behind it, and alternative approaches.

This repository contains **all original teaching material**: lecture plans,
case studies with instructor solutions, labs, activities, quizzes with answer
keys, assignments, term projects, and reproducible build/validation tooling.

## Who it is for

- **Students**: anyone with basic high-school mathematics. No prior programming
  is assumed; Python is introduced gradually inside the cases themselves.
- **Instructors**: every case study ships with a complete instructor-only
  solution, reasoning walkthrough, edge cases, alternatives, and a discussion
  prompt, so a case can be taught without extra preparation.

## Learning goals

Graduates of this course can:

1. Understand and analyse a problem before writing any code (LO1, LO2).
2. Identify inputs, outputs, constraints, assumptions, and edge cases (LO1).
3. Decompose complex problems and design algorithms with structured reasoning
   (LO1, LO2).
4. Write, read, and trace pseudocode and flowcharts (LO3).
5. Reason about Python programs and translate designs into code (LO4).
6. Trace, debug, and test systematically (LO5, LO6).
7. Apply mathematical and logical reasoning to concrete problems (LO8).
8. Reason about algorithm efficiency and compare alternatives (LO7).
9. Solve data-oriented and real-world problems — cleaning, aggregating,
   scheduling, simulating, and communicating results (LO9).
10. Choose among strategies — searching, sorting, recursion, greedy,
    backtracking, graphs, dynamic programming — and justify the trade-offs
    (LO10).

The full outcome map (what is taught, practised, and assessed where) is in
[docs/learning-outcomes.md](docs/learning-outcomes.md).

## Key documents

| Document | Purpose |
| --- | --- |
| [docs/course-overview.md](docs/course-overview.md) | What the course is and how it is organised |
| [docs/learning-outcomes.md](docs/learning-outcomes.md) | Outcomes LO1–LO10 and where each is taught and assessed |
| [docs/course-outline.md](docs/course-outline.md) | Week-by-week map of all 32 lectures |
| [docs/teaching-methodology.md](docs/teaching-methodology.md) | The 5-minute case method, differentiation, and classroom rhythm |
| [docs/assessment-plan.md](docs/assessment-plan.md) | Grading scheme and rubrics |
| [docs/instructor-guide.md](docs/instructor-guide.md) | How to run a lecture hour, handle mixed ability, and use solutions |
| [docs/deployment.md](docs/deployment.md) | GitHub Pages settings, workflow gates, and local testing |
| [docs/resources.md](docs/resources.md) | Terminal/Python setup and study strategy (no external links required) |
| [docs/glossary.md](docs/glossary.md) | Terms used across the course |
| [docs/faq.md](docs/faq.md) | Common questions from students and instructors |
| [docs/handover-report.md](docs/handover-report.md) | Repository handover: stack, commands, and remaining manual tasks |
| [case-studies/CATALOG.md](case-studies/CATALOG.md) | Auto-generated catalogue of all 144 cases |

## Repository structure

```
docs/                     Course handbook (11 public pages) + instructor audit
                          reports (docs/instructor-reports/, never published)
lectures/lecture-01..32/  plan.md + teaching pack per lecture (student notes,
                          verified worked examples, lecture quiz, instructor-only
                          teaching notes)
case-studies/student/     144 student-facing problem pages (cs-001 … cs-144)
case-studies/instructor/  144 matching full solutions (not published to students)
labs/                     12 guided labs + instructor checkpoint notes (keys/)
activities/               5 in-class non-graded activities + lecture-by-lecture
                          case facilitation map (instructor only)
quizzes/                  8 quizzes + separate answer keys (keys/)
assignments/              6 assignments + 6 rubrics + instructor marking keys
projects/                 3 term projects + proposal template + progress
                          checklist + rubric
resources/                Python/terminal starter guide and pseudocode style sheet
slides/                   Slide deck source and publishing workflow
scripts/                  Build and validation tooling (Python 3, no dependencies)
tests/                    Tooling tests (pytest)
.github/workflows/        CI validation and GitHub Pages deployment
```

## How to browse the student material

- **On the built site**: run the preview below and open the landing page —
  it carries the 32-lecture grid, the case catalog, and a browser-side search
  (`search.html`).
- **From the source tree**: start at `docs/index.md` (site map), then follow
  the [Course Outline](docs/course-outline.md), which links all 32 lecture
  plans; each plan links its cases. `case-studies/CATALOG.md` lists every case
  with difficulty, lecture, and topic tags.
- **Difficulty levels** used throughout: **Beginner · Foundational ·
  Intermediate · Advanced · Expert** (33 / 37 / 38 / 23 / 13 across the 144
  cases). Case IDs (`cs-NNN`) are stable and never renumbered.

## Case-study ID scheme

Every case has a stable identifier `cs-NNN` that never changes once assigned:

```
cs-001   difficulty: Beginner      topics: decomposition
cs-027   difficulty: Intermediate  topics: patterns, grids
cs-112   difficulty: Expert        topics: algorithm analysis, strategy
cs-129 … cs-144   applied cases: data science, systems, and communication
                  scenarios integrated into existing lectures
```

## Repository

- **GitHub repository:** <https://github.com/nadeem-majeedch/Problem-Solving-Course>
- **Published website:** <https://nadeem-majeedch.github.io/Problem-Solving-Course/>

## Published Website

The website is configured for publication through GitHub Pages. After the
workflow is enabled (one manual setting, below) and the repository is pushed,
it will be available at:

> **https://nadeem-majeedch.github.io/Problem-Solving-Course/**

This is a *project site*: the repository name (`Problem-Solving-Course`)
appears in the URL path. Every link in the built site is repository-relative,
so it works identically under this base path and in local preview — no
configuration change is needed for either.

**What it publishes** (`site/`, built by `scripts/build_site.py`): the
handbook, all 32 lectures (plans, notes, worked examples, quizzes), all 144
student case studies, the case catalog, student-facing labs / assignments /
projects / activities / resources, slide decks, and browser-side search.

**What it never publishes:** instructor solutions, every `keys/` answer-key
directory, lecture `teaching-notes.md`, and `docs/instructor-reports/`. The
build's leak check fails loudly if any of this material reaches the output,
and the deployment workflow re-verifies the artifact before upload.
Instructors get a separate `public_instructor/` build (including a search
over solutions) via `python scripts/build_instructor.py`.

**Enabling deployment (one-time, manual):**

1. Settings → Pages → Build and deployment → **Source: GitHub Actions**.
2. Push to `main` (or open the Actions tab and run
   **Deploy Problem Solving Course to GitHub Pages** manually).
3. When the workflow finishes, the URL above is live.

Until the first successful workflow run has completed, treat the URL above
as *configured but not yet verified*.

## Quick start

```bash
# Validate everything (links, case metadata, solution mapping, lecture references)
python scripts/validate.py

# Run the tooling test suite
python -m pytest tests/ -q

# Generate/refresh the case catalogue
python scripts/generate_catalog.py

# Build the public student site into site/
python scripts/build_site.py

# Preview the built site locally
python -m http.server 8000 --directory site
```

## Local preview and Pages parity

`python -m http.server 8000 --directory site` serves the same files GitHub
Pages will publish. Serving over HTTP (not opening files directly) matters:
`search.html` fetches its index, and some browsers restrict local-file
pages, so an HTTP server is the faithful local test. Because all site links
are relative, this preview is an accurate simulation of the project-site
URL — but it is not the deployment itself; only a completed workflow run
publishes the site.

## GitHub Pages

`python scripts/build_site.py` renders the handbook, all 32 lectures, all
student case studies, and the student-facing quizzes, labs, assignments,
projects, and activities into `site/`, with a landing page and a
dependency-free browser search (`search.html`). Instructor solutions and
**every `keys/` directory are physically excluded** — the build fails loudly
if any solution material appears in the output. Instructors get a separate
`public_instructor/` build (including a search over solutions) via
`python scripts/build_instructor.py`.

To publish: choose **Settings → Pages → Build and deployment → Source:
GitHub Actions**, then push to `main` — `.github/workflows/pages.yml`
("Deploy Problem Solving Course to GitHub Pages") validates, builds,
leak-checks, and deploys automatically. Full details and the pre-deploy
gate list are in [docs/deployment.md](docs/deployment.md).

> Security note: a private directory is **not** a guarantee of secrecy once
> deployed. The public Pages build physically excludes instructor files rather
> than relying on obscurity.

## Commits and pushes are performed by the instructor

This repository ships as a **handover package**: all automation (validation,
site build, deployment workflow) runs *on demand*, and nothing in this
repository ever commits, pushes, or publishes by itself. The course
instructor performs every `git commit` and `git push` manually, at their own
pace, and retains full control of what is published and when. Suggested
first push after review:

```bash
git add -A
git commit -m "Problem Solving course: 32 lectures, 144 case studies"
git push origin main
```

> Branch note: this checkout is currently on the `master` branch and the
> remote repository has no commits yet. The deployment workflow triggers on
> `main` (and manual runs), so either push the course as `main` directly
> (`git push origin master:main`) and make `main` the default branch, or
> create `main` locally first (`git branch -m master main` before the first
> push). Both leave the history intact.

## Status

All 32 lectures, 144 case studies with solutions, and all supporting materials
are complete and validated by `scripts/validate.py`. See
[docs/course-outline.md](docs/course-outline.md) for the full map.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Validation must pass for every change
to teaching content.

## License

Dual license: MIT for tooling code, CC BY 4.0 for teaching content — see
[LICENSE](LICENSE).
