# REL-LOGPERF-01-051-V2
- **标题**: 日志加载性能——200MB 日志下载与查看耗时
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
200MB 日志下载≤120s，完整性 100%。

## 做了什么
循环输出 6,000,000 行 LOG_LINE + 时间戳。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | download_time_seconds | nonfunctional | le 120 | LLM_DEPENDENT | 非功能性能指标 |
| 2 | log_integrity | positive | equals "100%" | COVERED | 行数可校验（6,000,000 行），由 harness 验证 |
