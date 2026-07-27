# REL-CACHE-01-046
- **标题**: 缓存 LRU 淘汰压力——连续写入 10 个大缓存后最旧缓存应被正确淘汰
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**缓存 LRU 淘汰——连续写入 10 个大缓存后最旧缓存应被正确淘汰**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-046
通过标准：
1. 最新 key 状态=hit
2. 最旧 key 状态=miss
3. 不所有 10 个 key 同时命中

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | save cache | `uses: cache` key=cache-${{ matrix.index }} | - | action 输出 cache hit/miss 状态 |
| 2 | generate cache data | `mkdir -p cache_data && dd if=/dev/urandom of=cache_data/data.bin bs=1M count=100` | - | 100MB 缓存数据 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | latest_cache_status = hit | positive | - | ✅ GENUINE | uses cache action 产生真实 cache hit/miss 状态 |
| 2 | oldest_cache_status = miss | positive | - | ✅ GENUINE | 同上，cache action 真实行为 |
---
