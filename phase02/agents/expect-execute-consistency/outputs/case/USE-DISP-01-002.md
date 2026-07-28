# USE-DISP-01-002
- **标题**: workflow_dispatch 未提供参数但存在 default 时应使用默认值运行
- **维度**: usability
- **评级**: 断言一致

## 想测什么
未提供 input 值时 workflow 使用 default 值成功运行。

## 做了什么
workflow 配置 default:staging 的 input（required:false），step `echo "env=${{ inputs.environment }}"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains:"env=staging" | COVERED | step 通过 `${{ inputs.environment }}` 显式 echo 默认值，精确匹配 |
