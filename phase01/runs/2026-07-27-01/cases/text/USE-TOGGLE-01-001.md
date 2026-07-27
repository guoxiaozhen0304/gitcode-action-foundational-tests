用例 ID:   USE-TOGGLE-01-001
维度标签:   ['usability', 'security']
维度:      usability
优先级:    P1
溯源意图:  INTENT-USE-053
参照来源:  inputs/gitcode-spec/syntax-reference/workflow-commands.md; inputs/gitcode-spec/writing-pipelines/using-script-commands.md; inputs/existing-cases/cases.md 问题 sheet TC-220
母意图:    —
标题:      隐藏安全开关 ATOMGIT_ACTIONS_ALLOW_UNSECURE_COMMANDS 默认值与文档缺失

前置条件:
  - 隔离测试实例可正常调度 workflow

操作步骤:
  1. 在 step 中读取该开关环境变量的实际默认值
  2. 检查 workflow-commands.md 与 using-script-commands.md 是否列出该开关及其默认值与安全影响

预期结果:
  所有影响安全行为的开关应在语法参考集中列出名称、默认值与安全影响；文档不应缺失

验证点:
  - [正向] 记录开关的实际默认值
  - [负向] 平台不应存在影响安全行为但文档未提的开关
  - [非功能] 开关清单应标注每个开关的安全影响与默认值

清理:      无
