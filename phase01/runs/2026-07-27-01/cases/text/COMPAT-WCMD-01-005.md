```
用例 ID:   COMPAT-WCMD-01-005
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-042
参照来源:  inputs/github-reference/reference/workflow-commands.md; baseline/case-base-detail.md（TC-099 FAIL）
母意图:    —（变体自 COMPAT-WCMD-01-004：debug 命令的门控机制差异）
标题:      debug 命令默认可见性与 GitHub ACTIONS_STEP_DEBUG 门控差异

前置条件:
  - 仓库已启用 GitCode Action，未配置任何 debug 门控开关

操作步骤:
  1. 提交一个输出 ::debug:: 命令的 workflow
  2. 触发并观察该消息在日志中的可见性

预期结果:
  - 无门控配置时 ::debug:: 的默认可见性得到确定结论并文档化
  - 与 GitHub（默认隐藏，需 ACTIONS_STEP_DEBUG=true 且 RUNNER_DEBUG=1）的差异进入差异清单

验证点:
  - [正向] ::debug:: 默认可见性行为确定且被记录
  - [非功能] debug 门控机制差异进入迁移对照文档

清理:      重置 fixture 仓库
```
