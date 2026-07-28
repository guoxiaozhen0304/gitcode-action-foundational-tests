# REL-ARTPERF-01-053
- **标题**: 制品传输性能——100MB artifact 上传下载耗时
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
hash_match 原为 MISSING_SOURCE（仅 ls -la）。改为真实 MD5 对账：upload job 生成文件时记录 md5.txt 并随 artifact 上传；download job 下载后 md5sum 比对，一致输出 HASH_MATCH_OK，不一致 exit 1。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | upload_time_seconds | nonfunctional | le 30 | ✅ COVERED | harness 计时测量，数值阈值可机器判定 |
| 2 | download_time_seconds | nonfunctional | le 30 | ✅ COVERED | 同上 |
| 3 | run_logs | positive | must_contain HASH_MATCH_OK | ✅ GENUINE | md5sum 真实比对通过后输出 |
| 4 | run_logs | negative | must_not_contain HASH_MISMATCH | ✅ GENUINE | 不一致时输出并 exit 1 |
