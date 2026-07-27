用例 ID:   USE-UNKN-01-004
维度标签:   ['usability', 'compatibility']
维度:      usability
优先级:    P1
溯源意图:  INTENT-USE-037
参照来源:  inputs/workflow-samples/testorg/full_pr.yaml; inputs/gitcode-spec/writing-pipelines/workflow-file-location-structure.md; inputs/gitcode-spec/syntax-reference/trigger-events.md
母意图:    —
标题:      未文档化字段 select/manual_override/code-update/顶层 inputs 的文档集合 diff

前置条件:
  - 真实样本 testorg/full_pr.yaml 已就绪；文档版本为 2026-07-20 抓取版本

操作步骤:
  1. 抽取样本中全部 YAML key 集合
  2. 与文档语法参考列出的合法 key 集合做 diff
  3. 对样本独有且文档未提的 key 逐条登记

预期结果:
  平台实际支持的每个字段都应在语法参考中有条目；样本独有且文档未提的 key 数量应为 0

验证点:
  - [负向] 样本独有且文档未提的 key 每多 1 个即一条缺陷
  - [非功能] 文档应对顶层 inputs 与 on.workflow_dispatch.inputs 的关系给出说明

清理:      无
