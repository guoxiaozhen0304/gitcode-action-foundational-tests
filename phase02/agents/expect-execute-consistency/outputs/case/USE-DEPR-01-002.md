# USE-DEPR-01-002
- **标题**: 使用 ::set-output 时应给出弃用警告与替代示例
- **维度**: usability
- **评级**: 断言一致

## 想测什么
使用已弃用的 `::set-output` 命令时日志中应出现明确弃用警告，包含替代命令示例。

## 做了什么
step `echo "::set-output name=mykey::myvalue"`。断言为 nonfunctional + llm_assisted 判定警告质量。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | nonfunctional | eval:llm_assisted | LLM_DEPENDENT | nonfunctional + llm_assisted 判定警告信息包含 deprecated + 替代命令示例 |
