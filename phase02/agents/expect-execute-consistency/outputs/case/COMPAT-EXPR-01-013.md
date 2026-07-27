# COMPAT-EXPR-01-013
- **标题**: success() 带括号与不带括号的兼容性差异
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**success() 带括号与不带括号的兼容性差异**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-004
通过标准：
1. 若支持无括号形式，应正常求值
2. 若不支持，应给出明确的语法错误提示
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Step with parens | echo "with_parens" | `${{ success() }}` | "with_parens" |
| 2 | Step without parens | echo "without_parens" | `${{ success }}` | "without_parens" |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs eval=llm_assisted | positive | — | 🔶 LLM_DEPENDENT | 由 LLM 判定无括号形式是否支持 |
| 2 | error_message eval=llm_assisted | positive | — | 🔶 LLM_DEPENDENT | 由 LLM 判定是否给出语法错误提示 |
### 问题
全部断言均为 LLM_DEPENDENT，无确定性断言可验证 workflow 步骤是否真正产生预期行为
---
