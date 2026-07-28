# COMPAT-EXPR-01-008
- **标题**: toJson 表达式输出格式差异（pretty-print vs compact）
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试 toJson 表达式序列化对象/数组的输出格式（compact 单行 vs pretty-print 多行），验证与 GitHub 行为一致性。

## 做了什么
通过 `echo` 分别输出 `${{ toJson({'key1': 'value1', 'key2': 'value2'}) }}` 和 `${{ toJson(['a', 'b', 'c']) }}`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain "key1" | COVERED | `echo` 含 `${{ }}` 表达式输出，key1 必然出现在 JSON 输出日志中 |
| 2 | run_logs | nonfunctional | llm_assisted rubric | LLM_DEPENDENT | 输出格式（pretty-print vs compact）需 LLM 辅助判断与 GitHub 行为一致性 |
