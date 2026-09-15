# UI Skills

Five focused skills cover product UI discovery, direction, design-system
contracts, implementation, and evidence-backed review. The library-wide
catalog is [INDEX.md](../INDEX.md); this file is not an executable router.

## Composition

Start a new project or materially new feature with `development-discovery` when
product behavior, state ownership, API boundaries, permissions, or acceptance
are unresolved. It reads available evidence and guides decisions before code.
For a pure UI task with known product behavior, begin with the relevant UI skill.

```text
confirmed product behavior
  -> product-ui-discovery (only missing UI flows/content/states)
  -> ui-direction-designer (only if direction is open)
  -> design-system-builder (only if new reuse/consistency work is warranted)
  -> ui-implementer (clear requirements + implementation authorization)
  -> visual-qa-critic
  -> targeted fixes, when authorized
```

| Skill | Responsibility |
| --- | --- |
| [product-ui-discovery](product-ui-discovery/SKILL.md) | UI tasks, information architecture, content and states |
| [ui-direction-designer](ui-direction-designer/SKILL.md) | Coherent visual and interaction direction |
| [design-system-builder](design-system-builder/SKILL.md) | Semantic tokens, component contracts and governance |
| [ui-implementer](ui-implementer/SKILL.md) | Scoped implementation and verification |
| [visual-qa-critic](visual-qa-critic/SKILL.md) | Reproducible defects and acceptance evidence |

## Shared handoff

Preserve the target project/ref, mode, confirmed requirements and sources,
spec/plan revision, assumptions, unresolved decisions, authorization scope,
acceptance criteria and verification limitations. Never turn an unresolved
product decision into a styling or event-handler choice.

Read relevant project rules and existing components before questioning. Do not
repeat a product interview already completed by development discovery. A clear
small fix may use a short inline brief; neither a full document set nor every
skill in this family is mandatory.

A direct call to an implementer does not bypass its readiness check. If a
critical gap appears, pause the affected work and return to its decision owner.
Peer skills are optional: when missing, apply the local question/stop behavior
and report the missing capability rather than pretending to invoke it.

## Installation

Install complete leaf folders; see [usage](../../docs/USAGE.md). Keep peer names
stable and local resources self-contained so repository and installed modes
both work. Review-only requests never authorize code changes or deployment.
