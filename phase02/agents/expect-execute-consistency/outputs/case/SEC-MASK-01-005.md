# SEC-MASK-01-005
- **标题**: Secret 日志脱敏不可通过多行值输出绕过
- **维度**: security
- **评级**: 断言一致

## 想测什么
多行 secret 每一行均被脱敏，换行符不成为脱敏边界。

## 做了什么
workflow echo 多行 secret MULTI_LINE_SECRET 直接到日志。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain_secret "MULTI_LINE_SECRET" | COVERED | 对应"多行 secret 的任一行均不应以明文出现"；platform→GENUINE |
| 2 | run_logs | positive | contains "***" | COVERED | 对应"日志中 secret 输出位置出现脱敏标记 ***"；platform→GENUINE |
