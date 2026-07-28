# COMPAT-EXPR-01-013
- **标题**: success() 带括号与不带括号的兼容性差异
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试 `${{ success() }}` 和 `${{ success }}` 两种写法在 GitCode 平台上的兼容性差异。

## 做了什么
在 workflow 中两个 step 分别用 `if: ${{ success() }}` 和 `if: ${{ success }}` 条件判断，各自 echo 输出标记。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | llm_assisted rubric | LLM_DEPENDENT | 需 LLM 判断无括号形式是否被支持 |
| 2 | error_message | positive | llm_assisted rubric | LLM_DEPENDENT | 错误信息质量需 LLM 辅助判断 |
