# REL-FAULT-01-032
- **标题**: 故障注入——artifact 上传时网络分区 30 秒后应失败并报网络错误
- **维度**: reliability
- **评级**: 部分不符
## 想测什么
在 upload-artifact 期间注入网络分区 30s，验证 step=failure、日志含 network 错误、不应无限挂起 >120s。
## 做了什么
YAML 使用 dd 生成 10MB 文件 + upload-artifact action，fault_injection network_partition duration 30s at step 2。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | step_status | positive | equals failure | COVERED | YAML upload-artifact action + fault_injection，platform/action 日志确认失败 |
| 2 | run_logs | positive | contains network | COVERED | YAML assert 日志含 network 关键词，对应文本"日志含 network/connection/timeout" |
| 3 | no_indefinite_hang | negative | 不应无限挂起 120 秒 | MISSING | 文本有负向断言"不应无限挂起超过 120 秒"，YAML 无对应 timing assertion |
