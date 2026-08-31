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
