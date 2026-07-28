# COMPAT-CTX-01-003

- **标题**: github 上下文嵌套属性访问应报错而非返回空
- **维度**: 兼容性
- **评级**: 断言一致

---

## 想测什么
验证非 PR 事件中访问 ${{ github.event.pull_request.number }} 不导致 workflow 崩溃。

## 做了什么
workflow_dispatch 触发，echo "pr_number=${{ github.event.pull_request.number }}"。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | llm_assisted | LLM_DEPENDENT | 需人工判定嵌套属性访问不导致崩溃 |
| 2 | run_logs | positive | llm_assisted | LLM_DEPENDENT | 需人工判定返回空值或 null |
