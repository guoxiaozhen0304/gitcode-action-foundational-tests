# COMPAT-SECRET-01-005
- **标题**: 环境级 secrets 不支持时应明确报错而非降级为项目级
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证环境级secrets(ENV_SECRET)不可用时系统行为——应明确报错且不静默降级为项目级secrets。

## 做了什么
job声明 `environment: prod`，step输出 `echo "project_secret=${{ secrets.PROJECT_SECRET }}"` + `echo "env_secret=${{ secrets.ENV_SECRET }}"` + `echo "done"`。PROJECT_SECRET作为对照。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative llm | "ENV_SECRET不应返回PROJECT_SECRET的值" | COVERED | ${{ secrets.ENV_SECRET }}/${{ secrets.PROJECT_SECRET }}为GENUINE(R1上下文表达式)；两值在日志中可对比判断是否有静默降级 |
| 2 | run_logs | positive llm | "project_secret值为project_value，项目级正常注入" | COVERED | ${{ secrets.PROJECT_SECRET }}输出(GENUINE R1) |
| 3 | error_message | positive llm | "系统对环境级secrets缺失给出明确提示" | COVERED | error_message为平台日志(GENUINE R1) |
