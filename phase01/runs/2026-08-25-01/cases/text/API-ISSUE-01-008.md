用例 ID:   API-ISSUE-01-008
维度标签:   ['completeness']
维度:      completeness
优先级:    P2
溯源意图:  INTENT-ISSUE-005
母意图:    —
标题:      探测 Issue 创建 API 是否支持模板参数

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 通过 API 创建 Issue，传入 `template` 参数
  2. 观察 API 响应

预期结果:
  - 如果支持模板参数：创建成功（201）且 body 按模板填充
  - 如果不支持模板参数：返回 422 参数无效或忽略该参数仍创建成功

验证点:
  - [正向] API 返回 201 或 422
  - [正向] 响应包含 Issue number

清理:      fixture
