# COMPAT-ACTION-01-002
- **标题**: checkout 短名等价性——path 参数支持   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
验证 `uses: checkout` 配合 path 参数可将代码检出到指定子目录。
## 做了什么
workflow_dispatch 触发，checkout path:subdir/checkout-path，后续 step 验证文件存在。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_status | positive | equals: completed_success | GENUINE→COVERED | checkout + 文件校验为真实操作 |
| 2 | run_logs | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；rubric 检查 CHECKOUT_PATH_OK |
| 3 | run_logs | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9 |
| 4 | workflow_parse | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9 |
