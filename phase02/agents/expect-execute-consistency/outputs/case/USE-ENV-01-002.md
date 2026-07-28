# USE-ENV-01-002
- **标题**: 引用 GITHUB_SHA 时日志应给出环境变量映射提示
- **维度**: usability
- **评级**: 断言一致

## 想测什么
引用 `$GITHUB_SHA` 时日志中应出现关于 GITHUB 变量不存在或建议使用 ATOMGIT 的提示。

## 做了什么
step `set -u; echo "sha=$GITHUB_SHA"` 引用不存在的 GITHUB 环境变量。断言为 nonfunctional + llm_assisted。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | error_message | nonfunctional | eval:llm_assisted | LLM_DEPENDENT | nonfunctional + llm_assisted 判定日志警告包含 ATOMGIT 映射指引 |
