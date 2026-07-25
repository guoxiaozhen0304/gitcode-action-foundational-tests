# REL-LATENCY-01-050

- 标题: 调度延迟基准——queued→running P50/P95 等待时间
- 维度: 稳定性 | 优先级: P1
- 评级: 完全不符

---

## 1. 想测什么（规格）

标题: 调度延迟基准——queued→running P50/P95 等待时间

- [正向] P95≤60s
- [负向] 不应出现 runner 空闲但 job 死等>10min

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | sleep step | sleep 5 | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| nonfunctional | p95_latency_seconds |  |
| nonfunctional | p50_latency_seconds |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] P95≤60s | NOT COVERED | no real steps, no assertions |
| [负向] 不应出现 runner 空闲但 job 死等>10min | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [正向] P95≤60s: no real steps, no assertions
- [负向] 不应出现 runner 空闲但 job 死等>10min: single dispatch cannot prove negative

---
