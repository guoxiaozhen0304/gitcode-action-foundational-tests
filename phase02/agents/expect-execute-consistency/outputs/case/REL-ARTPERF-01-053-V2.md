# REL-ARTPERF-01-053-V2
- **标题**: 制品传输性能——1GB artifact 上传下载耗时
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
1GB artifact 上传≤300s、下载≤300s、hash 完整匹配。

## 做了什么
upload job 生成 1GB 文件+md5；download job 下载后 md5 校验，输出 HASH_MATCH_OK/HASH_MISMATCH。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | upload_time_seconds | nonfunctional | le 300 | LLM_DEPENDENT | 非功能性能指标，由 harness 从平台日志计时 |
| 2 | download_time_seconds | nonfunctional | le 300 | LLM_DEPENDENT | 非功能性能指标 |
| 3 | run_logs | positive | must_contain "HASH_MATCH_OK" | COVERED | verify step 在 md5 匹配时 echo，真实执行 |
| 4 | run_logs | negative | must_not_contain "HASH_MISMATCH" | COVERED | verify step 的失败路径输出，可观测 |
