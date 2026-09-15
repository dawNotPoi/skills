# Feature Specification

## Title

`<feature or project name>`

## Problem

What problem or opportunity is being addressed? Describe the current limitation and why it matters.

## Outcome

What observable outcome should exist when this work succeeds?

## Actors

| Actor | Responsibility |
| --- | --- |
| `<user/client/service/agent>` | `<what it initiates or owns>` |

## Core behavior

Describe the shortest successful flow in concrete terms.

```text
trigger
  -> step
  -> step
  -> observable result
```

## Scope

### In scope

- ...

### Non-goals

- ...

## State and lifecycle

Document only what materially matters:

- state owner;
- durable vs ephemeral state;
- reconnect/restart behavior;
- cancellation/interruption/concurrency semantics;
- synchronization or conflict behavior.

## Permissions and security

Record relevant authorization, approval, credential, or trust-boundary decisions. Omit this section when genuinely irrelevant.

## Failure behavior

| Condition | Expected behavior |
| --- | --- |
| timeout | ... |
| offline | ... |
| retry/duplicate | ... |

Keep only relevant cases.

## Acceptance criteria

Use observable, testable statements.

- [ ] ...
- [ ] ...

## Decisions and rationale

| Decision | Choice | Why |
| --- | --- | --- |
| ... | ... | ... |

## Assumptions

List non-blocking assumptions that implementation may rely on.

## Open decisions

List only unresolved decisions. Mark any critical decision clearly. A specification with a critical open decision is not implementation-ready.
