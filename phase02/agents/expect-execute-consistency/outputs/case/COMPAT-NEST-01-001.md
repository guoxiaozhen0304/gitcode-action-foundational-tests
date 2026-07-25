# COMPAT-NEST-01-001

- 标题: workflow_call 嵌套层数 - 2 层正常执行
- 维度: 兼容性 | 优先级: P1
- 评级: 完全不符

---

## 1. 想测什么（规格）

标题: workflow_call 嵌套层数 - 2 层正常执行

- [正向] 2 层嵌套 workflow 能正常触发并执行
- [正向] 运行状态为成功

## 2. 实际做了什么（实现）

(无步骤)

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | run_status | success |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 2 层嵌套 workflow 能正常触发并执行 | NOT COVERED | no steps in workflow |
| [正向] 运行状态为成功 | NOT COVERED | no steps in workflow |

### 问题

- [正向] 2 层嵌套 workflow 能正常触发并执行: no steps in workflow
- [正向] 运行状态为成功: no steps in workflow

---
