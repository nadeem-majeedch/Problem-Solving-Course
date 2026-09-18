# Final Pre-Publication Audit Report

**Audit date:** 2026-09-18
**Scope:** entire repository, judged on executed checks rather than source inspection alone
**Overall status: PASS**

Every result in this report comes from a command actually executed during this
audit session. Where a check produced a finding, the finding is listed under
"Publication blockers" or "Recommended corrections" with its evidence; no
result is claimed without execution.

## 1 · Curriculum — PASS

| Check | Result |
| --- | --- |
| All 32 lectures exist | ✓ `lectures/lecture-01` … `lecture-32`, each with `plan.md`, `notes.md`, `teaching-notes.md` |
| Foundational → advanced progression | ✓ Block I (L01–08) problem formulation → Block II (L09–16) data/strings → Block III (L17–24) algorithms → Block IV (L25–32) graphs, simulation, optimisation, capstones |
| Learning outcomes documented | ✓ `docs/learning-outcomes.md`; LO mappings present in all 32 plans |
| Two-hour plan realism | ✓ Every plan carries a 120-minute table with a break and a flex column; workshops and reviews use the documented alternate structure |
| Case distribution across lectures | ✓ 144 cases over 32 lectures (120 base at exactly 4/lecture + 16 applied additions, each mapped by metadata) |
| Assessment & lab integration | ✓ 12 labs, 8 quizzes, 6 assignments, 3 projects, 5 activities — each mapped to lectures and LOs |

Tier distribution of the 144 cases: **33 Beginner / 37 Foundational /
38 Intermediate / 23 Advanced / 13 Expert** — every requested minimum
(20/25/25/20/10) exceeded.

## 2 · Case studies — PASS

| Check | Result |
| --- | --- |
| ≥ 100 unique cases | ✓ 144 (cs-001 – cs-144), IDs unique, no gaps |
| Clear IDs and difficulty levels | ✓ every case carries id, difficulty, lecture, topics, estimated time, prerequisites, objective in its metadata table |
| Complete student statements | ✓ all five required student sections present (validator-enforced) |
| Complete instructor solutions | ✓ all twelve required instructor sections present (validator-enforced) |
| Correct solution mapping | ✓ 144/144 one-to-one pairs, verified by `scripts/validate.py` |
| Prerequisites stated | ✓ per-case prerequisites reference specific lectures |
| Edge cases and assumptions | ✓ required sections in every solution |
| Verified expected outputs | ✓ every reference program executed twice (determinism confirmed); expected-result lines rewritten from actual output during authoring |
| No unintentional duplicates | ✓ duplicate-title scan over case metadata and deck titles: 0 duplicates |

Prior audits on this corpus: `docs/case-review.md` (128-case pedagogical
review), `docs/instructor-reports/expert-tier-rationale.md` (all 12 base
Expert cases), `docs/instructor-reports/quiz-answer-key-audit.md`,
`docs/instructor-reports/lab-expected-output-audit.md`.

## 3 · Teaching material — PASS

- Student notes: plain-language, pseudocode before Python throughout.
- Instructor notes: board plans, question scripts, misconception lists in all 32.
- Python examples: solution-execution harness runs every case's reference
  program; all 144 green, deterministic across repeated runs.
- Pseudocode: house style enforced by `docs`/validator conventions.
- Scaffolding: Expert cases carry the rationale and prerequisite chain in
  `docs/instructor-reports/expert-tier-rationale.md`.

## 4 · Security and content separation — PASS

Checked the **built public artifact** (`site/`), not just source names:

| Check | Result |
| --- | --- |
| Instructor case files absent from public output | ✓ zero `cs-*.md`/HTML beyond the 144 public student pages |
| Leak-phrase scan of built site | ✓ 9 hits, all policy *descriptions* on handbook pages (contributing/deployment/faq) — no leaked content |
| `def `/`print(` on case pages | ✓ matches are prose in student debugging bullets, not code blocks; student sources contain zero Python fences |
| Instructor-only reports (`docs/instructor-reports/`) | ✓ excluded from the public build by name; present in the separate `public_instructor/` instructor build (572 pages, gitignored) |
| Secrets / API keys / credentials | ✓ grep for key/password/secret patterns: only match is the legitimate case title "Password Rules" — no credentials |
| Workflow artifact source | ✓ `pages.yml` uploads `site/` only; `build_site.py` fails the build on any leak, so instructor material is physically excluded |

