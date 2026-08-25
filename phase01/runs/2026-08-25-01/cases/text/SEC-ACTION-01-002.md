用例 ID:   SEC-ACTION-01-002
维度标签:   ['security']
维度:      security
优先级:    P1
溯源意图:  INTENT-SEC-015
母意图:    —
标题:      本地 action 使用路径遍历引用仓库外路径应被拒绝

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 引用包含路径遍历的本地 action
  2. 验证平台拒绝该引用
  3. 验证后续 step 不执行

预期结果:
  1. 路径遍历的 action 引用被拒绝
  2. 返回清晰的校验错误

验证点:
  - [负向] workflow 不应成功完成
  - [正向] 错误提及路径问题
  - [负向] 后续 step 未执行

清理:      none
