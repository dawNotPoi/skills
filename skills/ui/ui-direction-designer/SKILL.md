---
name: ui-direction-designer
description: Translate an established UI brief into a coherent visual and interaction direction with layout, hierarchy, typography, color, motion, and responsive intent. Use for art direction, interface concepts, or resolving an inconsistent visual language. Do not perform product discovery, build a component library, or implement production code.
---

# UI Direction Designer

Choose a deliberate interface direction that serves the product brief and can
be implemented consistently.

## Inputs

Start from a UI discovery brief or equivalent product requirements. Inspect
existing brand assets, interface screenshots, design systems, and platform
conventions when available. Treat supplied references as constraints or
inspiration according to the user's wording; do not copy protected artwork or
another product's distinctive expression.

## Workflow

1. Extract the experience attributes the interface must communicate, such as
   dense, calm, playful, editorial, technical, or trustworthy.
2. Establish hierarchy and layout behavior around the primary tasks before
   choosing decorative details.
3. Explore a small number of meaningfully different directions when the choice
   is still open. Compare them under shared criteria: task clarity, brand fit,
   content fit, accessibility, responsiveness, and implementation cost.
4. Select or recommend one direction and explain the decisive trade-offs.
5. Specify typography roles, color roles, spacing rhythm, shape, elevation,
   imagery, iconography, motion, responsive transformations, and key states at
   the level needed for a downstream system or implementation.

Use concrete values when they have been approved or derived from an existing
system. Otherwise express relationships and intent without pretending that
provisional pixels are final tokens.

## Output: Direction Specification

Include:

- direction name and short rationale;
- experience attributes and visual principles;
- page hierarchy and responsive layout model;
- type, color, spacing, shape, imagery, icon, and motion guidance;
- representative key screens or annotated concepts when requested;
- accessibility implications and interaction-state intent;
- rejected alternatives and unresolved choices that affect implementation.

Do not expand product scope or define a full component API. Hand reusable
patterns to `design-system-builder`; hand an approved, sufficiently concrete
direction to `ui-implementer`.
