用例 ID:   REL-CACHEPERF-01-054
维度标签:   [reliability]
维度:      稳定性
优先级:    P2
溯源意图:  INTENT-REL-054
参照来源:  inputs/gitcode-spec/core-concepts/artifacts-and-cache.md
母意图:    —
标题:      缓存加速比——cache 命中 vs 未命中构建耗时对比

前置条件:
  - 仓库具备 cache 使用权限
  - fixture 仓库（with-cache）根目录含真实依赖的 package.json 与 lock 文件（含若干真实 npm 依赖，
    使 npm ci 冷安装耗时可测，建议冷安装 ≥60s 量级），YAML 层使用固定 cache key（第一轮 miss 后
    由 cache 插件保存，第二轮 hit）

操作步骤:
  1. 第一轮无 cache（key miss）记录安装耗时 T1
  2. 第二轮同一 key cache 命中记录耗时 T2

预期结果:
  - T2 ≤ 0.5 × T1
  - restore 耗时≤30s

验证点:
  - [正向] 加速比≥2x
  - [负向] cache 命中后不应仍执行完整安装

清理:      重置 fixture 仓库
