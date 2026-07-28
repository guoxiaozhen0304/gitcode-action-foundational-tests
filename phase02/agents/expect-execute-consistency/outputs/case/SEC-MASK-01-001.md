# SEC-MASK-01-001
- **标题**: Secret 值在运行日志中必须被自动脱敏为 ***
- **维度**: security
- **评级**: 断言一致

## 想测什么
echo secret 到日志时值被替换为 ***，全文搜索原值命中数为0。

## 做了什么
workflow echo secrets.DEPLOY_TOKEN 直接到日志。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain_secret "DEPLOY_TOKEN" | COVERED | 对应"日志中绝不应出现 DEPLOY_TOKEN 原值"；platform masking→GENUINE |
| 2 | run_logs | positive | contains "***" | COVERED | 对应"脱敏标记 *** 出现在对应位置"；platform→GENUINE |
