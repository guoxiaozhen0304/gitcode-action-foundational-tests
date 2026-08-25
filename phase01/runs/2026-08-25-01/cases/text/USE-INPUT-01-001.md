用例 ID:   USE-INPUT-01-001
维度标签:   ['usability']
维度:      usability
优先级:    P2
溯源意图:  INTENT-USE-007
母意图:    —
标题:      workflow_dispatch 缺少必填参数时 API 报错应指明参数名

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 对含必填 inputs 的 workflow 触发 dispatch 但不传参数
  2. 验证返回 422
  3. 验证错误信息指明缺少的参数名

预期结果:
  1. 返回 422
  2. 错误信息包含缺少的参数名称
  3. 提示参数来源为 workflow_dispatch inputs

验证点:
  - [正向] 返回 422
  - [正向] 错误提及 input

清理:      none
