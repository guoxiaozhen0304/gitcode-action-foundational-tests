# COMPAT-VARS-01-002

- 标题: vars 上下文若不支持应报错而非静默为空
- 维度: 兼容性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: vars 上下文若不支持应报错而非静默为空

- [负向] 不应静默求值为空
- [非功能] 报错信息应说明 vars 上下文不支持

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo vars unknown | echo "unknown_var=${{ vars.UNKNOWN_VAR }}" echo "done" | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| negative | run_logs |  |
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
| [负向] 不应静默求值为空 | COVERED | negative assertion present |
| [非功能] 报错信息应说明 vars 上下文不支持 | WEAK | 1 real steps but no assertions |

### 问题

- [非功能] 报错信息应说明 vars 上下文不支持: 1 real steps but no assertions

---
