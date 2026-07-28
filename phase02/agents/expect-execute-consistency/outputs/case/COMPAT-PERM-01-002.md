# COMPAT-PERM-01-002

- **标题**: 未声明 permissions 时 fork PR 写操作隔离   - **维度**: 兼容性   - **评级**: 部分不符

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | negative | ==success | COVERED | ; expects run to fail (genuine negative) |
| 2 | run_logs | negative | !secret[] | VACUOUS | must_not_contain_secret with empty value: always passes (空字符串永不出现在日志中) |
