# COMPAT-COMM-01-002
- **标题**: issue_comment types:created 不支持时应给出降级指引   - **维度**: 兼容性   - **评级**: 部分不符
## 想测什么
验证若 types:created 不支持应明确报错或给出替代 types 列表，不应静默忽略导致所有 issue_comment 都触发。
## 做了什么
issue_comment 事件触发，`on: issue_comment: types: [created]`，step echo `COMMENT_ACTION=${{ atomgit.event.action }}`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_status | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；不应静默忽略 types 配置 |
| 2 | run_logs | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；edited/deleted 评论不应产生新运行 |
| 3 | run_logs | positive | must_contain: COMMENT_ACTION=created | GENUINE→COVERED | `${{ atomgit.event.action }}` 为表达式引用，按 R6 GENUINE |
| 4 | error_message | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9 |
说明：文本要求"非 created 类型评论不应产生新运行"验证点，但 YAML 中 trigger.event=issue_comment 未设置具体 action 类型过滤在触发层，实际行为依赖平台 issue_comment 事件分发。此验证点因触发控制不在 YAML 中而存在局限。 |
