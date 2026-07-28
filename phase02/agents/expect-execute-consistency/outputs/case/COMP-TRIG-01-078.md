# COMP-TRIG-01-078
- **标题**: 多事件组合与分支路径过滤验证   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | equals: success | COVERED | 平台提供 |
| 2 | run_logs | positive | must_contain: TRIGGER_EVENT=push | COVERED | step echo TRIGGER_EVENT=\${{ atomgit.event_name }} |
| 3 | run_logs | positive | must_contain: multi_event_ok | COVERED | step echo multi_event_ok |
| 4 | workflow_parse | negative | eval: llm_assisted | LLM_DEPENDENT | R5: paths与paths-ignore共存变体 |
