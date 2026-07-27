# COMP-CACHE-01-002

- **标题**: restore-keys 前缀匹配兜底生效
- **维度**: completeness
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**restore-keys 前缀匹配兜底生效**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-016

通过标准：
1. [正向] cache 步骤通过 restore-keys 命中 —— 断言 cache_step=restore_hit

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Cache test file | `uses: cache` with key 和 restore-keys 配置 | - | 平台 cache action 按 restore-keys 前缀匹配兜底 |
| 2 | Use cache | `cat cached.txt \|\| echo "cache miss"` | - | 读取缓存内容 |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | cache_step | positive | equals: restore_hit | ✅ GENUINE | uses: cache 带 restore-keys 执行真实缓存恢复逻辑 |

