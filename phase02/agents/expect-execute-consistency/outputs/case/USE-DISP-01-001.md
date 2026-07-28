# USE-DISP-01-001
- **标题**: workflow_dispatch 必填参数未提供时应给出明确校验错误
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
workflow_dispatch 必填参数未提供时系统拒绝触发并提示缺少必填参数。

## 做了什么
workflow 定义必填 input environment（required: true），trigger 未提供该参数。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals: COMPLETED | COVERED | 缺少必填 input，不应以 COMPLETED 状态成功 |
| 2 | error_message | nonfunctional | llm_assisted | LLM_DEPENDENT | LLM 辅助判定报错是否指出缺少 environment 字段名 |

