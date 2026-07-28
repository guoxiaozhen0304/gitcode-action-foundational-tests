# SEC-SUPPLY-01-003
- **标题**: 第三方 Action 来源应具备信任边界（typosquatting 限制）
- **维度**: security
- **评级**: 部分不符

## 想测什么
与官方 Action 名称高度相似的恶意 Action 绝不应被静默解析为合法来源。

## 做了什么
step 使用 `uses: checkout-action@v1`（typo 名称）。无 run step。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | must_not_equal:success | COVERED | 平台 run_status 可观察，typo 名称应导致非 success |
| 2 | run_logs | positive | equals:action_not_found_or_unapproved | VACUOUS | step 无 run 语句输出该字符串；平台错误日志来自 uses 解析而非 step echo |
