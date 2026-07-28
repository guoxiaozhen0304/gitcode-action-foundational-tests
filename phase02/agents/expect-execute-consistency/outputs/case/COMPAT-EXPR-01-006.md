# COMPAT-EXPR-01-006
- **标题**: hashFiles 表达式无匹配路径边界
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试 hashFiles 表达式对不存在的文件模式返回空字符串的边界行为。

## 做了什么
通过 `echo` 输出 `${{ hashFiles('**/nonexistent-pattern.xyz') }}` 的求值结果。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains "hash no match:" | COVERED | `echo` 含 `${{ }}` 表达式输出，日志中可验证无匹配时的返回行为 |
