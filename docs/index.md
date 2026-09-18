# Problem Solving — Computer Science & Data Science

> The course handbook: how the course works, what is assessed, and how to
> navigate 32 lectures and 144 student case studies.

- New here? Read [Course Overview](course-overview.md) first.
- Planning your semester? See the [Course Outline](course-outline.md) —
  it links every lecture and lists the cases used in each.
- Teaching this course? [Teaching Methodology](teaching-methodology.md) and the
  [Instructor Guide](instructor-guide.md) are for you.
- Looking for a term? Check the [Glossary](glossary.md) or [FAQ](faq.md).

The homepage of the built site additionally carries the 32-lecture grid and
direct links to every material type.

## What is public, and what is not

The public site publishes the handbook, all lecture plans and notes, all
**student-facing** case studies, quizzes (without answer keys), and the
student side of labs, assignments, projects, and activities. Instructor
solutions and every answer-key directory are **excluded at build time** —
the build fails loudly rather than publish them. Full instructor materials
are distributed separately (see
[Instructor Guide](instructor-guide.md#instructor-only-materials-and-distribution)).

## Site map

- [Course Overview](course-overview.md)
- [Learning Outcomes](learning-outcomes.md)
- [Course Outline](course-outline.md) — all 32 lectures with case ranges
- [Teaching Methodology](teaching-methodology.md)
- [Assessment Plan](assessment-plan.md)
- [Instructor Guide](instructor-guide.md)
- [Resources](resources.md)
- [Glossary](glossary.md)
- [FAQ](faq.md)
- [Deployment](deployment.md) — how the site is built and published
- [Handover Report](handover-report.md) — repository handover: stack, commands, and the instructor's remaining manual tasks
- [Final Audit Report](final-audit-report.md) — pre-publication audit across curriculum, cases, security, site, and workflows
- [Case Review](case-review.md) — pedagogical audit of all 128 cases
- [Topic-Coverage Heatmap](topic-coverage-heatmap.md) — which topics the
  cases cover, lecture by lecture (with [CSV](topic-coverage-heatmap.csv)
  and [SVG heatmap](assets/topic-coverage-heatmap.svg))
- [Case-study catalog](../case-studies/CATALOG.md) — all 144 cases
- Lectures 01–32 — each folder holds the plan, notes, worked examples,
  and the lecture quiz (see the outline for per-lecture links)

## Using this repository

Everything is plain Markdown validated by `scripts/validate.py`. To rebuild
the site locally:

```bash
python scripts/build_site.py
python -m http.server 8000 --directory site
```

The site is dependency-free (plain HTML + one stylesheet); `search.html`
runs entirely in the browser over `pages.json`.

## License

Tooling is MIT-licensed; teaching content is CC BY 4.0. See [LICENSE](../LICENSE).
