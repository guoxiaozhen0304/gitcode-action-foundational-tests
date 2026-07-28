# COMPAT-PERM-01-006
- **标题**: job 级 permissions 字段的支持度与降级方式（权限不得宽于声明）
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试 job 级 permissions 字段——若不支持应明确报错，若支持则验证覆盖语义与 GitHub 一致（替换而非并集）。

## 做了什么
workflow 级声明 `contents: read`，job 级声明 `contents: write`，step 中 echo "JOB_LEVEL_PERM_JOB_RAN"。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | llm_assisted rubric | LLM_DEPENDENT | 需 LLM 判断是否被静默接受 |
| 2 | save_result | positive | llm_assisted rubric | LLM_DEPENDENT | 解析期报错质量需 LLM 辅助判断 |
| 3 | save_result | nonfunctional | llm_assisted rubric | LLM_DEPENDENT | 覆盖语义文档化需 LLM 辅助判断 |
