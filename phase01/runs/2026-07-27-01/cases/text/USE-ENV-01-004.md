用例 ID:   USE-ENV-01-004
维度标签:   ['usability', 'compatibility']
维度:      usability
优先级:    P0
溯源意图:  INTENT-USE-046
参照来源:  inputs/gitcode-spec/writing-pipelines/configure-jobs.md; inputs/gitcode-spec/writing-pipelines/using-script-commands.md; inputs/existing-cases/cases.md 问题 sheet TC-533
母意图:    —
标题:      job env 在 shell 层与表达式层取值一致性（文档承诺兑现验证）

前置条件:
  - 隔离测试实例可正常调度 workflow

操作步骤:
  1. 在 job 级声明 env，在同一 job 的 step 中分别以 shell 变量与表达式两种方式读取并打印
  2. 比对两层取值是否一致

预期结果:
  文档承诺 job env 对该 job 内所有 step 可见；shell 层与表达式层取值应一致；不一致即文档承诺未兑现

验证点:
  - [正向] 表达式层应取到 job env 值
  - [正向] shell 层应取到 job env 值（文档明文承诺）；取不到即实证文档承诺未兑现
  - [非功能] 平台行为修复前文档应给出显式 workaround

清理:      无
