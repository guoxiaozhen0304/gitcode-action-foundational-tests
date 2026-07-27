用例 ID:   COMP-RUNNER-01-081
维度标签:   [completeness, compatibility]
维度:      完备性
优先级:    P1
溯源意图:  INTENT-COMP-029
参照来源:  runs/2026-07-27-01/intents/spec.md; inputs/gitcode-spec/actions-market.md L215; inputs/workflow-samples/testorg (2026-07-22)
母意图:    —
标题:      四段式 runs-on（codearts-hosted 首段）调度行为裁定

前置条件:
  - 仓库已启用 AtomGit Action
  - 环境中存在四段式标签可匹配的托管 Runner 资源池

操作步骤:
  1. 编写 runs-on 为四段式（codearts-hosted 首段）的 workflow
  2. 手动触发，逐字记录实际调度到的 Runner 身份
  3. 与三段式调度行为（复用上轮 INTENT-COMP-010 证据）对比

预期结果:
  - 四段式的匹配语义与首段（疑似资源池标识）语义被确定；不应语法被接受但调度到与标签声明不符的 Runner 且无提示

验证点:
  - [正向/记录] 四段式的调度结果与首段语义逐字记录（实际 Runner 身份）
  - [正向] 三段式调度行为回归（复用基底证据，不重复造数）
  - [负向] 任一形式被接受后不应调度到与标签声明不符的 Runner 且无提示

清理:      重置 fixture 仓库
