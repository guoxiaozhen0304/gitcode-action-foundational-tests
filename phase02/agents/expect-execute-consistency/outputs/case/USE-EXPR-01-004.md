# USE-EXPR-01-004
- **标题**: 未文档化函数 default() 的文档缺失 diff（与平台行为断言合并证据链）
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
探测 `default()` 函数的实际求值行为并检查 expressions.md 函数表是否遗漏该函数条目。

## 做了什么
workflow 包含一个 `if: "${{ default() }}"` 的条件步骤和一个 `always()` 标记步骤，记录 default() 实际求值结果。文档侧检查函数表是否包含 default。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | 记录 default() 求值结果 | COVERED | ${{ default() }} 真实表达式求值，结果体现在日志中 → GENUINE |
| 2 | documentation | negative | 函数表缺失 default 即不合格 | COVERED | eval: deterministic，函数名集合包含检查可程序化 |
