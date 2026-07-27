用例 ID:   COMP-TRIG-01-080
维度标签:   [completeness, compatibility]
维度:      完备性
优先级:    P2
溯源意图:  INTENT-COMP-024
参照来源:  runs/2026-07-27-01/intents/spec.md; inputs/workflow-samples/cann/sub_pipline_support.yaml; core-concepts/trigger-events.md
母意图:    —
标题:      触发事件别名 pr_comment 的有效性与等价性记录

前置条件:
  - 仓库已启用 AtomGit Action
  - fixture 仓库存在开放 PR（可发表/删除评论）

操作步骤:
  1. 编写 on.pr_comment 的 workflow 并保存，记录校验结果
  2. 若保存成功，在 PR 下发表评论，观察是否触发；与 on.pull_request_comment 行为对比

预期结果:
  - pr_comment 的处理唯一确定：合法别名则与 pull_request_comment 逐点等价；非法字段则校验期报错而非静默不触发

验证点:
  - [正向/记录] on.pr_comment 的实际处理（触发成功 / 校验报错 / 静默忽略）逐字记录
  - [正向] pull_request_comment 的 comments 正则过滤行为（回归保护，复用基底证据）
  - [负向] 非法事件名不应静默保存导致 workflow 永不触发且无任何可见提示

清理:      重置 fixture 仓库（含清理夹具评论与 PR）
