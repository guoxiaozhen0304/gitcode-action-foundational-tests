# SEC-RUN-01-001
- **标题**: Job 结束后 workspace 与临时文件必须被彻底清理   - **维度**: 安全性   - **评级**: 断言一致
## 想测什么
job A写入的敏感临时文件不应被job B读取到，清理钩子应执行。
## 做了什么
YAML workflow含两个job：job-a写入/tmp/sensitive-temp.txt，job-b检查该文件是否存在。job-b中若存在输出"residual found"并exit 1，否则输出"cleaned as expected"。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | must_not_contain "residual found" | COVERED | 残留发现的标志字符串不应出现 |
| 2 | run_logs | positive | contains "cleaned as expected" | COVERED | 清理成功标志可观测 |
