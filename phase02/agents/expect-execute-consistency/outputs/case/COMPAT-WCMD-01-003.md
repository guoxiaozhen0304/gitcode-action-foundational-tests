# COMPAT-WCMD-01-003

- 标题: ::stop-commands:: 不被支持时应静默降级而非报错
- 维度: 兼容性 | 优先级: P2
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: ::stop-commands:: 不被支持时应静默降级而非报错

- [正向] workflow 不因 stop-commands 而失败
- [负向] 不通过 stop-commands 导致 workflow 报错中断

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Use stop-commands | echo "::stop-commands::pause" echo "::set-output name=K::V" echo "::pause::" echo "done" | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | run_status | success |
| negative | run_logs |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] workflow 不因 stop-commands 而失败 | WEAK | assertions present but all steps trivial |
| [负向] 不通过 stop-commands 导致 workflow 报错中断 | COVERED | negative assertion present |

### 问题

- [正向] workflow 不因 stop-commands 而失败: assertions present but all steps trivial

---
