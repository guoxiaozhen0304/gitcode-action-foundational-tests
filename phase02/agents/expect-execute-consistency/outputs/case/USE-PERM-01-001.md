# USE-PERM-01-001
- **标题**: 使用 GitCode 权限域命名时正常生效
- **维度**: 易用性/兼容性
- **评级**: 断言一致

## 想测什么
验证在 workflow 中使用 `permissions: repository: read`（GitCode 命名域）时，权限声明被正确解析且运行成功。

## 做了什么
workflow 声明 `permissions: repository: read`，job 使用 `uses: checkout` 执行检出步骤。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | 运行成功完成 | COVERED | uses: checkout 真实 action 调用 + 权限校验 → GENUINE |
