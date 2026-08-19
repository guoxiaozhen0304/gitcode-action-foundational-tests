用例 ID:   REL-CACH-01-001
维度标签:   ['reliability']
维度:      reliability
优先级:    P1
溯源意图:  INTENT-REL-021
母意图:    —
标题:      写入 500MB cache 观察上限与 LRU 淘汰

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 生成 500MB 缓存数据并保存
  2. 验证保存成功或给出清晰的超限报错
  3. 再次运行验证缓存命中或 LRU 淘汰

预期结果:
  1. 缓存保存成功或报错清晰
  2. 若超限则后续缓存可正常写入

验证点:
  - [正向] workflow 完成
  - [正向] 日志包含缓存操作结果

清理:      fixture
