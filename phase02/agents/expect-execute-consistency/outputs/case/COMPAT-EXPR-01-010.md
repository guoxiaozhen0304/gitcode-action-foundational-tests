# COMPAT-EXPR-01-010
- **标题**: loose equality null 与空字符串及零的等价性差异
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**loose equality null 与空字符串及零的等价性差异**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-009
通过标准：
1. null 与空字符串、null 与 0 的比较行为应与 GitHub Actions 一致
2. 表达式求值不报错
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Compare null and empty string | if `${{ null == '' }}` echo true, else echo false | — | NULL_EQ_EMPTY=true/false |
| 2 | Compare null and number zero | if `${{ null == 0 }}` echo true, else echo false | — | NULL_EQ_ZERO=true/false |
| 3 | Compare null and false | if `${{ null == false }}` echo true, else echo false | — | NULL_EQ_FALSE=true/false |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs must_contain "NULL_EQ_EMPTY=" | positive | — | ✅ GENUINE | 步骤使用 ${{ null == '' }} 真实表达式求值，输出依赖运行时求值 |
| 2 | run_logs must_contain "NULL_EQ_ZERO=" | positive | — | ✅ GENUINE | 步骤使用 ${{ null == 0 }} 真实表达式求值 |
| 3 | run_logs eval=llm_assisted | nonfunctional | — | 🔶 LLM_DEPENDENT | null 比较语义一致性由 LLM 判定 |
### 问题
- 断言3（LLM判定）被跳过
---
