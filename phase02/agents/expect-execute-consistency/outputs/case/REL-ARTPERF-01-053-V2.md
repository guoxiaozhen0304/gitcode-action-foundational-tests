# REL-ARTPERF-01-053-V2
- **标题**: 制品传输性能——1GB artifact 上传下载耗时
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
同 REL-ARTPERF-01-053：补真实 MD5 对账（md5.txt 随 artifact 上传，下载后比对），消除 hash_match MISSING_SOURCE。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | upload_time_seconds | nonfunctional | le 300 | ✅ COVERED | harness 计时测量 |
| 2 | download_time_seconds | nonfunctional | le 300 | ✅ COVERED | 同上 |
| 3 | run_logs | positive | must_contain HASH_MATCH_OK | ✅ GENUINE | md5sum 真实比对 |
| 4 | run_logs | negative | must_not_contain HASH_MISMATCH | ✅ GENUINE | 不一致时输出并 exit 1 |
