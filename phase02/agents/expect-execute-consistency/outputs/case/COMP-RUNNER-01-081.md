# COMP-RUNNER-01-081
- **标题**: 四段式 runs-on（codearts-hosted 首段）调度行为裁定   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | must_contain: RUNNER_NAME= | COVERED | step echo RUNNER_NAME=\${{ runner.name }} |
| 2 | runner_identity | nonfunctional | eval: llm_assisted | LLM_DEPENDENT | R5 |
| 3 | runner_mismatch | negative | eval: llm_assisted | LLM_DEPENDENT | R5 |
