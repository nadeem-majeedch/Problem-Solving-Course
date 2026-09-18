# Deployment — GitHub Pages

The course website is published by a single GitHub Actions workflow:
`.github/workflows/pages.yml`. There is deliberately **no second deployment
workflow** — CI validation lives in `.github/workflows/validate.yml`, which
never publishes anything.

## Required repository settings

1. **Settings → Pages → Build and deployment → Source: `GitHub Actions`.**
   This is the one setting that must be chosen manually. The workflow uses
   the documented Actions-based Pages deployment
   (`actions/upload-pages-artifact` + `actions/deploy-pages`), which only
   runs when the Pages source is set to *GitHub Actions*.
2. Nothing else. No branch selection, no Jekyll settings, no environment
   secrets. The `github-pages` environment is created automatically by the
   first deployment.
3. The workflow triggers on pushes to `main` and via **Run workflow**
   (`workflow_dispatch`) in the Actions tab.

> If the repository is private on a free plan, Pages availability depends on
> your plan; the workflow itself is plan-independent.

## What runs before deployment

The `pages.yml` build job fails — and therefore never deploys — unless every
gate passes:

| Step | Gate |
| --- | --- |
| `generate_catalog.py` | Case metadata complete and consistent |
| `gen_slides.py` | Slide decks regenerate cleanly from lecture sources |
| `validate.py` | 32 lectures, 144 paired student/instructor cases, internal links, catalog |
| `pytest tests/ -q` | Tooling tests (renderer, builders, validators) |
| `build_site.py` | Public site builds; built-in leak check passes |
| Artifact verification | Required pages exist; 32 lecture plans; 32 slide decks; 144 case pages; **zero instructor-only paths** |

The instructor build (`build_instructor.py` → `public_instructor/`) is
**never** run in the deployment workflow and its output is never uploaded.
It exists only for local instructor use (see
[the instructor guide](instructor-guide.md#instructor-only-materials-and-distribution)).

## Local testing

Run the same sequence the workflow runs:

```bash
# 1. Regenerate derived content
python scripts/generate_catalog.py
python scripts/gen_slides.py

# 2. Validate content, links, and case pairing
python scripts/validate.py

# 3. Tooling tests
python -m pytest tests/ -q

# 4. Build the public site (includes the leak check)
python scripts/build_site.py

# 5. Inspect locally
python -m http.server 8000 --directory site
# open http://localhost:8000/
```

To test the deployment *mechanism* without GitHub, serve `site/` anywhere
static; the artifact contains only plain HTML/CSS/JSON with no
server-side requirements.

## Workflow versions used

Maintained, first-party actions only:

- `actions/checkout@v4`
- `actions/setup-python@v5`
- `actions/upload-pages-artifact@v3`
- `actions/deploy-pages@v4`

## Runtime and reproducibility

- Python **3.12** (`actions/setup-python@v5`).
- The site build is **stdlib-only** — no third-party runtime dependencies.
- Test tooling is pinned in `requirements-dev.txt`
  (`pytest==8.3.4`), installed with `pip install -r requirements-dev.txt`
  after upgrading `pip`. There are no binaries to lock (`pip-tools`,
  hash-pinning) because the only dependency is pure-Python and the build
  itself installs nothing.
- Every push to `main` rebuilds the site from source; Pages never serves
  stale committed output.

## What gets published

`site/` only: the handbook, 32 lecture plans + notes + examples + quizzes,
144 student case studies, the catalog, student-facing labs/quizzes/
assignments/projects/activities (without their `keys/`), slide decks, the
search page, and assets. Instructor solutions and answer keys are excluded
at build time and re-verified against the artifact before upload.
