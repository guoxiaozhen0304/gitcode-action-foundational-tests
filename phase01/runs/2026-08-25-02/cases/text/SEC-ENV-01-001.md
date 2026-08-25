用例 ID:   SEC-ENV-01-001
维度标签:   ['security']
维度:      security
优先级:    P0
溯源意图:  INTENT-SEC-006
母意图:    —
标题:      通过 ATOMGIT_ENV 写入污染数据不得破坏后续步骤执行上下文

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 第一步向 ATOMGIT_ENV 写入污染数据（覆盖 PATH）
  2. 第二步验证 PATH 未被永久破坏
  3. 验证 MALICIOUS 若被注入也不影响系统变量

预期结果:
  1. PATH 保持原始系统路径
  2. MALICIOUS 若存在也仅为当前 job 级
  3. 无步骤间上下文破坏

验证点:
  - [正向] PATH 仍含系统路径
  - [正向] workflow 正常完成

清理:      fixture
