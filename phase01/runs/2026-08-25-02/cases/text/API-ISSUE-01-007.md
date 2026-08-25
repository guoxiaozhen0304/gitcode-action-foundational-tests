用例 ID:   API-ISSUE-01-007
维度标签:   ['completeness']
维度:      completeness
优先级:    P2
溯源意图:  INTENT-ISSUE-005
母意图:    —
标题:      探测仓库 Issue 模板目录存在性

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 通过 API 获取仓库 `.gitcode` 目录内容
  2. 检查响应中是否包含 `ISSUE_TEMPLATE` 目录项

预期结果:
  - 如果返回 200 且包含 `ISSUE_TEMPLATE` → 功能可用
  - 如果返回 200 但不包含 → 功能未配置
  - 如果返回 404 → 目录不存在

验证点:
  - [正向] API 返回 200 或 404
  - [正向] 响应体包含目录项列表

清理:      none
