# SEC-TOKEN-01-002
- **标题**: fork PR 中 ATOMGIT_TOKEN 写操作被平台拒绝
- **维度**: 安全性
- **评级**: 断言一致

## 想测什么
fork PR 中尝试推送操作返回权限拒绝（403）。

## 做了什么
workflow 使用 `${{ atomgit.token }}` clone 后尝试 git push，trigger 为 pull_request + untrusted_contributor。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | push_denied_or_403 | COVERED | `git push origin main || echo "push denied"` 真实 git 命令，push 被拒后产出 "push denied" |
| 2 | run_status | positive | completed | COVERED | 平台执行层面可观测，运行应完成不被中断 |

