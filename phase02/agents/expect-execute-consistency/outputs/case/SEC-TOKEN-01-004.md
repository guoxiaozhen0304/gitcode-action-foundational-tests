# SEC-TOKEN-01-004
- **标题**: 残留于 cache/artifact 的 token 在新 run 中绝不应通过鉴权
- **维度**: security
- **评级**: 部分不符

## 想测什么
残留 token 在新 run 中调用 API 返回 401/403；新 run 自身 token 正常工作。

## 做了什么
step1 curl 使用残留 token 调用 API，输出 RESIDUAL_TOKEN_HTTP / RESIDUAL_TOKEN_ACCEPTED_BAD / RESIDUAL_TOKEN_REJECTED_OK。step2 curl 使用当前 token 确认可用。断言 3 为外部 api_response 目标。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain:CURRENT_RUN_TOKEN_OPERATIONAL | COVERED | step2 显式 echo 该字符串 |
| 2 | run_logs | negative | must_not_contain:RESIDUAL_TOKEN_ACCEPTED_BAD | COVERED | step1 仅在 bad path 输出该字符串，为有效负向验证 |
| 3 | api_response | negative | must_not_equal:http_2xx_with_residual_token | MISSING_SOURCE | target 为外部 api_response，workflow step 代理了 API 调用但 target 指向外部 |
