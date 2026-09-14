# Skills

Reusable Codex skills for writing and engineering workflows.

## Available Skills

### write-evidence-driven-blog

Turn learning notes, technical discussions, debugging sessions, architecture
decisions, and completed engineering work into original, evidence-driven
Chinese technical blogs.

The skill emphasizes reader contracts, evidence selection, scoped technical
claims, accurate first-person attribution, and editing that removes generic AI
prose without imitating another author's voice.

[View the skill](skills/write-evidence-driven-blog/SKILL.md)

### UI skills

A composable workflow for discovering product UI requirements, choosing a
visual direction, building a design system, implementing interfaces, and
running visual QA. Each stage is an independent skill with explicit handoff
artifacts, so teams can use only the capability the task needs.

[View the UI skills overview](skills/ui/README.md)

## Install

Clone the repository and copy the selected skill into your Codex skills
directory:

```bash
git clone https://github.com/dawNotPoi/skills.git
cp -R skills/skills/write-evidence-driven-blog ~/.codex/skills/
```

Restart Codex or open a new task, then invoke it explicitly:

```text
$write-evidence-driven-blog Turn this engineering session into a Chinese technical blog.
```

The skill can also be discovered automatically for requests about technical
blogs, learning retrospectives, and evidence-driven project write-ups.
