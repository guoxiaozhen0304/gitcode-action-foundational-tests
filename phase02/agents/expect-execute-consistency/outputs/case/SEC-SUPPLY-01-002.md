# SEC-SUPPLY-01-002
- **标题**: commit hash 不匹配时第三方 Action 应被拒绝执行
- **维度**: security
- **评级**: 部分不符

## 想测什么
错误 commit SHA 引用 Action 时 job 应失败或拒绝，系统不应静默回退。

## 做了什么
step 使用 `uses: docker/build-push-action@0000...`（无效 SHA）。无 run step。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | must_not_equal:success | COVERED | 平台 run_status 可观察，无效 SHA 预期非 success |
| 2 | run_logs | positive | equals:action_not_found_or_sha_mismatch | VACUOUS | step 无 run 语句输出该字符串；平台日志可能包含相关错误但非 step 显式产出 |
