# UI Skills

Five focused skills cover interface requirements, direction, a reusable design
system, implementation and visual review. Entries and selection cues live in
the [canonical index](../INDEX.md); do not preload the whole family.

## Entry and composition

```text
unresolved product/system behavior
  -> development-discovery
known product intent, unclear interface flows
  -> product-ui-discovery
open visual/interaction direction
  -> ui-direction-designer
new reusable pattern or inconsistent tokens
  -> design-system-builder
approved and sufficiently specified interface
  -> ui-implementer
rendered result
  -> visual-qa-critic
```

These are conditional routes, not mandatory phases. Existing designs and
components should be reused. Small explicit changes skip discovery; a review
request stays review-only. Ordinary repository reading does not need a
code-learning session. System decisions such as queue versus interrupt belong
upstream; their placement and presentation belong to UI discovery.

## Implementation gate

Critical product behavior, UI flow, data/permission/failure semantics and
acceptance must be resolved for the affected change, and implementation must
be authorized. The same gate applies to code-producing design-system work.
Do not choose unresolved product behavior inside a component. Return the exact
missing decision to development or UI discovery with options and a recommendation.

A selected visual direction is not blanket implementation authorization. Reuse
explicit approval already given for this scope; do not demand another approval
for each downstream skill. Use compact inline artifacts for small clear fixes.

## Handoff and evidence

Preserve target/ref, goal, flow, constraints, references, selected direction,
existing system, assumptions, blockers, spec/plan version, approval source,
acceptance criteria and next step. Follow the target project's docs convention.
The library itself is not the destination for business specs or private data.

Semantic tokens and native/platform patterns should serve real needs; do not
create speculative component catalogs or silently replace branding. Explicitly
record justified token exceptions.

Inspect real rendered output when available. Screenshots support static state;
temporal behavior needs interaction evidence or recording. A build or a static
code review is not a visual pass. Without rendering tools, report unverified
states rather than claim completion. Review does not grant permission to fix,
deploy or publish.

## Installation

See [usage and migration](../../docs/usage.md). Install leaf skill folders by
stable name, not the `ui/` domain folder. Every specialist retains a local gate
so that selecting it directly does not depend on the router having run first.
