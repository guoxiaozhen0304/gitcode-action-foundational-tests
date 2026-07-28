# COMPAT-ENVIRON-01-001

- **标题**: 含 environment 字段的 job 应被报错或警告
- **维度**: 兼容性
- **评级**: 断言一致

---

## 想测什么
验证 job 级 environment: production 字段被平台报错或警告，不被静默接受。

## 做了什么
job 声明 environment: production，echo "hello"。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | llm_assisted | LLM_DEPENDENT | 需人工判定不静默接受导致正常运行 |
| 2 | error_message | nonfunctional | llm_assisted | LLM_DEPENDENT | 需人工判定平台给出明确报错或建议 |
