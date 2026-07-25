# COMPAT-SHELL-01-003

- 标题: Windows runner 默认 shell 差异
- 维度: 兼容性 | 优先级: P2
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: Windows runner 默认 shell 差异

- [正向] 默认 shell 正确执行 Windows 命令
- [正向] 若默认 shell 不是 powershell，系统应给出明确说明

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo OS | echo %OS% echo "done" | - |

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
| [正向] 默认 shell 正确执行 Windows 命令 | WEAK | assertions present but all steps trivial |
| [正向] 若默认 shell 不是 powershell，系统应给出明确说明 | WEAK | assertions present but all steps trivial |

### 问题

- [正向] 默认 shell 正确执行 Windows 命令: assertions present but all steps trivial
- [正向] 若默认 shell 不是 powershell，系统应给出明确说明: assertions present but all steps trivial

---
