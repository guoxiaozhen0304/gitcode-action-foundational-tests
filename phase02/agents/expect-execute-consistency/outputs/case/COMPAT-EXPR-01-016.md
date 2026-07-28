# COMPAT-EXPR-01-016
- **标题**: format() 花括号转义与字符串字面量引号规则边界
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试 format 表达式的双花括号转义语义和单引号转义规则，验证与 GitHub 行为的一致性。

## 做了什么
echo 输出 `${{ format('{{{0}}}', 'x') }}` 和 `${{ format('it''s {0}', 'ok') }}` 的求值结果。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain "PROBE_DONE" | COVERED | echo 输出可验证步骤完成 |
| 2 | run_logs | positive | llm_assisted rubric | LLM_DEPENDENT | format 转义求值结果需 LLM 辅助判断 |
| 3 | run_logs | negative | llm_assisted rubric | LLM_DEPENDENT | 双引号字符串行为需 LLM 辅助判断 |
