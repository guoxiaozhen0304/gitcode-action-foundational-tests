# COMPAT-OUTPUT-01-001
- **标题**: 跨 Job 引用未声明 output 时返回空值的差异
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**跨 Job 引用未声明 output 时返回空值的差异**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-NEW-006
通过标准：
1. 跨 Job 引用未声明 output 时不导致 workflow 崩溃
2. 返回值与 GitHub 行为一致（空字符串）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | job-a: Set output | `echo "declared_key=value_a" >> $ATOMGIT_OUTPUT` | — | declared_key=value_a |
| 2 | job-b: Echo outputs | echo declared/undeclared via needs 表达式 + "done" | — | declared=value_a, undeclared=<值> |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status equals success (eval=llm) | positive | llm_assisted | 🔶 LLM_DEPENDENT | 崩溃行为由 LLM 判定 |
| 2 | run_logs eval=llm_assisted | positive | — | 🔶 LLM_DEPENDENT | undeclared_key 空值由 LLM 判定 |
### 问题
全部断言均为 LLM_DEPENDENT
---
