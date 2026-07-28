# COMPAT-OUTPUT-01-001
- **标题**: 跨 Job 引用未声明 output 时返回空值的差异
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试通过 needs 引用上游 job 未声明的 output 键时，返回值应与 GitHub 行为一致（空字符串）。

## 做了什么
job A 声明 outputs.declared_key；job B 通过 needs 引用 declared_key 和未声明的 undeclared_key。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | llm_assisted rubric "equals success" | LLM_DEPENDENT | 需 LLM 判断未声明 output 引用是否导致崩溃 |
| 2 | run_logs | positive | llm_assisted rubric | LLM_DEPENDENT | undeclared_key 返回值需 LLM 辅助判断 |
