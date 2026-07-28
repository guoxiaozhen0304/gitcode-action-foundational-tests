# REL-CACHE-01-047
- **标题**: cache 容量上限探测——500MB/1GB/2GB 单 cache 的接受/拒绝语义
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
三档体积写 cache，接受则 MD5 一致，拒绝则含上限值；无静默损坏。

## 做了什么
save job matrix 三档生成数据+md5+写 cache；readback job 读回并 md5 -c 校验，输出 READBACK_MD5_OK/READBACK_MD5_BAD/CACHE_RESTORE_MISS 标记。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | write_outcome | positive | equals accepted_or_explicit_rejection_with_limit | COVERED | save+readback 组合可观测每个档位的接受/拒绝语义 |
| 2 | run_logs | negative | must_not_contain "READBACK_MD5_BAD_" | COVERED | 若出现 MD5 校验失败会 echo 该标记，真实可观测 |
| 3 | silent_corruption_detected | negative | equals "true" | COVERED | 通过 readback md5 校验与标记间接覆盖 |
| 4 | measured_cache_limit | nonfunctional | equals "recorded" | LLM_DEPENDENT | 实测记录型指标，依赖 harness 汇总 |
