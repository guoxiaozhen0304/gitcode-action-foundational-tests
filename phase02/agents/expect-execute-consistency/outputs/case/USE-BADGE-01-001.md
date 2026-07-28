# USE-BADGE-01-001
- **标题**: workflow 运行完成后状态徽标及时回写且语义清晰
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
状态徽标在 Commits 页面和 PR Checks 标签页及时刷新，成功/失败/跳过图标语义清晰。

## 做了什么
workflow 由 push 触发，执行简单的 `echo "success"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | COMPLETED | COVERED | 平台运行状态直接可观测 |
| 2 | ui_visual | nonfunctional | llm_assisted | LLM_DEPENDENT | LLM 辅助判定 UI 徽标尺寸、颜色语义、tooltip 内容 |

