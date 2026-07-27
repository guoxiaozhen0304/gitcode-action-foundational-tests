用例 ID:   COMP-EXPR-01-059
维度标签:   [completeness]
维度:      完备性
优先级:    P2
溯源意图:  INTENT-COMP-022
参照来源:  runs/2026-07-27-01/intents/spec.md; inputs/gitcode-spec/actions-market.md L1323/2511; syntax-reference/expressions.md
母意图:    —
标题:      未文档化函数 default() 的存在性与求值记录

前置条件:
  - 仓库已启用 AtomGit Action

操作步骤:
  1. 编写 job 级 if 引用 default() 的 workflow（含一个无条件 witness job）
  2. 保存并手动触发，逐字记录 default() 的处理（校验报错 / job 执行 / job 跳过）

预期结果:
  - default() 的存在性与返回语义被逐字记录；若不存在，引用处应报错而非静默求值

验证点:
  - [正向/记录] if 引用 default() 的实际求值结果（触发 / 跳过 / 校验报错）
  - [负向] 未文档化函数不应被静默求值为常量导致条件恒真或恒假且无提示
  - [非功能] 与手动触发表单（选择执行项）是否存在联动（证实/证伪）

清理:      重置 fixture 仓库
