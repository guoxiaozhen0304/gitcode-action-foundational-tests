# COMPAT-CTX-01-002
- **标题**: 使用 atomgit.ref 上下文应正确返回触发引用   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
验证 `${{ atomgit.ref }}` 返回非空的触发引用值（如 refs/heads/main）。
## 做了什么
workflow_dispatch 触发，step echo `atomgit_ref=${{ atomgit.ref }}`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_status | positive | equals: success | GENUINE→COVERED | 无可失败步骤 |
| 2 | run_logs | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；需 LLM 判定 atomgit_ref 为非空有效引用 |
