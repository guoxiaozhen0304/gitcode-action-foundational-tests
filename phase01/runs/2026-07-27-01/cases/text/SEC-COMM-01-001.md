用例 ID:   SEC-COMM-01-001
维度标签:   [security]
维度:      安全性
优先级:    P0
溯源意图:  INTENT-SEC-026
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      issue_comment / pull_request_comment 触发关键字过滤必须不可被绕过

前置条件:
  - 仓库配置了评论触发 workflow

操作步骤:
  1. 提交一个由 issue_comment 触发的 workflow，job 级配置关键字过滤条件（评论 body 包含指定关键字才执行）
  2. 提交一条将关键字伪装在 markdown 代码块中的评论
  3. 观察是否产生 workflow 运行及运行日志

预期结果:
  - 伪装在代码块或注释中的关键字绝不应触发 workflow（无可执行 run，或 job 被过滤条件跳过）
  - 触发记录应包含评论原始内容哈希，用于审计

验证点:
  - [负向] 伪装在代码块或注释中的关键字绝不应触发 workflow：日志中不应出现被触发步骤的输出
  - [正向] 该伪装评论对应的运行状态为未触发（not_triggered）
  - [非功能] 触发记录应包含评论原始内容哈希，用于审计（平台审计记录，LLM 辅助核验）

清理:      重置 fixture 仓库
