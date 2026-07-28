# SEC-SUPPLY-01-001
- **标题**: 第三方 Action 引用应支持完整 commit hash 固定
- **维度**: 安全性
- **评级**: 断言一致

## 想测什么
使用完整 commit SHA 引用第三方 Action 可成功执行。

## 做了什么
workflow 使用 `uses: docker/build-push-action@1234567890abcdef1234567890abcdef12345678` 完整 SHA 引用。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | success_or_action_executed | COVERED | 平台执行后可通过 run_status 验证 commit SHA 引用是否被接受并执行 |
| 2 | run_logs | negative | must_not_contain: unauthorized_action_execution | COVERED | 平台日志验证，无未授权行为 |

