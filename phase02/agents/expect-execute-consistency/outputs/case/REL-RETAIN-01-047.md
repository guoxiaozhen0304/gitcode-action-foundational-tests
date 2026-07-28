# REL-RETAIN-01-047
- **标题**: artifact 保留期 90 天边界——第 91 天应不可下载
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
retention-days=90的artifact，第90天下载200，第91天404/403。

## 做了什么
upload-artifact上传retention-days=90的文件，harness在第90天和91天尝试下载。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | download_day90_status | positive | equals=200 | COVERED | 文本"第90天下载成功(HTTP 200)"精确对应 |
| 2 | download_day91_status | positive | equals=404 | COVERED | 文本"第91天下载失败(404/403)"对应(取404) |
