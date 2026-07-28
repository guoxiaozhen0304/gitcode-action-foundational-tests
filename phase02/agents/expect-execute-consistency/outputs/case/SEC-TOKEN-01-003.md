# SEC-TOKEN-01-003
- **标题**: run 结束后旧 ATOMGIT_TOKEN 调用任何 API 必须失效
- **维度**: 安全性
- **评级**: 断言一致

## 想测什么
run 结束后旧 token 调用 API 返回 401/403；rerun 签发新 token 行为可判定。

## 做了什么
workflow 中用 `${{ atomgit.token }}` 执行 git ls-remote，harness 在 run 结束后持旧 token 调 API。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | in_run_token_operational | COVERED | `git ls-remote ... ${{ atomgit.token }}` 真实表达式和命令，验证 run 中 token 可用 |
| 2 | api_response | negative | must_not_equal: http_2xx_with_post_run_token | COVERED | harness 在 run 结束后持旧 token 调用 API，外部验证 |
| 3 | rerun_behavior | nonfunctional | new_token_issued_or_explicit_reuse | UNVERIFIABLE | 平台 rerun 行为，workflow 无对应产生物 |

