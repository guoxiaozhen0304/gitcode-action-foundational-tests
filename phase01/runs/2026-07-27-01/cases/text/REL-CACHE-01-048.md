用例 ID:   REL-CACHE-01-048
维度标签:   [reliability]
维度:      稳定性
优先级:    P2
溯源意图:  INTENT-REL-079
参照来源:  platform-config/README.md（max_cache_size 未声明）; testing-focus.md §8
母意图:    —
标题:      cache 同 key 并发写一致性——3 方并行写同一 key 不得产生混合/损坏内容

前置条件:
  - fixture 仓库可使用 cache 插件
  - 可触发 3 个并行 job 同时写同一 cache key

操作步骤:
  1. 3 个并行 job 各自写入不同标记内容到同一 cache key
  2. 全部完成后，由下游 job 读回该 key 内容并校验归属
  3. 观察最终内容是某一方完整胜出、明确冲突报错，还是混合/截断态

预期结果:
  - 最终 cache 内容确定：归属于单一写入方且完整，或平台明确冲突报错
  - 读回内容可校验、可归属

验证点:
  - [正向] 读回内容完整且可归属单一写入方（或收到明确冲突错误）
  - [负向] 读回内容不应为多个写入方的混合态/截断态（发现则升 P1）
  - [非功能] 并发写语义（last-writer-wins / 冲突报错）实测结论记录完整

清理:      重置 fixture 仓库（清理测试 cache）
