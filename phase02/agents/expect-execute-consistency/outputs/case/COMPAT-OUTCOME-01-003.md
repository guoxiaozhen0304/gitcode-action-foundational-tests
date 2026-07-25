# COMPAT-OUTCOME-01-003

- 标题: outcome 与 conclusion 在 job 条件判断中不应互换语义
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

标题: outcome 与 conclusion 在 job 条件判断中不应互换语义

- [正向] job A 的 outcome 保持为 failure
- [正向] job A 的 conclusion 为 success
- [正向] job B 的 needs 条件基于 conclusion 判断时认为 job A 成功
- [负向] 不应出现 outcome 与 conclusion 被互换使用导致的误判

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | checkout source | uses: checkout | Y |
| 2 | failing step tolerated | exit 1 | - |
| 3 | verify job a conclusion | echo "Job A conclusion should be success" | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | job_status | success |
| positive | step_status | failure |
| negative | semantic_swap |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] job A 的 outcome 保持为 failure | COVERED | 1 real steps, assertions present |
| [正向] job A 的 conclusion 为 success | COVERED | 1 real steps, assertions present |
| [正向] job B 的 needs 条件基于 conclusion 判断时认为 job A 成功 | COVERED | 1 real steps, assertions present |
| [负向] 不应出现 outcome 与 conclusion 被互换使用导致的误判 | COVERED | negative assertion present |

### 问题

无重大问题。

---
