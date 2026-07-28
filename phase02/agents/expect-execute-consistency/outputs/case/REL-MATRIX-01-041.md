# REL-MATRIX-01-041
- **标题**: matrix 组合数越界——300 组合超上限时应明确报错（含上限值）不得静默截断
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
300组合若超上限应明确报错(含上限值)，或全部展开(job数=300)，不应静默截断。

## 做了什么
10×30=300 组合探测型matrix，每实例仅echo组合标记。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | overflow_outcome | positive | equals=expanded_300_or_explicit_rejection_with_limit | COVERED | 文本"拒绝时错误信息含实际上限数值；或全部展开且job数=300"精确对应 |
| 2 | silent_truncation_detected | negative | equals=true | COVERED | 文本"不应静默截断"精确对应 |
| 3 | measured_matrix_limit | nonfunctional | equals=recorded | COVERED | 文本"实测上限值记录完整，可回写platform-config"对应 |
