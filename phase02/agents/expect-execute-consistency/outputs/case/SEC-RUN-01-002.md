# SEC-RUN-01-002
- **标题**: Runner 环境变量与共享目录必须跨 job 隔离   - **维度**: 安全性   - **评级**: 断言一致
## 想测什么
job B不应继承job A设置的环境变量或/tmp残留文件。
## 做了什么
YAML workflow含两个job：job-a-env设置MY_SECRET_ENV和写入/tmp/env-test.txt，job-b-env检查是否残留。job-b中若存在则输出"isolation broken"并exit 1，否则输出"isolated as expected"。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | must_not_contain "isolation broken" | COVERED | 隔离破坏标志字符串不应出现 |
| 2 | run_logs | positive | contains "isolated as expected" | COVERED | 隔离成功标志可观测 |
