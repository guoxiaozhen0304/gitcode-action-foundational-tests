# COMPAT-TARGET-01-003
- **标题**: pull_request_target 默认 types 与 GitHub 差异
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
验证 GitCode pull_request_target 的默认 types 行为是否与 GitHub 一致——opened、synchronize、reopened。
## 做了什么
创建不声明 types 的 pull_request_target workflow，创建 PR 并观察触发行为。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | llm_assisted 判断PR open应触发 | LLM_DEPENDENT | eval=llm_assisted |
| 2 | run_status | positive | llm_assisted 判断PR synchronize应触发 | LLM_DEPENDENT | eval=llm_assisted |
