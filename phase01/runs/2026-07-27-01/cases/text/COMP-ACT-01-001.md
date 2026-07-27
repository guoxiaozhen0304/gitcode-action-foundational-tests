用例 ID:   COMP-ACT-01-001
维度标签:   [completeness, compatibility]
维度:      完备性
优先级:    P2
溯源意图:  INTENT-COMP-026
参照来源:  runs/2026-07-27-01/intents/spec.md; inputs/gitcode-spec/action-development/top-level-fields.md L53
母意图:    —
标题:      action inputs.required 未传参时平台不自动校验

前置条件:
  - 仓库已启用 AtomGit Action
  - fixture 仓库含本地 action（action.yml 声明 required: true 的输入，脚本在对应环境变量为空时输出 REQ_INPUT_EMPTY）

操作步骤:
  1. 编写调用该本地 action 但不传 required 输入的 workflow
  2. 手动触发，观察是否在调度层失败，以及 action 内读到的环境变量值

预期结果:
  - 与文档声明一致：平台不因 required: true 缺参而失败；action 侧对应环境变量为空值

验证点:
  - [正向] workflow 不在调度层失败（运行可进入 action 执行）
  - [正向] action 内读取到该输入对应环境变量为空值
  - [非功能] 若平台后续加入校验，文档与行为需同步（回写差异声明）

清理:      重置 fixture 仓库
