# REL-FAULT-01-038
- **标题**: 故障注入——artifact 上传中途 runner 被杀，半成品不得作为有效 artifact 出现
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
上传 50% 时 SIGKILL，job=failure，无截断 artifact，rerun 后 MD5 一致。

## 做了什么
生成 100MB 文件 + upload；fault_injection 在上传 50% 时 kill_runner。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals "failure" | COVERED | kill 后 job failure |
| 2 | truncated_artifact_downloadable | negative | equals "true" | COVERED | 由 harness 检查 artifact 列表与可下载性；平台不应有半成品 artifact |
| 3 | rerun_upload_md5_match | positive | equals "true" | COVERED | 由 harness rerun 后验证 MD5 |
