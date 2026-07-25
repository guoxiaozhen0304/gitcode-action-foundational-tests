# REL-RACE-01-048

- 标题: 取消与 needs 条件竞态——job A 被取消时 job B(if: failure())应正确判定
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: 取消与 needs 条件竞态——job A 被取消时 job B(if: failure())应正确判定

- [正向] job A 状态=cancelled
- [正向] job B 状态=skipped
- [负向] job B 不应执行

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | sleep step | sleep 60 | - |
| 2 | should not run | echo this should not run | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | job_a_status | canceled |
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
| [正向] job A 状态=cancelled | WEAK | assertions present but all steps trivial |
| [正向] job B 状态=skipped | WEAK | assertions present but all steps trivial |
| [负向] job B 不应执行 | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [正向] job A 状态=cancelled: assertions present but all steps trivial
- [正向] job B 状态=skipped: assertions present but all steps trivial
- [负向] job B 不应执行: single dispatch cannot prove negative

---
