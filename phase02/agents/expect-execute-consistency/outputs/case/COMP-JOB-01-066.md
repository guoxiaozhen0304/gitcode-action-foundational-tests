# COMP-JOB-01-066

- **标题**: job 必填字段 name runs-on steps 验证
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 job 必须包含 `name`、`runs-on`、`steps` 字段；完整定义通过校验并执行。

## 做了什么
当前 YAML 为正向用例：定义含 name/runs-on/steps 的完整 job，echo `job_fields_ok`。变体 V1（缺 name）和 V2（缺 steps）通过独立的 workflow 提交由 harness 验证平台拒绝行为。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | COVERED | 完整 job 定义通过校验并执行 |
| 2 | run_logs | positive | must_contain: job_fields_ok | COVERED | echo 直接产生 marker |
| 3 | workflow_parse | negative | eval: llm_assisted | COVERED | LLM_DEPENDENT — 变体 V1（缺 name）由外部 harness 独立验证 |
| 4 | workflow_parse | negative | eval: llm_assisted | COVERED | LLM_DEPENDENT — 变体 V2（缺 steps）由外部 harness 独立验证 |
