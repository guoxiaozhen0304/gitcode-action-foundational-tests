用例 ID:   REL-RERUN-01-001
维度标签:   ['reliability']
维度:      reliability
优先级:    P1
溯源意图:  INTENT-REL-025
母意图:    —
标题:      连续请求第 4 次 rerun 观察拒绝行为

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 对同一 run 连续请求 4 次 rerun
  2. 验证第 4 次被拒绝
  3. 验证返回适当错误码与提示

预期结果:
  1. 第 4 次 rerun 请求被拒绝
  2. 返回 403/422/429

验证点:
  - [负向] 第 4 次被拒绝
  - [正向] 错误信息提及 rerun 限制

清理:      none
