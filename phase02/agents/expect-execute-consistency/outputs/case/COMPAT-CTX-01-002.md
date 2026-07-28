# COMPAT-CTX-01-002

- **标题**: 使用 atomgit.ref 上下文应正确返回触发引用
- **维度**: 兼容性
- **评级**: 断言一致

---

## 想测什么
验证 atomgit.ref 上下文正确返回触发事件的引用。

## 做了什么
echo "atomgit_ref=${{ atomgit.ref }}"。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | llm_assisted | LLM_DEPENDENT | 需人工判定运行成功 |
| 2 | run_logs | positive | llm_assisted | LLM_DEPENDENT | 需人工判定 atomgit_ref 非空且符合 refs/heads/ 格式 |
