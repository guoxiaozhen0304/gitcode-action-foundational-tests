# COMPAT-ENVIRON-01-002

- **标题**: environment 字段绑定 secrets 的行为差异
- **维度**: 兼容性
- **评级**: 断言一致

---

## 想测什么
验证 environment: prod 字段绑定环境 secret 时平台明确报错或警告。

## 做了什么
job 声明 environment: prod 并引用 ${{ secrets.ENV_SECRET }}。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | llm_assisted | LLM_DEPENDENT | 需人工判定不静默忽略 environment 字段 |
| 2 | error_message | positive | llm_assisted | LLM_DEPENDENT | 需人工判定系统对 environment 字段给出明确报错或警告 |
