# COMP-PR-01-001

- **标题**: fork PR 触发 pull_request 时不可读取项目 secrets
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 fork PR 的 `pull_request` workflow 无法访问项目 secrets，日志中 secret 值不出现明文。

## 做了什么
`on: pull_request` + `as: untrusted_contributor`；step 中 `echo "secret value is ${{ secrets.DEPLOY_TOKEN }}"` 实际引用 secret。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain_secret: DEPLOY_TOKEN | COVERED | `${{ secrets.DEPLOY_TOKEN }}` 在 fork PR 下被实际引用，must_not_contain_secret 校验明文不泄漏（即使为空或被脱敏为 ***） |
| 2 | run_status | positive | equals: success_or_blocked | COVERED | 运行成功或被平台阻止均符合预期（fork PR 安全策略） |
