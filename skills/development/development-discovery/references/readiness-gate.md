# Development Readiness Gate

Use this gate to decide whether a project or feature may move from discovery into specification, planning, or implementation.

## Critical unknown

An unresolved decision is critical when choosing differently would materially change one or more of:

- user-visible behavior or workflow;
- which process, client, service, or Agent owns important state;
- API, protocol, schema, persistence, or synchronization behavior;
- permissions, trust, security, or credential boundaries;
- cancellation, interruption, retry, duplicate-delivery, concurrency, or failure semantics;
- integration boundaries or compatibility guarantees;
- observable acceptance criteria.

Critical unknowns must not be hidden inside implementation choices.

## Non-critical unknown

An unknown is normally non-critical when:

- it is local to one implementation detail;
- it can be changed later without changing the product contract;
- it does not introduce irreversible migration or compatibility cost;
- a conventional default is available;
- the assumption can be stated explicitly and verified cheaply.

Non-critical unknowns may be handled as explicit assumptions.

## States

### BLOCKED

At least one critical decision remains open.

Allowed work:

- inspect repository evidence;
- prototype narrowly to answer a decision;
- compare options;
- update the specification.

Not allowed:

- committing production behavior that silently chooses the missing decision.

### READY_FOR_SPEC

The product outcome, actors, primary flow, scope, major lifecycle semantics, and relevant failure behavior are clear enough to record the contract.

### READY_FOR_PLAN

The specification is stable, major technical constraints are known, and the repository can be mapped into implementation tasks.

### READY_TO_IMPLEMENT

Proceed when all of the following are true for the requested scope:

- no critical product/system decision is open;
- acceptance criteria are observable;
- existing architecture is understood well enough to place the change;
- material compatibility/security constraints are known;
- a plan exists for non-trivial work.

## Escalation rule

If implementation exposes a missing critical decision, stop that branch of implementation and return to discovery. Do not treat sunk coding effort as a reason to preserve an accidental product decision.
