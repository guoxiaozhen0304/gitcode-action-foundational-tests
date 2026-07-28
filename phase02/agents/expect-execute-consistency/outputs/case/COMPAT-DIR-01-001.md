# COMPAT-DIR-01-001
- **标题**: 工作流目录差异——.gitcode/workflows/ 正常识别   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
验证 `.gitcode/workflows/` 下 .yml 文件被正确识别，对应事件触发时正常执行。
## 做了什么
push 事件触发，step echo `GITCODE_DIR_RECOGNIZED_OK`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_status | positive | equals: completed_success | GENUINE→COVERED | 正常 push 触发执行 |
| 2 | run_logs | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；rubric 检查 GITCODE_DIR_RECOGNIZED_OK |
| 3 | workflow_discovery | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；工作流被发现并触发依赖平台 discovery |
说明：核心验证点"工作流被正确识别"依赖于 YAML 被放置在 .gitcode/workflows/ 目录后平台能否 discovery，run_logs 断言为成功执行后的存在性检查。 |
