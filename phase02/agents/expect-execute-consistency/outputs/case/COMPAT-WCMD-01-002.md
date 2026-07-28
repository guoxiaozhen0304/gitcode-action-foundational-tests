# COMPAT-WCMD-01-002
- **标题**: ::group:: 不被支持时应静默降级而非报错
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
验证 GitCode 不支持 `::group::`/`::endgroup::` 工作流命令时静默降级，而非报错中断 workflow。
## 做了什么
在 run 步骤中使用 `::group::My Group` 和 `::endgroup::`，观察执行结果。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | equals=success eval=llm_assisted | LLM_DEPENDENT | eval=llm_assisted |
| 2 | run_logs | negative | llm_assisted 判断不应报错中断 | LLM_DEPENDENT | eval=llm_assisted |
