# REL-LONG-01-043
- **标题**: 长时运行接近 timeout 边界——350 分钟运行应成功且心跳保活正常
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
timeout-minutes=360 下 job 运行350分钟应成功完成、心跳保活正常、不被误判为死进程。

## 做了什么
workflow 执行350次循环（每次sleep 60秒并输出心跳日志）。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals=success | COVERED | 文本"job状态=success"直接对应 |
| 2 | heartbeat_interval_seconds | nonfunctional | le=60 | COVERED | 文本"心跳日志间隔≤60秒"直接对应 |
| 3 | (文本负向) job_not_terminated_before_350min | negative | — | MISSING | 文本"不应在350分钟前被误判为死进程"在YAML中无对应断言 |
