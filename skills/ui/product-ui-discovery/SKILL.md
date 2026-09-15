---
name: product-ui-discovery
description: Turn an ambiguous UI or interaction request into evidence-backed interface requirements, task flows, content needs, states, and acceptance criteria. Use before visual design when the UI workflow, user jobs, content hierarchy, or interface constraints are unclear but broader product/system behavior is already sufficiently defined. Do not decide state ownership, protocol semantics, permissions, backend architecture, visual style, or production implementation.
---

# Product UI Discovery

Define what the interface must enable before deciding how it should look.

If the request still contains broader software-product ambiguity — for example state ownership, concurrency/interruption behavior, permission semantics, protocol/data shape, or failure behavior outside the UI — route to `development/development-discovery` first.

## Inputs

Use available product notes, user feedback, analytics, screenshots, existing flows, platform constraints, and stakeholder decisions. Distinguish observed evidence from assumptions. Ask only about unknowns that would change the core UI workflow, scope, or safety of the result.

## Workflow

1. State the product outcome already established, target users, and the situation that triggers the interaction.
2. Identify primary and secondary user jobs. Rank them rather than treating every requested feature as equal.
3. Map the shortest successful UI flow and meaningful alternate paths.
4. Inventory required information, actions, permissions as surfaced in the UI, validation, loading, empty, error, partial, offline, and success states.
5. Capture platform, responsive, accessibility, localization, privacy, and technical constraints that affect the interface.
6. Convert the findings into testable UI acceptance criteria and record open questions with their decision impact.

Do not invent research findings. When evidence is unavailable, label a claim as a hypothesis and propose the cheapest useful validation.

## Output: UI Discovery Brief

Deliver a compact brief containing:

- outcome, users, context, and prioritized jobs;
- scope and explicit non-goals;
- primary UI flow plus relevant alternate and failure paths;
- content and state inventory;
- constraints and authoritative references;
- UI acceptance criteria;
- assumptions, evidence gaps, and unresolved interface decisions.

The brief should let a direction designer explore presentation without re-deciding the product problem. Stop before selecting typography, color, layout style, component APIs, or non-UI system architecture.
