# USE-BADGE-01-001
- **标题**: workflow 运行完成后状态徽标及时回写且语义清晰
- **维度**: usability
- **评级**: 断言一致

## 想测什么
状态徽标在 Commits 页面和 PR Checks 页面及时刷新，成功/失败图标语义清晰。

## 做了什么
step `echo "success"` 确保成功完成。断言检查 run_status 和 ui_visual。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals:COMPLETED | COVERED | 平台 run_status，GENUINE |
| 2 | ui_visual | nonfunctional | eval:llm_assisted | LLM_DEPENDENT | nonfunctional + llm_assisted 判定 UI 徽标渲染质量 |
