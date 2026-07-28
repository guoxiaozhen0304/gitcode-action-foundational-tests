# COMP-TRIG-01-074

- **标题**: workflow_dispatch 事件关键字段与 inputs 验证
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 workflow_dispatch 的 inputs 参数可访问，含 default 和 required。

## 做了什么
Steps: `echo "ENV=${{ inputs.environment }}"`、`echo "VER=${{ inputs.version }}"`——`${{ inputs.* }}` 表达式。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain ENV= | COVERED | `${{ inputs.environment }}` 上下文表达式（Rule 6） |
| 2 | run_logs | positive | must_contain VER= | COVERED | `${{ inputs.version }}` 上下文表达式 |
| 3 | run_logs | positive | must_contain dispatch_ok | COVERED | marker signal |
