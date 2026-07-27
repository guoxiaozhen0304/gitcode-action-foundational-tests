用例 ID:   USE-DOC-01-003
维度标签:   ['usability']
维度:      usability
优先级:    P0
溯源意图:  INTENT-USE-033
参照来源:  inputs/gitcode-spec/syntax-reference/trigger-events.md
母意图:    —
标题:      trigger-events 每分钟 cron 示例与最短间隔 5 分钟声明自相矛盾

前置条件:
  - 隔离测试实例可提交 schedule workflow

操作步骤:
  1. 按 trigger-events.md 示例提交每分钟 cron 的 schedule workflow
  2. 记录平台校验/调度行为，与文档同页最短间隔 5 分钟声明比对

预期结果:
  文档示例与同页约束声明应一致；照抄示例不应得到与文档描述相反的结果

验证点:
  - [负向] 文档不应在最短间隔 5 分钟提示下方仍给出每分钟 cron 示例
  - [正向] 记录平台对该 cron 的接受/拒绝行为，与文档两处声明比对（任一不符即为文档缺陷）

清理:      重置 fixture 仓库
