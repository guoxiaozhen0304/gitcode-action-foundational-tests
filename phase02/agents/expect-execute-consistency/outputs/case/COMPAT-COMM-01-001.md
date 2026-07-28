# COMPAT-COMM-01-001
- **标题**: issue_comment types 命名差异 - GitCode 合法 types 应被接受   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
验证 GitCode 风格 issue_comment types（created/edited）被接受并正常触发。
## 做了什么
issue_comment 事件触发，workflow 声明 `on: issue_comment: types: [created, edited]`，step echo `event_name=${{ atomgit.event_name }}`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_status | positive | equals: success + eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；需 LLM 判定 types 被接受且正常触发 |
| 2 | validation_error | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；不应因命名差异拒收 workflow |
