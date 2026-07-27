用例 ID:   USE-ACT-01-003
维度标签:   ['usability']
维度:      usability
优先级:    P1
溯源意图:  INTENT-USE-052
参照来源:  inputs/gitcode-spec/writing-pipelines/using-actions.md; inputs/gitcode-spec/actions-market.md; inputs/gitcode-spec/COMPAT-NOTES.md
母意图:    —
标题:      官方短名 Action 清单与 actions-market 插件目录的映射一致性

前置条件:
  - 文档版本为 2026-07-20 抓取版本；actions-market.md 49 插件目录已就绪

操作步骤:
  1. 抽取 using-actions.md 与 COMPAT-NOTES 中提到的官方短名集合
  2. 与 actions-market.md 插件名集合建立映射
  3. 检查文档是否给出短名与市场名的对照表及官方/社区标识

预期结果:
  文档应给出官方短名与市场插件名的完整对照表；市场页应标识官方维护属性；大小写与连字符规则应明示

验证点:
  - [负向] 文档短名在市场目录找不到对应项或映射关系文档未明示即不合格
  - [非功能] 市场页应标识官方与社区维护者属性

清理:      无
