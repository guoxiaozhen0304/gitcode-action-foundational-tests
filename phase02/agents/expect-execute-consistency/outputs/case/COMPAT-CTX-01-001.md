# COMPAT-CTX-01-001
- **标题**: 使用 github.ref 上下文应报错或求值为空   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
验证 `${{ github.ref }}` 不应用被静默映射为 atomgit.ref，应报错或求值为空。
## 做了什么
workflow_dispatch 触发，step echo `github_ref=${{ github.ref }}`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_logs | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；github_ref 应为空或 workflow 失败 |
| 2 | error_message | nonfunctional | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；报错应提示使用 atomgit.* 替代 |
