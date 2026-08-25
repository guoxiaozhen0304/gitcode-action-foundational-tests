用例 ID:   REL-GIT-01-001
维度标签:   ['reliability']
维度:      reliability
优先级:    P1
溯源意图:  INTENT-REL-010
母意图:    —
标题:      1GB+ 仓库克隆的耗时与资源稳定性

前置条件:
  - 仓库 fixture: large-repo-1gb

操作步骤:
  1. 克隆 1GB+ 仓库
  2. 记录耗时
  3. 验证本地仓库完整且无损坏

预期结果:
  1. clone 成功
  2. 耗时在合理范围内（<10 分钟）
  3. 仓库大小 >= 1GB

验证点:
  - [正向] clone 成功
  - [非功能] 克隆耗时不超过 10 分钟

清理:      fixture
