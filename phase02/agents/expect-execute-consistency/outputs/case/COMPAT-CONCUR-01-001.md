# COMPAT-CONCUR-01-001
- **标题**: concurrency cancel-in-progress false 时应排队而非报错
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**第二次触发不应直接报错失败，应进入排队状态等待第一次完成后执行**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-034
通过标准：
1. 第二次触发不应被标记为失败或取消
2. 第二次触发的状态为 queued/pending
3. 第一次完成后第二次正常开始执行
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | checkout source | `uses: checkout` | — | 检出代码 |
| 2 | long running step | `sleep 60; echo "Job done"` | — | Job done |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status != failure | negative | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 2 | run_status 排队状态 | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 3 | run_logs Job done | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
---
