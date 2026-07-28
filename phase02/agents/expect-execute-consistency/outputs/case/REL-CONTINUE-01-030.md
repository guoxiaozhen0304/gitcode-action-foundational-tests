# REL-CONTINUE-01-030
- **标题**: continue-on-error=true——job 失败后 workflow 不应终止
- **维度**: reliability
- **评级**: 断言一致
## 想测什么
配置 continue-on-error=true 的 job_a（exit 1 失败），验证 job_a=failure、job_b=success、workflow 不应整体 failure。
## 做了什么
YAML 定义 job_a continue-on-error:true 执行 exit 1，job_b 没有 needs 依赖直接执行 echo。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_a_status | positive | equals failure | COVERED | YAML exit 1 真实命令 + continue-on-error，platform 日志确认 job_a 失败 |
| 2 | job_b_status | positive | equals success | COVERED | YAML echo "job_b executed" 真实执行，platform 日志确认 job_b 正常完成 |
| 3 | workflow_status | positive | equals success | COVERED | YAML assert workflow_status=success，对应文本负向（"workflow 不应因 job_a 失败而整体 failure"）通过正向 success 覆盖 |
