# COMPAT-DIR-01-003

- **标题**: .github/workflows 目录不应被识别且应给出迁移提示
- **维度**: 兼容性
- **评级**: 断言一致

---

## 想测什么
验证 .github/workflows/ 下的 workflow 不被触发且系统给出迁移提示。

## 做了什么
push 触发，echo "hello"。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | llm_assisted | LLM_DEPENDENT | 需人工判定 workflow 不被触发 |
| 2 | error_message | positive | llm_assisted | LLM_DEPENDENT | 需人工判定系统给出正确目录迁移提示 |
