# COMP-CTX-01-053

- **标题**: 上下文在 Action 插件参数中注入验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**上下文在 Action 插件参数中注入验证**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-051

通过标准：
1. [正向] with 参数中的上下文表达式被正确替换并传入 Action —— 断言 run_status=success

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Checkout with explicit token | `uses: checkout` with: ref: `${{ atomgit.ref }}` | - | checkout action 接收平台上下文参数 |
| 2 | Echo env in action param | `echo "done"` | - | "done"（标志位） |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | ✅ GENUINE | uses: checkout 是真实 action，with 参数 ref: `${{ atomgit.ref }}` 测试上下文在 action 参数中的注入 |

