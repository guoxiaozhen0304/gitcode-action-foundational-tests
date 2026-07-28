# COMPAT-MIGRATE-01-002
- **标题**: GitHub 风格 run-name 语法迁移报错应给出可操作指引
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试含 GitHub 风格 run-name（含 `${{ github.actor }}` 表达式）的 workflow 被拒绝时，报错信息应包含可操作指引。

## 做了什么
在 workflow 根级别添加 `run-name: "Build by ${{ github.actor }}"`，包含 checkout + echo step。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | validation_error | negative | llm_assisted rubric | LLM_DEPENDENT | 需 LLM 判断报错信息质量 |
| 2 | error_message | positive | llm_assisted rubric | LLM_DEPENDENT | 需 LLM 判断是否包含 run-name 不支持及替代方案提示 |
