用例 ID:   COMP-UNKNOWN-01-005
维度标签:   [completeness]
维度:      完备性
优先级:    P2
溯源意图:  INTENT-COMP-031
参照来源:  runs/2026-07-27-01/intents/spec.md; inputs/workflow-samples/testorg/full_pr.yaml L24-86 (2026-07-22)
母意图:    —
标题:      顶层 inputs 与 manual_override 字段的实际处理记录

前置条件:
  - 仓库已启用 AtomGit Action

操作步骤:
  1. 编写顶层声明 inputs（含 default 与 manual_override）的 workflow
  2. 保存并手动触发，逐字记录顶层 inputs 的处理（校验报错 / 静默忽略 / 识别并注入 inputs 上下文）
  3. 观察 manual_override 对手动触发表单的实际影响

预期结果:
  - 顶层 inputs 的处理方式唯一确定：被识别则其与触发器 inputs 的合并/覆盖规则明确；被忽略则有校验提示；manual_override 语义（若生效）被确定

验证点:
  - [正向/记录] 顶层 inputs 的 default 是否注入 inputs 上下文（与 INTENT-COMP-020 互证）
  - [正向/记录] manual_override: true/false 对手动触发表单/参数覆盖的实际影响
  - [负向] 不应出现参数看似声明实则无效的静默忽略且无提示

清理:      重置 fixture 仓库
