# SEC-COMM-01-001
- **标题**: issue_comment/pull_request_comment 触发关键字过滤必须不可被绕过   - **维度**: 安全性   - **评级**: 部分不符
## 想测什么
伪装在markdown代码块中的关键字不应触发workflow，触发记录应包含评论哈希用于审计。
## 做了什么
YAML workflow包含if:${{ contains(...) }}条件过滤和echo "Triggered by comment"步骤。trigger为issue_comment，params含伪装评论body。断言含llm_assisted非功能断言。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | must_not_contain "Triggered by comment" | COVERED | 日志中搜索该echo输出可判定 |
| 2 | run_status | positive | equals "not_triggered" | COVERED | 运行状态为平台可观测值 |
| 3 | platform_audit_log | nonfunctional | 触发记录应含评论哈希 | UNVERIFIABLE | eval:llm_assisted，依赖LLM辅助核验平台审计记录 |
