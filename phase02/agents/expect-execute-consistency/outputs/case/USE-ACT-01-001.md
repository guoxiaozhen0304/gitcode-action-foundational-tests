# USE-ACT-01-001
- **标题**: 使用裸插件名 checkout 时正常拉取官方 Action
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
使用 `uses: checkout` 裸插件名时官方 Action 被正确拉取并执行。

## 做了什么
workflow 中 `uses: checkout` 后执行 `ls -la` 验证 checkout 成功。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | COMPLETED | COVERED | `uses: checkout` 真实 action 引用 + `ls -la` 验证，运行完成后检查状态 |

