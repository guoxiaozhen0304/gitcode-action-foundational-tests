# SEC-COMM-01-001
- **标题**: issue_comment / pull_request_comment 触发关键字过滤必须不可被绕过
- **维度**: security
- **评级**: 断言一致

## 想测什么
伪装在代码块中的关键字不应触发 workflow；触发记录应含评论哈希。

## 做了什么
workflow 配置 if: contains(comment.body, '/deploy')；触发评论含代码块包裹的关键字。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain "Triggered by comment" | COVERED | 对应"伪装在代码块中的关键字绝不应触发"；${{ }} 条件过滤→GENUINE |
| 2 | run_status | positive | equals "not_triggered" | COVERED | 对应"该伪装评论对应的运行状态为未触发"；COVERED |
| 3 | platform_audit_log | nonfunctional | eval llm_assisted | COVERED | 对应"触发记录应包含评论原始内容哈希"；LLM 辅助 = 断言一致 |
