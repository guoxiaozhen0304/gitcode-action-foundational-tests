```
用例 ID:   COMPAT-SCHEDULE-01-004
维度标签:   [compatibility, reliability]
维度:      兼容性
优先级:    P2
溯源意图:  INTENT-COMPAT-051
参照来源:  inputs/github-reference/reference/events.md; inputs/gitcode-spec/syntax-reference/trigger-events.md; baseline/case-base-detail.md（TC-563 FAIL）
母意图:    —（与 INTENT-COMPAT-013 互补：013 为 timezone，本条为生命周期与延迟语义；schedule 主题簇关联 REL-085、USE-047）
标题:      schedule 生命周期语义（自动停用策略与触发延迟可观测性）确认

前置条件:
  - fixture 仓库配置一个最短间隔的定时 workflow

操作步骤:
  1. 查阅 GitCode 官方文档确认是否存在 schedule 自动停用/保活策略（对照 GitHub 公开仓库 60 天无活动自动停用）
  2. 观察定时触发的计划时间与实际入队时间，评估延迟可观测性

预期结果:
  - GitCode 的 schedule 自动停用/保活策略得到确定结论并文档化；不存在未文档化的静默停用
  - 触发延迟可观测（计划时间与实际入队时间可见）；TC-563 修复后复验

验证点:
  - [正向] 自动停用策略有无得到确定结论
  - [负向] 不应存在未文档化的静默停用
  - [正向] 触发延迟可观测（计划 vs 实际入队时间）
  - [非功能] 结论文档化并回写 Parity Matrix

清理:      重置 fixture 仓库
```
