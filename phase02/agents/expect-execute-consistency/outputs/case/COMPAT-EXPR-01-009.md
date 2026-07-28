# COMPAT-EXPR-01-009
- **标题**: loose equality 跨类型强制求值差异
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试 eq 表达式对不同原始类型（字符串与数字、布尔与字符串）的跨类型比较行为，验证与 GitHub Actions loose equality 语义一致性。

## 做了什么
在 run 块中使用 `if ${{ '1' == 1 }}` 等条件判断，echo 输出 STRING_EQ_NUMBER、STRING_EQ_BOOL、ZERO_EQ_ZERO 的结果。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain "STRING_EQ_NUMBER=" | COVERED | 含 `${{ }}` 条件判断的 echo 输出，可观测跨类型比较结果 |
| 2 | run_logs | positive | must_contain "STRING_EQ_BOOL=" | COVERED | 同上，echo 输出可验证布尔-字符串比较 |
| 3 | run_logs | nonfunctional | llm_assisted rubric | LLM_DEPENDENT | 跨类型比较语义是否正确需 LLM 辅助判断 |
