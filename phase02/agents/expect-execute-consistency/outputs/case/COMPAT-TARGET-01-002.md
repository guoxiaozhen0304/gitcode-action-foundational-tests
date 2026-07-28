# COMPAT-TARGET-01-002
- **标题**: pull_request_target 在 fork 场景下应保持 secret 隔离
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
验证 pull_request_target 在 fork PR 场景下能正确访问仓库 secrets 但日志脱敏，同时在普通 pull_request 场景下 fork PR 无法访问 secrets。
## 做了什么
以 pull_request_target 触发 workflow 并引用 secrets.DEPLOY_TOKEN，观察执行结果和日志脱敏。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | must_not_contain_secret=DEPLOY_TOKEN eval=deterministic | COVERED | 机密脱敏检查，deterministic 可自动化；Harness 验证日志不含明文 |
| 2 | run_status | positive | equals=success eval=llm_assisted | LLM_DEPENDENT | eval=llm_assisted，需人工确认 pull_request_target 能成功引用 secrets |
