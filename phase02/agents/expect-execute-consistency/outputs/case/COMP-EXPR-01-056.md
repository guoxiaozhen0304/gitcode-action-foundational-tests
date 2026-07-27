# COMP-EXPR-01-056

- **标题**: toJson 函数边界行为
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**toJson 函数边界行为**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-056

通过标准：
1. [正向] toJson(atomgit.event) 输出以 { 开头 —— 断言 EVENT_JSON={
2. [正向] toJson(env) 输出合法 JSON —— 断言 ENV_JSON={

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Serialize event | `echo "EVENT_JSON=${{ toJson(atomgit.event) }}"` | - | atomgit.event 对象的 JSON 序列化结果 |
| 2 | Serialize env context | `echo "ENV_JSON=${{ toJson(env) }}"` | - | env 上下文的 JSON 序列化结果 |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: EVENT_JSON={ | ✅ GENUINE | `${{ toJson(atomgit.event) }}` 是真实平台函数对上下文对象的序列化 |
| 2 | run_logs | positive | must_contain: ENV_JSON={ | ✅ GENUINE | `${{ toJson(env) }}` 对 env 上下文的序列化 |

