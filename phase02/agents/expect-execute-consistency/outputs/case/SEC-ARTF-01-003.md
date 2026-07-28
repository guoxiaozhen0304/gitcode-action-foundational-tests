# SEC-ARTF-01-003
- **标题**: 宽通配打包含敏感文件名的 artifact 绝不应在无警示情况下静默成功且可被无痕下载
- **维度**: security
- **评级**: 断言一致

## 想测什么
workspace 宽通配上传含敏感文件名 artifact，平台应有警示；跨角色下载留痕。

## 做了什么
workflow 创建敏感命名文件并 upload-artifact(path: .)；断言含确定性锚点 + LLM 辅助判定。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain "SENSITIVE_GLOB_UPLOAD_ATTEMPTED" | COVERED | 确定性锚点，标记上传已尝试；echo→GENUINE |
| 2 | run_logs | negative | eval llm_assisted | COVERED | 对应"无警示静默成功"；平台日志判读→LLM→断言一致 |
| 3 | artifact_download | negative | must_not_equal "cross_role_download_without_trace" | COVERED | 对应"跨角色下载留痕"；harness 判定 |
| 4 | documentation | nonfunctional | eval llm_assisted | COVERED | 对应"文档明示风险"；LLM 辅助 = 断言一致 |
