# USE-ENV-01-002
- **标题**: 引用 GITHUB_SHA 时日志应给出环境变量映射提示
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
使用 `$GITHUB_SHA` 时日志应提示 GITHUB 变量不存在或建议使用 ATOMGIT 变量。

## 做了什么
workflow 中有 `set -u` 并使用 `echo "sha=$GITHUB_SHA"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | error_message | nonfunctional | llm_assisted | LLM_DEPENDENT | `$GITHUB_SHA` 环境变量不存在，LLM 辅助判定日志是否给出 GITHUB_* → ATOMGIT_* 映射提示 |

