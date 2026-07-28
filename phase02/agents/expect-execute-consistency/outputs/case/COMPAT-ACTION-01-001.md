# COMPAT-ACTION-01-001
- **标题**: checkout 短名等价性——ref 参数支持   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
验证 `uses: checkout` 裸插件名配合 ref 参数可正确检出指定分支，行为与 GitHub 全名写法等价。
## 做了什么
workflow_dispatch 触发，checkout ref:main，后续 step 验证 `git rev-parse --abbrev-ref HEAD` 是否等于 main。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_status | positive | equals: completed_success | GENUINE→COVERED | checkout + git 命令为真实操作 |
| 2 | run_logs | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；rubric 检查 CHECKOUT_REF_OK |
| 3 | run_logs | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；rubric 检查 CHECKOUT_REF_FAILED 不应出现 |
| 4 | workflow_parse | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；不应因裸插件名 checkout 解析失败 |
