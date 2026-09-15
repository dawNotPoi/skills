# Personal Agent Skills

可组合的个人 Agent Skill 库，用于需求澄清、代码学习、UI 设计与实现、视觉验收和技术写作。

**给 Agent 的入口：[AGENTS.md](AGENTS.md)。能力与路径的唯一索引：[skills/INDEX.md](skills/INDEX.md)。**

## 直接把仓库交给 Agent

```text
使用 https://github.com/dawNotPoi/skills 作为本次任务的技能库。
先读取根目录 AGENTS.md，再读取 skills/INDEX.md，按当前任务只加载必要的 SKILL.md。
目标项目是：<项目路径或仓库>。
本次任务是：<需求>。
已有决定不要重复问；关键行为不明确时先读项目，再给出选项、取舍和建议，引导我确认。
在关键决策未解决、实现范围未获授权前，不要直接修改业务代码。
```

仓库链接不是安装命令，也不会保证所有 Agent 自动读取入口。Agent 必须有读取仓库的工具；没有时，应明确说明缺少访问能力，而不是声称已加载。`AGENTS.md` 是本库的使用约定，不是覆盖目标项目规则或运行时权限的系统提示词。

## 领域

| 领域 | 职责 |
| --- | --- |
| [Core](skills/core/README.md) | 识别意图、定位技能、按需加载和交接 |
| [Development](skills/development/README.md) | 开发前需求澄清、方案、实施计划及代码学习 |
| [UI](skills/ui/README.md) | 界面需求、视觉方向、设计系统、实现和视觉验收 |
| [Writing](skills/writing/README.md) | 有证据的技术写作 |

目录采用 `skills/<domain>/<skill-name>/SKILL.md`。领域目录不是 Skill；单个 Skill 的名称在整个库内保持唯一。

## 开发类默认流程

```text
读取目标项目与已有决定
  -> 找到会影响行为、边界、数据、权限或验收的未知项
  -> 每轮提出最重要的 1 个问题，必要时最多 3 个
  -> 给出可选方案、取舍和推荐
  -> 形成 Spec 与可验证的 Plan
  -> 确认对应版本的实现范围
  -> 按需加载实现技能
  -> 验证、记录偏差、沉淀长期规则
```

明确的小修复走快速路径；学习和仅审查任务不自动进入开发。新增需求使原确认失效时，只重新确认受影响的部分。

## 安装与维护

推荐先使用整库入口。单独安装时，把选中的**叶子 Skill 文件夹**放入宿主支持的技能目录，不要把整个 `skills/` 分类树当成一个 Skill。

详见 [使用与迁移指南](docs/usage.md)。其中包括 Codex、Claude Code、通用 Agent、独立安装及目标项目入口片段。

```bash
python3 scripts/check_library.py
python3 -m unittest discover -s tests -p 'test_*.py'
```

[行为验收场景](tests/behavior-cases.md) 用于检查真实 Agent 是否正确路由、先澄清再开发，以及能否从上下文中断后恢复。静态校验不能证明这些运行时行为已经通过。
