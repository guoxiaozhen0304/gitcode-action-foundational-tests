# SEC-ORG-01-002
- **标题**: fork PR 触发的运行绝不应读取组织级 secret（与项目级同等隔离）
- **维度**: security
- **评级**: 断言一致

## 想测什么
fork PR 路径下组织级 secret 与项目级 secret 同等隔离，拿不到值。

## 做了什么
workflow 在 pull_request 下引用 secrets.ORG_SHARED_KEY 并 echo；as: untrusted_contributor。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain_secret "ORG_SHARED_KEY" | COVERED | 对应"fork PR 绝不应读到组织级 secret 原值"；platform→GENUINE |
| 2 | run_logs | positive | equals "fork_pr_org_secret_isolated" | COVERED | 对应"主仓 maintainer 可正常引用"→对照确认隔离有效 |
