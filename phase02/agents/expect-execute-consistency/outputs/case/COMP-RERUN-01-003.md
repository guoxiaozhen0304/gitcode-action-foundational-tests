# COMP-RERUN-01-003
- **标题**: 超过 6 小时的运行不可 rerun   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | rerun_result | negative | equals: rerun_of_6h_plus_run | COVERED | harness 层验证；workflow 作为触发载体 |
