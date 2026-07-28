# SEC-INJ-01-003
- **标题**: 不可信 issue/PR 评论内容不可直接插进 run 脚本导致命令注入   - **维度**: 安全性   - **评级**: 断言一致
## 想测什么
评论body中的shell元字符不应被解释为命令执行，评论编辑后重触发仍维持安全过滤。
## 做了什么
YAML workflow中step内联${{ atomgit.event.comment.body }}。trigger为issue_comment(untrusted_contributor)，types覆盖created和edited。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | must_not_contain "injected_command_executed" | COVERED | 检查日志中无注入执行标志 |
| 2 | run_status | positive | equals "success" | COVERED | 正常运行完成即可判定 |
