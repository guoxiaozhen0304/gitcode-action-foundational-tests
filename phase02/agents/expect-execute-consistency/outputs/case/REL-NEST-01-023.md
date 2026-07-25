# REL-NEST-01-023

- 标题: workflow_call 嵌套边界——2 层嵌套调用应成功执行
- 维度: 稳定性 | 优先级: P1
- 评级: 完全不符

---

## 1. 想测什么（规格）

标题: workflow_call 嵌套边界——2 层嵌套调用应成功执行

- [正向] 最外层运行状态=success
- [正向] 所有子运行均 success

## 2. 实际做了什么（实现）

(无步骤)

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | run_status | completed(success) |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 最外层运行状态=success | NOT COVERED | no steps in workflow |
| [正向] 所有子运行均 success | NOT COVERED | no steps in workflow |

### 问题

- [正向] 最外层运行状态=success: no steps in workflow
- [正向] 所有子运行均 success: no steps in workflow

---
