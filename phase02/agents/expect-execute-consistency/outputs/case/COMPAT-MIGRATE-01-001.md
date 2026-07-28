# COMPAT-MIGRATE-01-001
- **标题**: GitHub 风格 permissions 块迁移报错应给出可操作指引
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试含 GitHub 风格 permissions 块（contents: read, pull-requests: write）的 workflow 被拒绝时，报错信息应包含可操作指引。

## 做了什么
在 job 级别添加 permissions 块（contents: read, pull-requests: write），包含 checkout + echo step。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | validation_error | negative | llm_assisted rubric | LLM_DEPENDENT | 需 LLM 判断报错信息质量 |
| 2 | error_message | positive | llm_assisted rubric | LLM_DEPENDENT | 需 LLM 判断是否包含 permissions 关键字及可操作建议 |
