# SEC-SUPPLY-01-001
- **标题**: 第三方 Action 引用应支持完整 commit hash 固定
- **维度**: security
- **评级**: 部分不符

## 想测什么
完整 commit SHA 引用 Action 可成功执行；不匹配时 job 应失败或拒绝。

## 做了什么
step 使用 `uses: docker/build-push-action@<valid_sha>` 引用 Action。无 run step 产生验证输出。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals:success_or_action_executed | COVERED | 平台 run_status 为 GENUINE 来源，可观察 action 是否执行成功 |
| 2 | run_logs | negative | must_not_contain:unauthorized_action_execution | VACUOUS | step 仅 `uses:` 指令，无任何 run 语句输出该字符串；R4 规则：step 从不写入 forbidden string |
