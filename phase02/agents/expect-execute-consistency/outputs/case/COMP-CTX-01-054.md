# COMP-CTX-01-054

- **标题**: pull_request 触发下 inputs 上下文求值裁定
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
裁定 `inputs` 上下文在非 `workflow_dispatch`/`workflow_call` 触发（`pull_request`）下的求值行为（报错/空字符串/默认值）。

## 做了什么
PR 触发 workflow，step 中直接 echo `"INPUT_PR_ID=${{ inputs.pr_id }}"`（inputs.pr_id 未在 `on:` 中声明）。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: INPUT_PR_ID= | COVERED | `${{ inputs.pr_id }}` 在 PR 触发下的求值结果被 echo 输出，实际观察平台行为 |
| 2 | inputs_eval | nonfunctional | eval: llm_assisted | COVERED | LLM_DEPENDENT 断言 |
| 3 | inputs_determinism | negative | eval: llm_assisted | COVERED | LLM_DEPENDENT 断言 |
