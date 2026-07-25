# REL-TIMEOUT-01-008

- 标题: job timeout 越界触发——361 分钟应在 360 分钟被强制终止
- 维度: 可靠性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

```
用例 ID:   REL-TIMEOUT-01-008
维度标签:   [reliability]
维度:      稳定性
优先级:    P1
溯源意图:  INTENT-REL-008
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      job timeout 越界触发——361 分钟应在 360 分钟被强制终止

前置条件:
  - 仓库具备 workflow 运行权限

操作步骤:
  1. 触发 timeout-minutes=360 的 workflow，job 执行 sleep 21660

预期结果:
  - job 在 360±2 分钟时被终止
  - 状态为 failure
  - 日志含超时信息

验证点:
  - [正向] job 状态=failure
  - [正向] 日志含 timeout 或 超时
  - [负向] 不应运行超过 365 分钟

清理:      无需特殊清理
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | long sleep step (test) | sleep 21660  | GENUINE |

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
| 日志含 timeout 或 超时 | 覆盖 | potential failure paths exist |
| 不应运行超过 365 分钟 | 未覆盖 | 缺少负向断言 |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | failure | CONSISTENT | potential failure paths exist |
| 2 | run_logs | positive | timeout | MISSING_SOURCE | no step produces 'timeout' |

### 问题

- 验证点 `不应运行超过 365 分钟` → 未覆盖: 缺少负向断言

- 断言 `[positive] run_logs` → MISSING_SOURCE: no step produces 'timeout'

---
