# SEC-NET-01-001
- **标题**: Runner 网络出站必须受控，防止 SSRF 与内网跳板
- **维度**: security
- **评级**: 断言一致

## 想测什么
Runner 不应能访问内网元数据端点，日志不出现 instance-id 等特征内容。

## 做了什么
workflow curl 访问 169.254.169.254 和 192.168.1.1；curl 失败时 echo "access denied or timeout"。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain "instance-id" | COVERED | 对应"日志中绝不应出现元数据服务响应特征内容"；real curl→GENUINE |
| 2 | run_logs | positive | contains "access denied or timeout" | COVERED | 对应"访问尝试返回超时或连接拒绝"；real curl→GENUINE |
