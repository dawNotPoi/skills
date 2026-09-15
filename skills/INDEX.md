# Skill Index

Use this file to route a task before loading individual skills.

## Default selection protocol

1. Identify the user's actual intent and current stage.
2. Select the smallest skill set that can complete the task.
3. Prefer one primary skill plus only the downstream skills that are actually needed.
4. Do not preload unrelated skills.
5. If a task changes stage, hand off the explicit artifacts and decisions from the previous stage.

## Routing table

| User intent | Start with | Add only when needed | Do not start with |
| --- | --- | --- | --- |
| Start a new software project | `development/development-discovery` | UI family, implementation planning, repository setup | direct implementation |
| Add a materially new feature to an existing project | `development/development-discovery` | `development/learn-codebase`, UI family | direct implementation when behavior is unresolved |
| Understand or onboard to a repository | `development/learn-codebase` | development discovery if a later feature decision is needed | UI/design skills |
| Design a new product UI with unclear workflows | `ui/product-ui-discovery` | direction, system, implementation, QA | `ui/ui-implementer` |
| Choose or repair a visual direction | `ui/ui-direction-designer` | design system, implementation | product discovery if requirements are already settled |
| Build or evolve reusable UI primitives | `ui/design-system-builder` | UI implementation, visual QA | broad product discovery |
| Implement an approved interface | `ui/ui-implementer` | visual QA | discovery unless critical gaps are found |
| Review rendered UI quality | `ui/visual-qa-critic` | UI implementer for confirmed fixes | redesign-by-taste |
| Turn engineering evidence into a technical article | `writing/write-evidence-driven-blog` | repository learning for missing evidence | development discovery |
| Unsure which skill applies | `core/skill-router` | whatever the router selects | loading the whole library |

## Composition examples

### New project

```text
development-discovery
  -> product/technical specification
  -> UI family only if the project has a UI surface
  -> implementation
  -> verification
```

### Existing project, new feature

```text
development-discovery
  -> learn-codebase (only the relevant subsystem)
  -> feature specification
  -> implementation plan
  -> implementation
  -> verification
```

If understanding the existing architecture is necessary to answer discovery questions, `learn-codebase` may run before or during discovery. The goal is not a rigid sequence; the goal is to avoid implicit product decisions in code.

### UI-heavy feature

```text
development-discovery
  -> ui/product-ui-discovery
  -> ui/ui-direction-designer
  -> ui/design-system-builder (only when reuse/consistency warrants it)
  -> ui/ui-implementer
  -> ui/visual-qa-critic
```

## Critical decision rule

A task is not ready for implementation when an unresolved choice would materially change one or more of:

- user-visible behavior;
- system or state ownership;
- data model or protocol;
- permissions/security;
- failure, retry, interruption, or concurrency semantics;
- integration boundary;
- acceptance criteria.

Route such tasks back to `development-discovery` (or `product-ui-discovery` for a purely interface-specific unknown) before implementation.
