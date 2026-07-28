# REL-TIMEOUT-01-009
- **标题**: 自定义短超时——timeout-minutes=1 时 step 运行 2 分钟应被强制终止
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
timeout-minutes=1时sleep 120应在60±10s被终止，状态=failure。

## 做了什么
job timeout-minutes=1，step sleep 120。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals=failure | COVERED | 文本"状态为failure"精确对应 |
| 2 | job_duration_seconds | nonfunctional | le=70 | COVERED | 文本"实际运行时长60±10秒"对应(≤70覆盖60+10) |
