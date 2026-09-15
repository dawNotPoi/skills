---
name: development-discovery
description: Guide a developer from an ambiguous new software project or materially new feature request to an implementation-ready specification. Use when product behavior, scope, state ownership, architecture boundaries, permissions, failure semantics, concurrency/interruption behavior, integrations, or acceptance criteria are not yet clear. Summarize what is known, surface only the highest-impact unresolved decisions, explain trade-offs, recommend a default, and persist the result as a spec when useful. Do not write production code while critical decisions remain unresolved.
---

# Development Discovery

Clarify what the software must do before deciding how to implement it.

This skill is the default gateway for new projects and materially new features when the request still contains product or system ambiguity.

## Principle

Do not turn missing requirements into hidden implementation decisions.

When a developer has not specified a behavior that materially changes the product or architecture, surface that decision explicitly before coding.

Do not respond with a generic questionnaire. The Agent should do as much synthesis as possible first, then ask only the next 1-3 questions with the highest decision impact.

## Inputs

Use all available context:

- the user's request and prior decisions;
- repository instructions such as `AGENTS.md` or `CLAUDE.md`;
- existing architecture, code, tests, issues, and history when working in an existing project;
- product notes, screenshots, API contracts, schemas, and operational constraints;
- platform, security, deployment, and compatibility requirements.

For an existing repository, inspect enough of the current system to avoid asking questions that the codebase has already answered. Use `learn-codebase` when a subsystem requires deeper understanding.

## Conversation protocol

When the request is incomplete:

1. **Summarize what is already known.** State the goal, actors, core behavior, and constraints already established.
2. **Identify the next critical unknown.** Choose only decisions that would materially change implementation or acceptance.
3. **Explain why it matters.** Name the affected behavior, state model, protocol, security boundary, or user experience.
4. **Offer concrete options.** Present 2-4 realistic choices when useful.
5. **Recommend a default.** Give the best current recommendation and the trade-off behind it.
6. **Ask for the developer's preference.** Ask one decision at a time by default; group up to three tightly coupled decisions when that is more efficient.

Prefer this pattern:

```text
I understand the feature as X. A, B, and C are already clear.

One unresolved decision changes the architecture: what should happen when a second message arrives while the Agent is still running?

A. Interrupt the current run
B. Queue the message
C. Steer the current run
D. Start a parallel session

I recommend B + an explicit Interrupt action because it is predictable and keeps task history deterministic. Which behavior do you want?
```

Avoid:

```text
Please provide more requirements.
```

and avoid dumping a long checklist when only one decision is currently blocking progress.

## Discovery model

Internally scan these areas, but do not ask about all of them mechanically:

### Outcome

- What problem is being solved?
- What observable result means the feature succeeded?

### Actors

- Who initiates the action?
- Which client, service, Agent, worker, or external system performs each part?

### Trigger and flow

- What starts the behavior?
- What is the shortest successful path?
- Which alternate path is common enough to design now?

### Scope and boundaries

- What is included?
- What is explicitly out of scope?
- Which existing subsystem owns the behavior?

### State and data

- Where does important state live?
- Who is allowed to mutate it?
- What must survive restart, reconnect, failover, or device switching?
- Which data is durable, cached, derived, or ephemeral?

### Concurrency and lifecycle

- What happens when work overlaps?
- Can a task be queued, interrupted, resumed, retried, cancelled, or run in parallel?
- Who owns completion and cleanup?

### Permissions and security

- Who may trigger the action?
- Which capabilities require approval?
- Where do credentials and sensitive data live?

### Failure semantics

- What happens on timeout, offline state, partial success, retry, duplicate delivery, or conflicting writes?
- Which failures are safe to retry automatically and which are not?

### Acceptance

- What exact behavior proves the work is complete?
- Which edge cases must be demonstrated rather than inferred?

## Critical vs non-critical unknowns

Use [references/readiness-gate.md](references/readiness-gate.md).

A **critical unknown** is unresolved when the choice would materially change one or more of:

- user-visible behavior;
- system or state ownership;
- data model, API, protocol, or persistence;
- permissions or security;
- retry, interruption, concurrency, or failure behavior;
- integration boundaries;
- acceptance criteria.

Critical unknowns block implementation.

A **non-critical unknown** may be handled as an explicit assumption when it can be changed locally later without materially changing the product contract.

## When the developer does not know

Do not stall with repeated requests for confirmation.

If the developer says they are unsure:

1. describe the viable options;
2. compare them under shared criteria;
3. recommend a default based on the current product goal and repository constraints;
4. state the assumption clearly;
5. continue unless the decision carries high irreversible cost or safety/security risk.

The skill should reduce the developer's decision burden, not transfer analysis back to them.

## New project mode

Prioritize:

- product outcome;
- target user or caller;
- core loop;
- platform/runtime;
- system boundaries;
- state ownership;
- deployment model;
- security model;
- MVP scope;
- acceptance criteria.

Do not choose frameworks or infrastructure before the product and system boundaries are sufficiently understood unless a platform constraint already determines them.

## Existing feature mode

Before asking the developer about behavior already encoded in the system:

1. read repository instructions;
2. locate the relevant subsystem;
3. inspect representative tests and current data/state contracts;
4. identify which decisions are already fixed by compatibility;
5. ask only about genuinely unresolved product or architecture choices.

Use `learn-codebase` for deeper execution-path or abstraction analysis when needed.

## Readiness states

### BLOCKED

One or more critical decisions remain unresolved. Do not implement production code.

### READY_FOR_SPEC

Core product behavior and boundaries are clear enough to write a specification.

### READY_FOR_PLAN

The specification, major technical decisions, and acceptance criteria are stable enough to map onto the repository.

### READY_TO_IMPLEMENT

Implementation may begin when:

- a sufficient specification exists;
- no critical product/system decision remains open;
- the relevant architecture is understood;
- acceptance criteria exist;
- an implementation plan exists when the change is non-trivial.

## Output artifacts

For a small feature, a concise in-chat specification may be enough.

For a substantial feature or project, persist a spec using `templates/feature-spec.md`. Prefer a repository location such as:

```text
docs/specs/YYYY-MM-DD-feature-name.md
```

A specification answers **what and why**. It should capture:

- problem and outcome;
- actors and core behavior;
- scope and non-goals;
- state/lifecycle semantics;
- permissions and failure behavior when relevant;
- acceptance criteria;
- decisions and rationale;
- remaining non-blocking assumptions.

After the spec is stable, create an implementation plan using `templates/implementation-plan.md` when the work spans multiple files, layers, services, or verification steps.

A plan answers **how this repository will change**. Keep it separate from the product specification.

## Handoff

Possible downstream skills include:

- `development/learn-codebase` for deeper repository understanding;
- `ui/product-ui-discovery` when interface workflows still need UI-specific definition;
- `ui/ui-direction-designer` after UI requirements are established;
- implementation-specific tools or Agents once readiness reaches `READY_TO_IMPLEMENT`.

If a downstream implementer discovers a missing critical product decision, stop and return to this skill rather than deciding implicitly in code.

## Completion criteria

Discovery is complete when the developer and Agent can answer, with no critical ambiguity:

1. What outcome is being built?
2. Who/what initiates and owns the behavior?
3. What is the primary successful flow?
4. What are the important boundaries and non-goals?
5. Where does important state live and how does its lifecycle work?
6. What happens under relevant failure/concurrency conditions?
7. What observable evidence will prove the feature is complete?

Do not equate a long requirements document with readiness. The goal is resolved decisions, not document volume.
