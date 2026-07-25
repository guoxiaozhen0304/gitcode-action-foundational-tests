# REL-IGNORE-01-004

- 标题: concurrency IGNORE 策略——超上限运行应直接执行
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: concurrency IGNORE 策略——超上限运行应直接执行

- [正向] 4 个运行全部 completed(success)
- [负向] 不应出现 queued 状态

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | sleep step | sleep 30 | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | run_status | completed(success) |
| negative | run_status | queued |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 4 个运行全部 completed(success) | WEAK | assertions present but all steps trivial |
| [负向] 不应出现 queued 状态 | COVERED | negative assertion present |

### 问题

- [正向] 4 个运行全部 completed(success): assertions present but all steps trivial

---