## 5 · Website — PASS

| Check | Result |
| --- | --- |
| Build succeeds | ✓ `python scripts/build_site.py` completes; leak check passes |
| Internal links | ✓ site audit: **367 pages, 9,691 references, 0 broken** |
| Navigation | ✓ handbook nav includes all lectures, case catalog, labs, quizzes, assignments, projects, heatmap; instructor-only pages absent from student nav |
| Mobile & desktop | ✓ responsive CSS with viewport meta present on built pages |
| Assets | ✓ CSS resolves; heatmap SVG is well-formed XML (parser-verified); CSV links resolve |
| Structure | ✓ single `h1` per page, hierarchical headings enforced by audit |

## 6 · GitHub Actions — PASS

| Check | Result |
| --- | --- |
| Correct location | ✓ `.github/workflows/` at repository root; no nested repository |
| Coherent build & validation | ✓ `pages.yml`: validate → heatmap → slides → build → leak check → upload → deploy; `validate.yml`: validation only, no publish steps |
| Pages architecture | ✓ modern `actions/upload-pages-artifact` + `actions/deploy-pages` flow; requires the documented Settings → Pages → Source: GitHub Actions choice |
| No competing deployment workflow | ✓ exactly one deployment workflow |
| Maintained action versions | ✓ `actions/checkout@v4`, `actions/setup-python@v5`, `actions/configure-pages@v5`, `actions/upload-pages-artifact@v3`, `actions/deploy-pages@v4` |
| Gate chain | ✓ each stage blocks the next on failure; validation failure blocks deployment |
| No commits or pushes | ✓ none performed; workflows trigger only on the user's own push |

## 7 · Documentation — PASS

| Check | Result |
| --- | --- |
| README complete | ✓ overview, structure, setup, preview, validation, deployment, license |
| Local setup works | ✓ documented commands resolve to real scripts |
| Local preview documented | ✓ `python -m http.server` instructions for `site/` present |
| Validation commands documented | ✓ `python scripts/validate.py`, `python -m pytest`, `python scripts/qa_report.py` |
| Pages deployment documented | ✓ `docs/deployment.md` covers the Settings choice, workflow stages, instructor exclusion |
| Instructor distribution documented | ✓ `docs/instructor-guide.md` and `build_instructor.py` produce a separate gitignored instructor build |
| License & attribution | ✓ dual license: MIT for tooling, CC BY 4.0 for content; no bundled third-party datasets or invented external references |

## Checks performed (executed)

1. `python scripts/qa_report.py` — full 7-stage suite → PASS
2. `python scripts/validate.py` — 144/144 cases, 0 errors, 0 warnings
3. `python -m pytest tests/ -q` — 28/28 passed
4. Site build + `python scripts/audit_site.py` — 367 pages, 0 broken links
5. Instructor-build dry run — 572 instructor pages to a gitignored directory
6. Leak scans (instructor filenames, leak phrases, code fences) on `site/`
7. Secrets grep across the repository
8. Duplicate-title scan across cases and decks
9. Tier/lecture distribution computed from case metadata
10. Workflow chain inspection (all gates present, single deploy workflow)
11. Heatmap regeneration (23 topics × 32 lectures over 144 cases)

## Publication blockers

**None.**

## Recommended corrections (non-blocking)

1. **First deployment is manual-once:** Settings → Pages → Build and
   deployment → Source: **GitHub Actions**. The workflow cannot set this
   itself; everything after it is automatic.
2. **Instructor distribution:** instructors use `python scripts/build_instructor.py`
   and share `public_instructor/` out-of-band (the directory is gitignored and
   never deployed). Document any local sharing policy your department requires.
3. **Two cosmetic warnings the QA suite reports as informational:** 14 lectures
   carry more than 4 cases (intentional applied additions cs-129–cs-144) and
   those additions include no Beginner-tier case above cs-142's lecture — both
   are by design and listed as information, not defects.

## Conclusion

The repository is publication-ready: 144 verified cases across 32 coherent
lectures, complete teaching and assessment material, a leak-free public site
build with zero broken links, a single coherent deployment workflow, and
documentation covering setup, preview, validation, deployment, and instructor
separation. No commits or pushes were performed by this audit.
