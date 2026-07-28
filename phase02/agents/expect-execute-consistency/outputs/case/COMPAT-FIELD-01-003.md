# COMPAT-FIELD-01-003
- **标题**: 未知顶层字段不应被静默忽略而应给出警告
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试平台对未知顶层字段（如 custom_field）的处理——应给出警告或错误，而非静默忽略。

## 做了什么
在 workflow 根级别添加 `custom_field: value`，包含一个 echo "hello" step。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | llm_assisted rubric | LLM_DEPENDENT | 需 LLM 判断未知字段是否被静默忽略 |
| 2 | error_message | positive | llm_assisted rubric | LLM_DEPENDENT | 需 LLM 判断错误信息质量 |
