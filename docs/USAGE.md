# Usage and entry points

## 1. Repository mode

Ask the agent to read the library's `AGENTS.md`, then `skills/INDEX.md`, then
only the chosen skill. The library may be a local checkout or readable remote
repository. Use the same ref across files; a pinned commit makes a run easier
to reproduce. Record the actual ref when known, never invent one.

The business project remains the write target. If only the library is open and
no target project is known, resolve the target before scaffolding or editing.
If remote reading is unavailable, request a local checkout or file contents;
do not claim the URL activated anything.

## 2. Installed mode

The source taxonomy is not a required host discovery layout. Install complete
leaf folders directly under the host's configured skills location. From the
library checkout:

```bash
# Codex user-level; first preview, then explicitly apply
python3 scripts/library.py install --dest "$HOME/.agents/skills" --all
python3 scripts/library.py install --dest "$HOME/.agents/skills" --all --apply
# Claude Code user-level, or use a project-local .claude/skills destination
python3 scripts/library.py install --dest "$HOME/.claude/skills" --all --apply
# Selected capabilities only
python3 scripts/library.py install --dest /path/to/project/.agents/skills --skill skill-router --skill development-discovery --apply
```

No shell is needed to apply the instruction-only skills when the host can read
their Markdown. The installer is a convenience for environments with Python
3.9+; it is not a prerequisite for using the library by reference.

The installer defaults to dry-run, preflights all conflicts, rejects duplicate
names and unsafe source layout, and never overwrites existing destinations.
Back up and deliberately update an existing installation outside this script.
It does not install tools, authorize writes, edit host settings, or execute
bundled scripts. Refresh the host's discovery if an installed skill is missing.

In installed mode the router uses the host's actual registry, or sibling skill
metadata if file access is available. It does not require a copied root index.
Missing peers remain missing; install or expose them explicitly when needed.

## 3. Make it a project habit

Installing skills can make them discoverable but does not guarantee invocation
on every request. For predictable project use, merge a short instruction into
the target project's existing `AGENTS.md` or `CLAUDE.md`, with owner approval:

```text
Use my available skills for relevant tasks. Start new projects and materially
new features with development-discovery's readiness check. Read existing
project evidence before asking. Resolve critical product decisions before
implementation; clear authorized small edits use the fast path. Read only the
selected skills. If a required skill is unavailable, say so.
```

For a local library instead of installed skills, add its actual path and ask
the agent to read that library's entry. Do not overwrite existing instructions
or import every skill. Repository instructions are not system-level policy.
Claude's root adapter uses `@AGENTS.md` to import only this library's bootstrap;
that adapter does not automatically apply to other projects or remote URLs.

## 4. Expected interaction

A new feature with missing semantics should produce an evidence-backed summary,
the next important decision, options, a recommendation, and a focused question.
It must not start creating application files while that decision is unresolved.

A clear request such as "change this label and update its test" should not
trigger a long interview. A review-only request should not edit code. Resumed
work reuses confirmed decisions, but rechecks changed contracts and scope.

## Reference basis

Checked 2026-09-15; these are documentation sources, not claims that every host
was executed in this repository's tests:

- Agent Skills format and progressive disclosure: https://agentskills.io/specification
- OpenAI local skill discovery and symlink support: https://developers.openai.com/codex/skills/
- Claude Code skill directories: https://code.claude.com/docs/en/skills
- Claude Code instruction-file imports: https://code.claude.com/docs/en/memory

Host behavior evolves. Follow the installed host's current official documentation
when its discovery paths or activation behavior differ from these examples.
