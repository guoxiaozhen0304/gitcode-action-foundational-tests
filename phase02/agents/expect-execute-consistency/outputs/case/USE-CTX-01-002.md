# USE-CTX-01-002
- **标题**: 使用 github 上下文时报错应提示 atomgit 替代
- **维度**: usability
- **评级**: 断言一致

## 想测什么
`${{ github.ref }}` 应报错并提示使用 atomgit 上下文替代。

## 做了什么
step `echo "ref=${{ github.ref }}"`。断言检查 run_status 不应完成及 error_message 质量。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals:COMPLETED | COVERED | 平台 run_status，期望 github 上下文报错导致非 COMPLETED |
| 2 | error_message | nonfunctional | eval:llm_assisted | LLM_DEPENDENT | nonfunctional + llm_assisted 判定报错信息包含替代建议 |
