# REL-PRESSURE-01-055

- 标题: 并发压测——concurrency.max=5 时触发 20 个 workflow 的排队与完成率
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: 并发压测——concurrency.max=5 时触发 20 个 workflow 的排队与完成率

- [正向] completed=20
- [负向] running 峰值不应>5
- [负向] 不应出现运行静默消失

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | sleep step | sleep 30 | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | completed_count | 20 |
| nonfunctional | max_running_count |  |
| nonfunctional | total_duration_seconds |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] completed=20 | WEAK | assertions present but all steps trivial |
| [负向] running 峰值不应>5 | UNVERIFIABLE | single dispatch cannot prove negative |
| [负向] 不应出现运行静默消失 | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [正向] completed=20: assertions present but all steps trivial
- [负向] running 峰值不应>5: single dispatch cannot prove negative
- [负向] 不应出现运行静默消失: single dispatch cannot prove negative

---
