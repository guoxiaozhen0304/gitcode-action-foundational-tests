# SEC-TOKEN-01-004
- **标题**: 残留于 cache/artifact 的 token 在新 run 中绝不应通过鉴权
- **维度**: 安全性
- **评级**: 部分不符

## 想测什么
历史 artifact 中残留的旧 token 在新 run 中调用 API 返回 401/403。

## 做了什么
workflow step 中仅 echo 字面量标记，无真实命令执行 token 操作。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | current_run_token_operational | UNVERIFIABLE | step 仅 `echo "CURRENT_RUN_TOKEN_CHECK: ..."` — 字面量 echo，无真实 token 操作 |
| 2 | api_response | negative | must_not_equal: http_2xx_with_residual_token | COVERED | harness 持残留 token 调用 API 的外部验证 |

