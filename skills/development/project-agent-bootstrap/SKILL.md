---
name: project-agent-bootstrap
description: Bootstrap or refactor a repository's long-lived Agent instruction harness across AGENTS.md, Claude Code, Cursor, and other hosts. Use when initializing project Agent entry files, consolidating duplicated instructions, deciding what belongs in AGENTS.md versus host adapters, skills, or specs, or adding multi-host discovery without prompt drift. Inspect existing instructions first; preserve user rules and do not overwrite project files without authorization.
---

# Project Agent Bootstrap

Build a maintainable project-level Agent harness, not a pile of copied prompts.
The default outcome is **one canonical project memory + thin host adapters +
separate reusable procedures and feature artifacts**.

This skill is for repository-level instructions. It does not replace feature
requirements, implementation plans, or a user's global Agent configuration.

## Scope and boundary

Use this skill when the developer asks to initialize or reorganize files such as
`AGENTS.md`, `CLAUDE.md`, host rule directories, or project-local Agent skills;
when several coding Agents need to share the same project knowledge; or when
entry files have drifted into duplicated and contradictory prompts.

Do not run a bootstrap ceremony for normal feature work when the project already
has a coherent instruction layer. Analysis and a proposed harness are allowed
without write permission; modifying the target repository requires actual
implementation authorization. Never install global skills, change user-level
Agent settings, or weaken repository safeguards as an incidental part of this
skill.

## 1. Inspect before designing

Read the existing instruction surface before creating anything:

- root and nested Agent entry files such as `AGENTS.md`, `CLAUDE.md`, other
  host-specific instruction files, and any subtree-specific overrides;
- host directories such as `.agents/`, `.claude/`, `.cursor/`, or equivalents;
- README, manifests, architecture docs, build/test scripts, and CI commands that
  establish project facts referenced by the instructions;
- relevant history only when needed to determine which rule is current or why a
  constraint exists.

Classify each existing instruction as one of these: stable project invariant,
host discovery/metadata, reusable procedure, project-specific Skill adapter,
feature decision, transient troubleshooting note, or secret/user-specific data.
Preserve user-authored constraints and unrelated edits. If two sources conflict,
surface the conflict and resolve authority from project evidence or the user;
do not silently choose one and delete the other.

## 2. Choose one canonical project source

For a new multi-host project, prefer a host-neutral canonical project instruction
file that the intended Agents can consume. `AGENTS.md` is a good default when it
matches the actual host setup. In an existing repository, preserve the current
canonical source unless there is a concrete maintenance problem and migration is
authorized.

The canonical project source should contain durable facts every coding Agent
needs, such as:

- project identity, supported platforms, and explicit non-goals;
- architecture ownership, dependency direction, and boundaries between layers;
- stable prohibitions learned from real project decisions;
- security, privacy, credential, destructive-action, and generated-file rules;
- build, test, and verification expectations for claiming work complete;
- concise pointers to authoritative deeper docs when detail belongs elsewhere.

Keep it as **current truth**, not a development diary. Do not copy the entire
README or architecture manual into it. Do not put secrets, machine-local paths,
one-off debugging output, a current feature plan, or host-only metadata there.
A workaround belongs only if it has become a durable project invariant.

## 3. Build host adapters, not policy forks

For each host the project actually uses:

1. Prefer the host reading the canonical project source directly when supported.
2. If the host expects another filename or directory, add the thinnest reliable
   adapter: a symlink when the repository, platform, and host resolve it safely;
   otherwise a short native include/reference wrapper when supported; otherwise
   a minimal host-specific file containing only the unavoidable host content and
   a pointer to the canonical source.
3. Create a host-only rule only when the host's native mechanism adds capability
   the canonical file cannot express, such as path globs, `alwaysApply`, or other
   host-specific metadata/enforcement.

Do not create entry files for Agents the project does not use. Do not maintain a
full `AGENTS.md`, full `CLAUDE.md`, full Cursor ruleset, and full Copilot prompt
with the same semantic policy copied four times. If one rule is cross-host, its
meaning belongs in the canonical source; the host adapter should only make that
rule discoverable or enforceable.

Host conventions change. When a path, include syntax, symlink behavior, or rule
format is uncertain, inspect the installed host/version or current authoritative
documentation before claiming compatibility.

## 4. Route knowledge by responsibility

Use this table before writing a new instruction:

