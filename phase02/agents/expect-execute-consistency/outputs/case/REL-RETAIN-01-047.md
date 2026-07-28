# REL-RETAIN-01-047
- **标题**: artifact 保留期 90 天边界——第 91 天应不可下载   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证 artifact 保留期 90 天的边界语义：第 90 天可下载（HTTP 200），第 91 天不可下载（HTTP 404）。
## 做了什么
上传 retention-days=90 的 artifact，分别在第 90 天和第 91 天尝试下载。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | download_day90_status | positive | equals "200" | COVERED | harness 通过 API 在第 90 天下载并验证 HTTP 状态码 |
| 2 | download_day91_status | positive | equals "404" | COVERED | harness 通过 API 在第 91 天下载并验证 HTTP 状态码 |
