# COMP-ACT-01-003

- **标题**: 手动取消时 action runs.post 由调度服务调用
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**手动取消时 action runs.post 由调度服务调用**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-028

通过标准：
1. [正向] 取消后 post 逻辑被执行（日志含清理标记）—— 断言 run_logs must_contain POST_CLEANUP_DONE
2. [负向] 取消后运行不应为 success —— 断言 run_status != success
3. [非功能] 取消到 post 被调用的时延记录 —— 🔶 LLM_DEPENDENT（跳过）

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Run cancellable action | `uses: ./.gitcode/actions/post-hook` | - | main 长时间运行，post 输出 POST_CLEANUP_DONE |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | local-action-post |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: POST_CLEANUP_DONE | ✅ GENUINE | action 的 runs.post 入口在取消后被平台调用，输出清理标记 |
| 2 | run_status | negative | equals: success | ✅ GENUINE | 手动取消后运行终态为 cancelled，非 success |
| 3 | post_latency | nonfunctional | eval: llm_assisted | 🔶 LLM_DEPENDENT | 跳过 |

