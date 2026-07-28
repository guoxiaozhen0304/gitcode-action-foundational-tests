# SEC-DEFPERM-01-001
- **标题**: ATOMGIT_TOKEN 默认权限范围与 job 级覆盖必须正确生效   - **维度**: 安全性   - **评级**: 断言一致
## 想测什么
顶层permissions声明被job继承，job级声明可覆盖顶层，越权写操作返回403。
## 做了什么
YAML workflow含两个job：inherit-test(顶层read，尝试write回传WRITE_%{http_code})和override-write(job级write覆盖，尝试read回传READ_%{http_code})。使用真实curl命令和${{}}表达式。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | must_not_contain "WRITE_201" | COVERED | curl输出HTTP状态码到日志，可观测 |
| 2 | run_logs | positive | contains "WRITE_403" | COVERED | 同上，HTTP 403为预期拒绝响应 |
| 3 | run_logs | positive | contains "READ_200" | COVERED | override后读操作预期200成功 |
