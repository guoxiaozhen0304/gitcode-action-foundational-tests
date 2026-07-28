# COMP-TIMEOUT-01-002

- **标题**: 超时的 job 被强制终止并标记为 failure
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 timeout-minutes: 1 时，sleep 120 导致 job 被强制终止为 failure。

## 做了什么
Step 1: `echo "starting"`。Step 2: `sleep 120`——真实命令，超过 1min timeout 被平台终止。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals success | COVERED | sleep 120 超 1min timeout，run_status != success 为真实平台行为 |
| 2 | run_status | positive | equals failure | COVERED | 故意超时测试，run_status=failure 为正确预期（Rule 2） |
| 3 | run_logs | positive | contains starting | COVERED | 超时前日志保留，echo marker 证明日志完整性 |
