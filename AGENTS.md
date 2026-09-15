# Skill library entry

This repository is a reusable capability library, not the application being
built. Read this entry when the user asks to use the library. When editing the
library itself, also follow the maintenance section below.

## Bootstrap

1. Identify the user's task, requested mode, and target project from the current
   conversation and accessible workspace. Keep `library_root` and `project_root`
   distinct. Never create product code in this library unless it is the target.
2. Read [skills/INDEX.md](skills/INDEX.md). Use `skill-router` only when selection
   or sequencing is unclear; a clear specialist request may go directly to it.
3. Read the selected `SKILL.md` before applying it. Load supporting resources
   only as needed. Do not load all skills or infer their contents from names.
4. For new projects or materially new features, run the readiness check in
   `development-discovery`. Read available project evidence before asking.
   Critical product decisions must not be silently invented in code.
5. Preserve confirmed requirements, approval scope, evidence, unresolved
   decisions, and the next step across handoffs. Discovery and design are not
   permission to implement, deploy, publish, or change permissions.
6. Missing tools or inaccessible files are explicit limitations. Do not claim a
   skill ran, a test passed, or a UI was inspected without evidence.

## Boundaries

These are task instructions, not a system prompt or a security enforcement
mechanism. Respect host instructions, permissions, and target-project rules.
Surface conflicts instead of overriding them. A repository URL alone does not
install skills or make remote `AGENTS.md` files load automatically. Ask the host
to read this entry explicitly when automatic discovery is unavailable.

Project specs and plans belong in the target project (or the conversation when
file writing is not authorized), not in this library. Never copy credentials,
private transcripts, or project secrets into reusable skills.

## Maintaining this library

- Canonical source layout: `skills/<domain>/<skill-name>/SKILL.md`.
- Keep names stable and globally unique. Domain READMEs are documentation, not
  skills. `skills/INDEX.md` is the canonical repository routing index.
- Keep each skill self-contained. Refer to optional peer skills by name, not
  required relative paths that break after a leaf-folder installation.
- Use plain, single-line `name` and `description` frontmatter fields; put long
  explanations in the body or local references. This is a repository convention.
- Update the index, usage notes, and routing examples when behavior changes.
- Run `python3 scripts/library.py check` and
  `python3 -m unittest discover -s tests -v` before submitting a PR.
- Do not install skills, overwrite project instruction files, or merge PRs as an
  incidental part of maintaining this repository.
