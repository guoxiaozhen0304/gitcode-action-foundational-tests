用例 ID:   USE-NOTIF-01-001
维度标签:   ['usability']
维度:      usability
优先级:    P1
溯源意图:  INTENT-USE-008
母意图:    —
标题:      MR 触发 CI 失败后通知的时效性与信息完整性

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 创建 MR 触发 CI
  2. 等待 CI 失败
  3. 验证站内通知/邮件在合理时间内到达
  4. 验证通知包含失败 job 名称与链接

预期结果:
  1. 通知在 5 分钟内送达
  2. 通知包含 MR 标题、失败 job 名、查看链接

验证点:
  - [正向] 通知信息完整
  - [非功能] 通知延迟不超过 5 分钟

清理:      fixture
