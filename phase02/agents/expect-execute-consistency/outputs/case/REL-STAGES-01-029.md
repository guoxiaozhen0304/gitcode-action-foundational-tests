# REL-STAGES-01-029

- 标题: stages fail_fast 机制——阶段内任一 job 失败应立即终止同阶段其他 jobs
- 维度: 可靠性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

```
用例 ID:   REL-STAGES-01-029
维度标签:   [reliability]
维度:      稳定性
优先级:    P1
溯源意图:  INTENT-REL-029
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      stages fail_fast 机制——阶段内任一 job 失败应立即终止同阶段其他 jobs

前置条件:
  - 仓库具备 stages 使用权限

操作步骤:
  1. 触发含 stage 且 3 个 jobs 并行执行的 workflow，1 个 job 故意失败

预期结果:
  - 失败 job 状态=failure
  - 同阶段其余 jobs 状态=cancelled 或 skipped
  - 不应进入下一阶段

验证点:
  - [正向] 失败 job 状态=failure
  - [正向] 同阶段其余 jobs 状态∈{cancelled, skipped}
  - [负向] 不应进入下一阶段

清理:      无需特殊清理
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | fail step (job_a) | exit 1  | GENUINE |
| 2 | sleep step (job_b) | sleep 30  | GENUINE |
| 3 | sleep step (job_c) | sleep 30  | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 失败 job 状态=failure | 覆盖 | deliberate failure step exists |
| 同阶段其余 jobs 状态∈{cancelled, skipped} | 覆盖 | deliberate failure step exists |
| 不应进入下一阶段 | 未覆盖 | 缺少负向断言 |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | failure | CONSISTENT | deliberate failure step exists |
| 2 | cancelled_jobs_count | positive |  | CONSISTENT | real step logic exists |

### 问题

- 验证点 `不应进入下一阶段` → 未覆盖: 缺少负向断言

---
