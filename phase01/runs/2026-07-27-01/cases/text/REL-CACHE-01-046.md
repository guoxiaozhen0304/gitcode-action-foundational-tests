用例 ID:   REL-CACHE-01-046
维度标签:   [reliability]
维度:      稳定性
优先级:    P1
溯源意图:  INTENT-REL-046
参照来源:  inputs/gitcode-spec/core-concepts/artifacts-and-cache.md
母意图:    —
标题:      缓存 LRU 淘汰压力——连续写入 10 个大缓存后最旧缓存应被正确淘汰

前置条件:
  - 仓库具备 cache 使用权限

操作步骤:
  1. 连续 10 次 dispatch 触发同一 workflow，cache key 取每次运行唯一值（YAML 层为 cache-运行序号），
     每次写入 100 MB 缓存，共产生 10 个不同 key
  2. 随后由 harness 分别以最新 key 与最旧 key 各发起一次读取性运行，观测命中状态

预期结果:
  - 最新写入的缓存 key 可命中
  - 最旧的缓存 key 变为 miss
  - 不应出现所有 10 个 key 同时命中

验证点:
  - [正向] 最新 key 状态=hit
  - [正向] 最旧 key 状态=miss
  - [负向] 不应所有 10 个 key 同时命中

清理:      无需特殊清理
