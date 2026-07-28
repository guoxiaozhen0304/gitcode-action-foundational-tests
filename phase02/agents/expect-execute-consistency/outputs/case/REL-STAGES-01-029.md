# REL-STAGES-01-029
- **标题**: stages fail_fast 机制——阶段内任一 job 失败应立即终止同阶段其他 jobs   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证 stages 的 fail_fast 机制：第一阶段内 job_a 失败时，同阶段其余 2 个 jobs（job_b, job_c）应被 cancelled/skipped，且不应进入下一阶段。
## 做了什么
触发含两个 stage 的 workflow：第一阶段 3 个并行 jobs（job_a exit 1，job_b/job_c sleep 30），fail_fast=true；第二阶段 1 个 job 验证不进入。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals "failure" | COVERED | 平台 API 查询失败 job 状态 |
| 2 | cancelled_jobs_count | positive | ge "2" | COVERED | harness 统计同阶段被取消的 job 数 |
| 3 | next_stage_status | negative | equals "started" | COVERED | harness 验证下一阶段 job 不应启动 |
