# USE-CTX-01-002
- **标题**: 使用 github 上下文时报错应提示 atomgit 替代
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
引用 `${{ github.ref }}` 时报错并提示应使用 atomgit 上下文。

## 做了什么
workflow step 中 `echo "ref=${{ github.ref }}"` 引用 GitHub 上下文。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals: COMPLETED | COVERED | `${{ github.ref }}` 真实表达式，不应以 COMPLETED 状态成功 |
| 2 | error_message | nonfunctional | llm_assisted | LLM_DEPENDENT | LLM 辅助判定报错是否同时出现 github 与 atomgit 及替换建议 |

