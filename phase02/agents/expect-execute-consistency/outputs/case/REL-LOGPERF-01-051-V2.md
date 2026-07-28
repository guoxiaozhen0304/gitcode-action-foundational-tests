# REL-LOGPERF-01-051-V2
- **标题**: 日志加载性能——200MB 日志下载与查看耗时
- **维度**: reliability
- **评级**: 断言一致
## 想测什么
生成 200MB 日志，测量下载耗时 ≤120s，验证大小/行数 100% 一致。
## 做了什么
YAML 使用 shell 循环 echo 生成 600 万行日志（约 200MB）。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | download_time_seconds | nonfunctional | le 120 | COVERED | YAML echo 真实命令输出 200MB 日志，harness 测量下载耗时 |
| 2 | log_integrity | positive | equals 100% | COVERED | YAML assert 日志完整度 100%，对应文本"大小/行数 100% 一致" |
