# REL-LOG-01-041
- **标题**: 单 job 日志大小上限探测——500MB 带序号日志的完整保留或明确截断标识
- **维度**: reliability
- **评级**: 断言一致
## 想测什么
输出约 500MB 带连续行号日志，验证日志可下载、尾部完整或带明确截断标识、不应无提示静默丢失、记录实测上限。
## 做了什么
YAML 使用 seq 命令生成 800 万行带序号日志（约 500MB），行号可校验连续性。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | log_downloadable | positive | equals true | COVERED | YAML seq 真实命令生成带序号大日志，harness 下载校验 |
| 2 | tail_integrity | positive | complete_or_explicitly_marked_truncated | COVERED | YAML assert 尾部完整或显式截断标记，对应文本"完整（行号连续到末行）或带明确截断标识" |
| 3 | silent_tail_loss_detected | negative | equals true | COVERED | YAML 负向检测静默截断，对应文本"不应无截断提示却缺尾部行" |
| 4 | measured_log_limit | nonfunctional | equals recorded | COVERED | YAML assert 记录实测上限，对应文本"实测日志上限值记录完整" |
