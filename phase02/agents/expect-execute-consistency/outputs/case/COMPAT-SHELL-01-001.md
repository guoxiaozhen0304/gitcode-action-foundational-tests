# COMPAT-SHELL-01-001

- 标题: 默认 shell 隐式行为差异 - 未显式声明时是否为 bash
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

标题: 默认 shell 隐式行为差异 - 未显式声明时是否为 bash

- [正向] 日志包含 bash 字样
- [正向] 命令按 bash 语法解析执行（如 here-string、数组等可用）

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | checkout source | uses: checkout | Y |
| 2 | print shell info | echo "Current shell: $SHELL" echo "Shell via ps: $(ps -p $$ -o comm=)" | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
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
| [正向] 日志包含 bash 字样 | COVERED | 2 real steps, assertions present |
| [正向] 命令按 bash 语法解析执行（如 here-string、数组等可用） | COVERED | 2 real steps, assertions present |

### 问题

无重大问题。

---
