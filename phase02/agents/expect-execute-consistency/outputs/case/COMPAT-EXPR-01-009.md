# COMPAT-EXPR-01-009
- **标题**: loose equality 跨类型强制求值差异
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**loose equality 跨类型强制求值差异**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-009
通过标准：
1. 跨类型比较行为应与 GitHub Actions 的 loose equality 语义一致
2. 表达式求值不报错
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Compare string one and number one | if `${{ '1' == 1 }}` echo true, else echo false | — | STRING_EQ_NUMBER=true/false |
| 2 | Compare string true and boolean true | if `${{ 'true' == true }}` echo true, else echo false | — | STRING_EQ_BOOL=true/false |
| 3 | Compare number zero and string zero | if `${{ 0 == '0' }}` echo true, else echo false | — | ZERO_EQ_ZERO=true/false |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs must_contain "STRING_EQ_NUMBER=" | positive | — | ✅ GENUINE | 步骤使用 ${{ '1' == 1 }} 真实表达式求值，输出依赖求值结果 |
| 2 | run_logs must_contain "STRING_EQ_BOOL=" | positive | — | ✅ GENUINE | 步骤使用 ${{ 'true' == true }} 真实表达式求值 |
| 3 | run_logs eval=llm_assisted | nonfunctional | — | 🔶 LLM_DEPENDENT | 跨类型比较结果的语义一致性由 LLM 判定 |
### 问题
- 断言3（LLM判定）被跳过
---
