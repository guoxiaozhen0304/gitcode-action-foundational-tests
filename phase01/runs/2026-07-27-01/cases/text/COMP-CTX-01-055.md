用例 ID:   COMP-CTX-01-055
维度标签:   [completeness, compatibility]
维度:      完备性
优先级:    P1
溯源意图:  INTENT-COMP-020
参照来源:  runs/2026-07-27-01/intents/spec.md; inputs/gitcode-spec/manually-trigger-pipeline.md
母意图:    —
标题:      workflow_dispatch 触发下 inputs 正常求值（回归保护）

前置条件:
  - 仓库已启用 AtomGit Action

操作步骤:
  1. 编写 on.workflow_dispatch.inputs 声明 pr_id（带默认值）的 workflow
  2. 手动触发（不覆盖参数），验证 inputs.pr_id 求值为声明的默认值

预期结果:
  - workflow_dispatch 下 inputs 正常求值，未传参时取声明默认值

验证点:
  - [正向] inputs.pr_id 求值为声明默认值 default-pr
  - [正向] 运行成功

清理:      重置 fixture 仓库
