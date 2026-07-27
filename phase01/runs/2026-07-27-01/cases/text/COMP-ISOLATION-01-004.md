用例 ID:   COMP-ISOLATION-01-004
维度标签:   [completeness, security]
维度:      完备性
优先级:    P1
溯源意图:  INTENT-COMP-025
参照来源:  runs/2026-07-27-01/intents/spec.md; inputs/gitcode-spec/runner-management/configuring-images-toolchains.md; core-concepts/runner-and-environment.md
母意图:    —
标题:      托管 Runner 上特权 options 与敏感路径挂载的边界核查

前置条件:
  - 仓库已启用 AtomGit Action
  - 使用官方托管 Runner
  - 测试实例独立可重置

操作步骤:
  1. 编写 container.options 含提权类参数（--privileged、--network=host）且 volumes 挂载宿主根路径的 workflow
  2. 手动触发，逐字记录平台拒绝/放行行为及容器内实际可达的宿主面

预期结果:
  - 托管 Runner 不应能无限制挂载宿主敏感路径或传入提权类 docker options；实际拒绝/放行行为逐字记录，若放行则回写风险登记册

验证点:
  - [负向] 不应能读取宿主敏感路径内容（记录实际拒绝/放行）
  - [负向] 提权类 docker options 不应被无过滤放行
  - [非功能] 记录拒绝时的报错信息或放行时的实际访问面

清理:      重置 fixture 仓库
