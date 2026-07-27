用例 ID:   USE-ONBD-01-002
维度标签:   ['usability']
维度:      usability
优先级:    P0
溯源意图:  INTENT-USE-050
参照来源:  inputs/gitcode-spec/01-quick-start.md
母意图:    —
标题:      quick-start 示例提交后运行结果可见性检查点

前置条件:
  - 隔离测试实例的 fixture 仓库已开通 Action 功能

操作步骤:
  1. 按 quick-start 示例创建 workflow 文件并 push 到默认分支
  2. 在文档声称的位置查看运行列表
  3. 确认运行条目出现且结果与文档描述一致

预期结果:
  push 后运行条目应在运行列表可见，状态与文档成功结果描述一致

验证点:
  - [正向] workflow 运行成功
  - [正向] 运行条目在运行列表可见（可经 API 确定性判定）
  - [非功能] 从 push 到条目可见的时延应在分钟级

清理:      重置 fixture 仓库
