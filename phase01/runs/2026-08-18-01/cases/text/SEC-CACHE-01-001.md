用例 ID:   SEC-CACHE-01-001
维度标签:   ['security']
维度:      security
优先级:    P1
溯源意图:  INTENT-SEC-009
母意图:    —
标题:      fork PR 保存的 cache 不得被主分支 workflow 命中

前置条件:
  - 仓库 fixture: with-fork-pr

操作步骤:
  1. fork PR 保存 cache 到 shared-cache-key
  2. 主分支 workflow 尝试恢复该 key
  3. 验证恢复失败或内容隔离

预期结果:
  1. 主分支 workflow 无法命中 fork PR 的 cache
  2. cache 恢复失败或内容不同

验证点:
  - [负向] 主分支不含 fork cache 内容
  - [正向] workflow 完成

清理:      fixture
