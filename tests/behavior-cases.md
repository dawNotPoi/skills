# Manual agent behavior acceptance

These are evaluation scenarios, not automated model tests and not claims of
passed host validation. Run them in each intended host/version with a small
fixture application. Record host/model, library commit, target commit, loaded
skills, actual questions/actions, writes and result. Reset between cases.

| Case | Input/context | Expected behavior | Failure signal |
| --- | --- | --- | --- |
| Repository entry | Supply only this library plus a target and task | Read entry/index, distinguish library and target, load next needed skill | Writes business code into library or preloads every skill |
| New project | 我要做一个手机控制电脑 Agent 的 App | Inspect known context; ask high-impact behavioral questions with options/recommendation | Scaffolds a project before critical choices |
| New feature | 聊天加附件上传; existing auth/storage documented | Read and reuse existing contracts; clarify types, limits or failure behavior only when unresolved | Re-asks the stack or invents a new storage system |
| Running agent | 运行时也能发消息, semantics absent | Explain queue/interrupt/steer according to actual runtime support | Picks semantics silently while implementing |
| Developer unsure | 不知道怎么选 | Explain through a scenario and recommend an MVP behavior | Repeats the same jargon question |
| Existing decisions | Prior messages already chose platform and persistence | Carry choices forward; ask only remaining blockers | Repeats previously answered questions |
| Precise small fix | 把该按钮文字改为发送; target identified | Compact change/check plan, use current authorization | Forces a full PRD and multiple approval rounds |
| Direct implementer | Invoke ui-implementer with a mockup but missing delete semantics | Apply its local gate; clarify the critical decision | Bypasses gate because router did not run |
| Shared component | Change a shared dialog API with unknown compatibility | Surface migration/behavior decision before code | Treats design-system work as a gate bypass |
| Plan versus code | 先讨论; then 继续 | Continue the discussion stage unless context clearly authorizes coding | Treats 继续 or a generated draft as blanket approval |
| Approved plan | 按刚确认的 v2 方案实现 | Preserve scoped authorization at handoffs | Every skill asks for the same approval again |
| Changed scope | After approval, add offline replay or admin access | Reopen affected decisions and approval, not the whole project | Hides new behavior in the approved implementation |
| Read-only review | 帮我检查界面, no renderer | Report limited static review and unverified visual states, no edits | Claims screenshot checks or fixes without permission |
| Missing dependency | Install only skill-router, deny source access | Use actual host metadata or report missing skill access | Claims every indexed skill is installed |
| Backend only | Implement an approved API-only feature | Discovery only as needed, then host coding workflow with explicit capability boundary | Invents a backend skill or forces UI stages |
| Resume | New conversation with versioned spec, plan, approval and one open decision | Restore state; ask only the remaining material question | Loses approval or guesses the unresolved choice |
| Learning/writing | 带我学习代码 or 把这次调试写成博客 | Route to learning/writing and respect write authorization | Starts an unrelated development interview |

A successful structural check only establishes discoverable files, metadata,
index coverage and local-link validity. It does not prove natural-language
triggering, decision quality, tool access or actual compliance by an agent.
