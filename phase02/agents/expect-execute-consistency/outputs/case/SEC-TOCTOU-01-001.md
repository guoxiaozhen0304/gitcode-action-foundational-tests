# SEC-TOCTOU-01-001
- **标题**: 审批后推送新 commit 不应被已授权特权运行执行
- **维度**: security
- **评级**: 断言一致

## 想测什么
特权运行应绑定审批时刻的具体 commit SHA，审批后推送的新 commit 不应被自动采用。

## 做了什么
step `echo "EXECUTED_SHA=${{ atomgit.sha }}"` 输出实际执行的 commit SHA，供 harness 与锁定的 SHA 确定性比对。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | executed_commit_sha | negative | must_not_equal:post_approval_commit_sha | COVERED | step 通过 `${{ atomgit.sha }}` 显式输出 EXECUTED_SHA，harness 可捕获并与 post_approval_commit_sha 比对 |
| 2 | executed_commit_sha | positive | equals:approved_locked_sha (eval:deterministic) | COVERED | 同上，step 输出为可观察的 payload，harness 确定性比对 |
