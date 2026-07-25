# REL-LATENCY-01-050-V2

- 标题: 调度延迟压力——并发 20 个 job 的排队延迟与完成率
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: 调度延迟压力——并发 20 个 job 的排队延迟与完成率

- [正向] 20 个 job 全部完成
- [负向] 无 job 被无限饿死

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | sleep 60s | sleep 60 | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | completed_jobs_count | 20 |
| nonfunctional | max_queued_time_seconds |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 20 个 job 全部完成 | WEAK | assertions present but all steps trivial |
| [负向] 无 job 被无限饿死 | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [正向] 20 个 job 全部完成: assertions present but all steps trivial
- [负向] 无 job 被无限饿死: single dispatch cannot prove negative

---
