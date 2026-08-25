用例 ID:   API-ORG-01-001
维度标签:   ['completeness', 'compatibility']
维度:      completeness
优先级:    P1
溯源意图:  INTENT-AUTH-003
母意图:    —
标题:      团队权限批量分配到仓库

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 获取团队有权访问的仓库列表
  2. 验证目标仓库在列表中
  3. 验证权限继承正确

预期结果:
  1. 仓库列表包含目标仓库
  2. 权限级别与团队设置一致

验证点:
  - [正向] 查询成功

清理:      none
