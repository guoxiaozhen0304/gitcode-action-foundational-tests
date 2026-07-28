# REL-MATRIX-01-026
- **标题**: matrix fail-fast=true——任意 job 实例失败应立即取消其余实例
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
本次未改动（前一轮已修复）：当前 YAML 已为 3x3=9 实例 matrix + fail-fast=true，x=1,y=1 实例真实 exit 1 故意失败，其余 sleep 30；与文本规格完全一致，断言 cancelled_jobs_count=8 与组合数匹配。原分析的 IMPOSSIBLE（无失败路径、矩阵维度不符）已不存在。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals failure | ✅ GENUINE | x=1,y=1 实例真实 exit 1（故意失败合法） |
| 2 | cancelled_jobs_count | positive | equals 8 | ✅ GENUINE | 9 实例 - 1 失败 = 8 取消，fail-fast 真实触发 |
