# COMP-CTX-01-054
- **标题**: pull_request 触发下 inputs 上下文求值裁定
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
inputs.pr_id 在 pull_request 触发（非 dispatch）下的求值行为（报错/空字符串/默认值）确定。

## 做了什么
1. step `Echo inputs reference`：`echo "INPUT_PR_ID=${{ inputs.pr_id }}"`

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: INPUT_PR_ID= | COVERED | `${{ inputs.pr_id }}` 表达式在 pull_request 事件下求值并输出 |
| 2 | inputs_eval | nonfunctional | llm_assisted | LLM_DEPENDENT | eval=llm_assisted |
| 3 | inputs_determinism | negative | llm_assisted | LLM_DEPENDENT | eval=llm_assisted |
