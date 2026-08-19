用例 ID:   API-BRANCH-01-003
维度标签:   ['completeness', 'security']
维度:      completeness
优先级:    P0
溯源意图:  INTENT-GIT-002
母意图:    —
标题:      保护分支要求 CI 通过才可合并

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api
  - 分支保护: main

操作步骤:
  1. 设置 main 分支要求 CI 通过
  2. 创建 MR 到 main
  3. 验证合并按钮在 CI 失败时不可点击或被拒绝

预期结果:
  1. 保护规则生效
  2. CI 未通过时合并被阻止

验证点:
  - [正向] 规则设置成功
  - [负向] CI 失败时不可合并

清理:      fixture
