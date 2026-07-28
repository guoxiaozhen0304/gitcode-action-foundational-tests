# COMP-CALL-01-004
- **标题**: 未传 required secret 的 workflow_call 不应空值执行
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
调用方未传 required secret 时不应以空 secret 静默进入被调 workflow 执行，应在校验/调度期明确失败。

## 做了什么
1. caller job：`uses: ./.gitcode/workflows/reusable.yml`，不传 secrets（被调 workflow 声明 secrets required）

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals: success | COVERED | 期望因缺少 required secret 而失败，有真实拒绝路径 |
| 2 | run_logs | negative | must_contain: UPLOAD_DONE | COVERED | UPLOAD_DONE 是被调 workflow 正常执行的标记，不应出现 |
| 3 | error_message | nonfunctional | llm_assisted | LLM_DEPENDENT | eval=llm_assisted |
