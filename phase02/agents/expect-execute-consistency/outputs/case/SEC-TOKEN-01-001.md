# SEC-TOKEN-01-001
- **标题**: fork PR 触发 pull_request 时 ATOMGIT_TOKEN 必须仅拥有 read 权限
- **维度**: 安全性
- **评级**: 断言一致

## 想测什么
fork PR 场景下 ATOMGIT_TOKEN 可执行读操作，写操作被拒绝。

## 做了什么
workflow 使用 `${{ atomgit.token }}` 执行 git clone（读）和 curl POST（尝试写），trigger 为 pull_request + untrusted_contributor。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | clone_successful | COVERED | `git clone ... ${{ atomgit.token }}` 真实表达式+命令，clone 成功则日志中包含 Cloning 等平台日志 |
| 2 | run_logs | negative | must_not_contain: write_permission_granted | COVERED | `curl ... ${{ atomgit.token }}` 真实 API 调用，写操作返回 403，日志可验证 |

