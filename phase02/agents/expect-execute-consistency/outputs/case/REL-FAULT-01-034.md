# REL-FAULT-01-034
- **标题**: 故障注入——cache 服务 503 不可用时 job 应优雅降级为 cache miss
- **维度**: reliability
- **评级**: 断言一致
## 想测什么
在 cache restore 期间注入 503，验证 cache step 标记为 miss、后续 step 正常执行、job 不应整体 failure。
## 做了什么
YAML 使用 cache action（restore 步骤）+ 后续 echo step，fault_injection 对 cache 服务注入 503。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals success | COVERED | YAML assert job_status=success，对应文本"cache step 标记为 miss 或跳过" + "后续 step 正常执行" |
| 2 | run_logs | positive | contains "cache miss" | COVERED | YAML assert 日志含"cache miss"，cache action 层面的降级提示 → GENUINE |
| 3 | no_overall_failure | negative | job 不应因 cache 服务不可用而整体 failure | COVERED | job_status=success 隐含未因 cache 不可用而整体失败，对应文本负向断言 |
