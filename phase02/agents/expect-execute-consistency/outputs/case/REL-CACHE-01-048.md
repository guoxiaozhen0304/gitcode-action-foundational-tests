# REL-CACHE-01-048
- **标题**: cache 同 key 并发写一致性——3 方并行写同一 key 不得产生混合/损坏内容
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
3 方并行写同名 cache key，读回应归属单方且完整，或明确冲突错误。

## 做了什么
3 个 writer job（matrix alpha/beta/gamma）并行写 marker 到共享 cache key；verify job 读回并校验归属（case 匹配单方标记或报 ATTRIBUTION_MIXED_BAD）。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | cache_content_attribution | positive | equals single_writer_complete_or_explicit_conflict_error | COVERED | verify job 的 case 匹配逻辑可判定归属 |
| 2 | run_logs | negative | must_not_contain "ATTRIBUTION_MIXED_BAD" | COVERED | 混合态时 verify job 会 echo 该标记并 exit 1，可观测 |
| 3 | mixed_or_truncated_content_detected | negative | equals "true" | COVERED | 通过 ATTRIBUTION_MIXED_BAD 间接覆盖 |
| 4 | concurrent_write_semantics | nonfunctional | equals "recorded" | LLM_DEPENDENT | 记录型指标 |
