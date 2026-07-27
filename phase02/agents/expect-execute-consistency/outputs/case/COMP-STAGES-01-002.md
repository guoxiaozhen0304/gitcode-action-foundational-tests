# COMP-STAGES-01-002
- **标题**: fail_fast true 时 stage 内任一 job 失败终止同阶段其余 job
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**fail_fast true 时 stage 内任一 job 失败终止同阶段其余 job**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-007
通过标准：
1. 同 stage 其余 job 被终止（正向）
2. 后续 stage 不应执行（负向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Force failure | `exit 1` | - | (job 失败) |
| 2 | Should be skipped | `echo "should not execute"` | - | should not execute |
| 3 | Deploy | `echo "should not execute"` | - | should not execute |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals: skipped_for_should_skip | ✅ GENUINE | exit 1 故意失败触发 fail_fast 机制，harness 验证同 stage 内其余 job 被 skipped |
| 2 | stage_execution | negative | equals: deploy_stage_executed | ✅ GENUINE | exit 1 导致 stage 失败，harness 验证后续 deploy stage 不应执行 |
---
