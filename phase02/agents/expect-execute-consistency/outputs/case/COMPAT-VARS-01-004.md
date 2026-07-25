# COMPAT-VARS-01-004

- 标题: vars 与 env 同名时的优先级差异
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

标题: vars 与 env 同名时的优先级差异

- [正向] 若支持 vars，env 优先级高于 vars
- [正向] shell 环境变量 $MY_VAR 返回 env_value

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo vars and env | echo "shell_var=$MY_VAR" echo "expr_var=${{ vars.MY_VAR }}" echo "done" | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | run_logs |  |
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
| [正向] 若支持 vars，env 优先级高于 vars | COVERED | 1 real steps, assertions present |
| [正向] shell 环境变量 $MY_VAR 返回 env_value | COVERED | 1 real steps, assertions present |

### 问题

无重大问题。

---
