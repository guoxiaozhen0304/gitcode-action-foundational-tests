用例 ID:   USE-ONBD-01-001
维度标签:   ['usability']
维度:      usability
优先级:    P0
溯源意图:  INTENT-USE-050
参照来源:  inputs/gitcode-spec/00-overview.md; inputs/gitcode-spec/01-quick-start.md; inputs/gitcode-spec/writing-pipelines/workflow-file-location-structure.md; inputs/business-context/README.md
母意图:    —
标题:      新手快速开始路径端到端可复刻走查（判定方式：llm_assisted）

前置条件:
  - 一名无 GitCode 经验的评测者（或 LLM 模拟新手）
  - 一个全新的测试账号与空仓库

操作步骤:
  1. 按 00-overview 到 01-quick-start 顺序逐步操作
  2. 每一步记录是否有可观察验证点、是否卡壳
  3. 记录全部卡壳点（开通入口、仓库内容要求、push 后查看位置等）

预期结果:
  新手应能在 30 分钟内看到第一个成功运行；每一步有可验证检查点；卡壳点数量应为 0

验证点:
  - [正向] 每步有可观察验证点
  - [负向] 不应存在文档假设用户知道但新手不知道的隐式前提（如 Action 功能开通步骤）
  - [非功能] 全流程应在 30 分钟内可完成

清理:      无