| Knowledge | Preferred owner | What belongs there |
| --- | --- | --- |
| Project-wide Agent memory | `AGENTS.md` or the repository's existing canonical equivalent | Stable cross-host project invariants and verification contract |
| Host adapter | `CLAUDE.md`, host rule/config directories, or equivalent | Discovery pointer and unavoidable host-native metadata only |
| Reusable Skill | `SKILL.md` in a reusable Skill location | Portable procedure for a class of tasks |
| Project Skill adapter | Existing project convention; if none, a path such as `.agents/<skill>/PROJECT.md` | Local commands, ports, auth, surfaces, fixtures, and other repository-specific execution facts |
| Feature specification / plan | Existing project docs path such as `docs/specs/` or `docs/plans/` | Feature behavior, approved scope, alternatives, implementation steps, acceptance |
| Human documentation | README and architecture/docs tree | Comprehensive explanations and onboarding that Agents may reference instead of duplicate |

The paths above are patterns, not a mandate to create every directory. Follow an
existing project convention when one already works.

## 5. Keep generic Skills separate from project adapters

A reusable Skill should explain **how to perform a task in general**. If that
Skill needs local details to run in one repository — startup commands, bundle
identifiers, authentication constraints, test surfaces, fixtures, ports, or
teardown behavior — store those facts in a project layer instead of baking them
into the reusable `SKILL.md`.

A useful layering contract is:

```text
reusable SKILL.md
    owns generic procedure and validity criteria

project adapter (for example .agents/<skill>/PROJECT.md)
    owns how this repository runs that procedure
```

During execution, verified project facts win for local mechanics; the reusable
Skill still owns what counts as a valid result. Do not invent a project-adapter
hierarchy for a tiny repository that does not need one.

## 6. Bootstrap or refactor in a controlled sequence

### Inventory

List the existing canonical candidate, host adapters, Skill directories,
project-specific adapters, and feature docs. Record duplication and conflicts.

### Design

Propose the smallest coherent target shape. State:

- which file is canonical and why;
- which hosts need adapters;
- which duplicated rules will move or be removed;
- which facts belong in Skills, project adapters, or feature docs instead;
- portability risks such as symlink support or host-specific syntax.

### Apply

When writes are authorized, make the minimum diff needed to establish that
shape. Migrate rules rather than rewriting them from memory. Do not delete the
old entry until the replacement is known to be readable by the relevant host.
Avoid formatting churn and preserve unrelated worktree changes.

### Validate

Before calling the bootstrap complete, check as much as the environment allows:

- canonical instructions match repository evidence and contain no secrets;
- adapters point to the intended canonical source and links/symlinks resolve;
- the same large policy block is not maintained independently in multiple hosts;
- referenced commands and paths actually exist;
- host-native rules contain only the host-specific semantics they need;
- project-specific Skill facts are not leaking back into reusable Skills;
- relevant repository checks pass, or unrun checks are reported explicitly;
- the final diff contains no unrelated edits.

Do not claim cross-Agent compatibility merely because the filenames look right.
A host that was not actually checked remains unverified.

## 7. Maintain the harness after development

At the end of substantial work, promote only verified, durable learnings:

- stable cross-cutting project invariant -> canonical project instructions;
- reusable method across projects -> reusable Skill;
- local mechanics for one Skill -> project Skill adapter;
- feature-specific decision -> feature spec/plan;
- transient debugging discovery -> issue/log or nowhere unless it becomes a
  durable constraint.

When a new invariant replaces an old one, edit the old rule into current truth;
do not append contradictory history. Periodically remove stale rules whose
underlying code or constraint no longer exists.

## Reference pattern

A mature multi-host repository may legitimately look like this:

```text
project/
├── AGENTS.md                         # canonical project memory
├── CLAUDE.md -> AGENTS.md            # thin adapter when verified and portable
├── .agents/
│   ├── skills/<name>/SKILL.md        # reusable/project-local capability
│   └── <name>/PROJECT.md             # repository adapter for that capability
├── .claude/
│   └── skills -> ../.agents/skills   # discovery adapter when supported
└── .cursor/
    └── rules/<rule>.mdc              # Cursor-native metadata/enforcement only
```

This is an example of the layering, not a template to reproduce blindly. A
short `CLAUDE.md` wrapper may be safer than a symlink in another repository; a
project with one Agent host may need only the canonical file.

## Output

For an analysis-only request, return a compact inventory, proposed canonical
source, adapter map, migration decisions, risks, and validation plan.

For an authorized implementation, make the coherent repository change and
report changed paths, preserved/migrated rules, verification performed, and any
host compatibility that remains unverified. The success condition is not "more
Agent files"; it is **one maintainable source of project truth with the minimum
necessary adapters**.
