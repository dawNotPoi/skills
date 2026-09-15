# 使用、入口与迁移

## 1. 整库入口：优先方式

把仓库地址或本地路径交给 Agent，同时说明**目标项目**和**当前任务**：

```text
技能库：https://github.com/dawNotPoi/skills
先读取 AGENTS.md，再读取 skills/INDEX.md，按需读取下一阶段 SKILL.md。
目标项目：<路径或仓库>
任务：<本次需求>
关键行为没说清时，先检查已有实现，再给选项、取舍和建议，不要直接写代码。
```

Agent 必须具备对应的文件/仓库读取能力。单独发送 URL 不等于已安装，
也不保证远程 AGENTS.md 会被自动发现。读取不到时，提供可读 checkout
或入口和选中 Skill 的文本，不要假装加载成功。

远程引用应尽量锁定同一个 commit；索引和 Skill 相对路径都在技能库
内解析，不能在目标项目目录下猜同名文件。PR 尚未合并时，指定 PR 分支
或提交，而不是仍使用 main。

## 2. 让目标项目记住入口

确认目标项目允许后，把下面这段**追加或合并**进已有 AGENTS.md 或
CLAUDE.md；不要覆盖原文件，也不要复制整份技能库维护规则：

```text
Skill library: <可读的本地绝对路径或固定 ref 的仓库地址>
For tasks covered by this library, read its AGENTS.md and skills/INDEX.md,
then only the selected SKILL.md. This repository remains the work target.
Resolve critical product decisions before implementation; preserve existing
project constraints and previously approved scope.
```

入口文本仍是工作流约定，不是系统级权限控制。宿主自己的工具授权、
沙箱和审批机制独立存在。本文不承诺任意 Agent 都支持自动路由或脚本。

## 3. 安装叶子 Skill

源码按领域分组；安装按唯一 Skill 名展开：

```text
源码：skills/development/development-discovery/SKILL.md
安装：<宿主技能目录>/development-discovery/SKILL.md
```

不要把 `development/` 或 `ui/` 当成一个 Skill。需要一起保留叶子目录中的
references、templates 等资源。跨 Skill 交接以稳定名称定位，再根据宿主
实际可用的路径读取；未安装的依赖不是可调用能力。

本库提供可选的纯 Python 安装器，默认不覆盖任何现有目标文件夹：

```bash
# 在克隆的技能库根目录执行，先预览。
python3 scripts/install_skills.py --dest "$HOME/.agents/skills" --all --dry-run
python3 scripts/install_skills.py --dest "$HOME/.agents/skills" --all

# Claude Code 可使用相同叶子目录，换成其个人技能路径。
python3 scripts/install_skills.py --dest "$HOME/.claude/skills" --all

# 只安装一个 Skill；其本地资源会一起复制。
python3 scripts/install_skills.py --dest /your/skill-directory --skill development-discovery
```

也可把 `--dest` 指向目标项目的 `.agents/skills` 或 `.claude/skills`。
工具不会修改目标项目的入口文件，不运行 Skill 附带脚本、不读取密钥、
不自动安装依赖、不进行部署。出现同名目录时先停止；请人工比较备份后
处理，不使用强制覆盖。复制式安装不会自动跟随源仓库更新。

安装 router 时会附带源索引的生成快照。快照用于路由，不代表其他 Skill
已安装；实际可用性仍以宿主元数据/可读文件为准。只复制 router 而不给它
其他可用 Skill 或源仓库，不会凭空拥有整个技能库。

## 4. 触发与能力边界

Codex CLI/IDE 可通过 `$skill-router` 或 `$development-discovery` 显式选择；
Claude Code 可使用 `/skill-router` 或 `/development-discovery`。自然语言
是否自动匹配取决于宿主、技能可见性和 description，不作必触发保证。
通用 Agent 不支持原生 Skill 时，可手动读取入口、索引和选中的正文。

正常的触发检验：给出一个模糊的新功能请求，确认 Agent 先读目标项目，
提出行为选项并停在决策阶段，而不是先创建文件。再给出一个清晰的小
修改，确认它不会反复提问。完整场景见
[行为验收](../tests/behavior-cases.md)。

已核对的宿主文档（2026-09-15；以后以当前官方说明为准）：

- [Codex Skills](https://developers.openai.com/codex/skills/)
- [Codex AGENTS.md](https://developers.openai.com/codex/guides/agents-md/)
- [Claude Code Skills](https://code.claude.com/docs/en/skills)

本次采用 Codex 文档中的 `.agents/skills` 路径；旧版本可能有不同兼容
路径，不能把旧 README 中的 `~/.codex/skills` 当作跨版本统一约定。

## 5. 目录迁移

| 旧源码路径 | 新源码路径 |
| --- | --- |
| `skills/learn-codebase/` | `skills/development/learn-codebase/` |
| `skills/write-evidence-driven-blog/` | `skills/writing/write-evidence-driven-blog/` |

这两个 Skill 的名称、正文和内部资源保持不变。已有的复制式安装不因
源码移动立即失效，但旧安装命令、文档链接和指向旧源码路径的符号链接
需要更新。不要在新旧源位置保留两个同名 SKILL.md，以免重复发现。

新增 Skill 时更新唯一索引并运行结构校验，不维护多套手写路由表。
