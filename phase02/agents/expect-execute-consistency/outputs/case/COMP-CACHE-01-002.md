# COMP-CACHE-01-002
- **标题**: restore-keys 前缀匹配兜底生效
- **维度**: completeness
- **评级**: 完全不符

## 想测什么
精确 key 不匹配但 restore-keys 前缀匹配时成功恢复缓存。

## 做了什么
1. step `Cache test file`：`uses: cache` with key: cache-test-v2-${{ runner.os }}，restore-keys: cache-test-v1-${{ runner.os }}、cache-test-
2. step `Use cache`：`cat cached.txt || echo "cache miss"`

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | cache_step | positive | equals: restore_hit | UNVERIFIABLE | 目标不是 run_logs/run_status，需平台 API 返回 cache 状态 |
