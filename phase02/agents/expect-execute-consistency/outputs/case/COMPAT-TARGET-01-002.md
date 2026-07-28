# COMPAT-TARGET-01-002
- **标题**: pull_request_target 在 fork 场景下应保持 secret 隔离
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证pull_request_target允许访问仓库secrets且日志中脱敏，同时确认该场景下能成功引用DEPLOY_TOKEN。

## 做了什么
step1使用 `uses: checkout`；step2输出 `echo "Token is: ${{ secrets.DEPLOY_TOKEN }}"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative must_not_contain_secret deterministic | "日志中不应出现DEPLOY_TOKEN明文" | COVERED | must_not_contain_secret为平台脱敏机制验证(R4★可观测)；步骤确实尝试输出secrets.DEPLOY_TOKEN(GENUINE R1)，平台日志脱敏后应显示*** |
| 2 | run_status | positive equals success llm | "pull_request_target场景下能成功引用secrets" | COVERED | run_status成功=secret注入成功+执行完毕(GENUINE R1平台日志) |
