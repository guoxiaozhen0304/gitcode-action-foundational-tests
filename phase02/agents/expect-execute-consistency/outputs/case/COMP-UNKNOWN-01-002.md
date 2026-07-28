# COMP-UNKNOWN-01-002
- **标题**: 不应静默忽略未知字段导致用户误以为配置生效   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | negative | equals: success_with_unknown_field_silently_ignored | COVERED | harness 验证未知字段不应被静默忽略 |
