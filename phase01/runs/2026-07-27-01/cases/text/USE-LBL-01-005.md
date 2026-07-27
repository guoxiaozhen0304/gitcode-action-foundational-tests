用例 ID:   USE-LBL-01-005
维度标签:   ['usability']
维度:      usability
优先级:    P1
溯源意图:  INTENT-USE-040
参照来源:  inputs/workflow-samples/cann/; inputs/workflow-samples/testorg/; inputs/workflow-samples/op-plugin/PR-pipeline_op-plugin.yml; inputs/gitcode-spec/runner-management/selecting-runner-labels.md
母意图:    —
标题:      runs-on 含资源池名写法的文档资源池清单 diff

前置条件:
  - 真实样本 cann/testorg/op-plugin 已就绪；文档版本为 2026-07-20 抓取版本

操作步骤:
  1. 从全部样本中抽取 runs-on 首段出现的资源池名集合
  2. 与 selecting-runner-labels.md 列出的资源池名集合做包含检查

预期结果:
  样本中出现的资源池名应全部被文档列出，并说明与 os/arch/flavor 的组合规则

验证点:
  - [负向] 样本中出现的资源池名不在文档清单内每 1 个即一条缺陷
  - [非功能] 资源池名清单、flavor 范围与组合规则应集中在 Runner 文档一节

清理:      无
