# COMP-CACHE-01-003

- **标题**: fork PR 不应覆盖或污染主分支 cache
- **维度**: completeness
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**fork PR 不应覆盖或污染主分支 cache**
- 触发事件: `pull_request`
- 规格引用: INTENT-COMP-016

通过标准：
1. [负向] fork PR 不应覆盖主分支 cache —— 断言 cache_pollution != main_cache_overwritten
2. [正向] 主分支 cache 内容保持不变 —— 断言 main_cache_content=original

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Cache write | `uses: cache` with key: shared-cache-key | - | 尝试写入同名 cache key |
| 2 | Write poison | `echo "poison" > cached.txt` | - | 写入毒化内容到缓存目录 |

## 3. 触发与运行环境

| 触发事件 | pull_request |
| 触发身份 | untrusted_contributor |
| Repo 环境 | with-cache |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | cache_pollution | negative | equals: main_cache_overwritten | ✅ GENUINE | uses: cache 真实写入缓存，harness 级断言验证主分支 cache 未被污染 |
| 2 | main_cache_content | positive | equals: original | ✅ GENUINE | harness 级断言，workflow 已正确设置 fork PR 污染场景 |

