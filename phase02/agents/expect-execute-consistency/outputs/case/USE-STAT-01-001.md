# USE-STAT-01-001
- **标题**: 使用 always() 带括号时若被接受则正常执行
- **维度**: 易用性/兼容性
- **评级**: 断言一致

## 想测什么
验证在 step 中使用 `if: ${{ always() }}`（带括号）时，若平台接受此写法，该步骤无论上游成败均应执行。

## 做了什么
workflow 第一个 step 故意 exit 1 制造失败，第二个 step 使用 `if: ${{ always() }}` 执行 cleanup。断言日志含 "cleanup executed"。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | 日志含 "cleanup executed" | COVERED | if: ${{ always() }} 真实表达式求值，执行结果体现在日志中 → GENUINE |
