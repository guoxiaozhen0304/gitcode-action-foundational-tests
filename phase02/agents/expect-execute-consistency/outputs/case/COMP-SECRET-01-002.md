# COMP-SECRET-01-002
- **标题**: secret 原始值不应以明文出现在标准日志中   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | must_not_contain_secret: TEST_SECRET | COVERED | env 方式 echo \$MY_SECRET，平台脱敏 |
