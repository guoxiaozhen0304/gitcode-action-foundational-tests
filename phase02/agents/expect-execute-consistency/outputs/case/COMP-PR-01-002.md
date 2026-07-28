# COMP-PR-01-002

- **标题**: pull_request_target 可访问 secrets 且 TOKEN 拥有写权限
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 `pull_request_target` 下可访问项目 secrets（日志中脱敏显示为 ***），TOKEN 拥有写权限。

## 做了什么
`on: pull_request_target` + `as: maintainer`；step 中 `echo "secret is ${{ secrets.DEPLOY_TOKEN }}"` 并输出 TOKEN 长度。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains_masked: DEPLOY_TOKEN | COVERED | `${{ secrets.DEPLOY_TOKEN }}` 被引用后平台对其脱敏，日志中应显示为 *** |
| 2 | run_status | positive | equals: success | COVERED | pull_request_target 下可正常访问 secrets + TOKEN |
