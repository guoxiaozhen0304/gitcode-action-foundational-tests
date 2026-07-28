# COMPAT-TOKEN-01-003
- **标题**: GITHUB_TOKEN 不应被静默映射为 ATOMGIT_TOKEN
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
验证 GitCode 不将 GITHUB_TOKEN 环境变量和 secrets 静默映射为 ATOMGIT_TOKEN 的值。
## 做了什么
输出 `$GITHUB_TOKEN` 和 `$ATOMGIT_TOKEN` 环境变量，以及 `${{ secrets.GITHUB_TOKEN }}` 引用，比对值。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | llm_assisted 判断GITHUB_TOKEN不等于ATOMGIT_TOKEN | LLM_DEPENDENT | eval=llm_assisted，需人工比对日志值 |
| 2 | run_logs | positive | llm_assisted 判断GITHUB_TOKEN为空或未定义 | LLM_DEPENDENT | eval=llm_assisted |
| 3 | run_logs | negative | llm_assisted 判断secrets.GITHUB_TOKEN不被静默映射 | LLM_DEPENDENT | eval=llm_assisted |
