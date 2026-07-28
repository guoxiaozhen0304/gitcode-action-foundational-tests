# COMPAT-PR-01-001
- **标题**: pull_request types 命名差异 - GitCode 合法 types 应被接受
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试 GitCode 风格的 pull_request types（open, reopen, update）被平台正常接受并触发。

## 做了什么
配置 `pull_request.types: [open, reopen, update]`，step 中 echo `${{ atomgit.event.action }}` 和 "PR_TYPES_OK"。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals success | COVERED | GitCode 合法 types 的 PR 应成功触发执行 |
| 2 | run_logs | positive | must_contain "PR_TYPES_OK" | COVERED | echo 输出可验证 workflow 执行 |
