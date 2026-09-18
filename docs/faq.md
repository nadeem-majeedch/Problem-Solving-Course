# FAQ

## For students

**Do I need programming experience?**
No. The course assumes none. Weeks 1–3 deliberately use pseudocode and
flowcharts before Python appears in Lecture 04. Students who already program
should attempt the case extensions instead of finishing early.

**I'm in semester 1 — will Advanced and Expert cases count against me?**
No. Only core cases and the graded components count. Advanced/Expert cases
are discussion targets: the class reasons together, and the instructor's
reveal does the heavy lifting. You are expected to follow the *reasoning*, not
reproduce it in week 2.

**Why pseudocode first?**
Because the course grades reasoning, not syntax. Pseudocode lets you show the
algorithm before you fight a language. From Block III you may go straight to
Python, but every discussion still asks *why* it works.

**What if I can't solve a case in five minutes?**
That is normal — most students can't solve most cases at first. Write what you
*would* try: a diagram, a smaller example, a question. That is a serious
attempt and earns full participation credit.

**Is Python the only language?**
Examples and solutions are Python because it is the CS and DS teaching
standard here. If your programme uses another language in parallel courses,
you may still submit pseudocode or flowcharts for participation.

**How much work outside class?**
About 30 minutes per lecture of optional but strongly recommended practice
(re-solving one case), plus assignments, labs, and the project.

**Where are the solutions?**
With your instructor. Public pages show student-facing problem statements
only; publishing solutions would defeat the attempt-first method.

## For instructors

**Can I show the instructor page on the projector by mistake?**
Guard against it: keep student and instructor tabs in different windows and
close the instructor window during the attempt phase. The instructor page
title names the approach, which spoils the discussion.

**The class solves everything instantly — what now?**
Release the Extensions, then move to the next lecture's first case. Every
student page carries optional extensions sized for this situation.

**The class solves nothing — what now?**
Check you are not skipping the *What to notice* observation question; it gives
every student a foothold. Then use the instructor page as a worked mini-lecture
and continue. Discussion-target cases are designed for this.

**Can I reorder lectures or cases?**
Within a block, yes — cases are tagged with the lectures that reference them,
and the validator checks those references. Across blocks, no: the course
builds deliberately (e.g., recursion in Lecture 22 needs invariants from 19).

**Can I publish a modified student site for my section?**
Yes. Build with `scripts/build_site.py` — instructor material is excluded at
build time and the build fails if it detects any solution file in the output.
Never deploy `public_instructor/` anywhere public.

**How do I add my own cases?**
Follow [CONTRIBUTING](../CONTRIBUTING.md): a student file and an instructor
file sharing one ID and slug, difficulty and lecture metadata, and regenerate
the catalog. The validator will catch mismatches.

**Is this enough for a full semester of a 2-2 schedule?**
Yes: 32 meetings of 2 hours. For 3-credit variants, use the adaptation notes
in the [Instructor Guide](instructor-guide.md#adaptation-notes).

## Technical

**Why a static site with no framework?**
Plain HTML generated from Markdown is readable forever, needs no toolchain
for readers, and keeps the GitHub Pages deployment a single workflow with no
dependencies to break.

**What exactly does the validator check?**
Required files, case ID uniqueness and pairing, difficulty and lecture
reference validity, all internal links, required headings in lecture plans,
and that no instructor-only material appears in student pages or the public
build. See [CONTRIBUTING](../CONTRIBUTING.md) for the list.

**The build failed with a leak error — what does that mean?**
A file matching instructor patterns (an `instructor/` path or a solution
heading) reached the public output. Do not bypass it; find how the file got
there. This check exists because the strongest safeguard against leaking
solutions is refusing to ship them.
