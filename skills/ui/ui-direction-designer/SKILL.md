---
name: ui-direction-designer
description: Translate an established UI brief into visual and interaction direction, including hierarchy, color, typography, motion, and responsive intent. Use for 视觉方向、界面风格 and inconsistent design language. Recommend options but distinguish proposals from accepted choices. Do not implement production code.
---

# UI Direction Designer

Choose a deliberate interface direction that serves the product brief and can
be implemented consistently.

## Inputs

Read the established brief, current decisions, project rules, brand assets,
existing components, screenshots, and platform constraints. References are
constraints or inspiration according to the user's wording; do not copy
protected artwork or another product's distinctive expression.

If core UI flows are missing, return to `product-ui-discovery`; for cross-cutting
product/system decisions use `development-discovery`. If a peer is unavailable,
identify the gap and guide the decision locally rather than claiming invocation.
Do not repeat choices already confirmed or change an existing design system
without a reason within scope.

## Workflow

1. Extract the experience attributes: for example dense, calm, playful,
   editorial, technical, or trustworthy.
2. Establish hierarchy around primary tasks before decorative details.
3. If direction is open, propose two or three meaningful alternatives with
   common criteria: task clarity, content fit, brand, accessibility,
   responsiveness, and implementation cost. Do not fabricate design research.
4. Recommend a direction. Obtain a choice or use explicit delegation before
   treating it as accepted. Do not force alternatives when direction is already
   established, and do not ask the user to pick every hex code.
5. Specify roles and relationships for typography, color, spacing, shape,
   elevation, imagery, icons, motion, responsive transformations and states.

Concrete values may be proposed by the agent; mark their status. Once the
visual direction is accepted, reversible values can be refined within it.
A static mockup cannot validate interaction timing or runtime behavior.

## Output: Direction Specification

Include direction/rationale, visual principles, hierarchy and responsive model,
role guidance, relevant concepts, accessibility implications, rejected
alternatives and open choices. Preserve references, approval source, scope and
current revision. Do not expand the product requirement.

This is a design stage, not implementation authorization. An isolated prototype
requires agreed scope; it is not the production implementation. Hand reusable
patterns to `design-system-builder` and an accepted direction with explicit
implementation permission to `ui-implementer`.
