# COMP-STAGES-01-001
- **标题**: stages 阶段间串行、阶段内 job 并行执行
- **维度**: 完备性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**stages 阶段间串行、阶段内 job 并行执行**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-007
通过标准：
1. stage 2 的 job 开始时间晚于 stage 1 所有 job 的结束时间（正向）
2. 同 stage 内 job 的开始时间相近，并行执行（正向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Build A step | `echo "build-a"` | - | build-a |
| 2 | Build B step | `echo "build-b"` | - | build-b |
| 3 | Test step | `echo "test"` | - | test |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | ⚠️ STATUS_GUARANTEED | 所有步骤均为 echo 字面量，无条件失败路径 |
| 2 | stage_order | positive | equals: serial_across_stages | ✅ GENUINE | harness 通过 job 开始/结束时间戳验证 stages 串行语义 |
| 3 | job_parallelism | positive | equals: parallel_within_stage | ✅ GENUINE | harness 通过同 stage 内 job 的开始时间验证并行语义 |
### 问题
**断言 1 — STATUS_GUARANTEED**: 步骤仅 echo 字面量，无条件失败路径，运行永远成功。
---
