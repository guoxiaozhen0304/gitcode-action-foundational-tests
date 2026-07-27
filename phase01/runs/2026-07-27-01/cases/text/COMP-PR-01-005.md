用例 ID:   COMP-PR-01-005
维度标签:   [completeness]
维度:      完备性
优先级:    P1
溯源意图:  INTENT-COMP-033
参照来源:  runs/2026-07-27-01/intents/spec.md; inputs/workflow-samples/testorg (2026-07-22)
母意图:    COMP-PR-01-004
标题:      源分支更新后 pre-merge ref 指向刷新验证

前置条件:
  - 仓库已启用 AtomGit Action
  - fixture 仓库存在开放 PR（编号固定为 1）；夹具支持向 PR 源分支推送新提交并再次触发运行

操作步骤:
  1. 首次触发运行，checkout 该 ref 并记录 HEAD sha
  2. 向 PR 源分支推送新提交，再次触发运行并记录 HEAD sha
  3. 对比两次 sha；PR 合并/关闭后再次解析该 ref，记录行为（报错 / 保留快照）

预期结果:
  - 源分支新增提交后该 ref 指向刷新（两次 HEAD sha 不同）；PR 关闭后的解析行为被确定并逐字记录

验证点:
  - [正向] 源分支更新后 ref 内容刷新（sha 变化）
  - [非功能] PR 合并/关闭后再次解析该 ref 的行为逐字记录
  - [负向] 不应源分支已更新但 ref 仍为陈旧合并结果而无标识

清理:      重置 fixture 仓库（含关闭夹具 PR）
