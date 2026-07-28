# SEC-DEFPERM-01-002
- **标题**: job 级覆盖后权限正确收窄   - **维度**: 安全性   - **评级**: 断言一致
## 想测什么
顶层permissions:write被job级read覆盖后，job不应保留顶层更大权限，越权写被403拒绝。
## 做了什么
YAML workflow顶层声明repository:write，job级覆盖为repository:read，在job内执行curl写操作并输出WRITE_%{http_code}。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | must_not_contain "WRITE_201" | COVERED | curl输出HTTP状态码到日志 |
| 2 | run_logs | positive | contains "WRITE_403" | COVERED | 收窄后写操作预期403 |
