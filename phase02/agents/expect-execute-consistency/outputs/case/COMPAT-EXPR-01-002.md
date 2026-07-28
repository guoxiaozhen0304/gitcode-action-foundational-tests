# COMPAT-EXPR-01-002
- **标题**: success() 函数的处理行为差异   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
探测 `if: ${{ success() }}` 在 GitCode 平台的处理行为（接受并条件执行 vs 拒绝并表达式解析错误）。
## 做了什么
workflow_dispatch 触发，job-a（checkout + 真实校验），job-b（needs: job-a，`if: ${{ success() }}` echo `SUCCESS_FN_ACCEPTED`）。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_status | positive | equals: success | GENUINE→COVERED | job-a checkout + ls 为真实操作 |
| 2 | run_logs | positive | must_contain: JOB_A_VERIFIED | GENUINE→COVERED | 真实校验产生 |
| 3 | workflow_parse | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；`if: ${{ success() }}` 为显式探针 |
| 4 | workflow_parse | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；不应静默忽略表达式 |
