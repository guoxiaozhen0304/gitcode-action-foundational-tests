# REL-FAULT-01-038
- **标题**: 故障注入——artifact 上传中途 runner 被杀，半成品不得作为有效 artifact 出现
- **维度**: reliability
- **评级**: 断言一致
## 想测什么
artifact 上传约 50% 时 SIGKILL runner，验证 job=failure、半成品不可见/标记 incomplete、不应有可下载但截断的 artifact、rerun 后 MD5 一致。
## 做了什么
YAML 使用 dd 生成 100MB 文件 + upload-artifact action，fault_injection kill_runner during artifact_upload at 50% progress。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals failure | COVERED | YAML dd + upload-artifact action + kill_runner，platform 日志确认 job 失败 |
| 2 | truncated_artifact_downloadable | negative | equals true | COVERED | YAML 负向检测不应存在可下载但截断的 artifact，对应文本"不应存在可下载且 HTTP 200 但内容截断" |
| 3 | rerun_upload_md5_match | positive | equals true | COVERED | YAML assert rerun 后同名 artifact MD5 一致，对应文本"rerun 后同名 artifact 上传成功、下载 MD5 一致" |
