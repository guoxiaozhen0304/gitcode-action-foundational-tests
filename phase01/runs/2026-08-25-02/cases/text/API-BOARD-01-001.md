用例 ID:   API-BOARD-01-001
维度标签:   ['completeness']
维度:      completeness
优先级:    P2
溯源意图:  INTENT-ISSUE-006
母意图:    —
标题:      探测仓库 Projects/看板 API 可用性

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 通过 API 获取仓库 Projects/看板列表
  2. 观察 API 响应状态码

预期结果:
  - 如果返回 200 且包含看板数据 → 功能可用
  - 如果返回 404 → 功能未实现

验证点:
  - [正向] API 返回 200 或 404
  - [正向] 响应体为数组格式

清理:      none
