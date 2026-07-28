# REL-CACHE-01-046
- **标题**: 缓存 LRU 淘汰压力——连续写入 10 个大缓存后最旧缓存应被正确淘汰
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
连续写 10 个 100MB 缓存后最新 key hit、最旧 key miss、非全部命中。

## 做了什么
单 workflow 含 cache save step，key 使用 `cache-${{ atomgit.run_number }}`，生成 100MB 缓存数据。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | latest_cache_status | positive | equals "hit" | MISSING | workflow 仅有 save step，无读回验证；latest/oldest 命中状态需 harness 通过后续读取性运行判定，YAML 内无对应步骤 |
| 2 | oldest_cache_status | positive | equals "miss" | MISSING | 同上，需 harness 侧再次读取最旧 key |
