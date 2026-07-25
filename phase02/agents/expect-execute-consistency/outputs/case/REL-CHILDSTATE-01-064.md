# REL-CHILDSTATE-01-064

- 标题: 子任务状态传播——workflow_call 失败时父 workflow 不应假阳性完成
- 维度: 稳定性 | 优先级: P0
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: 子任务状态传播——workflow_call 失败时父 workflow 不应假阳性完成

- [正向] 父 workflow 状态=failure
- [正向] 下游 job 被 skip
- [负向] 父 workflow 不应显示 success

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | should not run | echo downstream | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | parent_status | failure |
| positive | downstream_status | skipped |
| negative | parent_status | success |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 父 workflow 状态=failure | WEAK | assertions present but all steps trivial |
| [正向] 下游 job 被 skip | WEAK | assertions present but all steps trivial |
| [负向] 父 workflow 不应显示 success | COVERED | negative assertion present |

### 问题

- [正向] 父 workflow 状态=failure: assertions present but all steps trivial
- [正向] 下游 job 被 skip: assertions present but all steps trivial

---
