# REL-SCHED-01-057

- 标题: 资源调度状态一致性——空闲 runner 存在时 job 不应死等
- 维度: 可靠性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

```
用例 ID:   REL-SCHED-01-057
维度标签:   [reliability]
维度:      稳定性
优先级:    P1
溯源意图:  INTENT-REL-057
参照来源:  inputs/gitcode-spec/runner-management/selecting-runner-labels.md; inputs/platform-config/instance-config.md
母意图:    —
标题:      资源调度状态一致性——空闲 runner 存在时 job 不应死等

前置条件:
  - runner 池存在空闲 runner

操作步骤:
  1. 连续触发 10 次单 job workflow，每次完成后等待 runner 空闲再触发下一次

预期结果:
  - 10 次全部 queued→running ≤60s
  - 平均≤30s

验证点:
  - [正向] 10 次全部≤60s
  - [非功能] 平均≤30s
  - [负向] 不应出现 runner 空闲但 job 死等>5min

清理:      无需特殊清理
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | sleep step (test) | sleep 30  | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 10 次全部≤60s | 未覆盖 | 缺少正向断言 |
| 平均≤30s | 覆盖 | 非功能断言存在(LLM评估) |
| 不应出现 runner 空闲但 job 死等>5min | 未覆盖 | 缺少负向断言 |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | max_queued_to_running_seconds | nonfunctional |  | LLM_DEPENDENT | LLM/nonfunctional assertion:  |
| 2 | avg_queued_to_running_seconds | nonfunctional |  | LLM_DEPENDENT | LLM/nonfunctional assertion:  |

### 问题

- 验证点 `10 次全部≤60s` → 未覆盖: 缺少正向断言

- 验证点 `不应出现 runner 空闲但 job 死等>5min` → 未覆盖: 缺少负向断言

---
