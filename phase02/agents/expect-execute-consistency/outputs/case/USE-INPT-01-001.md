# USE-INPT-01-001
- **标题**: 使用 string 类型 input 时正常通过校验
- **维度**: 易用性/兼容性
- **评级**: 断言一致

## 想测什么
验证 workflow_dispatch inputs 声明 type: string 时 YAML 校验通过、可手动触发且输入参数正常传递。

## 做了什么
workflow 声明一个 string 类型的 env input（有 default: staging），step 通过 `${{ inputs.env }}` 引用并 echo 输出。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | 运行成功完成 | COVERED | 正常输入类型校验 + 调度执行 → GENUINE |
