# COMPAT-RUNNER-01-005

- 标题: 内网环境 Runner 不支持时的差异
- 维度: 兼容性 | 优先级: P2
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: 内网环境 Runner 不支持时的差异

- [正向] 系统对内网标签给出明确报错
- [负向] 不通过无限排队

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo hello | echo "hello" | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | error_message |  |
| negative | run_status |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 系统对内网标签给出明确报错 | WEAK | assertions present but all steps trivial |
| [负向] 不通过无限排队 | COVERED | negative assertion present |

### 问题

- [正向] 系统对内网标签给出明确报错: assertions present but all steps trivial

---
