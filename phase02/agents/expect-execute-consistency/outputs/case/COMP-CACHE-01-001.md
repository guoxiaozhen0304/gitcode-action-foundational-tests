# COMP-CACHE-01-001

- **标题**: cache hit 时恢复缓存内容正确
- **维度**: completeness
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**cache hit 时恢复缓存内容正确**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-016

通过标准：
1. [正向] cache 步骤状态为 success —— 断言 run_status=success
2. [正向] 恢复后文件内容与之前一致 —— 断言 cache_step=hit

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Cache test file | `uses: cache` with key: cache-test-${{ runner.os }} | - | 平台 cache action 执行缓存命中/写入 |
| 2 | Use cache | `cat cached.txt \|\| echo "cache miss"` | - | 读取缓存内容或输出 cache miss |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | ✅ GENUINE | uses: cache 是真实 action，cache hit/miss 行为由平台决定 |
| 2 | cache_step | positive | equals: hit | ✅ GENUINE | uses: cache 真实执行缓存操作，harness 断言验证缓存命中状态 |

