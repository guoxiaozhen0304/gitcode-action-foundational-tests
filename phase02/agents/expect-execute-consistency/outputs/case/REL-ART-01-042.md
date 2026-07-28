# REL-ART-01-042
- **标题**: artifact 大小上限探测——2GB 上传应完整成功（MD5 一致）或上传阶段明确拒绝
- **维度**: 稳定性
- **评级**: 断言一致
## 想测什么
探测 GitCode artifact 大小上限——2GB 上传应完整成功（MD5 一致）或上传阶段明确拒绝并给出上限值。
## 做了什么
上游生成 2GB 文件上传 artifact，下游下载（若上传成功）并校验 MD5 一致性。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | upload_outcome | positive | equals=success_or_explicit_rejection_with_limit | COVERED | Harness 可判定上传成功或明确拒绝 |
| 2 | md5_match | positive | equals=true_if_upload_success | COVERED | 条件性 MD5 检查，Harness 可逻辑判定 |
| 3 | ghost_artifact_detected | negative | equals=true（不应当出现幽灵 artifact） | COVERED | Harness 校验：上传成功但查不到/下载 404/MD5 不匹配 |
| 4 | measured_artifact_limit | nonfunctional | equals=recorded | LLM_DEPENDENT | type=nonfunctional，文档化回写任务 |
