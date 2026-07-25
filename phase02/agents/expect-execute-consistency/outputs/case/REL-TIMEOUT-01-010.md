# REL-TIMEOUT-01-010

- 标题: 默认超时——未声明 timeout-minutes 运行 361 分钟应被强制终止
- 维度: 可靠性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

```
用例 ID:   REL-TIMEOUT-01-010
维度标签:   [reliability]
维度:      稳定性
优先级:    P1
溯源意图:  INTENT-REL-010
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    —
标题:      默认超时——未声明 timeout-minutes 运行 361 分钟应被强制终止

前置条件:
  - 仓库具备 workflow 运行权限

操作步骤:
  1. 触发未声明 timeout-minutes 的 workflow，job 执行 sleep 21660

预期结果:
  - job 在 360 分钟时被终止
  - 状态为 failure
  - 日志含超时信息

验证点:
  - [正向] job 状态=failure
  - [负向] 不应无限运行

清理:      无需特殊清理
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | sleep step (test) | sleep 21660  | GENUINE |

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
| 不应无限运行 | 未覆盖 | 缺少负向断言 |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | failure | CONSISTENT | potential failure paths exist |
| 2 | run_logs | positive | timeout | MISSING_SOURCE | no step produces 'timeout' |

### 问题

- 验证点 `不应无限运行` → 未覆盖: 缺少负向断言

- 断言 `[positive] run_logs` → MISSING_SOURCE: no step produces 'timeout'

---
