用例 ID:   USE-DISP-01-003
维度标签:   ['usability']
维度:      usability
优先级:    P1
溯源意图:  INTENT-USE-051
参照来源:  inputs/gitcode-spec/writing-pipelines/configure-triggers.md; inputs/workflow-samples/testorg/full_pr.yaml
母意图:    —
标题:      workflow_dispatch 手动触发 UI 与 YAML inputs 定义的集合一致性

前置条件:
  - fixture 仓库提交了含 5 个 inputs（含 description、required、default）的 workflow

操作步骤:
  1. 在 YAML 定义 5 个 inputs 并提交
  2. 打开手动触发 UI，枚举实际渲染的表单字段集合
  3. 与 YAML inputs 集合做 diff

预期结果:
  UI 应逐一渲染 YAML 定义的 inputs；required 标星、default 预填、description 呈现；不多渲染不漏渲染

验证点:
  - [正向] UI 渲染字段集合与 YAML inputs 集合一致
  - [负向] UI 不应渲染 YAML 未定义字段，不应漏渲染已定义字段
  - [非功能] required、default、description 在 UI 均有对应呈现；manual_override 为 false 的字段应锁死只读

清理:      无
