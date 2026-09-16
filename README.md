# Personal Agent Skills

可长期复用的个人 Agent 能力库。按领域组织源码，按当前任务选择能力，
而不是把所有 Skill 一次性塞进上下文。

**Agent 入口：[AGENTS.md](AGENTS.md) → [技能索引](skills/INDEX.md) → 选中的 `SKILL.md`。**
Claude Code 入口 [CLAUDE.md](CLAUDE.md) 复用同一份说明。

## 直接把仓库交给 Agent

复制下面这段，并补上当前任务。项目路径已在上下文中明确时不用重复填写。

```text
使用 https://github.com/dawNotPoi/skills 作为技能库。
先读取该仓库的 AGENTS.md，再按 skills/INDEX.md 选择当前需要的 Skill。
目标是当前业务项目，不要把业务文件写进技能库。
关键需求不明确时，先结合项目现状给方案、引导我决策，不要直接开发。
当前任务：……
```

只有链接不代表已安装或自动生效；Agent 需要能读取仓库文件。每个阶段只读取
实际需要的技能。入口、独立安装、项目级接入见 [使用说明](docs/USAGE.md)。

## 能力分类

| 领域 | 内容 |
| --- | --- |
| [Core](skills/core/README.md) | 选择 Skill、控制加载范围、阶段交接、交互学习状态管理 |
| [Development](skills/development/README.md) | 开发前需求引导、项目 Agent 入口与多宿主适配、Spec/Plan、代码库学习 |
| [UI](skills/ui/README.md) | 界面需求、视觉方向、设计系统、实现、视觉验收 |
| [Writing](skills/writing/README.md) | 基于证据的技术博客与项目复盘 |

具体 Skill 和触发条件只维护在 [skills/INDEX.md](skills/INDEX.md)。
Skill 提供执行指引，不会自动赋予工具权限，也不是强制安全隔离层。

## 安装与检查

源码按领域分组；安装时复制完整的叶子 Skill 目录，保持名称不变。
安装脚本只使用 Python 标准库，默认预览、不覆盖已有目录。

```bash
git clone https://github.com/dawNotPoi/skills.git personal-skills
cd personal-skills
python3 scripts/library.py list
python3 scripts/library.py check
# 预览安装；检查输出后加 --apply 才写入
python3 scripts/library.py install --dest "$HOME/.agents/skills" --all
# Claude Code 可使用 --dest "$HOME/.claude/skills"
```

脚本只复制技能文件，不执行 Skill 内脚本，不改项目指令，不自动安装依赖。
用 `--skill interactive-learning --skill learn-codebase` 可组合通用交互学习与源码学习；
安装 router 不会自动安装其他技能。平台路径依据见使用说明中的官方来源。

## 目录迁移

已有 Skill 名称和显式调用名保持不变：

| 旧源码目录 | 新源码目录 |
| --- | --- |
| `skills/learn-codebase/` | `skills/development/learn-codebase/` |
| `skills/write-evidence-driven-blog/` | `skills/writing/write-evidence-driven-blog/` |

已复制的安装不受源码移动影响；指向旧目录的符号链接需要手动更新。
不保留重复的 `SKILL.md` 别名，避免发现同名技能。遇到已有安装，脚本拒绝覆盖；
先备份并按当前宿主的安装方式更新，不批量删除旧目录。

## 维护

新增技能遵循 `skills/<domain>/<name>/SKILL.md`，同步索引和
[路由回归场景](tests/routing-cases.md)。提交前执行：

```bash
python3 scripts/library.py check
python3 -m unittest discover -s tests -v
```

结构检查不等于真实 Agent 行为测试；各宿主的自动触发和执行仍需单独验证。
