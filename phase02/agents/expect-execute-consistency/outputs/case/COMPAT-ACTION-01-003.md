# COMPAT-ACTION-01-003
- **标题**: GitHub 风格 action 引用 actions/checkout@v4 的解析域探测   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
探测 `uses: actions/checkout@v4` GitHub 风格全名引用能否被解析（成功执行或保存期明确报错），不应无限排队或模糊失败。
## 做了什么
workflow_dispatch 触发，step 使用 uses: actions/checkout@v4，后续 echo `GITHUB_STYLE_REF_EXECUTED`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | save_result | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；保存期报错或运行成功两种结局均需 LLM 判定 |
| 2 | run_status | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；不应长期 queued 或模糊失败 |
| 3 | save_result | nonfunctional | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；报错/文档应有映射指引 |
