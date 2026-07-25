# REL-QUEUE-01-003

- 标题: concurrency QUEUE 策略——超上限运行应排队等待
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: concurrency QUEUE 策略——超上限运行应排队等待

- [正向] 4 个运行最终全部 completed(success)
- [负向] 运行 3-4 不应被丢弃

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | sleep step | sleep 30 | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | run_status | completed(success) |
| nonfunctional | queued_count | 2 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 4 个运行最终全部 completed(success) | WEAK | assertions present but all steps trivial |
| [负向] 运行 3-4 不应被丢弃 | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [正向] 4 个运行最终全部 completed(success): assertions present but all steps trivial
- [负向] 运行 3-4 不应被丢弃: single dispatch cannot prove negative

---
