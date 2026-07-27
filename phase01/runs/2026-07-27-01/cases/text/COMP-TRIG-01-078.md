用例 ID:   COMP-TRIG-01-078
维度标签:   [completeness]
维度:      完备性
优先级:    P1
溯源意图:  KEEP-TC-423
参照来源:  inputs/existing-cases/cases.md
母意图:    —
标题:      多事件组合与分支路径过滤验证

前置条件:
  - 仓库已启用 AtomGit Action

操作步骤:
  1. 配置 push 和 workflow_dispatch 多事件组合，push 带 branches 与 paths 过滤
  2. 推送匹配分支与路径的提交，观察触发并输出触发事件上下文
  3. 变体：在同一 on.push 下同时配置 paths 与 paths-ignore 提交，观察平台行为（拒绝或忽略其一）

预期结果:
  - 同一 workflow 可配置多个事件，push 的 branches 和 paths 同时过滤
  - paths 与 paths-ignore 互斥：共存时平台拒绝该 workflow 或忽略其中之一，不应两者同时静默生效

验证点:
  - [正向] 多事件组合通过校验
  - [正向] push 到匹配分支且路径匹配时触发
  - [负向] paths 与 paths-ignore 同时存在时平台拒绝或只保留 paths

清理:      重置 fixture 仓库
