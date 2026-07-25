# REL-CACHE-01-046

- 标题: 缓存 LRU 淘汰压力——连续写入 10 个大缓存后最旧缓存应被正确淘汰
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: 缓存 LRU 淘汰压力——连续写入 10 个大缓存后最旧缓存应被正确淘汰

- [正向] 最新 key 状态=hit
- [正向] 最旧 key 状态=miss
- [负向] 不应所有 10 个 key 同时命中

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | save cache | uses: cache | Y |
| 2 | generate cache data | mkdir -p cache_data dd if=/dev/urandom of=cache_data/data.bin bs=1M count=100 | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | latest_cache_status | hit |
| positive | oldest_cache_status | miss |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 最新 key 状态=hit | COVERED | 1 real steps, assertions present |
| [正向] 最旧 key 状态=miss | COVERED | 1 real steps, assertions present |
| [负向] 不应所有 10 个 key 同时命中 | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [负向] 不应所有 10 个 key 同时命中: single dispatch cannot prove negative

---
