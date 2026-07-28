# COMPAT-ARTIFACT-01-002
- **标题**: upload-artifact 保留期行为等价性   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
验证 upload-artifact 支持 retention-days 参数，保留期内可下载，超期后被清理。
## 做了什么
workflow_dispatch 触发，创建 marker 文件，uses: upload-artifact retention-days:1，echo `ARTIFACT_UPLOADED_OK`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_status | positive | equals: completed_success | GENUINE→COVERED | upload + echo 为真实操作 |
| 2 | run_logs | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；rubric 检查 ARTIFACT_UPLOADED_OK |
| 3 | artifact_state | nonfunctional | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；保留期行为需 LLM 分析 artifact 状态 |
| 4 | run_logs | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9 |
