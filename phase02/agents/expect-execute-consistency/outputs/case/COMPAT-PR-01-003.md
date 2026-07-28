# COMPAT-PR-01-003
- **标题**: PR types 配置后匹配类型不触发与 GitHub 行为差异
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试已知问题——配置 pull_request.types 后，匹配类型的 PR 变更可能不触发 workflow（假阴性）。

## 做了什么
配置 `pull_request.types: [open, reopen, update]`，step 中 echo `${{ atomgit.event_name }}`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | llm_assisted rubric | LLM_DEPENDENT | 假阴性行为需 LLM 辅助判断 |
| 2 | run_status | positive | llm_assisted rubric "equals success" | LLM_DEPENDENT | 修复后触发行为需 LLM 辅助判断 |
