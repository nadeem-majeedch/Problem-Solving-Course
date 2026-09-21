# Deployment — GitHub Pages

The course website is published by a single GitHub Actions workflow:
`.github/workflows/pages.yml` (**Deploy Problem Solving Course to GitHub
Pages**). There is deliberately **no second deployment workflow** — CI
validation lives in `.github/workflows/validate.yml`, which never publishes
anything.

## Key addresses

| What | Value |
| --- | --- |
| GitHub repository | <https://github.com/nadeem-majeedch/Problem-Solving-Course> |
| Published website (project site) | <https://nadeem-majeedch.github.io/Problem-Solving-Course/> |

The site is a GitHub Pages **project site**: the repository name is part of
the URL path. It is *not* served from `https://nadeem-majeedch.github.io/`
(the user root). The built site uses only relative links, so every page,
image, stylesheet, and the search index resolve correctly under the
`/Problem-Solving-Course/` base path with no per-deployment configuration.

> Until the first workflow run has completed successfully, the website URL
> is *configured but not yet live*. Verify after deployment (section below).

## Required repository settings

1. **Settings → Pages → Build and deployment → Source: `GitHub Actions`.**
   This is the one setting that must be chosen manually. The workflow uses
   the documented Actions-based Pages deployment
   (`actions/configure-pages` + `actions/upload-pages-artifact` +
   `actions/deploy-pages`), which only runs when the Pages source is set to
   *GitHub Actions*.
2. Nothing else. No branch selection, no Jekyll settings, no environment
   secrets. The `github-pages` environment is created automatically by the
   first deployment.
3. The workflow triggers on pushes to `main` and via **Run workflow**
   (`workflow_dispatch`) in the Actions tab.

> If the repository is private on a free plan, Pages availability depends on
> your plan; the workflow itself is plan-independent.

## How to publish, step by step

1. Commit and push your reviewed changes to the `main` branch. (See the
   branch note in the repository README: the deployment workflow triggers
   on `main` and on manual runs only.)
2. Choose the Settings → Pages source (`GitHub Actions`) once, if not
   already chosen.
3. Either wait for the push-triggered run, or open the **Actions** tab,
   select **Deploy Problem Solving Course to GitHub Pages**, and click
   **Run workflow** → **Run workflow**.
4. Watch the run: the `build` job must finish green before the `deploy` job
   starts. Deployment happens only after every gate has passed.
5. Open <https://nadeem-majeedch.github.io/Problem-Solving-Course/> and
   verify.

## What runs before deployment

The `pages.yml` build job fails — and therefore never deploys — unless every
gate passes:

| Step | Gate |
| --- | --- |
| `generate_catalog.py` | Case metadata complete and consistent |
| `gen_topic_heatmap.py` | Heatmap regenerates; no unmapped case tags |
| `gen_slides.py` | Slide decks regenerate cleanly from lecture sources |
| `validate.py` | 32 lectures, 144 paired student/instructor cases, internal links, catalog |
| `pytest tests/ -q` | Tooling tests (renderer, builders, validators) |
| `build_site.py` | Public site builds; built-in leak check passes |
| `audit_site.py` | Built-artifact audit: coverage, links, navigation, a11y |
| Artifact verification | Required pages exist; 32 lecture plans; 32 slide decks; 144 case pages; **zero instructor-only paths** |

No step uses `|| true` or similar error suppression: a genuine failure at
any stage fails the job and blocks publication.

