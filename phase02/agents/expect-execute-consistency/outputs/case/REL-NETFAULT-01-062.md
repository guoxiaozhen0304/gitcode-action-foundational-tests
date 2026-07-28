# REL-NETFAULT-01-062
- **标题**: 网络依赖容错——workflow 中访问不可达地址的明确失败与有界超时
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
curl可达地址成功、不可达地址在≤60s失败、失败归因清晰。

## 做了什么
依次curl公网可达端点、RFC5737黑洞地址、不存在域名。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | reachable_status | positive | equals=success | COVERED | 文本"可达地址成功返回"精确对应 |
| 2 | unreachable_timeout_seconds | positive | le=60 | COVERED | 文本"不可达地址在≤60s内失败"精确对应 |
| 3 | failure_attribution | positive | equals=clear | COVERED | 文本"归因清晰"对应 |
