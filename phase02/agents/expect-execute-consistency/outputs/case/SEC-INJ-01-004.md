# SEC-INJ-01-004
- **标题**: 不可信 commit message 不可直接插进 run 脚本导致命令注入   - **维度**: 安全性   - **评级**: 断言一致
## 想测什么
commit message中的反引号或分号不应被解释为shell命令执行。
## 做了什么
YAML workflow中step内联${{ atomgit.event.commits[0].message }}和通过env引用作为对照。trigger为push(untrusted_contributor)。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | must_not_contain "injected_command_executed" | COVERED | 检查日志中无注入执行标志 |
| 2 | run_status | positive | equals "success" | COVERED | 正常运行完成即可判定 |
