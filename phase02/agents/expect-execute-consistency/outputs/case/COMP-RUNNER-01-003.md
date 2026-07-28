# COMP-RUNNER-01-003
- **标题**: 不存在的标签组合导致 job 排队或失败   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | negative | equals: success | COVERED | step echo 'should not run'，不存在的标签导致 job 不成功 |
| 2 | error_message | nonfunctional | eval: llm_assisted | LLM_DEPENDENT | R5 |
