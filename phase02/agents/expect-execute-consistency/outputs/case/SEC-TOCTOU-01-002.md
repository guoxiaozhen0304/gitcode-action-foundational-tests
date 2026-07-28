# SEC-TOCTOU-01-002
- **标题**: 评论触发不应绕过代码固定与 PR 审批
- **维度**: security
- **评级**: 完全不符

## 想测什么
issue_comment 触发后推送的新 commit 不应被该次特权运行自动执行，运行日志中 commit SHA 应与触发时刻一致。

## 做了什么
step `echo "Executing commit: ${{ atomgit.sha }}"` 输出当前 commit SHA，但未输出断言期望的任意特定字符串。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain:new_commit_after_trigger | VACUOUS | step 从不输出该字符串；R4 规则触发 |
| 2 | run_logs | positive | equals:trigger_sha_matched | VACUOUS | step 不输出该字符串；R1 规则：无任何 echo 产生该字面量 |
