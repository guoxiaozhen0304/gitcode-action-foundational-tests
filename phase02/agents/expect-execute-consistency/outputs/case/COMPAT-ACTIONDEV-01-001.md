# COMPAT-ACTIONDEV-01-001
- **标题**: action.yml 元数据校验与 GitHub 差异   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
验证不支持的 action.yml 字段不导致 workflow 失败，系统给出明确提示。
## 做了什么
workflow_dispatch 触发，checkout 后 uses: ./.github/actions/my-action 本地 action。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_status | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；不支持的字段不应导致失败 |
| 2 | error_message | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；系统应提示不支持的元数据 |
