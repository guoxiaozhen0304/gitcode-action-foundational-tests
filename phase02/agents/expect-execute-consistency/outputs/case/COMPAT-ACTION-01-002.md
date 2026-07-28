# COMPAT-ACTION-01-002

- **标题**: checkout 短名等价性——path 参数支持
- **维度**: 兼容性
- **评级**: 断言一致

---

## 想测什么
验证 uses: checkout 配合 path 参数可将代码检出到指定子目录。

## 做了什么
checkout path: subdir/checkout-path 后，verify step 检查子目录下文件是否存在，输出 CHECKOUT_PATH_OK 或 CHECKOUT_PATH_FAILED。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | completed_success | LLM_DEPENDENT | 需人工判定运行状态与预期一致 |
| 2 | run_logs | positive | llm_assisted | LLM_DEPENDENT | 需人工判定日志中出现 CHECKOUT_PATH_OK |
| 3 | run_logs | negative | llm_assisted | LLM_DEPENDENT | 需人工判定日志中不出现 CHECKOUT_PATH_FAILED |
| 4 | workflow_parse | negative | llm_assisted | LLM_DEPENDENT | 需人工判定裸插件名 checkout 不导致解析失败 |
