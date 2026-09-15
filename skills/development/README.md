# Development Skills

Development skills cover the path from an ambiguous software request to a well-understood codebase and an implementation-ready specification.

## Skills

| Skill | Use it to | Primary output |
| --- | --- | --- |
| [development-discovery](development-discovery/SKILL.md) | Clarify a new project or materially new feature before coding | Feature/project specification and readiness decision |
| [learn-codebase](learn-codebase/SKILL.md) | Build an evidence-backed mental model of an unfamiliar repository or subsystem | Repository map, execution path, core abstractions |

## Default development flow

```text
ambiguous project or feature request
  -> development-discovery
  -> learn-codebase when existing architecture must be understood
  -> specification
  -> implementation plan
  -> implementation
  -> verification
```

The order is flexible. Existing code may need to be inspected during discovery, and discovery may resume when repository evidence exposes a product decision that was previously hidden.

## Core rule

Do not use implementation to decide product behavior implicitly. If an unresolved choice would materially change user-visible behavior, state ownership, data/protocol shape, permissions, failure semantics, or acceptance criteria, resolve it in discovery first.
