# REL-TIMEOUT-01-009

- 标题: 自定义短超时——timeout-minutes=1 时 step 运行 2 分钟应被强制终止
- 维度: 可靠性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   REL-TIMEOUT-01-009
维度标签:   [reliability]
维度:      稳定性
优先级:    P1
溯源意图:  INTENT-REL-009
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    —
标题:      自定义短超时——timeout-minutes=1 时 step 运行 2 分钟应被强制终止

前置条件:
  - 仓库具备 workflow 运行权限

操作步骤:
  1. 触发 timeout-minutes=1 的 workflow，step 执行 sleep 120

预期结果:
  - job 在 60±10 秒时被终止
  - 状态为 failure
  - 日志含超时信息

验证点:
  - [正向] job 状态=failure
  - [正向] 实际运行时长 60±10 秒

清理:      无需特殊清理
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | long sleep step (test) | sleep 120  | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| job 状态=failure | 覆盖 | potential failure paths exist |
| 实际运行时长 60±10 秒 | 覆盖 | potential failure paths exist |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | failure | CONSISTENT | potential failure paths exist |
| 2 | job_duration_seconds | nonfunctional |  | LLM_DEPENDENT | LLM/nonfunctional assertion:  |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
