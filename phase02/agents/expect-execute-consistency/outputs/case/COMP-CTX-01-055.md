# COMP-CTX-01-055
- **标题**: workflow_dispatch 触发下 inputs 正常求值（回归保护）
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
workflow_dispatch 下 inputs 正常求值，未传参时取声明默认值。

## 做了什么
1. workflow 声明 `on.workflow_dispatch.inputs.pr_id`（default: default-pr）
2. step `Echo dispatch input`：`echo "DISPATCH_INPUT=${{ inputs.pr_id }}"`

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | success | COVERED | ${{ }} 表达式可求值 |
| 2 | run_logs | positive | must_contain: DISPATCH_INPUT=default-pr | COVERED | ${{ inputs.pr_id }} 取默认值并 echo 输出 |
