# COMPAT-CTX-01-005
- **标题**: atomgit 缺位字段（job/run_attempt/triggering_actor/ref_protected）求值行为探测   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
探测 atomgit.job / run_attempt / triggering_actor / ref_protected 四个字段的求值行为（有值/空/报错），与 env 侧对照。
## 做了什么
workflow_dispatch 触发，分三步 echo 各字段上下文值和 ENV_RUN_ATTEMPT 环境变量，最后 echo `PROBE_DONE`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_logs | positive | must_contain: PROBE_DONE | GENUINE→COVERED | 多步 `${{ }}` 引用使 echo 标记按 R6 GENUINE |
| 2 | run_logs | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；逐字段记录求值行为需 LLM 分析 |
