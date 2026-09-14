---
name: ui-implementer
description: Implement an approved UI direction or specification in an existing or new codebase, including responsive behavior, interaction states, accessibility, and verification. Use when the user asks to build or modify the interface. Do not silently change product requirements or substitute a new visual direction.
---

# UI Implementer

Build the specified experience faithfully in the target environment and prove
that its important behavior works.

## Inputs

Inspect the repository instructions, existing architecture, design system,
assets, UI specification, supported viewports, and acceptance criteria. Reuse
the project's components and conventions when they satisfy the specification.
Record material gaps or conflicts before resolving them; ask only when the
choice changes product behavior or an approved direction.

## Workflow

1. Trace the relevant routes, components, styles, data boundaries, and tests
   before editing.
2. Plan the smallest coherent change. Separate reusable primitives only when
   actual repetition or ownership boundaries justify it.
3. Implement semantic structure, content hierarchy, responsive layout,
   interactions, keyboard behavior, focus, validation, and loading, empty,
   error, disabled, and success states in scope.
4. Use real assets and data contracts when available. Do not disguise missing
   behavior with decorative mock controls or fabricate production data.
5. Verify the changed UI at representative viewport sizes and interaction
   states. Run relevant automated checks and inspect rendered output when the
   environment supports it.

Follow established framework and styling choices. Adding a dependency,
rewriting architecture, or changing a shared system requires a concrete need
within the requested scope.

## Output

Provide:

- the working implementation;
- a concise mapping from specification or acceptance criteria to changed
  behavior;
- checks performed and their results;
- screenshots or preview references when useful;
- remaining gaps, assumptions, and any follow-up that needs a product or design
  decision.

Implementation does not authorize deployment, publishing, or unrelated
repository changes. Use `visual-qa-critic` for a separate visual review when
requested or when fidelity is central to acceptance.
