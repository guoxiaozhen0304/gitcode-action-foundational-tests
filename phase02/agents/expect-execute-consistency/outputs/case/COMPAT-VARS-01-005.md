# COMPAT-VARS-01-005
- **标题**: vars 在条件表达式 if 中的可用性差异
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证 `${{ vars.ENABLE_FEATURE == 'true' }}` 在if条件中正常求值，条件步骤应执行输出feature_enabled。

## 做了什么
setup配置 `variables: {ENABLE_FEATURE: "true"}`；step1无条件输出always；step2 if条件 `${{ vars.ENABLE_FEATURE == 'true' }}` 输出feature_enabled。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive llm | "若支持vars，条件步骤应执行并输出feature_enabled" | COVERED | if中有${{ vars.ENABLE_FEATURE }}为GENUINE(R1)；feature_enabled的出现证明if求值正确 |
| 2 | run_logs | negative llm | "vars不应被静默视为空字符串导致条件步骤跳过" | COVERED | 若feature_enabled不出现而always出现，证明vars在if中被视为空(R1推证) |
