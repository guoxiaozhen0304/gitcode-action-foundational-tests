# COMPAT-DIR-01-002
- **标题**: 工作流目录差异——.github/workflows/ 不应被识别   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
验证 `.github/workflows/` 下工作流不被 GitCode 平台识别触发。
## 做了什么
repo_fixture: with-github-dir，push 事件触发，step echo `GITHUB_DIR_WORKFLOW_RAN`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | workflow_discovery | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；.github 目录下不应被识别 |
| 2 | run_logs | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；不应出现 GITHUB_DIR_WORKFLOW_RAN |
| 3 | run_status | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；仅 .gitcode 下应被触发 |
说明：此用例为负向探测——若平台正确忽略 .github/workflows/，则本 workflow 不应被触发，所有断言均为"不应发生"类型。若确实未被触发，则断言成立但无 run_logs 可读取。依赖 LLM 确认平台行为。 |
