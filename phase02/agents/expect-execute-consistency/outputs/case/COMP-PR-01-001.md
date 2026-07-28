# COMP-PR-01-001
- **标题**: fork PR 触发 pull_request 时不可读取项目 secrets
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
fork PR 的 pull_request workflow 无法获取 DEPLOY_TOKEN 值，日志中不出现明文。

## 做了什么
1. trigger: pull_request, as: untrusted_contributor
2. step `Attempt to read secret`：`echo "secret value is ${{ secrets.DEPLOY_TOKEN }}"`

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain_secret: DEPLOY_TOKEN | GENUINE | step 使用 `${{ secrets.DEPLOY_TOKEN }}` 尝试输出 secret，平台应阻止/mask；断言检查日志不含明文 secret 值 |
| 2 | run_status | positive | equals: success_or_blocked | COVERED | fork PR 模式下可能被 blocked 或成功但 secret 为空 |
