# Implementation Plan

## Goal

Link this plan to the approved feature/project specification and summarize the implementation outcome in one paragraph.

## Existing system

Record the relevant current architecture, ownership boundaries, and constraints discovered in the repository. Reference concrete files, symbols, tests, APIs, or services.

## Change strategy

Explain the smallest coherent approach and why it fits the existing system.

## Tasks

### Task 1 — `<bounded change>`

**Files / symbols**

- `path/to/file` — `SymbolName`

**Change**

- ...

**Verification**

- ...

### Task 2 — `<bounded change>`

**Files / symbols**

- ...

**Change**

- ...

**Verification**

- ...

## Integration order

Describe dependencies between tasks and the order that reduces risk.

## Data / migration / compatibility

Record schema, protocol, persistence, migration, backwards-compatibility, or rollout concerns when relevant.

## Verification plan

Map acceptance criteria to observable checks:

| Acceptance criterion | Verification |
| --- | --- |
| ... | test/runtime/screenshot/log/etc. |

## Risks and rollback

List concrete failure modes, risky assumptions, and rollback boundaries when relevant.

## Deferred work

Keep non-goals and intentionally deferred improvements out of the implementation path.

## Implementation deviations

After implementation, record material differences between this plan and what was actually shipped, with reasons. Promote only stable cross-feature rules into repository-level instructions such as `AGENTS.md`.
