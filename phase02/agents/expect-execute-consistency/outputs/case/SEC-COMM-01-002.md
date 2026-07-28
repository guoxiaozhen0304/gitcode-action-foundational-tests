# SEC-COMM-01-002
- **标题**: 引用/反讽/代码块内嵌指令文本绝不应造成 pull_request_comment 预期外触发   - **维度**: 安全性   - **评级**: 部分不符
## 想测什么
评论过滤中引用块、反讽、代码块内的指令文本不应造成预期外触发，触发应可回溯到具体评论内容。
## 做了什么
YAML workflow包含comments过滤配置('^/deploy fixture-environment$')和echo步骤。trigger为pull_request_comment，params含boundary_comments列表。第三个断言target trigger_audit为抽象平台面目标。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_trigger | positive | equals "exact_command_triggers" | COVERED | 精确指令的触发行为可通过run状态判定 |
| 2 | run_trigger | negative | must_not_equal "triggered_by_quoted_or_embedded_text" | COVERED | 边界评论的触发行为可通过run状态判定 |
| 3 | trigger_audit | nonfunctional | equals "trigger_traceable_to_comment_content" | UNVERIFIABLE | trigger_audit为抽象目标，无具体workflow步骤对应 |
