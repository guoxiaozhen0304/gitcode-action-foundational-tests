# SEC-TOCTOU-01-002
- **标题**: 评论触发不应绕过代码固定与 PR 审批
- **维度**: 安全性
- **评级**: 断言一致

## 想测什么
评论触发后推送的新 commit 绝不应被该次特权运行自动执行。

## 做了什么
workflow 使用 issue_comment 触发，step 中 `echo "Executing commit: ${{ atomgit.sha }}"` 输出固定 commit。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain: new_commit_after_trigger | COVERED | `${{ atomgit.sha }}` 真实上下文 + issue_comment 触发，harness 验证执行 commit 未跳变 |
| 2 | run_logs | positive | trigger_sha_matched | COVERED | harness 验证执行 commit 与触发时刻一致 |

