# COMPAT-ARTIFACT-01-001
- **标题**: upload/download-artifact 跨 job 传递等价性   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
验证 upload-artifact/download-artifact 裸插件名可跨 job 传递文件，行为与 GitHub 全名写法等价。
## 做了什么
workflow_dispatch 触发，job-upload（创建 marker 文件 + uses: upload-artifact），job-download（needs: job-upload + uses: download-artifact + 验证 marker 内容）。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_status | positive | equals: completed_success | GENUINE→COVERED | upload/download/校验均为真实操作 |
| 2 | run_logs | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；rubric 检查 ARTIFACT_TRANSFER_OK |
| 3 | run_logs | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9 |
| 4 | workflow_parse | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9 |
