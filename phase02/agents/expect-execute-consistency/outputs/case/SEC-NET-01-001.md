# SEC-NET-01-001
- **标题**: Runner 网络出站必须受控，防止 SSRF 与内网跳板   - **维度**: 安全性   - **评级**: 断言一致
## 想测什么
Runner不应能访问内网元数据端点或内部服务，访问尝试返回超时或连接拒绝。
## 做了什么
YAML workflow中两个step分别curl云元数据端点(169.254.169.254)和内网地址(192.168.1.1)，均绑定|| echo "access denied or timeout"失败回退。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | must_not_contain "instance-id" | COVERED | 元数据服务响应特征为可机器判定 |
| 2 | run_logs | positive | contains "access denied or timeout" | COVERED | 失败回退字符串到日志 |
