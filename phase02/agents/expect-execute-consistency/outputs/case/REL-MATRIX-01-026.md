# REL-MATRIX-01-026
- **标题**: matrix fail-fast=true——任意 job 实例失败应立即取消其余实例
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
3x3 matrix 中1个实例故意失败时，fail-fast=true 应取消其余8个实例，且不应继续执行已失败的其余实例。

## 做了什么
9个实例中 x=1,y=1 故意 exit 1，其余 sleep 30。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals=failure | COVERED | 文本"失败job状态=failure"，但YAML未区分哪个job失败，绑定到matrix整体 |
| 2 | cancelled_jobs_count | positive | equals=8 | TRIVIAL | 文本仅说"其余未完成jobs状态=cancelled"，YAML精确为8，实际执行结果可覆盖 |
| 3 | (文本负向) 不应继续执行 | negative | — | MISSING | 文本"不应继续执行已失败的matrix其余实例"在YAML中无独立negative断言 |
