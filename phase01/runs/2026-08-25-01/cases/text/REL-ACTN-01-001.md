用例 ID:   REL-ACTN-01-001
维度标签:   ['reliability']
维度:      reliability
优先级:    P1
溯源意图:  INTENT-REL-017
母意图:    —
标题:      依赖 action 不可用时 workflow 失败与报错清晰度

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 引用不存在的 action
  2. 触发 workflow
  3. 验证失败模式与报错清晰度

预期结果:
  1. workflow 在解析或执行阶段失败
  2. 错误信息指明 action 不存在或无法获取
  3. 后续 step 被跳过

验证点:
  - [正向] workflow 失败
  - [正向] 错误提及 action 名称
  - [负向] 后续 step 未执行

清理:      fixture
