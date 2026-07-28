# COMPAT-SECRET-01-005
- **标题**: 环境级 secrets 不支持时应明确报错而非降级为项目级
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
验证 GitCode 不支持环境级 secrets 时给出明确报错，而非将环境级 secret 静默降级为项目级（安全模型变化）。
## 做了什么
创建 `environment: prod` 的 job 并引用 `${{ secrets.ENV_SECRET }}`，同时引用 `${{ secrets.PROJECT_SECRET }}` 作为对照。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | llm_assisted 判断ENV_SECRET不返PROJECT_SECRET值 | LLM_DEPENDENT | eval=llm_assisted，需人工比对日志值 |
| 2 | run_logs | positive | llm_assisted 判断项目级secrets正常注入 | LLM_DEPENDENT | eval=llm_assisted |
| 3 | error_message | positive | llm_assisted 判断环境级secrets缺失给出提示 | LLM_DEPENDENT | eval=llm_assisted |
