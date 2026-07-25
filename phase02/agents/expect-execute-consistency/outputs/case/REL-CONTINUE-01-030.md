# REL-CONTINUE-01-030

- 标题: continue-on-error=true——job 失败后 workflow 不应终止
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: continue-on-error=true——job 失败后 workflow 不应终止

- [正向] job_a 状态=failure
- [正向] job_b 状态=success
- [负向] workflow 不应因 job_a 失败而整体 failure

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | fail step | exit 1 | - |
| 2 | success step | echo job_b executed | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | job_a_status | failure |
| positive | job_b_status | success |
| positive | workflow_status | success |

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
| [正向] job_b 状态=success | WEAK | assertions present but all steps trivial |
| [负向] workflow 不应因 job_a 失败而整体 failure | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [正向] job_a 状态=failure: assertions present but all steps trivial
- [正向] job_b 状态=success: assertions present but all steps trivial
- [负向] workflow 不应因 job_a 失败而整体 failure: single dispatch cannot prove negative

---
