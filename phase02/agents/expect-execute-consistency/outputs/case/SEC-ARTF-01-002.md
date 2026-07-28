# SEC-ARTF-01-002
- **标题**: 跨仓库 artifact 下载返回 403 或 404
- **维度**: security
- **评级**: 断言一致

## 想测什么
在主仓 workflow 中尝试下载 fork PR 的 artifact，应返回 403/404。

## 做了什么
workflow 中用 curl 直接请求 fork artifact API，脚本判 HTTP 状态码并输出 CROSS_REPO_BLOCKED_OK 或 CROSS_REPO_DOWNLOAD_LEAKED。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain "CROSS_REPO_BLOCKED_OK" | COVERED | 对应"返回明确的 404 或 403 错误"；real curl → GENUINE（${{ }} / real cmds） |
| 2 | run_logs | negative | must_not_contain "CROSS_REPO_DOWNLOAD_LEAKED" | COVERED | 对应"跨仓库下载绝不应成功"；脚本在 HTTP 200 时输出→non-trivial |
