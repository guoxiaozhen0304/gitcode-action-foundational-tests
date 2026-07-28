# COMPAT-PERM-01-003
- **标题**: permissions 命名差异——GitHub contents 权限项应报错
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试使用 GitHub 风格 `contents: read` 权限项时，平台解析应报错拒绝。

## 做了什么
声明 `permissions: { contents: read }`，包含 checkout + echo "CONTENTS_PERM_ACCEPTED" step。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | workflow_parse | negative | llm_assisted rubric | LLM_DEPENDENT | 需 LLM 判断解析阶段是否报错 |
| 2 | run_logs | positive | llm_assisted rubric | LLM_DEPENDENT | 错误信息质量需 LLM 辅助判断 |
| 3 | run_logs | negative | llm_assisted rubric | LLM_DEPENDENT | CONTENTS_PERM_ACCEPTED 不应出现 |
