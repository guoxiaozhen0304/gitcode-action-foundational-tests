# REL-CONC-01-001

- 标题: concurrency.max=5 时同时触发 5 个运行应全部进入执行态
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: concurrency.max=5 时同时触发 5 个运行应全部进入执行态

- [正向] 5 个运行状态均为 completed(success)
- [非功能] queued→in_progress 调度时延 ≤60 秒

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | sleep step | sleep 10 | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | run_status | completed(success) |
| nonfunctional | queued_to_running_latency |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 5 个运行状态均为 completed(success) | WEAK | assertions present but all steps trivial |
| [非功能] queued→in_progress 调度时延 ≤60 秒 | WEAK | assertions present but all steps trivial |

### 问题

- [正向] 5 个运行状态均为 completed(success): assertions present but all steps trivial
- [非功能] queued→in_progress 调度时延 ≤60 秒: assertions present but all steps trivial

---
