# SEC-RUN-01-001
- **标题**: Job 结束后 workspace 与临时文件必须被彻底清理
- **维度**: security
- **评级**: 断言一致

## 想测什么
job A 写入 /tmp/sensitive-temp.txt，job B 不应读取到残留文件。

## 做了什么
workflow 两个 job：job-a 写敏感临时文件，job-b 检查是否存在。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain "residual found" | COVERED | 对应"job B 绝不应能读取到 job A 残留的敏感文件"；script check→GENUINE |
| 2 | run_logs | positive | contains "cleaned as expected" | COVERED | 对应"job B 日志包含 cleaned as expected"；echo→GENUINE |
