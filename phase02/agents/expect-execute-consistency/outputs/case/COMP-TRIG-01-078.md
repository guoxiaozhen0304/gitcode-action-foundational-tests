# COMP-TRIG-01-078

- **标题**: 多事件组合与分支路径过滤验证
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证多事件（push + workflow_dispatch）组合及 branches + paths 过滤。

## 做了什么
Steps: `echo "TRIGGER_EVENT=${{ atomgit.event_name }}"`、`echo "TRIGGER_REF=${{ atomgit.ref }}"`——`${{ }}` 表达式。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals success | COVERED | step 含 `${{ }}`，非必然 success |
| 2 | run_logs | positive | must_contain TRIGGER_EVENT=push | COVERED | `${{ atomgit.event_name }}` 上下文表达式（Rule 6） |
| 3 | run_logs | positive | must_contain multi_event_ok | COVERED | marker signal |
| 4 | workflow_parse | negative | eval=llm_assisted | LLM_DEPENDENT | paths 与 paths-ignore 互斥变体需人工验证 |
