# REL-NETFAULT-01-062
- **标题**: 网络依赖容错——workflow 中访问不可达地址的明确失败与有界超时   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证 job 内访问不可达地址时在 ≤60s 内明确失败、失败归因清晰，可达地址正常返回。
## 做了什么
job 内依次 curl 访问：公网可达端点（gitcode.com）、不可达域名、RFC5737 黑洞地址，均加 --connect-timeout 10。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | reachable_status | positive | equals "success" | COVERED | harness 检查可达地址 curl 的返回码 |
| 2 | unreachable_timeout_seconds | positive | le "60" | COVERED | harness 测量不可达地址的 step 耗时 |
| 3 | failure_attribution | positive | equals "clear" | COVERED | harness 解析 curl 的 verbose 输出确认失败归因清晰 |
