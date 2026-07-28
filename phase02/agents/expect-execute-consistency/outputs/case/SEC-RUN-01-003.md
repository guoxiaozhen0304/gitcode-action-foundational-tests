# SEC-RUN-01-003
- **标题**: 自托管 Runner 跨项目残留必须被隔离
- **维度**: security
- **评级**: 断言一致

## 想测什么
项目 A 写 /tmp 文件，项目 B 在同 runner 不应读到跨项目残留。

## 做了什么
workflow 两个 job 均 runs-on: self-hosted；project-a 写 /tmp 文件，project-b 检查残留。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain "cross project leak" | COVERED | 对应"项目 B 绝不应读取到项目 A 残留的敏感文件"；script check→GENUINE |
| 2 | run_logs | positive | contains "isolated as expected" | COVERED | 对应"项目 B 日志包含 isolated as expected"；echo→GENUINE |
