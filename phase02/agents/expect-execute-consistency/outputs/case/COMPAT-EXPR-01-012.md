# COMPAT-EXPR-01-012
- **标题**: fromJSON() 函数缺失时的降级行为
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试平台对不支持的 fromJSON() 表达式函数的处理行为——应给出明确校验错误而非静默求值。

## 做了什么
在 run 块中调用 `${{ fromJSON('{"a": 1}').a }}`，echo 输出结果。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain "fromjson-result=1" | COVERED | 若 fromJSON() 不支持，日志中不应出现预期结果；步骤输出可验证 |
| 2 | error_message | nonfunctional | llm_assisted rubric | LLM_DEPENDENT | 错误信息质量需 LLM 辅助判断 |
