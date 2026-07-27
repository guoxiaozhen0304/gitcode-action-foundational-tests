用例 ID:   USE-DOC-01-005
维度标签:   ['usability']
维度:      usability
优先级:    P0
溯源意图:  INTENT-USE-033
参照来源:  inputs/gitcode-spec/writing-pipelines/configure-steps.md
母意图:    —
标题:      configure-steps 的 shell 类型与命令语言不匹配示例照抄失败

前置条件:
  - 隔离测试实例可正常调度 workflow

操作步骤:
  1. 按 configure-steps.md 示例分别提交 shell bash 配 PowerShell 命令、shell python 配 shell 命令的 job
  2. 观察运行结果

预期结果:
  照抄文档示例应失败（shell 类型与命令语言不匹配），实证示例不可复刻

验证点:
  - [正向] 两个照抄示例的 job 运行失败即为示例缺陷实证
  - [负向] 文档示例中 shell 类型应与示例命令语言匹配

清理:      无
