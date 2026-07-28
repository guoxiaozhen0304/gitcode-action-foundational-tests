# COMPAT-PR-01-009
- **标题**: pull_request 触发时 atomgit.sha/ref 的代码版本语义（对齐 GitHub merge commit 模型）
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
确定 GitCode 在 pull_request 触发时 atomgit.sha/atomgit.ref 的取值语义——是否对齐 GitHub 的 merge commit 模型。
## 做了什么
在 pull_request 触发的工作流中输出 atomgit.sha、atomgit.ref 及环境变量，检出代码后记录实际 SHA，与 head/base/试合并 SHA 逐一比对。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | must_contain PROBE_DONE | COVERED | 工作流步骤输出 PROBE_DONE，Harness 可直接 grep 日志 |
| 2 | run_logs | positive | llm_assisted 比对 SHA 语义 | LLM_DEPENDENT | eval=llm_assisted，需人工比对 head/base/merge SHA |
| 3 | run_logs | negative | llm_assisted CHECKOUT_HEAD不应与CTX_SHA不一致 | LLM_DEPENDENT | eval=llm_assisted，需人工比对两个SHA值 |
