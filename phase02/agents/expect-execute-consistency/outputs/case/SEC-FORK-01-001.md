# SEC-FORK-01-001
- **标题**: fork PR 触发 pull_request 时不可读取项目 secrets
- **维度**: security
- **评级**: 断言一致

## 想测什么
fork PR 场景下 DEPLOY_TOKEN 被阻止访问，日志不出现原值。

## 做了什么
workflow 在 pull_request 下引用 secrets.DEPLOY_TOKEN 并 echo/env；as: untrusted_contributor。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain_secret "DEPLOY_TOKEN" | COVERED | 对应"日志不含 DEPLOY_TOKEN 明文"；platform masking→GENUINE |
| 2 | run_status | positive | equals "completed_or_blocked" | COVERED | 对应"fork PR job 中 secrets 引用为空或不可访问" |
