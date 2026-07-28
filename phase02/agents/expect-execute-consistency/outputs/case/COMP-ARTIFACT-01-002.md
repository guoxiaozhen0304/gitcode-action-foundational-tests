# COMP-ARTIFACT-01-002
- **标题**: 下载全部制品功能正常
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
不指定 name 时 download-artifact 下载所有上传的 artifacts。

## 做了什么
1. build job: 创建 `dist/app.txt`（内容 "app"）和 `reports/coverage.txt`（内容 "report"），分别上传为 "app" 和 "reports" artifacts
2. verify job (needs: build): download-artifact 不指定 name，path: artifacts/，然后 `cat artifacts/app/app.txt` 和 `cat artifacts/reports/coverage.txt`

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | success | COVERED | 真实 action 调用和文件操作 |
| 2 | run_logs | positive | contains: app | COVERED | `cat artifacts/app/app.txt` 输出 "app" 到日志 |
| 3 | run_logs | positive | contains: report | COVERED | `cat artifacts/reports/coverage.txt` 输出 "report" 到日志 |
