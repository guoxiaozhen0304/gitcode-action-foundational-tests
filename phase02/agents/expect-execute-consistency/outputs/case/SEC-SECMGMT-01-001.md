# SEC-SECMGMT-01-001
- **标题**: Secret 写入后任何 API/UI 路径绝不应回读明文
- **维度**: security
- **评级**: 部分不符

## 想测什么
验证 secret 写入后，任何读取接口/UI 均不返回明文，且 workflow 正常引用时日志脱敏。

## 做了什么
Workflow 使用 `${{ secrets.DEPLOY_TOKEN }}` 在 run 步骤中 echo 引用 secret，触发后检查 run_logs 与 secret_mgmt_api。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | equals:masked_with_asterisks | COVERED | step 通过 `${{ secrets.DEPLOY_TOKEN }}` 引用真实 secret，平台日志脱敏可观察 |
| 2 | secret_mgmt_api | negative | must_not_contain_secret:DEPLOY_TOKEN | MISSING_SOURCE | target 为外部 API 面，workflow 无任何 step 枚举 API 或验证 API 响应；需 harness 外置验证 |
