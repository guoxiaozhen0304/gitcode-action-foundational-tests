# COMPAT-NEST-01-002

- 标题: workflow_call 嵌套层数 - 3 层越界应报错
- 维度: 兼容性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: workflow_call 嵌套层数 - 3 层越界应报错

- [负向] 3 层嵌套不应被静默接受
- [正向] 错误信息应明确指出嵌套层数限制

## 2. 实际做了什么（实现）

(无步骤)

| 断言类型 | 目标 | 值 |
|---------|------|----|
| negative | run_status | success |
| nonfunctional | error_message |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [负向] 3 层嵌套不应被静默接受 | COVERED | negative assertion present |
| [正向] 错误信息应明确指出嵌套层数限制 | NOT COVERED | no steps in workflow |

### 问题

- [正向] 错误信息应明确指出嵌套层数限制: no steps in workflow

---
