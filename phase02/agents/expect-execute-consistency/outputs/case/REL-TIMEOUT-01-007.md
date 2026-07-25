# REL-TIMEOUT-01-007

- 标题: job timeout 边界值——359 分钟运行应在 360 分钟边界前完成
- 维度: 可靠性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

```
用例 ID:   REL-TIMEOUT-01-007
维度标签:   [reliability]
维度:      稳定性
优先级:    P1
溯源意图:  INTENT-REL-007
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    —
标题:      job timeout 边界值——359 分钟运行应在 360 分钟边界前完成

前置条件:
  - 仓库具备 workflow 运行权限

操作步骤:
  1. 触发 timeout-minutes=360 的 workflow，job 执行 sleep 21540

预期结果:
  - job 在 359 分钟前成功完成
  - 状态为 success

验证点:
  - [正向] job 状态=success
  - [负向] 不应在 358 分钟前被强制终止

清理:      无需特殊清理
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | long sleep step (test) | sleep 21540  | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| job 状态=success | 覆盖 | workflow can potentially fail |
| 不应在 358 分钟前被强制终止 | 未覆盖 | 缺少负向断言 |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | success | CONSISTENT | workflow can potentially fail |
| 2 | job_duration_minutes | nonfunctional |  | LLM_DEPENDENT | LLM/nonfunctional assertion:  |

### 问题

- 验证点 `不应在 358 分钟前被强制终止` → 未覆盖: 缺少负向断言

---
