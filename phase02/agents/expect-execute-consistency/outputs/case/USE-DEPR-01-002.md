# USE-DEPR-01-002
- **标题**: 使用 ::set-output 时应给出弃用警告与替代示例
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
`echo ::set-output name=key::val` 日志中出现明确的弃用警告。

## 做了什么
workflow step 中 `echo "::set-output name=mykey::myvalue"` 使用已弃用的工作流命令。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | nonfunctional | llm_assisted | LLM_DEPENDENT | LLM 辅助判定日志是否包含 deprecated/废弃/ATOMGIT_OUTPUT 字样及替代示例 |

