# USE-DIR-01-002
- **标题**: .github/workflows/ 下 workflow 未被识别时应给出目录差异提示
- **维度**: usability
- **评级**: 断言一致

## 想测什么
workflow 误放在 .github/workflows/ 时，系统应提示 .gitcode/workflows/ 为正确目录。

## 做了什么
workflow: null。纯文档/系统消息验证用例，断言指向 system_message。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | system_message | nonfunctional | eval:llm_assisted | LLM_DEPENDENT | nonfunctional + llm_assisted 判定系统提示信息质量 |
