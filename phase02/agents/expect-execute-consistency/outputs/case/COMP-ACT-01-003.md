# COMP-ACT-01-003
- **标题**: 手动取消时 action runs.post 由调度服务调用
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
取消运行中的 workflow 后，声明 runs.post 的 action 的 post 入口是否被调度服务调用。

## 做了什么
1. 步骤 `Run cancellable action`：`uses: ./.gitcode/actions/post-hook`，main 长时间运行便于中途取消，post 输出 POST_CLEANUP_DONE

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: POST_CLEANUP_DONE | COVERED | action post hook 在取消后执行时输出此标记 |
| 2 | run_status | negative | equals: success | COVERED | 取消后终态为 cancelled，不应为 success，有真实失败路径 |
| 3 | post_latency | nonfunctional | llm_assisted | LLM_DEPENDENT | eval=llm_assisted，记录时延 |
