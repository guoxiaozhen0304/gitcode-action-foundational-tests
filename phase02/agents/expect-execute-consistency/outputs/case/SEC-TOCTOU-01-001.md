# SEC-TOCTOU-01-001
- **标题**: 审批后推送新 commit 不应被已授权特权运行执行
- **维度**: 安全性
- **评级**: 断言一致

## 想测什么
特权运行应绑定审批时刻的具体 commit SHA，审批后推送的新 commit 不应被自动采用。

## 做了什么
workflow 中 `echo "EXECUTED_SHA=${{ atomgit.sha }}"` 输出执行时的 SHA，harness 与审批锁定的 SHA 比对。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | executed_commit_sha | negative | must_not_equal: post_approval_commit_sha | COVERED | `${{ atomgit.sha }}` 真实上下文输出当前 SHA，harness 可确定性比对 |
| 2 | executed_commit_sha | positive | equals: approved_locked_sha | COVERED | eval=deterministic，harness 比对执行 SHA 与审批锁定 SHA |

