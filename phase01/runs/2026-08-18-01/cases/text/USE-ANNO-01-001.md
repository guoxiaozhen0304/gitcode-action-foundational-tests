用例 ID:   USE-ANNO-01-001
维度标签:   ['usability']
维度:      usability
优先级:    P1
溯源意图:  INTENT-USE-016
母意图:    —
标题:      workflow 命令 ::error:: / ::warning:: 注解在 UI 中的可读性与定位能力

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 触发含 error/warning 注解的 workflow
  2. 在 UI 中查看运行结果页
  3. 验证注解显示位置、文件链接、行号

预期结果:
  1. UI 中显示 error 和 warning 注解
  2. 注解包含文件路径与行号
  3. 点击可跳转到对应位置

验证点:
  - [正向] UI 注解可读
  - [正向] workflow 完成

清理:      fixture
