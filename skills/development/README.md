# Development

[development-discovery](development-discovery/SKILL.md) guides a developer from
an incomplete project or feature idea to explicit decisions, a specification,
and a scoped implementation plan. It checks readiness rather than requiring
an interview for every edit.

[project-agent-bootstrap](project-agent-bootstrap/SKILL.md) initializes or
refactors a repository's long-lived Agent instruction layer. It separates one
canonical project memory from thin Claude/Cursor/other host adapters, reusable
Skills, project-specific Skill adapters, and feature docs so instructions do not
drift into duplicated prompt stacks.

[learn-codebase](learn-codebase/SKILL.md) builds an evidence-backed mental model.
Use its guided-learning mode only when learning is the user's goal. Existing
feature work normally needs a narrow repository inspection, not a full lesson.

After readiness, hand UI work to the relevant UI skill and non-UI work to the
host's available engineering capabilities. This family currently contains no
generic production-code executor.
