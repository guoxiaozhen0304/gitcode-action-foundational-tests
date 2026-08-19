用例 ID:   SEC-CACHE-01-002
维度标签:   ['security']
维度:      security
优先级:    P1
溯源意图:  INTENT-SEC-010
母意图:    —
标题:      不同仓库使用相同 cache key 时数据隔离

前置条件:
  - 仓库 fixture: repo-a

操作步骤:
  1. 在 repo-a 保存 cache 到 common-key-123
  2. 在 repo-b 尝试恢复相同 key
  3. 验证 repo-b 无法读取 repo-a 的数据

预期结果:
  1. repo-b 恢复 cache 失败或内容不同
  2. 跨仓库 cache 完全隔离

验证点:
  - [负向] repo-b 不含 repo-a 数据
  - [正向] workflow 完成

清理:      fixture
