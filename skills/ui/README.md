# UI Skills

Five focused skills cover the path from an ambiguous product request to a
verified interface. They share handoff artifacts, but none requires the whole
pipeline.

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
unclear product problem
  -> product-ui-discovery
  -> ui-direction-designer
  -> design-system-builder (when reuse or consistency warrants it)
  -> ui-implementer
  -> visual-qa-critic
  -> ui-implementer (targeted fixes)
```

Common shortcuts:

- Existing brief, new look: start with `ui-direction-designer`.
- Existing design system and mockup: use `ui-implementer`, then
  `visual-qa-critic`.
- Component-library work: use `design-system-builder` directly.
- Review only: use `visual-qa-critic`; it reports issues but does not silently
  redesign or edit code.

## Shared Handoff Contract

Each handoff should preserve:

- the user goal and priority tasks;
- target users, platforms, breakpoints, and accessibility needs;
- known constraints, existing assets, and authoritative references;
- decisions already made, their rationale, and unresolved questions;
- acceptance criteria and observable evidence.

Downstream skills may refine an artifact but must not quietly replace an
approved product requirement or visual direction. When inputs conflict, state
the conflict and ask only when the choice would materially change the result.

## Design Principles

- Separate product decisions, visual decisions, system decisions,
  implementation, and critique.
- Treat existing product conventions and repository constraints as evidence,
  not obstacles to overwrite.
- Prefer explicit, inspectable artifacts over taste-only claims.
- Make accessibility, responsive behavior, states, and content part of the
  design rather than a final polish pass.
- Keep external writes and production changes within the user's authorization.

## Installation

Copy the individual skill folders you need into your Codex skills directory.
The skills remain independently discoverable; this overview is documentation,
not a required router.
