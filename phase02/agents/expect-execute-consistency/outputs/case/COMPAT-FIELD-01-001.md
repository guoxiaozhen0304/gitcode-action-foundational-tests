# COMPAT-FIELD-01-001
- **标题**: 含 run-name 字段的 workflow 应被报错或警告
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试平台对 workflow 根级别 run-name 字段的处理——应给出明确报错或警告，而非静默接受。

## 做了什么
在 workflow 中添加 `run-name: Test Run Name`，包含一个 echo "hello" step。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | error_message | nonfunctional | llm_assisted rubric | LLM_DEPENDENT | 需 LLM 判断报错信息是否明确指出 run-name 不支持 |
