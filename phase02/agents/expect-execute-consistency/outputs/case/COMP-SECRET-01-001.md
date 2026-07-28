# COMP-SECRET-01-001
- **标题**: echo secret 在日志中被脱敏为 ***   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | contains: *** | COVERED | step echo \${{ secrets.TEST_SECRET }}，平台脱敏输出 *** |
| 2 | run_logs | negative | must_not_contain_secret: TEST_SECRET | COVERED | secret 明文不得出现在日志 |
