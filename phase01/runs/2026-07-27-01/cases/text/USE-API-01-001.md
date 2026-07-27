用例 ID:   USE-API-01-001
维度标签:   ['usability', 'compatibility']
维度:      usability
优先级:    P2
溯源意图:  INTENT-USE-048
参照来源:  inputs/gitcode-spec/syntax-reference/trigger-events.md; inputs/existing-cases/cases.md 问题 sheet TC-064
母意图:    —
标题:      API 字段值与事件类型命名同一概念分裂的对照检查

前置条件:
  - fixture 仓库存在 PR；可通过 API 查询 PR 状态字段

操作步骤:
  1. 通过 API 查询 PR 状态字段返回值
  2. 与 trigger-events.md 事件类型命名集合做同概念对照
  3. 检查文档是否在两处给出命名对照表

预期结果:
  同一概念命名应在事件、API、文档三处一致；若已分裂，文档应在两处互相引用对照

验证点:
  - [负向] 同一概念在事件类型与 API 字段值上命名分裂且文档无对照表即不合格
  - [非功能] 触发事件页与 API 参考页应互相给出命名对照

清理:      无
