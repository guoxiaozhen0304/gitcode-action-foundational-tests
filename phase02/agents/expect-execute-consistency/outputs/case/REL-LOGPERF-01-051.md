# REL-LOGPERF-01-051
- **标题**: 日志加载性能——50MB 日志下载与查看耗时
- **维度**: reliability
- **评级**: 部分不符
## 想测什么
生成 50MB 日志，测量下载与查看耗时 ≤30s，验证内容完整且大小/行数 100% 一致，不应 UI 卡死。
## 做了什么
YAML 使用 shell 循环 echo 生成约 50MB 带序号日志。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | download_time_seconds | nonfunctional | le 30 | COVERED | YAML echo 真实命令输出 50MB 日志，harness 测量下载耗时 |
| 2 | log_integrity | positive | equals 100% | COVERED | YAML assert 日志完整度 100%，对应文本"内容完整、不乱序、不截断" |
| 3 | no_ui_freeze | negative | 不应 UI 卡死 | MISSING | 文本有负向断言"不应 UI 卡死"，YAML 无对应 assertion（UI 行为需前端观测） |
