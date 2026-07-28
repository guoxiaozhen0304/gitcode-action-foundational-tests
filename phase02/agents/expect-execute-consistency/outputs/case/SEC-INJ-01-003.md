# SEC-INJ-01-003
- **标题**: 不可信 issue/PR 评论内容不可直接插进 run 脚本导致命令注入
- **维度**: security
- **评级**: 断言一致

## 想测什么
评论 body 含 shell 元字符不应被解释执行；即使编辑后重触发仍保持安全过滤。

## 做了什么
workflow 在 issue_comment 下内联引用 ${{ atomgit.event.comment.body }}；as: untrusted_contributor。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain "injected_command_executed" | COVERED | 对应"含 shell 元字符的评论内容绝不应被解释为命令执行"；${{ }}→GENUINE |
| 2 | run_status | positive | equals "success" | COVERED | 安全过滤正常工作 |
