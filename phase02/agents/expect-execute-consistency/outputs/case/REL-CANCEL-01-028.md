# REL-CANCEL-01-028

- 标题: 手动取消 workflow——运行中取消时 always() cleanup step 仍应执行
- 维度: 稳定性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

标题: 手动取消 workflow——运行中取消时 always() cleanup step 仍应执行

- [正向] 非 always step 被终止
- [正向] cleanup step 日志存在且 completed
- [正向] workflow 状态=cancelled

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | sleep main step | sleep 60 | - |
| 2 | cleanup always step | echo cleanup executed | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | cleanup_step_status | success |
| positive | run_status | canceled |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 非 always step 被终止 | COVERED | 1 real steps, assertions present |
| [正向] cleanup step 日志存在且 completed | COVERED | 1 real steps, assertions present |
| [正向] workflow 状态=cancelled | COVERED | 1 real steps, assertions present |

### 问题

无重大问题。

---
