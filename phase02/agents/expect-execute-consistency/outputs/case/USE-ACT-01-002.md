# USE-ACT-01-002
- **标题**: 使用 actions/checkout@v4 时报错应给出迁移指引
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
使用 GitHub 风格 Action 引用时系统报错并提示 GitCode 官方 Action 使用短名引用。

## 做了什么
workflow 中 `uses: actions/checkout@v4`，预期运行失败并给出迁移指引。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals: COMPLETED | COVERED | 不应以 COMPLETED 状态成功（应失败），平台状态可观测 |
| 2 | error_message | nonfunctional | llm_assisted | LLM_DEPENDENT | LLM 辅助判定报错是否含 actions/checkout 与 checkout 对照及短名说明 |

