# COMP-UNKNOWN-01-004

- **标题**: select 与 selected_by_default 声明时的实际行为记录
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
记录 select: selected_by_default 在 stage 和 job 两级声明的实际行为，与 COMP-UNKNOWN-01-003 对比。

## 做了什么
单 job beta，select: selected_by_default 声明在 stage 和 job 两级，run 步骤 echo "SELECT_JOB_RAN"。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | select_handling | nonfunctional | llm_assisted | LLM_DEPENDENT | 需人工判定 select 字段实际处理行为 |
| 2 | run_logs | negative | llm_assisted | LLM_DEPENDENT | 需人工判定 select 是否被静默忽略 |
