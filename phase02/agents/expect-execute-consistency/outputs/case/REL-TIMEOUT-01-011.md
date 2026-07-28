# REL-TIMEOUT-01-011
- **标题**: 自定义 timeout 超默认值——timeout-minutes=720 的接受/拒绝语义探测
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
timeout-minutes=720二选一：接受(可超360运行)或拒绝(含上限值)，不应静默截断到360，探测结果可回写。

## 做了什么
探测型job timeout-minutes=720，echo标记(不实际跑720分钟)。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | config_outcome | positive | equals=accepted_or_explicitly_rejected | COVERED | 文本"接受→超360仍运行；拒绝→错误信息含上限数值"对应二选一 |
| 2 | silent_truncation_to_360_detected | negative | equals=true | COVERED | 文本"不应静默截断(发现升P1)"精确对应 |
| 3 | rejection_error_contains_limit | nonfunctional | equals=true_if_rejected | COVERED | 文本"探测结果记录完整可回写"对应(仅在拒绝时生效) |
