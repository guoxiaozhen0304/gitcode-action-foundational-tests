用例 ID:   USE-ACT-01-004
维度标签:   ['usability']
维度:      usability
优先级:    P1
溯源意图:  INTENT-USE-052
参照来源:  inputs/gitcode-spec/writing-pipelines/using-actions.md; inputs/gitcode-spec/actions-market.md
母意图:    —
标题:      文档短名与市场名两种写法解析一致性验证

前置条件:
  - 隔离测试实例可正常调度 workflow

操作步骤:
  1. 分别用文档短名与市场目录名引用同一类插件并提交
  2. 观察两种写法是否解析到同一插件

预期结果:
  若两种写法同物，平台应解析到同一插件；解析结果回写文档映射判定

验证点:
  - [正向] 记录两种写法的解析结果是否一致
  - [负向] 两种写法指向不同插件或其一报错而文档未说明即不合格

清理:      无
