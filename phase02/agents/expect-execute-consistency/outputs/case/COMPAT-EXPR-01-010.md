# COMPAT-EXPR-01-010
- **标题**: loose equality null 与空字符串及零的等价性差异
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试 eq 表达式比较 null 与空字符串、null 与 0、null 与 false 的行为，验证 null 强制转换规则一致性。

## 做了什么
在 run 块中使用 `if ${{ null == '' }}` 等条件判断，echo 输出 NULL_EQ_EMPTY、NULL_EQ_ZERO、NULL_EQ_FALSE 的结果。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain "NULL_EQ_EMPTY=" | COVERED | 含 `${{ }}` 条件判断的 echo 输出，可观测比较结果 |
| 2 | run_logs | positive | must_contain "NULL_EQ_ZERO=" | COVERED | 同上 |
| 3 | run_logs | nonfunctional | llm_assisted rubric | LLM_DEPENDENT | null 比较语义是否正确需 LLM 辅助判断 |
