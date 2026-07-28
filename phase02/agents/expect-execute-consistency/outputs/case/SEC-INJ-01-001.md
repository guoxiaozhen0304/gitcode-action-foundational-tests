# SEC-INJ-01-001
- **标题**: 不可信 PR 标题不可直接插进 run 脚本导致命令注入   - **维度**: 安全性   - **评级**: 断言一致
## 想测什么
含特殊字符的PR标题不应被解释为shell命令执行，表达式值应在脚本生成前完成求值并安全转义。
## 做了什么
YAML workflow中step内联${{ atomgit.event.pull_request.title }}和通过env引用作为对照。trigger为pull_request(untrusted_contributor)。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | must_not_contain "injected_command_executed" | COVERED | 检查日志中无注入执行标志 |
| 2 | run_status | positive | equals "success" | COVERED | 正常运行完成即可判定 |
