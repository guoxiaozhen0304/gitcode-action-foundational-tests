# REL-STAGES-01-029
- **标题**: stages fail_fast 机制——阶段内任一 job 失败应立即终止同阶段其他 jobs
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
第一阶段3jobs并行(jobA故意失败)→同阶段其余cancelled/skipped、不应进入下一阶段。

## 做了什么
stages两阶段：test_stage(fail_fast=true)含3jobs(A失败,B,C sleep30)，next_stage含jobD。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals=failure | COVERED | 文本"失败job状态=failure"对应 |
| 2 | cancelled_jobs_count | positive | ge=2 | COVERED | 文本"同阶段其余jobs状态∈{cancelled,skipped}"对应(ge=2覆盖B和C) |
| 3 | next_stage_status | negative | equals=started | COVERED | 文本"不应进入下一阶段"精确对应(negative+equals=started) |
