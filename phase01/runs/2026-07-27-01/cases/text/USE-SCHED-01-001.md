用例 ID:   USE-SCHED-01-001
维度标签:   ['usability', 'reliability']
维度:      usability
优先级:    P1
溯源意图:  INTENT-USE-047
参照来源:  inputs/gitcode-spec/writing-pipelines/configure-triggers.md; inputs/existing-cases/cases.md 问题 sheet TC-391 S3
母意图:    —
标题:      schedule 不触发时的可观测提示（判定方式：llm_assisted）

前置条件:
  - 隔离测试实例的 fixture 仓库配置了 schedule workflow
  - 存在 schedule 未触发的历史窗口（非默认分支或间隔过短场景）

操作步骤:
  1. 配置 schedule workflow 并制造不触发条件（如 cron 作用于非默认分支）
  2. 等待一个触发周期后检查 workflow 列表、运行列表与详情页
  3. 确认是否展示下次预计触发时间、跳过记录及原因

预期结果:
  schedule 未触发时平台不应完全静默；应展示下次预计触发时间；跳过的触发应留记录并附原因

验证点:
  - [负向] schedule 未触发时平台不应完全静默
  - [非功能] workflow 列表应显示下次预计触发时间字段
  - [非功能] 跳过的触发应有原因记录（非默认分支、间隔过短、cron 非法、平台故障）

清理:      重置 fixture 仓库
