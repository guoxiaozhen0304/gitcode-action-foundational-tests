# COMPAT-WCMD-01-004
- **标题**: 注解命令 error/warning/notice 的不中断降级行为
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
验证 GitCode 处理 `::error::`/`::warning::`/`::notice::` 注解命令时不导致 step 或 workflow 失败，后续命令正常执行。
## 做了什么
输出注解命令后执行正常命令，观察 workflow 是否仍成功完成且后续日志无截断。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | equals=success | COVERED | 注解命令后流程正常结束，Harness 直接验证状态 |
| 2 | run_logs | positive | must_contain=AFTER_ANNOTATION_OK | COVERED | 标志字符串确认后续步骤执行 |
| 3 | run_logs | negative | llm_assisted 判断不应截断后续日志 | LLM_DEPENDENT | eval=llm_assisted，需人工检查日志完整性 |
