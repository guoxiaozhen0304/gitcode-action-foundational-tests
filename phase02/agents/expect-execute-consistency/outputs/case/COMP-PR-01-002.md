# COMP-PR-01-002
- **标题**: pull_request_target 可访问 secrets 且 TOKEN 拥有写权限
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
pull_request_target 可访问 secrets，日志中 secret 脱敏显示。

## 做了什么
1. trigger: pull_request_target, as: maintainer
2. step `Read secret and token`：`echo "secret is ${{ secrets.DEPLOY_TOKEN }}"` 和 `echo "token length is ${#ATOMGIT_TOKEN}"`

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains_masked: DEPLOY_TOKEN | COVERED | ${{ secrets.DEPLOY_TOKEN }} 表达式在 pull_request_target 下可求值，平台 mask 后日志显示 *** |
| 2 | run_status | positive | success | COVERED | pull_request_target 有真实执行路径 |
