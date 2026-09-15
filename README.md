# Skills

Reusable Agent skills for software development, product UI, repository learning, and technical writing.

This repository is designed to work both as a human-browsable skill library and as a repository that can be handed directly to a coding Agent.

## Entry points

- **Human:** start here, then browse by domain under `skills/`.
- **Agent:** read [`AGENTS.md`](AGENTS.md) first.
- **Skill routing:** use [`skills/INDEX.md`](skills/INDEX.md) to select the smallest useful set of skills.
- **Generic software-development request:** start with `development-discovery` when important product or system decisions are still unresolved.

## Domains

| Domain | Purpose | Entry |
| --- | --- | --- |
| `core` | Route tasks to the right skills without preloading the library | `skills/core/skill-router/SKILL.md` |
| `development` | Clarify new projects/features and learn unfamiliar codebases | `skills/development/README.md` |
| `ui` | Discover, design, systematize, implement, and review product UI | `skills/ui/README.md` |
| `writing` | Turn engineering evidence into technical writing | `skills/writing/README.md` |

## Repository usage

When giving the whole repository to an Agent, use a simple instruction such as:

```text
Use my skills repository for this task. Read AGENTS.md first and select only the skills you need.
```

The Agent should not load every `SKILL.md`. The library is intentionally routed through `skills/INDEX.md` so context stays focused.

## Install individual skills

Clone the repository and copy only the skill directories you need into your Agent's skill directory. For example:

```bash
git clone https://github.com/dawNotPoi/skills.git
cp -R skills/skills/development/learn-codebase ~/.codex/skills/
cp -R skills/skills/development/development-discovery ~/.codex/skills/
```

Skills remain independently discoverable through their frontmatter descriptions, so installing the whole repository is not required.

## Design principles

- Prefer the smallest skill set that resolves the task.
- Keep product decisions, design decisions, implementation, and critique distinct.
- Do not silently resolve material product decisions in code.
- Persist important specifications and implementation plans when they are needed for handoff or later maintenance.
- Treat tests, runtime behavior, repository history, screenshots, and other observable evidence as stronger than unsupported inference.
