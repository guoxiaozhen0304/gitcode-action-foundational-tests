用例 ID:   USE-ENV-01-003
维度标签:   ['usability', 'compatibility']
维度:      usability
优先级:    P1
溯源意图:  INTENT-USE-044
参照来源:  inputs/gitcode-spec/action-development/runtime-environment-variables.md; inputs/gitcode-spec/running-pipelines/view-job-logs.md; inputs/existing-cases/cases.md 问题 sheet TC-206 TC-220
母意图:    —
标题:      ATOMGIT 系统环境变量实际注入集合与文档清单双向 diff

前置条件:
  - 隔离测试实例可正常调度 workflow

操作步骤:
  1. 在 step 中导出全部 ATOMGIT 前缀环境变量并排序
  2. 与 runtime-environment-variables.md 和 view-job-logs.md 两页清单分别做 diff
  3. 比对两页文档清单彼此是否一致

预期结果:
  文档列出的变量应在实际注入集合中全部存在；两页文档清单应一致或有唯一权威清单页

验证点:
  - [正向] 实际注入集合应被完整记录
  - [负向] 文档列出而实际未注入的变量每 1 个即一条缺陷
  - [非功能] 两页文档清单不一致即为缺陷；应有唯一权威清单页

清理:      无
