# COMP-ACT-01-003

- **标题**: 手动取消时 action runs.post 由调度服务调用
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证手动取消运行中的 workflow 时，声明 `runs.post` 的 action 的 post 入口被调度服务调用。

## 做了什么
通过 `uses: ./.gitcode/actions/post-hook` 调用声明 `runs.main`（长时间运行）与 `runs.post`（输出 `POST_CLEANUP_DONE`）的本地 action；运行至约 50% 时手动取消。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: POST_CLEANUP_DONE | COVERED | action.post 脚本在被调用后输出该标记，trace 到真实的 post 入口执行 |
| 2 | run_status | negative | equals: success | COVERED | 取消后的终态应为 cancelled（非 success），行为依赖实际的取消+post 调用路径 |
| 3 | post_latency | nonfunctional | eval: llm_assisted | COVERED | LLM_DEPENDENT 断言 |
