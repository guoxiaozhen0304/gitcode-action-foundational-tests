# USE-ACT-01-002
- **标题**: 使用 actions/checkout@v4 时报错应给出迁移指引
- **维度**: usability
- **评级**: 断言一致

## 想测什么
`uses: actions/checkout@v4` 应报错并提示 GitCode 官方 Action 使用短名引用。

## 做了什么
step uses:actions/checkout@v4（GitHub 风格）。断言检查 run_status 不应完成，及 error_message 的 LLM 辅助判定。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals:COMPLETED | COVERED | 平台 run_status，期望不应成功完成；GENUINE |
| 2 | error_message | nonfunctional | eval:llm_assisted | LLM_DEPENDENT | nonfunctional + llm_assisted 判定报错信息质量 |
