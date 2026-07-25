# REL-NEEDS-01-025

- 标题: needs 失败传播——上游 job 失败时下游 job 应被 skip
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: needs 失败传播——上游 job 失败时下游 job 应被 skip

- [正向] job_a 状态=failure
- [正向] job_b 状态=skipped
- [负向] job_b 不应在 job_a 失败后仍执行

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | fail step | exit 1 | - |
| 2 | should be skipped | echo this should not run | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | job_a_status | failure |
| positive | job_b_status | skipped |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] job_a 状态=failure | WEAK | assertions present but all steps trivial |
| [正向] job_b 状态=skipped | WEAK | assertions present but all steps trivial |
| [负向] job_b 不应在 job_a 失败后仍执行 | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [正向] job_a 状态=failure: assertions present but all steps trivial
- [正向] job_b 状态=skipped: assertions present but all steps trivial
- [负向] job_b 不应在 job_a 失败后仍执行: single dispatch cannot prove negative

---
