# COMP-CTX-01-055

- **标题**: workflow_dispatch 触发下 inputs 正常求值（回归保护）
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 `workflow_dispatch` 触发时 `inputs` 正常求值，未传参时取声明默认值。

## 做了什么
workflow 的 `on.workflow_dispatch.inputs` 声明 `pr_id` 默认值为 `default-pr`；step 中 `echo "DISPATCH_INPUT=${{ inputs.pr_id }}"` 输出求值结果。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | COVERED | workflow_dispatch inputs 正常求值，完整执行 |
| 2 | run_logs | positive | must_contain: DISPATCH_INPUT=default-pr | COVERED | `${{ inputs.pr_id }}` 求值为默认值 `default-pr` 后 echo 输出 |
