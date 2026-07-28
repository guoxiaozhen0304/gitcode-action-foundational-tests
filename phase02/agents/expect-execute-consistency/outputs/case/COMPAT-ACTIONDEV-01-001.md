# COMPAT-ACTIONDEV-01-001

- **标题**: action.yml 元数据校验与 GitHub 差异
- **维度**: 兼容性
- **评级**: 断言一致

---

## 想测什么
验证不支持的 action.yml 元数据字段（如 branding）不导致 workflow 失败，系统应给出提示。

## 做了什么
checkout 后使用本地 action ./.github/actions/my-action。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | llm_assisted | LLM_DEPENDENT | 需人工判定不支持的字段不导致失败 |
| 2 | error_message | positive | llm_assisted | LLM_DEPENDENT | 需人工判定系统对不支持的元数据给出提示 |
