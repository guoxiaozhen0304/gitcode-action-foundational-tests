# REL-TIMEOUT-01-008
- **标题**: job timeout 越界触发——361 分钟应在 360 分钟被强制终止
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
job sleep 21660(361min)应在360±2min时被终止，状态=failure，日志含超时信息，不应超过365分钟。

## 做了什么
job sleep 21660秒(≈361分钟)。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals=failure | COVERED | 文本"状态为failure"精确对应 |
| 2 | run_logs | positive | contains=timeout | COVERED | 文本"日志含超时信息"对应(contains timeout) |
| 3 | (文本负向) 不应运行超过365分钟 | — | — | MISSING | 文本"不应运行超过365分钟"在YAML中无独立断言 |
