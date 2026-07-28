# REL-MATRIX-01-040
- **标题**: matrix 组合数边界——256 组合（GitHub 上限）应全部展开或被明确拒绝
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
256组合全部展开(job数=256)或被明确拒绝，不应静默截断，展开时延≤600s。

## 做了什么
8×32=256 组合探测型matrix，max-parallel=5，每实例仅echo组合标记。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | jobs_expanded_count | positive | equals=256_or_explicit_rejection | COVERED | 文本"job数与声明组合数一致(256)或收到明确错误"精确对应 |
| 2 | silent_truncation_detected | negative | equals=true | COVERED | 文本"不应静默截断"精确对应(negative+equals=true语义一致) |
| 3 | expand_enqueue_seconds | nonfunctional | le=600 | COVERED | 文本"展开/入队时延≤600秒"精确对应 |
