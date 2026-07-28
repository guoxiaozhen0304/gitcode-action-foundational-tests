# COMPAT-ENV-01-002
- **标题**: GITHUB_SHA 环境变量在 GitCode 中应为空或未定义   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
验证 $GITHUB_SHA 在 GitCode 中为空或未定义，不应被静默映射到 ATOMGIT_SHA。
## 做了什么
workflow_dispatch 触发，step echo `github_sha=$GITHUB_SHA`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_logs | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；github_sha 应为空或不含 40 位 SHA |
| 2 | error_message | nonfunctional | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；若因未定义变量报错，应提示 ATOMGIT_* 替代 |
