# COMPAT-CONCUR-01-001
- **标题**: concurrency cancel-in-progress false 时应排队而非报错   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
验证 cancel-in-progress:false 时并发运行进入排队（queued/pending）而非直接失败，与 GitHub 排队语义一致。
## 做了什么
workflow_dispatch 触发，concurrency group + cancel-in-progress:false，step sleep 60 + echo `Job done`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_status | negative | equals: failure + eval:llm_assisted | LLM_DEPENDENT→COVERED | 校准9；第二次触发不应被标记为失败 |
| 2 | run_status | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；需 LLM 判断排队状态 |
| 3 | run_logs | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；需 LLM 判定第一次完成后第二次正常执行 |
