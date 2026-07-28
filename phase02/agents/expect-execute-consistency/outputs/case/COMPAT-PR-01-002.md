# COMPAT-PR-01-002
- **标题**: pull_request types 命名差异 - GitHub 风格 types 应报错
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试 GitHub 风格的 pull_request types（opened, closed, reopened）被平台拒绝并报错。

## 做了什么
配置 `pull_request.types: [opened, closed, reopened]`，step 中 echo `${{ atomgit.event.action }}` 和 "PR_TYPES_OK"。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals success | COVERED | GitHub 风格 types 被拒绝时 run 不应成功 |
| 2 | error_message | nonfunctional | llm_assisted rubric | LLM_DEPENDENT | 错误信息质量需 LLM 辅助判断 |
