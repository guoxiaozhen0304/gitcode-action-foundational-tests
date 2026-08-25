用例 ID:   SEC-PRTARGET-01-003
维度标签:   ['security']
维度:      security
优先级:    P0
溯源意图:  INTENT-SEC-008
母意图:    —
标题:      pull_request_target 的 workflow 文件来源校验

前置条件:
  - 仓库 fixture: with-fork-pr

操作步骤:
  1. 验证 pull_request_target 触发时，workflow 文件路径与来源
  2. 确认 atomgit.workflow 指向目标仓库

预期结果:
  1. workflow 文件来自目标仓库 base 分支
  2. atomgit.base_ref 为 main

验证点:
  - [正向] base_ref 正确
  - [正向] workflow 完成

清理:      fixture
