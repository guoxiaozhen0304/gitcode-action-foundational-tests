# COMP-PRTARGET-01-003
- **标题**: fork PR 按文档推荐配置 pull_request_target 的 secret 暴露面核查   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | must_not_contain_secret: TEST_SECRET | COVERED | step echo SECRET_INJECTED/not，secret 通过 env 使用 |
| 2 | secret_injection | negative | eval: llm_assisted | LLM_DEPENDENT | R5: llm_assisted 跳过 |
