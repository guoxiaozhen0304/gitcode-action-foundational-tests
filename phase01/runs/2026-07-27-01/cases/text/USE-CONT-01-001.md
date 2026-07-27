用例 ID:   USE-CONT-01-001
维度标签:   ['usability', 'compatibility']
维度:      usability
优先级:    P1
溯源意图:  INTENT-USE-042
参照来源:  inputs/gitcode-spec/writing-pipelines/configure-jobs.md; inputs/existing-cases/cases.md 问题 sheet TC-273
母意图:    —
标题:      container.image 文档声明可用与实际可用性的一致性

前置条件:
  - 隔离测试实例可提交 workflow

操作步骤:
  1. 按文档示例提交含 container.image 的 workflow
  2. 观察平台行为（报错、忽略或实际生效）
  3. 检查文档是否标注该能力的可用状态

预期结果:
  文档出现的字段集合与实际平台可用字段集合应一致；未 GA 能力应显式标注

验证点:
  - [正向] 记录平台对 container.image 的实际处理行为
  - [负向] 文档不应把不可用的能力以正式语法呈现且不加状态标注
  - [非功能] 能力可用性状态应在字段说明旁显式标注

清理:      无
