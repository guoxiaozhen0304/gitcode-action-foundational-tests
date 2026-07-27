用例 ID:   REL-CACHE-01-047
维度标签:   [reliability]
维度:      稳定性
优先级:    P2
溯源意图:  INTENT-REL-079
参照来源:  platform-config/README.md（max_cache_size 未声明）
母意图:    —
标题:      cache 容量上限探测——500MB/1GB/2GB 单 cache 的接受/拒绝语义

前置条件:
  - fixture 仓库可使用 cache 插件读写缓存
  - 平台 max_cache_size 未公开（探测型用例）

操作步骤:
  1. 分别以 500MB/1GB/2GB 三档体积写入独立 key 的 cache
  2. 逐档观察平台行为：接受并完整保存，或明确拒绝（含上限值）
  3. 写后读回校验内容完整性（MD5），记录实测上限并回写 platform-config

预期结果:
  - 每档行为确定可归因：接受（读回 MD5 一致）或明确拒绝（错误含上限值）
  - 实测单 cache 上限被记录

验证点:
  - [正向] 接受的档位读回内容完整（MD5 一致）；拒绝的档位错误信息含上限值
  - [负向] 不应「保存报成功但读回内容截断/损坏」的静默损坏（发现则升 P1）
  - [非功能] 实测 cache 上限值记录完整，可回写 platform-config

清理:      重置 fixture 仓库（清理测试 cache）
