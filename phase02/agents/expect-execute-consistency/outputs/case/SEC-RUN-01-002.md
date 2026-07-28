# SEC-RUN-01-002
- **标题**: Runner 环境变量与共享目录必须跨 job 隔离
- **维度**: security
- **评级**: 断言一致

## 想测什么
job A 设置环境变量和 /tmp 文件，job B 不应继承。

## 做了什么
workflow 两个 job：job-a-env 写 $ATOMGIT_ENV 和 /tmp/env-test.txt，job-b-env 检查。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain "isolation broken" | COVERED | 对应"job B 绝不应继承到 job A 的设置"；script check→GENUINE |
| 2 | run_logs | positive | contains "isolated as expected" | COVERED | 对应"job B 日志包含 isolated as expected"；echo→GENUINE |
