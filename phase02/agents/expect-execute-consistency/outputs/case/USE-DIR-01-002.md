# USE-DIR-01-002
- **标题**: .github/workflows/ 下 workflow 未被识别时应给出目录差异提示
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
错误放置到 .github/workflows/ 的 workflow 应被提示 .gitcode/workflows/ 为正确目录。

## 做了什么
workflow 为 null，harness 观察系统在运行页面/日志/校验信息中是否给出目录提示。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | system_message | nonfunctional | llm_assisted | LLM_DEPENDENT | LLM 辅助判定提示是否同时包含 .github/workflows 与 .gitcode/workflows 对照字样 |

