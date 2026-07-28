# REL-LOG-01-041
- **标题**: 单 job 日志大小上限探测——500MB 带序号日志的完整保留或明确截断标识
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
500MB 带序号日志可下载，行号连续或明确截断标识；无静默尾部丢失。

## 做了什么
seq 输出 8,000,000 行带序号日志（约 500MB）。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | log_downloadable | positive | equals "true" | COVERED | 日志可下载性由平台验证 |
| 2 | tail_integrity | positive | equals "complete_or_explicitly_marked_truncated" | COVERED | 行号连续性校验由 harness 执行，日志内容提供了判定数据 |
| 3 | silent_tail_loss_detected | negative | equals "true" | COVERED | 若静默丢失尾部则行号不连续且无截断提示 |
| 4 | measured_log_limit | nonfunctional | equals "recorded" | LLM_DEPENDENT | 实测记录型指标 |
