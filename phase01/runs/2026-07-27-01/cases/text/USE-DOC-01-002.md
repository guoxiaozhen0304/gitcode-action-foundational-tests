用例 ID:   USE-DOC-01-002
维度标签:   ['usability']
维度:      usability
优先级:    P0
溯源意图:  INTENT-USE-032
参照来源:  inputs/gitcode-spec/00-overview.md; inputs/gitcode-spec/writing-pipelines/workflow-file-location-structure.md; inputs/gitcode-spec/running-pipelines/view-run-results.md; inputs/workflow-samples/cann/ops-nn_action.yml
母意图:    —
标题:      stages 与 stages 内 jobs 字段语法跨文档四种形态互相矛盾的扫描

前置条件:
  - 文档版本为 2026-07-20 抓取版本；真实样本 cann/ops-nn_action.yml 已就绪

操作步骤:
  1. 对 gitcode-spec 全文检索 stages: 定义，归纳 list 形态与 map 形态
  2. 对 stages 内 jobs 归纳 list-of-name-map 与 map-by-id 两种形态
  3. 检查同一文档内是否自相矛盾（workflow-file-location-structure.md 同页两种形态）

预期结果:
  文档应给出 stages 与 jobs 的唯一权威形态定义，或显式声明等价形态；同页不应自相矛盾

验证点:
  - [负向] 同一字段在同一页面给出两种形态而不加说明即为缺陷
  - [负向] 全文档形态组合数大于 1 且无集中等价说明即为缺陷
  - [非功能] 工作流文件位置与基本结构页应给出 stages 单一权威形态定义

清理:      无
