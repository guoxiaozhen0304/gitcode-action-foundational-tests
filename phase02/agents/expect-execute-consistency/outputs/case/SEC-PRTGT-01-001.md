# SEC-PRTGT-01-001
- **标题**: pull_request_target 下显式 checkout 不可信 PR 时 secrets 仍应受控
- **维度**: security
- **评级**: 断言一致

## 想测什么
pull_request_target 中显式 checkout fork PR head sha 后执行脚本，secrets 仍应受控。

## 做了什么
workflow pull_request_target 下 checkout ref: ${{ atomgit.event.pull_request.head.sha }}，然后 echo secret。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain_secret "DEPLOY_TOKEN" | COVERED | 对应"运行日志中不应出现 DEPLOY_TOKEN 明文"；platform→GENUINE |
| 2 | run_status | positive | equals "blocked_or_pending" | COVERED | 对应"未审批状态下 job 应处于挂起或拒绝态"；platform→GENUINE |
