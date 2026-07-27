用例 ID:   COMP-ISOLATION-01-003
维度标签:   [completeness, security]
维度:      完备性
优先级:    P1
溯源意图:  INTENT-COMP-025
参照来源:  runs/2026-07-27-01/intents/spec.md; inputs/gitcode-spec/runner-management/configuring-images-toolchains.md
母意图:    —
标题:      container.volumes 常规挂载在托管 Runner 的行为记录

前置条件:
  - 仓库已启用 AtomGit Action
  - 使用官方托管 Runner

操作步骤:
  1. 编写带 container.image 与常规 volumes 挂载（构建缓存目录）的 workflow
  2. 手动触发，逐字记录 container 与 volumes 的处理结果

预期结果:
  - 规格声明的能力边界被确定：container/volumes 是否被支持、挂载是否按声明工作，逐字记录事实并回写规格缺口清单

验证点:
  - [正向/记录] 常规 volumes 挂载是否按声明工作（逐字记录）
  - [非功能] credentials/env/options 组合下的行为一致性
  - [负向] volumes 声明不应被静默忽略而无任何提示

清理:      重置 fixture 仓库
