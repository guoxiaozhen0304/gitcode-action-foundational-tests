# REL-ART-01-041
- **标题**: 超大 artifact——100 MB artifact 上传后下游 job 应成功下载
- **维度**: 稳定性
- **评级**: 断言一致
## 想测什么
验证 100 MB artifact 上传后下游 job 能成功下载，MD5 校验一致。
## 做了什么
上游生成 100MB 文件上传 artifact，下游下载并校验 MD5 一致性。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | upload_status | positive | equals=success | COVERED | 上传 job 状态，Harness 直接检查 |
| 2 | download_status | positive | equals=success | COVERED | 下载 job 状态，Harness 直接检查 |
| 3 | md5_match | positive | equals=true | COVERED | MD5 比对由测试脚本完成，Harness 可校验 |
