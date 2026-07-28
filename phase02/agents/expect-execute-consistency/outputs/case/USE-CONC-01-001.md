# USE-CONC-01-001
- **标题**: concurrency.max 配置 0 或 10 时报错应提示有效范围 1-5
- **维度**: usability
- **评级**: 断言一致

## 想测什么
concurrency.max 配置超出范围（10）时应 YAML 校验报错，不应静默截断。

## 做了什么
workflow 配置 `concurrency: max: 10`，step `echo "hello"`。断言检查 run_status 不应完成及 error_message 质量。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals:COMPLETED | COVERED | 平台 run_status，期望校验拦截导致非 COMPLETED |
| 2 | error_message | nonfunctional | eval:llm_assisted | LLM_DEPENDENT | nonfunctional + llm_assisted 判定报错信息包含范围提示 |
