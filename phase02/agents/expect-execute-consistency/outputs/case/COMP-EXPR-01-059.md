# COMP-EXPR-01-059

- **标题**: 未文档化函数 default() 的存在性与求值记录
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
探测 `default()` 函数是否存在及其求值行为（校验报错 / 执行 / 跳过）。

## 做了什么
gated job 在 `if: ${{ default() }}` 条件下执行并输出 `DEFAULT_FN_JOB_RAN`；witness job 无条件执行输出 `WITNESS_RAN`。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: WITNESS_RAN | COVERED | witness job 无条件执行，echo 输出 marker |
| 2 | default_fn_eval | nonfunctional | eval: llm_assisted | COVERED | LLM_DEPENDENT 断言 |
| 3 | run_logs | negative | eval: llm_assisted | COVERED | LLM_DEPENDENT 断言 |
