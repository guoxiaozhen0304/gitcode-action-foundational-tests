# REL-NEST-01-024

- 标题: workflow_call 嵌套越界——3 层嵌套调用应被拒绝
- 维度: 稳定性 | 优先级: P1
- 评级: 完全不符

---

## 1. 想测什么（规格）

标题: workflow_call 嵌套越界——3 层嵌套调用应被拒绝

- [正向] 运行状态=failure
- [正向] 日志明确提示嵌套超限
- [负向] 不应死循环或挂起

## 2. 实际做了什么（实现）

(无步骤)

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | run_status | completed(failure) |
| positive | run_logs |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 运行状态=failure | NOT COVERED | no steps in workflow |
| [正向] 日志明确提示嵌套超限 | NOT COVERED | no steps in workflow |
| [负向] 不应死循环或挂起 | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [正向] 运行状态=failure: no steps in workflow
- [正向] 日志明确提示嵌套超限: no steps in workflow
- [负向] 不应死循环或挂起: single dispatch cannot prove negative

---
