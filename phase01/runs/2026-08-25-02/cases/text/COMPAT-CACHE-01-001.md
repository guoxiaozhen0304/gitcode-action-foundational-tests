用例 ID:   COMPAT-CACHE-01-001
维度标签:   ['compatibility', 'security']
维度:      compatibility
优先级:    P1
溯源意图:  INTENT-COMPAT-025
母意图:    —
标题:      fork PR 写入的 cache 不得被目标仓库主分支读取

前置条件:
  - 仓库 fixture: with-fork-pr
  - 配置 secrets: ['CACHE_KEY']

操作步骤:
  1. 在 fork PR 中写入 cache
  2. 在目标仓库主分支 workflow 中尝试读取同名 cache
  3. 验证读取失败或内容隔离

预期结果:
  1. 目标仓库 workflow 无法读取 fork PR 产生的 cache
  2. cache key 命中失败或内容不同

验证点:
  - [负向] 目标仓库日志不含 fork cache 内容
  - [正向] workflow 运行完成

清理:      fixture
