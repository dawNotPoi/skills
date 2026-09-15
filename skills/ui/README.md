# UI Skills

Five focused skills cover the path from UI-specific product discovery to a verified interface. They share handoff artifacts, but none requires the whole pipeline.

For a new software project or materially new feature whose broader product/system behavior is still unclear, start upstream with [`../development/development-discovery`](../development/development-discovery/SKILL.md). UI discovery should not be used to decide state ownership, protocol semantics, permissions, or other non-UI product/system boundaries.

## Skills

| Skill | Use it to | Primary output |
| --- | --- | --- |
| [product-ui-discovery](product-ui-discovery/SKILL.md) | Turn product context into evidence-backed UI requirements | UI discovery brief |
| [ui-direction-designer](ui-direction-designer/SKILL.md) | Choose a coherent visual and interaction direction | Direction specification |
| [design-system-builder](design-system-builder/SKILL.md) | Define or evolve reusable tokens, components, and governance | Design-system contract |
| [ui-implementer](ui-implementer/SKILL.md) | Build the approved interface in the target codebase | Working implementation |
| [visual-qa-critic](visual-qa-critic/SKILL.md) | Find and prioritize visual, responsive, and interaction defects | Evidence-backed QA report |

## Composition

Use the smallest sequence that resolves the task:

```text
broader feature behavior unclear
  -> development/development-discovery

UI workflow unclear
  -> product-ui-discovery
  -> ui-direction-designer
  -> design-system-builder (when reuse or consistency warrants it)
  -> ui-implementer
  -> visual-qa-critic
  -> ui-implementer (targeted fixes)
```

Common shortcuts:

- Existing brief, new look: start with `ui-direction-designer`.
- Existing design system and mockup: use `ui-implementer`, then `visual-qa-critic`.
- Component-library work: use `design-system-builder` directly.
- Review only: use `visual-qa-critic`; it reports issues but does not silently redesign or edit code.

## Shared Handoff Contract

Each handoff should preserve:

- the user goal and priority tasks;
- target users, platforms, breakpoints, and accessibility needs;
- known constraints, existing assets, and authoritative references;
- decisions already made, their rationale, and unresolved questions;
- acceptance criteria and observable evidence.

Downstream skills may refine an artifact but must not quietly replace an approved product requirement or visual direction.

If implementation exposes an unresolved choice that would materially change user-visible behavior, state ownership, protocol/data shape, permissions, failure semantics, or acceptance criteria, stop and route back to `development-discovery`. If the unknown is purely about interface workflow, route back to `product-ui-discovery`.

## Design Principles

- Separate product decisions, visual decisions, system decisions, implementation, and critique.
- Treat existing product conventions and repository constraints as evidence, not obstacles to overwrite.
- Prefer explicit, inspectable artifacts over taste-only claims.
- Make accessibility, responsive behavior, states, and content part of the design rather than a final polish pass.
- Keep external writes and production changes within the user's authorization.

## Installation

Copy the individual skill folders you need into your Agent's skill directory. The skills remain independently discoverable; this overview is documentation, not a required router. When the entire repository is available, `../INDEX.md` is the routing entry point.
