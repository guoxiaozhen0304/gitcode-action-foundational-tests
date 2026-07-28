# COMP-ARTIFACT-01-002

- **标题**: 下载全部制品功能正常
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 `download-artifact` 不指定 name 时可下载全部已上传的 artifacts。

## 做了什么
job1 上传两个 artifact（`app` 含 `dist/app.txt`，`reports` 含 `reports/coverage.txt`）；job2 不指定 name 全量下载后 `cat` 验证两个文件均存在。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | COVERED | 全流程（多上传→全量下载→双文件验证）成功 |
| 2 | run_logs | positive | contains: app | COVERED | `cat artifacts/app/app.txt` 输出 `app` |
| 3 | run_logs | positive | contains: report | COVERED | `cat artifacts/reports/coverage.txt` 输出 `report` |
