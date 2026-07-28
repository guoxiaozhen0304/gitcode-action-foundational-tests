# COMPAT-DIR-01-002

- **标题**: 工作流目录差异——.github/workflows/ 不应被识别
- **维度**: 兼容性
- **评级**: 断言一致

---

## 想测什么
验证 .github/workflows/ 下的 workflow 不被 GitCode 平台识别。

## 做了什么
fixture with-github-dir，push 触发，echo "GITHUB_DIR_WORKFLOW_RAN"。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | workflow_discovery | negative | llm_assisted | LLM_DEPENDENT | 需人工判定 .github/ 下 workflow 不被触发 |
| 2 | run_logs | negative | llm_assisted | LLM_DEPENDENT | 需人工判定不出现 GITHUB_DIR_WORKFLOW_RAN |
| 3 | run_status | positive | llm_assisted | LLM_DEPENDENT | 需人工判定无意外运行记录 |
