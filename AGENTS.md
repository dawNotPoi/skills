# Agent entry

This repository is a reusable skill library, not the application being built.
These instructions are workflow guidance. They do not override the user's
current request, the target project's instructions, or the host's permissions.

## Using the library

1. Resolve `LIBRARY_ROOT` (this checkout or a readable repository URL/ref) and
   `PROJECT_ROOT` (the actual target). Reuse paths already supplied. Reading
   this repository does not authorize editing it or installing anything.
2. Read [skills/INDEX.md](skills/INDEX.md). This is the canonical capability
   catalog. Read only the selected leaf `SKILL.md` and the resources it needs.
   If routing is ambiguous, load `skill-router`; otherwise go directly to the
   matching skill. Do not load every skill or recursively invoke the router.
3. Read the target project's applicable instructions, existing decisions and
   relevant code before asking questions. Record confirmed facts separately
   from inferences, proposed defaults and unresolved decisions.
4. For a new project or materially new feature with critical unknowns, use
   `development-discovery`. Do not resolve product behavior implicitly in
   implementation. Give options, trade-offs and a recommendation; ask one
   high-impact question at a time, at most three closely related questions.
5. Keep discovery, design approval, implementation authorization and external
   action permissions distinct. A draft spec, a selected option, or an agent's
   recommendation is not blanket permission to code. Reuse explicit approval
   already given for the current scope; do not repeatedly ask for it.
6. A precise, low-risk fix can use a compact inline spec and plan. Learning,
   review-only and writing requests do not need a development interview.
7. Resolve skills by their stable `name` using the host's available metadata
   or this index. A handoff is instructions, not a promise that the host can
   spawn agents or execute scripts. Never claim unavailable tools were used.
8. Write project specs/plans/evidence into `PROJECT_ROOT`, following its
   conventions, only within authorized writes. With read-only tools, provide
   the artifacts in the conversation and mark them as unsaved. Never store
   credentials, raw private transcripts or business artifacts in this library.
9. Report what was verified, what was only inspected, what remains blocked,
   and the next decision. Missing rendering tools mean visual QA is unverified.

For a remote library, resolve relative paths against the same repository and
ref, not the target project. Pin a commit for reproducible work when possible.
When access fails, explain the specific missing resource; do not invent paths,
capabilities or successful loads. See [docs/usage.md](docs/usage.md).

## Maintaining this library

When explicitly asked to change this library, it becomes `PROJECT_ROOT`.
Preserve existing skill names and resources unless a rename is authorized.
Keep domain folders one level above leaf skills. Update the canonical index,
entry links and migration guidance in the same change. Do not copy the entire
library entry into another project's AGENTS.md or CLAUDE.md.

Run `python3 scripts/check_library.py` and
`python3 -m unittest discover -s tests -p 'test_*.py'` when execution is available.
Use [tests/behavior-cases.md](tests/behavior-cases.md) for manual host evaluation;
structural checks do not prove semantic compliance. Do not merge or deploy
merely because creating a pull request was authorized.
