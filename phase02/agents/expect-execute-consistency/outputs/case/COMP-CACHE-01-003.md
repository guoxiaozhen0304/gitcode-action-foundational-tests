# COMP-CACHE-01-003
- **标题**: fork PR 不应覆盖或污染主分支 cache
- **维度**: completeness
- **评级**: 完全不符

## 想测什么
fork PR 写入 cache 不应覆盖主分支 cache，主分支 cache 内容保持不变。

## 做了什么
1. step `Cache write`：`uses: cache` with path: cached.txt, key: shared-cache-key
2. step `Write poison`：`echo "poison" > cached.txt`

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | cache_pollution | negative | equals: main_cache_overwritten | UNVERIFIABLE | 目标不在 step 内，需跨运行的平台 API 数据对比 |
| 2 | main_cache_content | positive | equals: original | UNVERIFIABLE | 同上，需要外部平台 API 探测主分支 cache 内容 |
