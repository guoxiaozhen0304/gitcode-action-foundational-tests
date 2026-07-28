# SEC-RUN-01-003
- **标题**: 自托管 Runner 跨项目残留必须被隔离   - **维度**: 安全性   - **评级**: 断言一致
## 想测什么
自托管runner上项目B不应读取到项目A残留的敏感文件或环境变量。
## 做了什么
YAML workflow含两个job使用self-hosted runner标签：project-a写入/tmp/project-a-temp.txt，project-b检查该文件是否存在。project-b中若存在输出"cross project leak"并exit 1，否则输出"isolated as expected"。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | must_not_contain "cross project leak" | COVERED | 跨项目泄漏标志字符串不应出现 |
| 2 | run_logs | positive | contains "isolated as expected" | COVERED | 隔离成功标志可观测 |
