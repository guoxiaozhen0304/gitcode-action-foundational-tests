# USE-DISP-01-001
- **标题**: workflow_dispatch 必填参数未提供时应给出明确校验错误
- **维度**: usability
- **评级**: 断言一致

## 想测什么
缺少 required input 时系统拒绝触发并提示缺少必填参数。

## 做了什么
workflow 配置 required:true 的 input（无 default），params:{} 触发。断言检查 run_status 不应完成及 error_message。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals:COMPLETED | COVERED | 平台 run_status，期望缺少必填参数时触发被拒；GENUINE |
| 2 | error_message | nonfunctional | eval:llm_assisted | LLM_DEPENDENT | nonfunctional + llm_assisted 判定报错信息包含字段名 |
