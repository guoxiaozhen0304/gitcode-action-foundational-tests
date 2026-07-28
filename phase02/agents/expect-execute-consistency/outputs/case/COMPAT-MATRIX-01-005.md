# COMPAT-MATRIX-01-005
- **标题**: matrix exclude 全排除不被支持时的差异
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试 strategy.matrix.exclude 排除所有组合导致空矩阵时的行为——系统应报 matrix is empty 错误。

## 做了什么
配置单组合 matrix 并使用 exclude 排除该组合，step 中 echo matrix 值。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | validation_error | positive | llm_assisted rubric | LLM_DEPENDENT | 需 LLM 判断空矩阵报错是否存在 |
| 2 | run_status | negative | llm_assisted rubric | LLM_DEPENDENT | 静默忽略行为需 LLM 辅助判断 |
