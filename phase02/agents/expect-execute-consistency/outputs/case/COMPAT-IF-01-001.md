# COMPAT-IF-01-001
- **标题**: step 失败后后续 step 默认跳过行为
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试当某 step 失败（exit 1）且无 continue-on-error 时，后续 step 是否被默认跳过。

## 做了什么
第一个 step 执行 `exit 1`，第二个 step 执行 `echo "This should not appear"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals failure | COVERED | exit 1 直接导致 job 失败，status 可验证 |
| 2 | run_logs | negative | contains "This should not appear" | COVERED | 若第二个 step 被跳过，该字符串不出现在日志中 |
