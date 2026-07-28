# COMPAT-VARS-01-003
- **标题**: vars 项目级覆盖组织级的优先级差异
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
验证 GitCode vars 的项目级值应覆盖组织级值（与 GitHub 优先级一致）。
## 做了什么
在 workflow 中输出 `${{ vars.ORG_VAR }}`，检查返回的是项目级值还是组织级值。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | llm_assisted 判断ORG_VAR=proj_value | LLM_DEPENDENT | eval=llm_assisted，需人工确认值 |
| 2 | run_logs | negative | llm_assisted 判断不应返回组织级值 | LLM_DEPENDENT | eval=llm_assisted |
