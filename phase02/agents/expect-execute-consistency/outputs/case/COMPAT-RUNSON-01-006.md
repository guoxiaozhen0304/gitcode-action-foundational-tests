# COMPAT-RUNSON-01-006
- **标题**: Runner OS 多样性探测：macos-latest 的调度结局（不支持应明确报错）
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
探测 GitCode 是否支持 macOS Runner，不支持时应明确报错并列出受支持 OS。
## 做了什么
提交 `runs-on: [macos-latest, x64, small]` 的工作流，观察校验/调度阶段响应。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | llm_assisted 判断调度或报错结局确定 | LLM_DEPENDENT | eval=llm_assisted |
| 2 | run_status | negative | llm_assisted 判断不应无限queued无提示 | LLM_DEPENDENT | eval=llm_assisted |
| 3 | run_status | nonfunctional | llm_assisted 结论合并回写parity-matrix | LLM_DEPENDENT | type=nonfunctional，文档化任务 |
