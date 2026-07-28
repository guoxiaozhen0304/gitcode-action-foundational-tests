# COMPAT-DIR-01-001

- **标题**: 工作流目录差异——.gitcode/workflows/ 正常识别
- **维度**: 兼容性
- **评级**: 断言一致

---

## 想测什么
验证 .gitcode/workflows/ 下的 workflow 被平台正常识别。

## 做了什么
push 触发，echo "GITCODE_DIR_RECOGNIZED_OK"。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | completed_success | LLM_DEPENDENT | 需人工判定运行状态与预期一致 |
| 2 | run_logs | positive | llm_assisted | LLM_DEPENDENT | 需人工判定日志中出现 GITCODE_DIR_RECOGNIZED_OK |
| 3 | workflow_discovery | positive | llm_assisted | LLM_DEPENDENT | 需人工判定 .gitcode/workflows/ 被正确识别 |
