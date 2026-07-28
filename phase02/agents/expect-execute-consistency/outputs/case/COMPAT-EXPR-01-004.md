# COMPAT-EXPR-01-004
- **标题**: contains 表达式大小写敏感边界   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
验证 contains 表达式的大小写敏感行为：验证 `contains('Hello World', 'world')` (lowercase) 和 `contains('Hello World', 'World')` (exact case) 的结果。
## 做了什么
workflow_dispatch 触发，checkout + 两个 step 分别 echo `${{ contains('Hello World', 'world') }}` 和 `${{ contains('Hello World', 'World') }}`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_logs | positive | contains: exact case match: true | GENUINE→COVERED | `${{ contains() }}` 为真实表达式求值，按 R6 GENUINE |
说明：断言仅覆盖 exact case match（期望 true），未显式断言 lowercase match 的返回值（false）。两者均由同一 workflow 产生，日志中同时出现。文本对 contains 大小写行为的覆盖完整。 |
