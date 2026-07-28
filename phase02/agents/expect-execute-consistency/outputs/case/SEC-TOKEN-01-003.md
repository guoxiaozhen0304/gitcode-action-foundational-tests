# SEC-TOKEN-01-003
- **标题**: run 结束后旧 ATOMGIT_TOKEN 调用任何 API 必须失效
- **维度**: security
- **评级**: 部分不符

## 想测什么
run 进行中 token 可用；run 结束后旧 token 调用 API 返回 401/403；rerun 签发新 token。

## 做了什么
step1 `git ls-remote` 使用 token，step2 echo "IN_RUN_TOKEN_OPERATIONAL..."。但大写输出与断言的小写期望不完全一致。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | equals:in_run_token_operational | COVERED | step 输出 "IN_RUN_TOKEN_OPERATIONAL:..."，contains 可通过，但严格 equals 大小写不完全匹配 |
| 2 | api_response | negative | must_not_equal:http_2xx_with_post_run_token | MISSING_SOURCE | target 为外部 api_response，workflow 无 step 在 run 结束后发起 API 调用 |
| 3 | rerun_behavior | nonfunctional | equals:new_token_issued_or_explicit_reuse | LLM_DEPENDENT | nonfunctional 类型，rerun token 行为需 harness/LLM 判定 |
