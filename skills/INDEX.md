# Skill index

This is the canonical repository catalog. Read metadata here, then read only the
selected skill. Paths are relative to this file, not the target project.

| Skill | Start here when | Output / boundary |
| --- | --- | --- |
| [skill-router](core/skill-router/SKILL.md) | 使用我的技能库；choose or sequence capabilities | Route and handoff; no product implementation |
| [interactive-learning](core/interactive-learning/SKILL.md) | 带我学、一步一步学；long conversational learning with follow-up questions or frequent detours | Stable learning roadmap, branch/return-point handling, checkpoints; does not replace domain-specific evidence methods |
| [development-discovery](development/development-discovery/SKILL.md) | 新项目、新功能；behavior, scope, state, permissions, or acceptance unclear | Guided decisions, spec and plan; readiness before code |
| [project-agent-bootstrap](development/project-agent-bootstrap/SKILL.md) | 初始化/重构项目 Agent 入口；AGENTS.md、CLAUDE.md、Cursor/Claude/Codex 等规则职责或多宿主兼容不清 | One canonical project memory plus minimal host adapters; preserve existing rules and avoid prompt duplication |
| [learn-codebase](development/learn-codebase/SKILL.md) | 学习源码、熟悉仓库、解释执行链路 | Evidence-backed understanding; not a mandatory lesson before every feature |
| [product-ui-discovery](ui/product-ui-discovery/SKILL.md) | UI tasks, navigation, content, or screen states unclear | UI brief; reuse existing product decisions |
| [ui-direction-designer](ui/ui-direction-designer/SKILL.md) | 视觉方向、界面风格尚未确定 | Direction options and recommendation; no production code |
| [design-system-builder](ui/design-system-builder/SKILL.md) | 统一主题、tokens、组件契约 | System contract; code only with implementation authorization |
| [ui-implementer](ui/ui-implementer/SKILL.md) | 按已明确的需求实现或修改界面 | Scoped code and verification; stop on critical missing decisions |
| [visual-qa-critic](ui/visual-qa-critic/SKILL.md) | 检查界面、视觉验收、交互回归 | Evidence-backed findings; review-only by default |
| [write-evidence-driven-blog](writing/write-evidence-driven-blog/SKILL.md) | 技术博客、学习复盘、项目文章 | Original draft from evidence; no automatic publication |

## Routing rules

- General conversational learning, especially when the user asks to proceed step
  by step or frequently interrupts with questions, may use `interactive-learning`
  to preserve the roadmap, branch stack, return point, parking lot, and learning
  checkpoints. Do not use it for a one-shot factual answer or force quiz mode on
  users who asked for a report.
- Repository/source learning still belongs to `learn-codebase`. When the user is
  learning interactively, compose it with `interactive-learning`: repository
  evidence and execution-path methodology stay with `learn-codebase`; pacing and
  conversational state stay with `interactive-learning`.
- New project / material feature: start with a scoped readiness check. If
  requirements and authorization are already sufficient, take the fast path;
  do not repeat a discovery interview or demand redundant confirmations.
- Project Agent entry/init/refactor work goes to `project-agent-bootstrap`.
  Inspect existing instructions before creating files; do not treat bootstrap as
  permission to overwrite a repository's current rules or generate every host
  adapter by default.
- Existing project: inspect instructions, related code/contracts, and tests
  before questioning. Use `learn-codebase` only for an actual learning or deep
  orientation need, not to quiz a developer who asked for implementation.
- Pure UI design with known product behavior may start at UI discovery or
  direction. Cross-cutting product/system unknowns go to development discovery.
- A tiny, unambiguous fix can go directly to the relevant implementer. There is
  no need for a full spec ceremony or new design system.
- Review and writing requests do not imply code changes. Route newly discovered
  uncertainty back to the owning skill, not automatically to the entire pipeline.
- There is no backend implementation, deployment, or debugging skill in this
  catalog yet. Hand off to the host's actual capabilities after readiness; do
  not invent a missing skill or force an API task through `ui-implementer`.

When only individual skills are installed, use the host's actual skill registry
or inspect sibling `SKILL.md` metadata. This index is for repository mode; it is
not an implicit installation manifest or an executable workflow.
