# SEC-FORK-01-002
- **标题**: fork PR 中 secrets 引用返回空值且 job 不崩溃
- **维度**: security
- **评级**: 断言一致

## 想测什么
fork PR 场景下 API_KEY 返回空字符串，环境变量未设置，job 成功完成。

## 做了什么
workflow 在 pull_request 下将 secrets.API_KEY 注入 env；脚本检查 $API_KEY 是否为空。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain_secret "API_KEY" | COVERED | 对应"环境变量 API_KEY 为空或未定义"→同时确保原值不泄露 |
| 2 | run_status | positive | equals "success" | COVERED | 对应"job 状态为成功完成"；脚本判空后正常退出→GENUINE |
