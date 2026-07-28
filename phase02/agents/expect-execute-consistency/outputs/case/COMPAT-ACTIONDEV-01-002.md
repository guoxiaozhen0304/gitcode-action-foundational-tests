# COMPAT-ACTIONDEV-01-002

- **标题**: action 运行时 runs.using 类型覆盖（node16/composite/docker/node20）探测
- **维度**: 兼容性
- **评级**: 断言一致

---

## 想测什么
确定 GitCode 对 runs.using 各类型（node16/composite/docker/node20）的支持情况。

## 做了什么
依次引用四类本地 action（probe-node16/composite/docker/node20），最后 echo "USING_PROBE_DONE"。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | llm_assisted | LLM_DEPENDENT | 需人工判定各类型 action 执行结果 |
| 2 | run_logs | negative | llm_assisted | LLM_DEPENDENT | 需人工判定不出现运行期模糊失败 |
| 3 | run_logs | nonfunctional | llm_assisted | LLM_DEPENDENT | 需人工将支持清单写入差异文档 |
