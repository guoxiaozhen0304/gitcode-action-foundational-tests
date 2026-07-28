# COMPAT-ARTIFACT-01-001

- **标题**: upload/download-artifact 跨 job 传递等价性
- **维度**: 兼容性
- **评级**: 断言一致

---

## 想测什么
验证 upload-artifact 和 download-artifact 插件在 job 间正确传递文件。

## 做了什么
job-upload 创建 marker 文件并 upload-artifact；job-download（needs: job-upload）download 后验证内容，输出 ARTIFACT_TRANSFER_OK 或 FAILED。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | completed_success | LLM_DEPENDENT | 需人工判定运行状态与预期一致 |
| 2 | run_logs | positive | llm_assisted | LLM_DEPENDENT | 需人工判定日志中出现 ARTIFACT_TRANSFER_OK |
| 3 | run_logs | negative | llm_assisted | LLM_DEPENDENT | 需人工判定日志中不出现 ARTIFACT_TRANSFER_FAILED |
| 4 | workflow_parse | negative | llm_assisted | LLM_DEPENDENT | 需人工判定裸插件名不导致解析失败 |
