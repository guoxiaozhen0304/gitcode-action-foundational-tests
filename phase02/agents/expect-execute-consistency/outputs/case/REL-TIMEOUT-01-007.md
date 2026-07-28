# REL-TIMEOUT-01-007
- **标题**: job timeout 边界值——359 分钟运行应在 360 分钟边界前完成
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
timeout-minutes=360时job sleep 21540(359min)应success，不应在358分钟前被强制终止。

## 做了什么
job sleep 21540秒(≈359分钟)。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals=success | COVERED | 文本"job状态=success"精确对应 |
| 2 | job_duration_minutes | nonfunctional | le=359 | COVERED | 文本"job在359分钟前成功完成"对应 |
| 3 | (文本负向) 不应在358分钟前被终止 | — | — | MISSING | 文本"不应在358分钟前被强制终止"在YAML中无独立negative断言 |
