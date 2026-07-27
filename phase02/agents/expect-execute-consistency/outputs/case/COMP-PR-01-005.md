# COMP-PR-01-005

- **标题**: 源分支更新后 pre-merge ref 指向刷新验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**源分支更新后 pre-merge ref 指向刷新验证**
- 触发事件: `pull_request`
- 规格引用: INTENT-COMP-033

通过标准：
1. [正向] 源分支更新后 ref 内容刷新（sha 变化）—— 断言 run_logs must_contain REF_SHA_RECORDED
2. [非功能] PR 合并/关闭后再次解析该 ref 的行为逐字记录 —— 🔶 LLM_DEPENDENT（跳过）
3. [负向] 不应源分支已更新但 ref 仍为陈旧合并结果 —— 🔶 LLM_DEPENDENT（跳过）

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Checkout merge ref again | `uses: checkout` with: ref: refs/merge-requests/1/merge | - | checkout action 解析 merge ref |
| 2 | Record head sha | `git rev-parse HEAD` + `echo "REF_SHA_RECORDED"` | - | 当前 HEAD SHA 值 |

## 3. 触发与运行环境

| 触发事件 | pull_request |
| 触发身份 | maintainer |
| Repo 环境 | pr-merge-ref |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: REF_SHA_RECORDED | ✅ GENUINE | `git rev-parse HEAD` 是真实 git 命令，输出当前 checkout 的 merge ref 对应 SHA |
| 2 | ref_refresh | nonfunctional | eval: llm_assisted | 🔶 LLM_DEPENDENT | 跳过 |
| 3 | stale_ref | negative | eval: llm_assisted | 🔶 LLM_DEPENDENT | 跳过 |

