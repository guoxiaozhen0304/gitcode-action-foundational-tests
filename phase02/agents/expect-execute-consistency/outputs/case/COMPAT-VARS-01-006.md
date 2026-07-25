# COMPAT-VARS-01-006

- 标题: vars 在 Action 中的可用性差异
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

标题: vars 在 Action 中的可用性差异

- [正向] 若支持 vars，Action 的 with 参数正确接收值
- [负向] 不通过 vars 在 Action 中被静默视为空字符串

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Use vars in action | uses: checkout | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | run_status |  |
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
| [正向] 若支持 vars，Action 的 with 参数正确接收值 | COVERED | 1 real steps, assertions present |
| [负向] 不通过 vars 在 Action 中被静默视为空字符串 | COVERED | negative assertion present |

### 问题

无重大问题。

---
