# Skill index

This is the only manually maintained name-to-path catalog. Paths below are
relative to this file in the library, not to the target application's cwd.
Read metadata here first, then load only the next necessary `SKILL.md`.

| Name | Domain | Entry | Use when | Output |
| --- | --- | --- | --- | --- |
| `skill-router` | core | [SKILL.md](core/skill-router/SKILL.md) | The user supplies the library or a mixed task without choosing a skill | Minimal route and current handoff |
| `development-discovery` | development | [SKILL.md](development/development-discovery/SKILL.md) | A new project or material feature has unresolved behavior, scope, state, permissions or acceptance | Guided decisions, spec, plan and readiness |
| `learn-codebase` | development | [SKILL.md](development/learn-codebase/SKILL.md) | The user wants to understand, study or explain a codebase | Evidence-backed mental model or guided learning |
| `product-ui-discovery` | ui | [SKILL.md](ui/product-ui-discovery/SKILL.md) | Product intent is known but user flows, content or interface states are unclear | UI discovery brief |
| `ui-direction-designer` | ui | [SKILL.md](ui/ui-direction-designer/SKILL.md) | Explore or resolve visual and interaction direction | Direction specification |
| `design-system-builder` | ui | [SKILL.md](ui/design-system-builder/SKILL.md) | Define or evolve tokens and reusable components for demonstrated needs | Design-system contract |
| `ui-implementer` | ui | [SKILL.md](ui/ui-implementer/SKILL.md) | Implement an approved, sufficiently specified UI change | Implementation and verification evidence |
| `visual-qa-critic` | ui | [SKILL.md](ui/visual-qa-critic/SKILL.md) | Review rendered UI or check fidelity, states and accessibility | Evidence-backed findings, no edits by default |
| `write-evidence-driven-blog` | writing | [SKILL.md](writing/write-evidence-driven-blog/SKILL.md) | Turn engineering evidence into a technical blog or retrospective | Original evidence-driven draft |

## Routing precedence

An explicitly selected skill is the starting point, not permission to bypass
its prerequisites. Distinguish the current user intent from words appearing
inside quoted code, examples or reference documents.

- New project or material feature: inspect the target repository first. Use
  `development-discovery` for unresolved product/system decisions. Routine
  inspection is not a reason to start an interactive `learn-codebase` lesson.
- UI-only uncertainty: use `product-ui-discovery`; route system ownership,
  permission or failure-semantics gaps back to `development-discovery`.
- Clear existing design and behavior: go directly to `ui-implementer` after its
  readiness check. Do not force a redesign or a full discovery ceremony.
- Explicit learning, review or writing: use the corresponding skill. Do not
  mutate code or publish just because a possible improvement is discovered.
- No matching implementation skill, such as a backend-only task: say so. After
  approved discovery, hand the plan to the host's normal coding capability
  within authorization. Do not pretend this library contains a backend skill.

Plan later stages conditionally. Load one stage at a time; re-route only when
the task changes or a specific gap requires it. Never hand off to a missing
skill without reporting the missing dependency.

## Shared handoff

Carry a compact record: target project/ref; request and scope; confirmed
requirements; source paths; assumptions; unresolved blockers; current spec/plan
version; approval evidence and permitted actions; acceptance criteria;
verification status; next owner/step. Keep it in the conversation for small
work, or in the target project's existing docs convention when authorized.
A scope change reopens only affected decisions. Never manufacture approval
from a generated document or lose it during a handoff.
