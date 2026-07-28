# COMPAT-EXPR-01-005
- **标题**: contains 表达式空值与空字符串边界
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试 contains 表达式对空值、空字符串的边界求值行为，验证与 GitHub Actions 的一致性。

## 做了什么
通过 `echo` 输出 `${{ contains('', 'a') }}` 和 `${{ contains('abc', '') }}` 的求值结果到日志。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains "empty needle:" | COVERED | `echo` 输出含 `${{ }}` 表达式，日志中可观测边界求值结果 |
