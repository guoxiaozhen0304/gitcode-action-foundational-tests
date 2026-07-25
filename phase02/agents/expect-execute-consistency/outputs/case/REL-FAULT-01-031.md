# REL-FAULT-01-031

- 标题: 故障注入——job 执行中 runner 进程被 SIGKILL 后应记录失败并保留已执行日志
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: 故障注入——job 执行中 runner 进程被 SIGKILL 后应记录失败并保留已执行日志

- [正向] job 状态=failure
- [正向] step 1-2 日志完整
- [负向] 不应状态=in_progress 挂起超过 5 分钟

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | step one | echo step_one_marker | - |
| 2 | step two | echo step_two_marker | - |
| 3 | step three | sleep 30 | - |
| 4 | step four | echo step_four_marker | - |
| 5 | step five | echo step_five_marker | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | job_status | failure |
| positive | run_logs |  |
| negative | run_logs |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] job 状态=failure | WEAK | assertions present but all steps trivial |
| [正向] step 1-2 日志完整 | WEAK | assertions present but all steps trivial |
| [负向] 不应状态=in_progress 挂起超过 5 分钟 | COVERED | negative assertion present |

### 问题

- [正向] job 状态=failure: assertions present but all steps trivial
- [正向] step 1-2 日志完整: assertions present but all steps trivial

---
