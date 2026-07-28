# COMP-EXPR-01-059
- **标题**: 未文档化函数 default() 的存在性与求值记录
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
default() 函数在 if 中的存在性与返回语义逐字记录。

## 做了什么
1. gated job（if: ${{ default() }}）：`echo "DEFAULT_FN_JOB_RAN"`
2. witness job：`echo "WITNESS_RAN"`

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: WITNESS_RAN | COVERED | witness job 无条件执行（无 if），echo 固定输出 |
| 2 | default_fn_eval | nonfunctional | llm_assisted | LLM_DEPENDENT | eval=llm_assisted |
| 3 | run_logs | negative | llm_assisted | LLM_DEPENDENT | eval=llm_assisted |
