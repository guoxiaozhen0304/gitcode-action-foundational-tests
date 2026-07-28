# COMPAT-EXPR-01-007
- **标题**: hashFiles 表达式多路径组合边界
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试 hashFiles 同时匹配多个路径模式时返回组合哈希值的边界行为。

## 做了什么
通过 `echo` 输出 `${{ hashFiles('**/package.json', '**/package-lock.json') }}` 的求值结果。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains "hash multi:" | COVERED | `echo` 含 `${{ }}` 多路径表达式输出，日志可验证组合哈希行为 |
