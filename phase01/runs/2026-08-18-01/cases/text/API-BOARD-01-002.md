用例 ID:   API-BOARD-01-002
维度标签:   ['completeness']
维度:      completeness
优先级:    P2
溯源意图:  INTENT-ISSUE-006
母意图:    —
标题:      探测 Issues 列表 API 是否返回项目/看板字段

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api
  - 仓库中至少存在 1 个 Issue

操作步骤:
  1. 通过 API 获取 Issue 列表（per_page=1）
  2. 检查响应字段中是否包含 `project` 或 `project_column` 等看板相关字段

预期结果:
  - 如果字段存在 → 看板功能与 Issue 集成
  - 如果字段不存在 → 看板功能未与 Issue 集成或未实现

验证点:
  - [正向] API 返回 200
  - [正向] 响应包含 Issue 基础字段

清理:      none
