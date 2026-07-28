# COMPAT-TARGET-01-001
- **标题**: pull_request_target 默认 checkout 应为 base 分支而非 head 分支
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
验证 pull_request_target 触发时默认 checkout 的是目标分支（base）最新 commit，而非 fork PR 的 head commit，确保不执行不可信代码。
## 做了什么
以 pull_request_target 触发的 workflow 中 checkout 代码，输出当前 SHA 与 base/head SHA 比对。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | llm_assisted 判断检出SHA不应等于fork PR head SHA | LLM_DEPENDENT | eval=llm_assisted，需人工比对SHA值 |
| 2 | run_logs | positive | llm_assisted 判断检出SHA等于base分支SHA | LLM_DEPENDENT | eval=llm_assisted，需人工比对SHA值 |
| 3 | run_status | positive | equals=success eval=deterministic | COVERED | 标准运行状态检查，eval=deterministic 可自动化 |
