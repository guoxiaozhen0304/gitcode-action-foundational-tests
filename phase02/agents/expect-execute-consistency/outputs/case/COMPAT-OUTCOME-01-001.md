# COMPAT-OUTCOME-01-001

- 标题: continue-on-error false 时 outcome 与 conclusion 应均为 failure
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

标题: continue-on-error false 时 outcome 与 conclusion 应均为 failure

- [正向] 失败 step 的 outcome 为 failure
- [正向] 失败 step 的 conclusion 为 failure
- [正向] job 整体状态为 failure

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | checkout source | uses: checkout | Y |
| 2 | failing step | exit 1 | - |
| 3 | check status | echo "Check step outcome and conclusion" | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | step_status | failure |
| positive | step_conclusion | failure |
| positive | run_status | failure |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 失败 step 的 outcome 为 failure | COVERED | 2 real steps, assertions present |
| [正向] 失败 step 的 conclusion 为 failure | COVERED | 2 real steps, assertions present |
| [正向] job 整体状态为 failure | COVERED | 2 real steps, assertions present |

### 问题

无重大问题。

---