The instructor build (`build_instructor.py` → `public_instructor/`) is
**never** run in the deployment workflow and its output is never uploaded.
It exists only for local instructor use (see
[the instructor guide](instructor-guide.md#instructor-only-materials-and-distribution)).

## Inspecting workflow logs

1. Open the repository's **Actions** tab.
2. Click the run you care about (its commit message or "Run workflow").
3. The `build` job lists each gate as a step; the `deploy` job shows the
   Pages deployment. A failed step is marked red and can be expanded to see
   the exact validator output.
4. After a successful run, the deployment URL is also shown on the run
   summary page and in **Settings → Pages**.

## Troubleshooting failed builds

| Symptom | Meaning | Fix |
| --- | --- | --- |
| `Validate repository content and links` fails | Content-structure or link error | Run `python scripts/validate.py` locally; fix the reported error; push again |
| `Run tooling tests` fails | Tooling regression | Run `python -m pytest tests/ -q` locally; fix; push |
| `Build public student site` fails | Build error **or leak check hit** — instructor material reached `site/` | Inspect the step log; the leak lines name the offending file and pattern |
| `Audit built site` fails | Broken link/navigation/a11y in the artifact | Run `python scripts/audit_site.py` locally; fix the reported reference |
| `Verify artifact before upload` fails | Missing required pages, wrong case count, or banned content in `site/` | Rebuild locally and compare; never hand-patch `site/` |
| `Deploy to GitHub Pages` fails | Usually the Pages source is not `GitHub Actions`, or the environment is protected | Check Settings → Pages → Source; re-run the workflow |
| Run never starts on push | Push did not go to `main` | Push to `main` or use **Run workflow** manually |
| 404 at the site URL | First deployment not completed yet, or source is "Deploy from a branch" | Wait for the run / switch the source to `GitHub Actions` and re-run |

## Verifying the published website

After a green run:

1. Open <https://nadeem-majeedch.github.io/Problem-Solving-Course/> — the
   landing page shows the hero and the 32-lecture grid.
2. Spot-check navigation: Course, Outline, Cases (catalog), Lectures,
   Search — all under the `/Problem-Solving-Course/` prefix.
3. Open Lecture 01, a case page, the catalog, and `search.html` (try a
   query such as `binary search`).
4. Confirm images/CSS load (no unstyled pages).
5. Confirm no instructor-only material: URLs such as
   `/Problem-Solving-Course/case-studies/instructor/…` or
   `/Problem-Solving-Course/quizzes/keys/…` must 404 — see the
   content-separation section below.
6. Hard-refresh (Ctrl+F5) if an older deployment is cached.

## Local testing

Run the same sequence the workflow runs:

```bash
# 1. Regenerate derived content
python scripts/generate_catalog.py
python scripts/gen_topic_heatmap.py
python scripts/gen_slides.py

# 2. Validate content, links, and case pairing
python scripts/validate.py

# 3. Tooling tests
python -m pytest tests/ -q

# 4. Build the public site (includes the leak check)
python scripts/build_site.py

# 5. Audit the built artifact (links, navigation, a11y, leaks)
python scripts/audit_site.py

# 6. Inspect locally
python -m http.server 8000 --directory site
# open http://localhost:8000/
```

The full suite in one command (writes `qa-report.md`):

```bash
python scripts/qa_report.py
```

### Rebuilding the site

`build_site.py` wipes and rebuilds `site/` from scratch on every run —
never hand-edit anything under `site/`; edit the Markdown sources and
rebuild. Regenerated derived content (catalog, heatmap, slides) is likewise
overwritten; edit its sources.

### Validating links locally

- `python scripts/validate.py` — checks every Markdown link in the
  repository sources resolves to an existing file.
- `python scripts/audit_site.py` — checks every `href`/`src` in the built
  HTML resolves inside `site/`, and every `#fragment` has a matching `id`.

To test the deployment *mechanism* without GitHub, serve `site/` anywhere
static; the artifact contains only plain HTML/CSS/JSON with no server-side
requirements. Serving over HTTP (rather than opening files directly) is the
faithful local test: `search.html` loads its index via HTTP, and Pages
serves over HTTP too.

## Base-path behaviour

The generated site uses **relative links exclusively** (verified by the
build/audit tooling), so:

- it works locally at `http://localhost:8000/`,
- it works on the project site at
  `https://nadeem-majeedch.github.io/Problem-Solving-Course/`,
- no `site_url`, base-tag, or absolute-path configuration is required, and
  none should be introduced.

## Workflow versions used

Maintained, first-party actions only:

- `actions/checkout@v4`
- `actions/setup-python@v5`
- `actions/configure-pages@v5`
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
- Deployments are serialised by the `pages` concurrency group: a new run
  cancels a still-running obsolete one, so the latest push wins.

## What gets published

`site/` only: the handbook, 32 lecture plans + notes + examples + quizzes,
144 student case studies, the catalog, student-facing labs/quizzes/
assignments/projects/activities (without their `keys/`), slide decks, the
search page, and assets. Instructor solutions and answer keys are excluded
at build time and re-verified against the artifact before upload.

## Public/instructor content separation

**Never published to the website:**

- `case-studies/instructor/` (144 full solutions)
- every `keys/` directory: `quizzes/keys/`, `labs/keys/`,
  `activities/keys/`, `assignments/keys/`
- `lectures/lecture-*/teaching-notes.md`
- `docs/instructor-reports/` (instructor-only audits)
- the separate `public_instructor/` instructor build (gitignored, local
  only)

**How separation is enforced:**

1. `scripts/build_site.py` builds the public site by allowlist, physically
   excluding all of the above, then scans its own output for
   instructor-only solution phrasing (the same solution-heading markers
   the validator requires in instructor files) and fails the build on any
   hit.
2. `scripts/audit_site.py` re-checks the built artifact for banned paths
   and phrases, plus link/navigation integrity.
3. The deployment workflow re-verifies the artifact before upload: zero
   `instructor`/`keys`/`teaching-notes` paths, all required pages present,
   and case-page count equal to the source corpus (144).
4. `scripts/validate.py` verifies the 144 student/instructor pairs in the
   sources themselves.

Security comes from build-time exclusion, not from CSS hiding, hidden URLs,
or directory obscurity. `public_instructor/` must never be deployed or
committed; distribute it only through your institution's access-controlled
system.
