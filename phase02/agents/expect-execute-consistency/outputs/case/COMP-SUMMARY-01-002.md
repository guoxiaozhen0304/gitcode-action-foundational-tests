# COMP-SUMMARY-01-002
- **标题**: summary 中不应暴露系统内部路径   - **维度**: 完备性   - **评级**: 完全不符
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | step_summary | negative | must_not_contain: /tmp/runner | VACUOUS | R4: step 只写 Results: OK，从不写 /tmp/runner，断言真空成立 |
| 2 | step_summary | negative | must_not_contain: /opt/actions | VACUOUS | R4: 同上，step 从不写 /opt/actions |
