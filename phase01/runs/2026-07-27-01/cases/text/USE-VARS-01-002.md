用例 ID:   USE-VARS-01-002
维度标签:   ['usability', 'compatibility']
维度:      usability
优先级:    P1
溯源意图:  INTENT-USE-038
参照来源:  inputs/workflow-samples/testorg/full_pr.yaml; inputs/gitcode-spec/core-concepts/variables-secrets-context-expressions.md; inputs/gitcode-spec/syntax-reference/context.md
母意图:    —
标题:      变量插值双语法与 atomgit 属性名的文档清单 diff 及求值探测

前置条件:
  - 隔离测试实例可正常调度 workflow；真实样本已就绪

操作步骤:
  1. 提交含美元单括号遗留插值与标准双花括号插值的探针 workflow
  2. 观察各语法是否被求值
  3. 对样本插值语法与属性名集合和文档清单做 diff

预期结果:
  文档应列出平台支持的全部插值语法与 atomgit 上下文合法属性清单；样本出现而文档未列的数量应为 0

验证点:
  - [正向] 记录遗留插值语法是否被求值
  - [负向] 若遗留语法已废弃，平台应在解析时给出 deprecation 警告而非静默
  - [非功能] atomgit 上下文属性应有完整且大小写明确的官方列表

清理:      无
