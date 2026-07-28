# SEC-SIDE-01-001
- **标题**: Secret 不经 output 侧信道绕过脱敏外泄
- **维度**: security
- **评级**: 断言一致

## 想测什么
Secret 明文不应通过 ATOMGIT_OUTPUT 侧信道未遮蔽外泄。

## 做了什么
step1 将 `${{ secrets.API_KEY }}` 写入 `$ATOMGIT_OUTPUT`，step2 通过 `steps.step1.outputs.result` 读取并 echo。两条断言分别检查 run_logs 和 step_output 中无 secret 明文。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain_secret:API_KEY | COVERED | step2 `echo` 引用 outputs.result，平台应对日志中 secret 值脱敏；可观察 |
| 2 | step_output | negative | must_not_contain_secret:API_KEY | COVERED | step1 写入 output、step2 读取回显，output 值可通过日志间接观察 |
