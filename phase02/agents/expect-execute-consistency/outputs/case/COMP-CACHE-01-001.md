# COMP-CACHE-01-001
- **标题**: cache hit 时恢复缓存内容正确
- **维度**: completeness
- **评级**: 部分不符

## 想测什么
cache hit 后正确恢复缓存内容。

## 做了什么
1. step `Cache test file`：`uses: cache` with key: cache-test-${{ runner.os }}
2. step `Use cache`：`cat cached.txt || echo "cache miss"`

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | success | COVERED | 真实 cache action 调用 + cat 文件操作 |
| 2 | cache_step | positive | equals: hit | UNVERIFIABLE | 目标不是 run_logs/run_status，cache 命中状态需平台 API 返回 |
