# COMPAT-CTX-01-005

- **标题**: atomgit 缺位字段（job/run_attempt/triggering_actor/ref_protected）求值行为探测
- **维度**: 兼容性
- **评级**: 断言一致

---

## 想测什么
逐一确定四个 atomgit 上下文缺位字段的求值行为。

## 做了什么
依次 echo atomgit.job、atomgit.run_attempt、atomgit.triggering_actor、atomgit.ref_protected，并对照 $ATOMGIT_RUN_ATTEMPT。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: PROBE_DONE | COVERED | run 步骤 echo "PROBE_DONE" |
| 2 | run_logs | positive | llm_assisted | LLM_DEPENDENT | 需人工逐字段记录求值行为 |
