用例 ID:   API-BRANCH-01-002
维度标签:   ['completeness', 'security']
维度:      completeness
优先级:    P0
溯源意图:  INTENT-GIT-002
母意图:    —
标题:      设置保护分支规则并验证强制推送被拒绝

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api
  - 分支保护: main

操作步骤:
  1. 通过 API 设置 main 分支保护规则（禁止 force push）
  2. 尝试强制推送
  3. 验证返回 403 或推送被拒绝

预期结果:
  1. 保护分支规则设置成功
  2. 强制推送被拒绝
  3. 非允许角色推送被拒绝

验证点:
  - [正向] 保护规则设置成功
  - [负向] 强制推送被拒绝

清理:      fixture
