用例 ID:   COMP-BOUND-01-084
维度标签:   [completeness]
维度:      完备性
优先级:    P1
溯源意图:  KEEP-TC-514~559
参照来源:  inputs/existing-cases/cases.md
母意图:    —
标题:      路径与分支过滤组合及否定模式边界验证

前置条件:
  - 仓库已启用 AtomGit Action

操作步骤:
  1. 配置 push 的 branches（main、feature/**、!feature/experimental）与 paths（src/**、!src/docs/**）组合过滤
  2. 推送匹配肯定模式且未被否定模式排除的提交，观察 workflow 触发并输出触发分支上下文
  3. 变体（排除侧观测）：推送到被否定模式排除的分支 feature/experimental，或仅修改被排除路径 src/docs/**，观察是否产生本 workflow 的新运行（预期不产生）

预期结果:
  - branches 和 paths 同时存在时为 AND 关系，否定模式 ! 需与肯定模式组合生效
  - 命中肯定模式且未被排除时触发 workflow，日志可见触发分支
  - 仅命中否定模式排除项时不触发 workflow

验证点:
  - [正向] branches + paths 组合过滤生效
  - [负向] 仅否定模式时不触发 workflow
  - [正向] 否定模式与肯定模式组合生效

清理:      重置 fixture 仓库
