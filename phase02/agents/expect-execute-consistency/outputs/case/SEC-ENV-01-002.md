# SEC-ENV-01-002
- **标题**: 环境级 secret 审批前 workflow 不可读取   - **维度**: 安全性   - **评级**: 断言一致
## 想测什么
审批前job无法读取环境secret值，job应处于挂起或失败状态。
## 做了什么
YAML workflow使用environment:production，step中检查$PROD_TOKEN是否为空：为空输出"secret not accessible"，不为空则exit 1。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | must_not_contain "secret accessible unexpectedly" | COVERED | 日志中不应出现意外访问成功标志 |
| 2 | run_status | positive | equals "pending_or_failed" | COVERED | 运行状态为平台可观测值 |
