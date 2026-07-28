# REL-TIMEOUT-01-010
- **标题**: 默认超时——未声明 timeout-minutes 运行 361 分钟应被强制终止
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
未声明timeout-minutes时sleep 21660应在360分钟被终止，状态=failure，日志含超时，不应无限运行。

## 做了什么
job无timeout-minutes声明，step sleep 21660。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals=failure | COVERED | 文本"状态为failure"精确对应 |
| 2 | run_logs | positive | contains=timeout | COVERED | 文本"日志含超时信息"对应 |
| 3 | (文本负向) 不应无限运行 | — | — | MISSING | 文本"不应无限运行"在YAML中无独立negative断言 |
